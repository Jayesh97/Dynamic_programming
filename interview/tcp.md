## multiple tcp

The procedure also works if two TCP
  simultaneously initiate the procedure.  When simultaneous attempt
  occurs, each TCP receives a "SYN" segment which carries no
  acknowledgment after it has sent a "SYN".  Of course, the arrival of
  an old duplicate "SYN" segment can potentially make it appear, to the
  recipient, that a simultaneous connection initiation is in progress.
  Proper use of "reset" segments can disambiguate these cases.

## fields in 3 way handshake

sequence number, control flags, and ACK field.  Other
  fields such as window, addresses, lengths, and text

ACK does not occupy sequence number space

      TCP A                                                TCP B

  1.  CLOSED                                               LISTEN

  2.  SYN-SENT    --> <SEQ=100><CTL=SYN>               --> SYN-RECEIVED

  3.  ESTABLISHED <-- <SEQ=300><ACK=101><CTL=SYN,ACK>  <-- SYN-RECEIVED

  4.  ESTABLISHED --> <SEQ=101><ACK=301><CTL=ACK>       --> ESTABLISHED

  5.  ESTABLISHED --> <SEQ=101><ACK=301><CTL=ACK><DATA> --> ESTABLISHED

          Basic 3-Way Handshake for Connection Synchronization



  Simultaneous initiation is only slightly more complex,Each TCP cycles from CLOSED to SYN-SENT to SYN-RECEIVED to
  ESTABLISHED


        TCP A                                            TCP B

  1.  CLOSED                                           CLOSED

  2.  SYN-SENT     --> <SEQ=100><CTL=SYN>              ...

  3.  SYN-RECEIVED <-- <SEQ=300><CTL=SYN>              <-- SYN-SENT

  4.               ... <SEQ=100><CTL=SYN>              --> SYN-RECEIVED

  5.  SYN-RECEIVED --> <SEQ=100><ACK=301><CTL=SYN,ACK> ...

  6.  ESTABLISHED  <-- <SEQ=300><ACK=101><CTL=SYN,ACK> <-- SYN-RECEIVED

  7.               ... <SEQ=101><ACK=301><CTL=ACK>     --> ESTABLISHED

                Simultaneous Connection Synchronization



The principle reason for the three-way handshake is to prevent old
  duplicate connection initiations from causing confusion.  To deal with
  this, a special control message, reset, has been devised


If the
  receiving TCP is in a  non-synchronized state (i.e., SYN-SENT,
  SYN-RECEIVED), it returns to LISTEN on receiving an acceptable reset.
  If the TCP is in one of the synchronized states (ESTABLISHED,
  FIN-WAIT-1, FIN-WAIT-2, CLOSE-WAIT, CLOSING, LAST-ACK, TIME-WAIT), it
  aborts the connection and informs its user.


      TCP A                                                TCP B

  1.  CLOSED                                               LISTEN

  2.  SYN-SENT    --> <SEQ=100><CTL=SYN>               ...

  3.  (duplicate) ... <SEQ=90><CTL=SYN>               --> SYN-RECEIVED

  4.  SYN-SENT    <-- <SEQ=300><ACK=91><CTL=SYN,ACK>  <-- SYN-RECEIVED

  5.  SYN-SENT    --> <SEQ=91><CTL=RST>               --> LISTEN


  6.              ... <SEQ=100><CTL=SYN>               --> SYN-RECEIVED

  7.  SYN-SENT    <-- <SEQ=400><ACK=101><CTL=SYN,ACK>  <-- SYN-RECEIVED

  8.  ESTABLISHED --> <SEQ=101><ACK=401><CTL=ACK>      --> ESTABLISHED

                    Recovery from Old Duplicate SYN



  As a simple example of recovery from old duplicates, consider
  figure 9.  At line 3, an old duplicate SYN arrives at TCP B.  TCP B
  cannot tell that this is an old duplicate, so it responds normally
  (line 4).  TCP A detects that the ACK field is incorrect and returns a
  RST (reset) with its SEQ field selected to make the segment
  believable


   When the original SYN (pun intended) finally arrives at line 6, the
  synchronization proceeds normally.  If the SYN at line 6 had arrived
  before the RST, a more complex exchange might have occurred with RST's
  sent in both directions.

  ## Half-Open Connections and Other Anomalies

   An established connection is said to be  "half-open" if one of the
  TCPs has closed or aborted the connection at its end without the
  knowledge of the other, or if the two ends of the connection have
  become desynchronized owing to a crash that resulted in loss of
  memory


  
  If at site A the connection no longer exists, 
