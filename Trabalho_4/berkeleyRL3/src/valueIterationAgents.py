# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util, copy
from operator import itemgetter 
from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0

        # Write value iteration code here
        l_estados = mdp.getStates()
        recompensa = 0.0
        sum_prob = 0.0
        l_values = copy.deepcopy(self.values)
        total_prob = 0.0
        
        list_sum_prob = list()
        
        for i in range(iterations):
            for estado in l_estados:
                if(mdp.isTerminal(estado)):
                    self.values[estado] = 0.0
                    continue

                l_acoes = mdp.getPossibleActions(estado)
                for acao in l_acoes:
                    l_estado_prob = mdp.getTransitionStatesAndProbs(estado, acao)
                    sum_prob = 0.0
                    
                    for prox_estado, prox_prob in l_estado_prob:
                        sum_prob += prox_prob * l_values[prox_estado]

                    proximo_estado =  copy.deepcopy(max(l_estado_prob, key=itemgetter(1))[0])
                    total_prob = copy.deepcopy(sum_prob)
                    list_sum_prob.append((total_prob, proximo_estado, acao))
                
                valor_maximo = copy.deepcopy(max(list_sum_prob, key=itemgetter(0))[0])
                recompensa = mdp.getReward(estado, max(list_sum_prob, key=itemgetter(0))[2], max(list_sum_prob, key=itemgetter(0))[1])
                self.values[estado] = recompensa + self.discount * valor_maximo
                list_sum_prob.clear()

            l_values = copy.deepcopy(self.values)




    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        q = 0.0

        l_estado_prob = self.mdp.getTransitionStatesAndProbs(state, action)

        for prox_estado, prox_prob in l_estado_prob:
            recompensa = self.mdp.getReward(state, action, prox_estado)
            q += recompensa + self.discount * self.values[prox_estado] * prox_prob 


        return q


        #util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        l_acoes = self.mdp.getPossibleActions(state)
        l_valor_acoes = list()

        for acao in l_acoes:
            q = self.computeQValueFromValues(state, acao)
            l_valor_acoes.append((acao, q))

        if(len(l_valor_acoes) == 0):
            return None

        return max(l_valor_acoes, key=itemgetter(1))[0]


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
