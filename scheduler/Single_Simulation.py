from .Scheduler import *
import numpy as np

class Single_Simulation(Scheduler):
    def __init__(self):
        super().__init__()

    def selection(self):
        selectedContainerIDs_single = []
        for hostID, host in enumerate(self.env.hostlist):
            if host.getCPU() > 70:
                containerIDs = self.env.getContainersOfHost(hostID)
                if containerIDs:
                    containerIPS = [self.env.containerlist[cid].getBaseIPS() for cid in containerIDs]
                    selectedContainerIDs_single.append(containerIDs[np.argmax(containerIPS)])
        return selectedContainerIDs_single

    def placement(self, containerIDs):
        single_decision = []

        for cid in containerIDs:
            scores = [self.env.stats.runSingleSimulation([(cid, hostID)])[0] for hostID, _ in enumerate(self.env.hostlist)]
            single_decision.append((cid, np.argmin(scores)))
        return single_decision