then an attempt by the  user at site B to send any data on it will result in the site B TCP
  receiving a reset control message.  Such a message indicates to the
  site B TCP that something is wrong, and it is expected to abort the
  connection


      TCP A                                           TCP B

  1.  (CRASH)                               (send 300,receive 100)

  2.  CLOSED                                           ESTABLISHED

  3.  SYN-SENT --> <SEQ=400><CTL=SYN>              --> (??)

  4.  (!!)     <-- <SEQ=300><ACK=100><CTL=ACK>     <-- ESTABLISHED

  5.  SYN-SENT --> <SEQ=100><CTL=RST>              --> (Abort!!)

  6.  SYN-SENT                                         CLOSED

  7.  SYN-SENT --> <SEQ=400><CTL=SYN>              -->

                     Half-Open Connection Discovery


When the TCP is up again,
  A is likely to start again from the beginning or from a recovery
  point.  As a result, A will probably try to OPEN the connection again
  or try to SEND on the connection it believes open.  In the latter
  case, it receives the error message "connection not open" from the
  local (A's) TCP.  In an attempt to establish the connection, A's TCP
  will send a segment containing SYN.

## Alternative case

 An interesting alternative case occurs when TCP A crashes and TCP B
  tries to send data on what it thinks is a synchronized connection.


        TCP A                                              TCP B

  1.  (CRASH)                                   (send 300,receive 100)

  2.  (??)    <-- <SEQ=300><ACK=100><DATA=10><CTL=ACK> <-- ESTABLISHED

  3.          --> <SEQ=100><CTL=RST>                   --> (ABORT!!)

           Active Side Causes Half-Open Connection Discovery



we find the two TCPs A and B with passive connections
  waiting for SYN.  An old duplicate arriving at TCP B (line 2) stirs B
  into action.  A SYN-ACK is returned (line 3) and causes TCP A to
  generate a RST (the ACK in line 3 is not acceptable).  TCP B accepts
  the reset and returns to its passive LISTEN state.

     TCP A                                         TCP B

  1.  LISTEN                                        LISTEN

  2.       ... <SEQ=Z><CTL=SYN>                -->  SYN-RECEIVED

  3.  (??) <-- <SEQ=X><ACK=Z+1><CTL=SYN,ACK>   <--  SYN-RECEIVED

  4.       --> <SEQ=Z+1><CTL=RST>              -->  (return to LISTEN!)

  5.  LISTEN                                        LISTEN

       Old Duplicate SYN Initiates a Reset on two Passive Sockets


As a general rule, reset (RST) must be sent whenever a segment arrives
  which apparently is not intended for the current connection.  A reset
  must not be sent if it is not clear that this is the case.

## states in tcp handshake



----------gap-------------


## closing a connection

The user who CLOSEs may continue to RECEIVE
  until he is told that the other side has CLOSED also

###   Case 1:  Local user initiates the close




      TCP A                                                TCP B

  1.  ESTABLISHED                                          ESTABLISHED

  2.  (Close)
      FIN-WAIT-1  --> <SEQ=100><ACK=300><CTL=FIN,ACK>  --> CLOSE-WAIT

  3.  FIN-WAIT-2  <-- <SEQ=300><ACK=101><CTL=ACK>      <-- CLOSE-WAIT

  4.                                                       (Close)
      TIME-WAIT   <-- <SEQ=300><ACK=101><CTL=FIN,ACK>  <-- LAST-ACK

  5.  TIME-WAIT   --> <SEQ=101><ACK=301><CTL=ACK>      --> CLOSED

  6.  (2 MSL)
      CLOSED

                         Normal Close Sequence



   In this case, a FIN segment can be constructed and placed on the
    outgoing segment queue.  No further SENDs from the user will be
    accepted by the TCP, and it enters the FIN-WAIT-1 state.  RECEIVEs
    are allowed in this state.  All segments preceding and including FIN
    will be retransmitted until acknowledged.  When the other TCP has
    both acknowledged the FIN and sent a FIN of its own, the first TCP
    can ACK this FIN.  Note that a TCP receiving a FIN will ACK but not
    send its own FIN until its user has CLOSED the connection also.
