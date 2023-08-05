import typing
import warnings

import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Alphas.Serialization
import QuantConnect.Util
import System


class SerializedInsight(System.Object):
    """
    DTO used for serializing an insight that was just generated by an algorithm.
    This type does not contain any of the analysis dependent fields, such as scores
    and estimated value
    """

    @property
    def Id(self) -> str:
        """See Insight.Id"""
        ...

    @Id.setter
    def Id(self, value: str):
        """See Insight.Id"""
        ...

    @property
    def GroupId(self) -> str:
        """See Insight.GroupId"""
        ...

    @GroupId.setter
    def GroupId(self, value: str):
        """See Insight.GroupId"""
        ...

    @property
    def SourceModel(self) -> str:
        """See Insight.SourceModel"""
        ...

    @SourceModel.setter
    def SourceModel(self, value: str):
        """See Insight.SourceModel"""
        ...

    @property
    def GeneratedTime(self) -> float:
        """
        Pass-through for CreatedTime
        
        Deprecated as of 2020-01-23. Please use the `CreatedTime` property instead.
        """
        warnings.warn("Deprecated as of 2020-01-23. Please use the `CreatedTime` property instead.", DeprecationWarning)

    @GeneratedTime.setter
    def GeneratedTime(self, value: float):
        """
        Pass-through for CreatedTime
        
        Deprecated as of 2020-01-23. Please use the `CreatedTime` property instead.
        """
        warnings.warn("Deprecated as of 2020-01-23. Please use the `CreatedTime` property instead.", DeprecationWarning)

    @property
    def CreatedTime(self) -> float:
        """See Insight.GeneratedTimeUtc"""
        ...

    @CreatedTime.setter
    def CreatedTime(self, value: float):
        """See Insight.GeneratedTimeUtc"""
        ...

    @property
    def CloseTime(self) -> float:
        """See Insight.CloseTimeUtc"""
        ...

    @CloseTime.setter
    def CloseTime(self, value: float):
        """See Insight.CloseTimeUtc"""
        ...

    @property
    def Symbol(self) -> str:
        """
        See Insight.Symbol
        The symbol's security identifier string
        """
        ...

    @Symbol.setter
    def Symbol(self, value: str):
        """
        See Insight.Symbol
        The symbol's security identifier string
        """
        ...

    @property
    def Ticker(self) -> str:
        """
        See Insight.Symbol
        The symbol's ticker at the generated time
        """
        ...

    @Ticker.setter
    def Ticker(self, value: str):
        """
        See Insight.Symbol
        The symbol's ticker at the generated time
        """
        ...

    @property
    def Type(self) -> int:
        """
        See Insight.Type
        
        This property contains the int value of a member of the QuantConnect.Algorithm.Framework.Alphas.InsightType enum.
        """
        ...

    @Type.setter
    def Type(self, value: int):
        """
        See Insight.Type
        
        This property contains the int value of a member of the QuantConnect.Algorithm.Framework.Alphas.InsightType enum.
        """
        ...

    @property
    def ReferenceValue(self) -> float:
        """See Insight.ReferenceValue"""
        ...

    @ReferenceValue.setter
    def ReferenceValue(self, value: float):
        """See Insight.ReferenceValue"""
        ...

    @property
    def ReferenceValueFinal(self) -> float:
        """See Insight.ReferenceValueFinal"""
        ...

    @ReferenceValueFinal.setter
    def ReferenceValueFinal(self, value: float):
        """See Insight.ReferenceValueFinal"""
        ...

    @property
    def Direction(self) -> int:
        """
        See Insight.Direction
        
        This property contains the int value of a member of the QuantConnect.Algorithm.Framework.Alphas.InsightDirection enum.
        """
        ...

    @Direction.setter
    def Direction(self, value: int):
        """
        See Insight.Direction
        
        This property contains the int value of a member of the QuantConnect.Algorithm.Framework.Alphas.InsightDirection enum.
        """
        ...

    @property
    def Period(self) -> float:
        """See Insight.Period"""
        ...

    @Period.setter
    def Period(self, value: float):
        """See Insight.Period"""
        ...

    @property
    def Magnitude(self) -> typing.Optional[float]:
        """See Insight.Magnitude"""
        ...

    @Magnitude.setter
    def Magnitude(self, value: typing.Optional[float]):
        """See Insight.Magnitude"""
        ...

    @property
    def Confidence(self) -> typing.Optional[float]:
        """See Insight.Confidence"""
        ...

    @Confidence.setter
    def Confidence(self, value: typing.Optional[float]):
        """See Insight.Confidence"""
        ...

    @property
    def Weight(self) -> typing.Optional[float]:
        """See Insight.Weight"""
        ...

    @Weight.setter
    def Weight(self, value: typing.Optional[float]):
        """See Insight.Weight"""
        ...

    @property
    def ScoreIsFinal(self) -> bool:
        """See InsightScore.IsFinalScore"""
        ...

    @ScoreIsFinal.setter
    def ScoreIsFinal(self, value: bool):
        """See InsightScore.IsFinalScore"""
        ...

    @property
    def ScoreMagnitude(self) -> float:
        """See InsightScore.Magnitude"""
        ...

    @ScoreMagnitude.setter
    def ScoreMagnitude(self, value: float):
        """See InsightScore.Magnitude"""
        ...

    @property
    def ScoreDirection(self) -> float:
        """See InsightScore.Direction"""
        ...

    @ScoreDirection.setter
    def ScoreDirection(self, value: float):
        """See InsightScore.Direction"""
        ...

    @property
    def EstimatedValue(self) -> float:
        """See Insight.EstimatedValue"""
        ...

    @EstimatedValue.setter
    def EstimatedValue(self, value: float):
        """See Insight.EstimatedValue"""
        ...

    @typing.overload
    def __init__(self) -> None:
        """Initializes a new default instance of the SerializedInsight class"""
        ...

    @typing.overload
    def __init__(self, insight: QuantConnect.Algorithm.Framework.Alphas.Insight) -> None:
        """
        Initializes a new instance of the SerializedInsight  class by copying the specified insight
        
        :param insight: The insight to copy
        """
        ...


class InsightJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[QuantConnect.Algorithm.Framework.Alphas.Insight, QuantConnect.Algorithm.Framework.Alphas.Serialization.SerializedInsight]):
    """Defines how insights should be serialized to json"""

    @typing.overload
    def Convert(self, value: QuantConnect.Algorithm.Framework.Alphas.Insight) -> QuantConnect.Algorithm.Framework.Alphas.Serialization.SerializedInsight:
        """
        Convert the input value to a value to be serialized
        
        This method is protected.
        
        :param value: The input value to be converted before serialization
        :returns: A new instance of TResult that is to be serialized.
        """
        ...

    @typing.overload
    def Convert(self, value: QuantConnect.Algorithm.Framework.Alphas.Serialization.SerializedInsight) -> QuantConnect.Algorithm.Framework.Alphas.Insight:
        """
        Converts the input value to be deserialized
        
        This method is protected.
        
        :param value: The deserialized value that needs to be converted to T
        :returns: The converted value.
        """
        ...


