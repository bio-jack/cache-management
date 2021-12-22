# Global vars
cache = []
requests = []
cacheSize = 8
cacheMethod = None


def updateRequests():
    """
    Takes user page requests as ints and updates requests until 0 is entered.

    Parameters: None
    Returns: None
    """
    print("\nEnter requests INDIVIDUALLY as positive ints. Enter 0 when finished.")

    # Append user inputs to requests
    userInput = None
    while True:
        userInput = int(input("> "))
        if userInput == 0:
            break
        else:
            requests.append(userInput)


def getCacheMethod():
    """
    Gets preferred cache method from user, either First-in-First-out or Least Frequently Used.

    Paramaters: None
    Returns: string
    """
    print("\nEnter 1 for FIFO, Enter 2 for LFU, enter Q to exit")
    userMethod = input(">")
    if userMethod == "1":
        return "FIFO"
    elif userMethod == "2":
        return "LFU"
    elif userMethod.upper() == "Q":
        return "exit"


def fifo():
    """
    Iterates over a list of requests for "pages". Checks cache and inserts "page" if not present. If cache length exceeds
    cache size, implements First In First Out management method, so "page" added earliest is ejected from cache.

    Prints "Hit" if page already present in cache, "Miss" if not present.

    Parameters: None
    Returns: None
    """
    for req in requests:
        if req in cache:
            print("Hit: " + str(req))
        else:
            print("Miss: " + str(req))
            if len(cache) < cacheSize:
                cache.append(req)
            # Remove earliest added request in cache, append new request
            else:
                cache.pop(0)
                cache.append(req)


def lfu():
    """
    Iterates over requests for "pages". Checks cache and inserts "page" if not present. If cache exceeds
    cache size, implements Least Frequently Used management method, so least requested "page" is ejected from cache.

    Prints "Hit" if page already present in cache, "Miss" if not present.
    
    Parameters: None
    Returns: None
    """

    # Dictionary where keys are requests and values are times requested
    reqCount = {
    }

    for req in requests:
        # If request not present in reqCount, add to reqCount with default value 0
        reqCount.setdefault(req, 0)
        # Increment request in reqCount by 1
        reqCount[req] += 1

        # Print hit if request present in cache
        if req in cache:
            print("Hit: " + str(req))
        # Print miss if request not present in cache
        else:
            print("Miss: " + str(req))
            # If cache size not exceeded
            if len(cache) < cacheSize:
                cache.append(req)
            # If cache size exceeded, implement LFU
            else:
                # Create reqCount instance with only keys currently in cache
                reqCountInstance = {x: reqCount[x] for x in cache if x in cache}
                # Find least accessed value in cache using reqCount instance, remove value from cache and append
                # new request
                leastAccessed = min(reqCountInstance, key=reqCountInstance.get)
                cache.remove(leastAccessed)
                cache.append(req)


## Main body ##
print("***CACHE MANAGEMENT SYSTEM***")
# Loop through menus for getting user requests and preferred cache management method
# Exit when user enters Q for cache method
while cacheMethod != "exit":
    cache = []
    requests = []
    updateRequests()

    while True:
        cacheMethod = getCacheMethod()
        if cacheMethod == "FIFO":
            fifo()
            print("\nFinal cache = " + str(cache))
            break
        elif cacheMethod == "LFU":
            lfu()
            print("\nFinal cache = " + str(cache))
            break
        elif cacheMethod == "exit":
            break
        else:
            print("Invalid input! Please select 1, 2 or Q.")

print("\nProgram exited.")
