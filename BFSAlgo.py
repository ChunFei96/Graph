import random
import os

class BFSAlgo:
    @staticmethod
    def adjVerticesIsHospital(graphFile, hospitalFile):
        adjVertices = {}
        nodeL1 = []
        nodeL2 = []

        # read in Graph
        with open(graphFile, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line[0].isdigit():
                    nodes = [int(s) for s in line.split() if s.isdigit()]
                    nodeL1.append(nodes[0])
                    nodeL2.append(nodes[1])
        tempSet = set(nodeL1 + nodeL2)
        noOfNodes = len(tempSet)
        # print(noOfNodes)

        # Lee read in Hospital
        hospitalList = []
        noOfHospital = 0
        # if Hospital file has no nodeId inside, random generate Hospitals
        if os.stat(hospitalFile).st_size == 0:
            noOfHospital = random.randint(0, int(noOfNodes/2))
            hospitalList = random.sample(tempSet, noOfHospital)
            hospitalList.sort()

            with open(hospitalFile, 'w') as writeFile:
                writeFile.writelines("%d\n" % node for node in hospitalList)
                writeFile.seek(0)
                writeFile.write('%d' % hospitalList[0])

            print("hospital list")
            print(hospitalList)
        else:
            with open(hospitalFile, 'r') as f:
                lines = f.readlines()
                lines = [item.rstrip("\n") for item in lines]
                for line in lines:
                    if line[0].isdigit():
                        hospitalList.append(int(line))

            noOfHospital = len(hospitalList)
            if noOfHospital > noOfNodes:
                print('Invalid no of hospital. Should input a hospital size no more than ' + str(noOfNodes))
                return {}, []
            print("hospital list")
            print(hospitalList)

        tempL1 = [False] * len(nodeL1)
        i = 0
        for node in nodeL1:
            if node in hospitalList:
                tempL1[i] = True
            i += 1
        # print(tempL1)
        nodeL1 = list(zip(nodeL1, tempL1))

        tempL2 = [False] * len(nodeL2)
        i = 0
        for node in nodeL2:
            if node in hospitalList:
                tempL2[i] = True
            i += 1
        nodeL2 = list(zip(nodeL2, tempL2))

        if len(nodeL2) != len(nodeL1):
            print('Not equal!!!!!!!!!!!!!!!!!!!!!!')

        for i in range(len(nodeL1)):
            if nodeL1[i] not in adjVertices.keys():
                adjVertices[nodeL1[i]] = []
            if nodeL2[i] not in adjVertices[nodeL1[i]]:
                adjVertices[nodeL1[i]].append(nodeL2[i])
            if nodeL2[i] not in adjVertices.keys():
                adjVertices[nodeL2[i]] = []
            if nodeL1[i] not in adjVertices[nodeL2[i]]:
                adjVertices[nodeL2[i]].append(nodeL1[i])

        with open('NodesList.txt', 'w') as writeFile:
            writeFile.write(str(adjVertices))

        return adjVertices, hospitalList, tempSet

    @staticmethod
    def BFS(adjList, source, hospitalList, k):
        if k > len(hospitalList):
            print("There are only " + str(len(hospitalList)) + " hospitals in this area.")
            k = len(hospitalList)
            # return None
        # map = graph(graphFile)

        distance = 0
        path = []
        pathList = []

        isVisitedHospital = []

        if source in hospitalList:
            print("The source is a hospital!")
            source = (source, True)
            isVisitedHospital.append(source)
            pathList = [[[source], 0]]
            num = 1
            if num == k:
                return 
        else:
            source = (source, False)
            num = 0

        queue = [[source]]

        isVisited = []

        print(hospitalList)
        # print(adjList[1])

        while (queue):
            tempP = queue.pop(0)
            vertex = tempP[-1]

            if vertex not in isVisited:
                for node in adjList[vertex]:
                    ttempP = list(tempP)
                    ttempP.append(node)
                    queue.append(ttempP)

                if vertex[-1]:
                    if vertex in isVisitedHospital:
                       continue
                    # if vertex in isVisitedHospital:
                    isVisitedHospital.append(vertex)
                    print(tempP)
                    distance = len(tempP) - 1

                    pathList.append([tempP, distance])
                    print('Here')
                    print(pathList)
                    num += 1
                    # print(pathList)
                    print(num)
                    if num == k:
                        print('num is ' + str(k))
                        print(pathList)
                        return pathList

                isVisited.append(vertex)
        print(pathList)
        return pathList

    @staticmethod
    def search(graphFile, hospitalFile, resultFile, KnoOfHospital):
        hospitalList = []

        finalPathList = []

        while True:
            # try:
            #     noOfHospital = int(input("Please input no of hospital you want to defined in this area:"))
            # except:
            #     print("Invalid input! Please try again!")
            #     continue
            # if noOfHospital == 0:
            #     print("Invalid input! Please try again!")
            #     continue

            adjList, hospitalList, nodeList = BFSAlgo.adjVerticesIsHospital(graphFile, hospitalFile)
            if not hospitalList:
                continue
            else:
                break

        # while True:
        #     try:
        #         searchHospital = int(input("Please input no of hospital you want to search in this area:"))
        #     except:
        #         print("Invalid input! Please try again!")
        #         continue
        #     if searchHospital == 0:
        #         print("Invalid input! Please try again!")
        #         continue
        #     else:
        #         break

        # while True:
        #     try:
        #         inputSource = int(input("Please input the starting location in this area:"))
        #     except:
        #         print("Invalid input! Please try again!")
        #         continue
        #     if inputSource not in nodeList:
        #         print("The input location is not inside this area! Please try again!")
        #         continue
        #     else:
        #         break

        #Lee

        print("nodeList: " + str(nodeList))
        print("hospitalList: " + str(hospitalList))

        showPath = 'Hospital list: ' + str(hospitalList) + '\n'
        for node in nodeList:
            if node not in hospitalList:
                inputSource = node

                pathList = BFSAlgo.BFS(adjList, inputSource, hospitalList, KnoOfHospital)

                print(pathList)

                if not pathList:
                    print('There is no path from the current location [' + str(inputSource) + '] to the nearby hospital.')
                    showPath += '\nThere is no path from the current location [' + str(inputSource) + '] to the nearby hospital.\n'
                else:
                    if KnoOfHospital > len(hospitalList):
                        showPath += ("There are only " + str(len(hospitalList)) + " hospitals in this area.\n")
                    showPath += ('\n' + 'No of hospital near starting location [' + str(inputSource) + ']: ' + str(
                        len(pathList)) + '\n\n')
                    # showPath += ('Nearby Hospital ID:'+len([]))
                    if len(pathList) == 1:
                        showPath += 'The path and distance to the hospital is shown below:\n'
                    else:
                        showPath += 'The paths and distance to the hospitals are shown below:\n'

                    for i in range(len(pathList)):
                        partialPathList = []
                        distance = pathList[i][1]
                        path = pathList[i][0]
                        print(path)
                        showPath += 'Path: '
                        for m in range(len(path)):
                            if m == 0:
                                pathStr = '[' + str(path[m][0]) + ']'
                            else:
                                pathStr = str(path[m][0])

                            if m + 1 == len(path):
                                print('path[m][0]')
                                print(path[m][0])
                                showPath += (pathStr + ' || Distance = ' + str(distance) + '\n')
                            else:

                                print('=====path[m][0]=====')
                                print(path[m][0])
                                showPath += (pathStr + ' ==>> ')

                            partialPathList.append(path[m][0])
                        finalPathList.append(partialPathList)

        with open(resultFile, 'w') as outputFile:
            outputFile.write(showPath)

        print(type(adjList))
        dict_pairs = adjList.items()
        pairs_iterator = iter(dict_pairs)
        first_pair = next(pairs_iterator)
        print(first_pair)

        return showPath
        #
        # return showPath, finalPathList


# if __name__ == "__main__":
#     graphFile = 'roadNet-CA.txt'
#     hospitalFile = 'Hospital.txt'
#     resultFile = 'Path To Nearby Hospital.txt'
#
#     search(graphFile, hospitalFile, resultFile)
