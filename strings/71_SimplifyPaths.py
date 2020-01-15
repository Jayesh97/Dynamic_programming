def simplifyPath(path: str) -> str:
    locs = [location for location in path.split("/") if location and location != "."]
    #print(locs)
    stack = []
    for location in locs:
        if location != "..":
            stack.append(location)
        else:
            if not stack:
                continue
            stack.pop()
    return "/"+"/".join(stack)

print(simplifyPath(path="/a/../../b/../c//.//"))