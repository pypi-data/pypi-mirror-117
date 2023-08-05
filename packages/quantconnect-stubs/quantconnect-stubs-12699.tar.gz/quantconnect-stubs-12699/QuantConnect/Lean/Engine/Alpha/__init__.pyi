import abc

import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.Alpha
import QuantConnect.Lean.Engine.TransactionHandlers
import QuantConnect.Packets


class IAlphaHandler(metaclass=abc.ABCMeta):
    """Alpha handler defines how to process insights generated by an algorithm"""

    @property
    @abc.abstractmethod
    def IsActive(self) -> bool:
        """Gets a flag indicating if this handler's thread is still running and processing messages"""
        ...

    @property
    @abc.abstractmethod
    def RuntimeStatistics(self) -> QuantConnect.AlphaRuntimeStatistics:
        """Gets the current alpha runtime statistics"""
        ...

    def Exit(self) -> None:
        """Stops processing in the Engine.Run method"""
        ...

    def Initialize(self, job: QuantConnect.Packets.AlgorithmNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm, messagingHandler: QuantConnect.Interfaces.IMessagingHandler, api: QuantConnect.Interfaces.IApi, transactionHandler: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler) -> None:
        """
        Initializes this alpha handler to accept insights from the specified algorithm
        
        :param job: The algorithm job
        :param algorithm: The algorithm instance
        :param messagingHandler: Handler used for sending insights
        :param api: Api instance
        :param transactionHandler: Algorithms transaction handler
        """
        ...

    def OnAfterAlgorithmInitialized(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Invoked after the algorithm's Initialize method was called allowing the alpha handler to check
        other things, such as sampling period for backtests
        
        :param algorithm: The algorithm instance
        """
        ...

    def ProcessSynchronousEvents(self) -> None:
        """Performs processing in sync with the algorithm's time loop to provide consisten reading of data"""
        ...


