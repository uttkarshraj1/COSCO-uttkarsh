from .Scheduler import *
import numpy as np

class Multiple_Simulation(Scheduler):
    def __init__(self):
        super().__init__()

    def selection(self):
        selectedContainerIDs_Multiple = []
        for hostID, host in enumerate(self.env.hostlist):
            if host.getCPU() > 70:
                containerIDs = self.env.getContainersOfHost(hostID)
                if containerIDs:
                    containerIPS = [self.env.containerlist[cid].getBaseIPS() for cid in containerIDs]
                    selectedContainerIDs_Multiple.append(containerIDs[np.argmax(containerIPS)])
        return selectedContainerIDs_Multiple

    def placement(self, containerIDs):
        decisions = []
        for cid in containerIDs:
            scores = [self.env.stats.runMultipleSimulation([(cid, hostID)])[0] for hostID, _ in enumerate(self.env.hostlist)]
            decisions.append((cid, np.argmin(scores)))
        return decisions[:10] #Running for multiple decisons like for 10,20,30 & 40 default is set at 10 

        