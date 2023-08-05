from setuptools import setup

long_description = """
# QuantConnect Stubs

This package contains type stubs for QuantConnect's [Lean](https://github.com/QuantConnect/Lean) algorithmic trading engine and for parts of the .NET library that are used by Lean.

These stubs can be used by editors to provide type-aware features like autocomplete and auto-imports in QuantConnect strategies written in Python.

After installing the stubs, you can copy the following line to the top of every Python file to have the same imports as the ones that are added by default in the cloud:
```py
from AlgorithmImports import *
```

This line imports [all common QuantConnect members](https://github.com/QuantConnect/Lean/blob/master/Common/AlgorithmImports.py) and provides autocomplete for them.
""".strip()

setup(
    name="quantconnect-stubs",
    version="12692",
    description="Type stubs for QuantConnect's Lean",
    author="QuantConnect",
    author_email="support@quantconnect.com",
    url="https://github.com/QuantConnect/quantconnect-stubs-generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3"
    ],
    install_requires=["pandas>=0.25.3", "matplotlib>=3.2.1"],
    packages=[
        "AlgorithmImports",
        "clr",
        "Internal",
        "Internal.Runtime",
        "Internal.Runtime.CompilerServices",
        "Internal.Win32",
        "Internal.Win32.SafeHandles",
        "Microsoft",
        "Microsoft.Win32",
        "Microsoft.Win32.SafeHandles",
        "MS",
        "MS.Internal",
        "MS.Internal.Xml",
        "MS.Internal.Xml.Linq",
        "MS.Internal.Xml.Linq.ComponentModel",
        "Oanda",
        "Oanda.RestV20",
        "Oanda.RestV20.Api",
        "Oanda.RestV20.Client",
        "Oanda.RestV20.Model",
        "Oanda.RestV20.Session",
        "QuantConnect",
        "QuantConnect.Algorithm",
        "QuantConnect.Algorithm.Framework",
        "QuantConnect.Algorithm.Framework.Alphas",
        "QuantConnect.Algorithm.Framework.Alphas.Analysis",
        "QuantConnect.Algorithm.Framework.Alphas.Analysis.Functions",
        "QuantConnect.Algorithm.Framework.Alphas.Analysis.Providers",
        "QuantConnect.Algorithm.Framework.Alphas.Serialization",
        "QuantConnect.Algorithm.Framework.Execution",
        "QuantConnect.Algorithm.Framework.Portfolio",
        "QuantConnect.Algorithm.Framework.Risk",
        "QuantConnect.Algorithm.Framework.Selection",
        "QuantConnect.Algorithm.Selection",
        "QuantConnect.AlgorithmFactory",
        "QuantConnect.AlgorithmFactory.Python",
        "QuantConnect.AlgorithmFactory.Python.Wrappers",
        "QuantConnect.Api",
        "QuantConnect.Api.Serialization",
        "QuantConnect.Benchmarks",
        "QuantConnect.Brokerages",
        "QuantConnect.Brokerages.Backtesting",
        "QuantConnect.Brokerages.Binance",
        "QuantConnect.Brokerages.Binance.Messages",
        "QuantConnect.Brokerages.Bitfinex",
        "QuantConnect.Brokerages.Bitfinex.Converters",
        "QuantConnect.Brokerages.Bitfinex.Messages",
        "QuantConnect.Brokerages.GDAX",
        "QuantConnect.Brokerages.GDAX.Messages",
        "QuantConnect.Brokerages.InteractiveBrokers",
        "QuantConnect.Brokerages.InteractiveBrokers.Client",
        "QuantConnect.Brokerages.InteractiveBrokers.FinancialAdvisor",
        "QuantConnect.Brokerages.Oanda",
        "QuantConnect.Brokerages.Paper",
        "QuantConnect.Brokerages.Tradier",
        "QuantConnect.Brokerages.Zerodha",
        "QuantConnect.Brokerages.Zerodha.Messages",
        "QuantConnect.Configuration",
        "QuantConnect.Data",
        "QuantConnect.Data.Auxiliary",
        "QuantConnect.Data.Consolidators",
        "QuantConnect.Data.Custom",
        "QuantConnect.Data.Custom.IconicTypes",
        "QuantConnect.Data.Custom.Intrinio",
        "QuantConnect.Data.Custom.Tiingo",
        "QuantConnect.Data.Fundamental",
        "QuantConnect.Data.Market",
        "QuantConnect.Data.Shortable",
        "QuantConnect.Data.UniverseSelection",
        "QuantConnect.DataSource",
        "QuantConnect.Exceptions",
        "QuantConnect.Indicators",
        "QuantConnect.Indicators.CandlestickPatterns",
        "QuantConnect.Interfaces",
        "QuantConnect.Lean",
        "QuantConnect.Lean.Engine",
        "QuantConnect.Lean.Engine.Alpha",
        "QuantConnect.Lean.Engine.Alphas",
        "QuantConnect.Lean.Engine.DataFeeds",
        "QuantConnect.Lean.Engine.DataFeeds.Enumerators",
        "QuantConnect.Lean.Engine.DataFeeds.Enumerators.Factories",
        "QuantConnect.Lean.Engine.DataFeeds.Queues",
        "QuantConnect.Lean.Engine.DataFeeds.Transport",
        "QuantConnect.Lean.Engine.DataFeeds.WorkScheduling",
        "QuantConnect.Lean.Engine.HistoricalData",
        "QuantConnect.Lean.Engine.RealTime",
        "QuantConnect.Lean.Engine.Results",
        "QuantConnect.Lean.Engine.Server",
        "QuantConnect.Lean.Engine.Setup",
        "QuantConnect.Lean.Engine.Storage",
        "QuantConnect.Lean.Engine.TransactionHandlers",
        "QuantConnect.Lean.Launcher",
        "QuantConnect.Logging",
        "QuantConnect.Messaging",
        "QuantConnect.Notifications",
        "QuantConnect.Optimizer",
        "QuantConnect.Optimizer.Launcher",
        "QuantConnect.Optimizer.Objectives",
        "QuantConnect.Optimizer.Parameters",
        "QuantConnect.Optimizer.Strategies",
        "QuantConnect.Orders",
        "QuantConnect.Orders.Fees",
        "QuantConnect.Orders.Fills",
        "QuantConnect.Orders.OptionExercise",
        "QuantConnect.Orders.Serialization",
        "QuantConnect.Orders.Slippage",
        "QuantConnect.Orders.TimeInForces",
        "QuantConnect.Packets",
        "QuantConnect.Parameters",
        "QuantConnect.Python",
        "QuantConnect.Queues",
        "QuantConnect.Report",
        "QuantConnect.Report.ReportElements",
        "QuantConnect.Research",
        "QuantConnect.Scheduling",
        "QuantConnect.Securities",
        "QuantConnect.Securities.Cfd",
        "QuantConnect.Securities.Crypto",
        "QuantConnect.Securities.CurrencyConversion",
        "QuantConnect.Securities.Equity",
        "QuantConnect.Securities.Forex",
        "QuantConnect.Securities.Future",
        "QuantConnect.Securities.FutureOption",
        "QuantConnect.Securities.FutureOption.Api",
        "QuantConnect.Securities.Index",
        "QuantConnect.Securities.IndexOption",
        "QuantConnect.Securities.Interfaces",
        "QuantConnect.Securities.Option",
        "QuantConnect.Securities.Option.StrategyMatcher",
        "QuantConnect.Securities.Positions",
        "QuantConnect.Securities.Volatility",
        "QuantConnect.Statistics",
        "QuantConnect.Storage",
        "QuantConnect.Util",
        "QuantConnect.Util.RateLimit",
        "System",
        "System.Buffers",
        "System.Buffers.Binary",
        "System.Buffers.Text",
        "System.CodeDom",
        "System.CodeDom.Compiler",
        "System.Collections",
        "System.Collections.Concurrent",
        "System.Collections.Generic",
        "System.Collections.Immutable",
        "System.Collections.ObjectModel",
        "System.Collections.Specialized",
        "System.ComponentModel",
        "System.ComponentModel.DataAnnotations",
        "System.ComponentModel.DataAnnotations.Schema",
        "System.ComponentModel.Design",
        "System.ComponentModel.Design.Serialization",
        "System.Configuration",
        "System.Configuration.Assemblies",
        "System.Diagnostics",
        "System.Diagnostics.CodeAnalysis",
        "System.Diagnostics.Contracts",
        "System.Diagnostics.SymbolStore",
        "System.Diagnostics.Tracing",
        "System.Drawing",
        "System.Globalization",
        "System.IO",
        "System.IO.Enumeration",
        "System.IO.Strategies",
        "System.Linq",
        "System.Net",
        "System.Net.Cache",
        "System.Net.NetworkInformation",
        "System.Net.Security",
        "System.Net.Sockets",
        "System.Numerics",
        "System.Numerics.Hashing",
        "System.Reflection",
        "System.Reflection.Emit",
        "System.Reflection.Metadata",
        "System.Resources",
        "System.Runtime",
        "System.Runtime.CompilerServices",
        "System.Runtime.ConstrainedExecution",
        "System.Runtime.ExceptionServices",
        "System.Runtime.InteropServices",
        "System.Runtime.InteropServices.ComTypes",
        "System.Runtime.InteropServices.ObjectiveC",
        "System.Runtime.Intrinsics",
        "System.Runtime.Intrinsics.Arm",
        "System.Runtime.Intrinsics.X86",
        "System.Runtime.Loader",
        "System.Runtime.Remoting",
        "System.Runtime.Serialization",
        "System.Runtime.Versioning",
        "System.Security",
        "System.Security.Authentication",
        "System.Security.Authentication.ExtendedProtection",
        "System.Security.Cryptography",
        "System.Security.Permissions",
        "System.Security.Principal",
        "System.Text",
        "System.Text.Unicode",
        "System.Threading",
        "System.Threading.Tasks",
        "System.Threading.Tasks.Sources",
        "System.Timers",
        "System.Windows",
        "System.Windows.Input",
        "System.Windows.Markup"
    ],
    package_data={
        "AlgorithmImports": ["*.py", "*.pyi"],
        "clr": ["*.py", "*.pyi"],
        "Internal": ["*.py", "*.pyi"],
        "Internal.Runtime": ["*.py", "*.pyi"],
        "Internal.Runtime.CompilerServices": ["*.py", "*.pyi"],
        "Internal.Win32": ["*.py", "*.pyi"],
        "Internal.Win32.SafeHandles": ["*.py", "*.pyi"],
        "Microsoft": ["*.py", "*.pyi"],
        "Microsoft.Win32": ["*.py", "*.pyi"],
        "Microsoft.Win32.SafeHandles": ["*.py", "*.pyi"],
        "MS": ["*.py", "*.pyi"],
        "MS.Internal": ["*.py", "*.pyi"],
        "MS.Internal.Xml": ["*.py", "*.pyi"],
        "MS.Internal.Xml.Linq": ["*.py", "*.pyi"],
        "MS.Internal.Xml.Linq.ComponentModel": ["*.py", "*.pyi"],
        "Oanda": ["*.py", "*.pyi"],
        "Oanda.RestV20": ["*.py", "*.pyi"],
        "Oanda.RestV20.Api": ["*.py", "*.pyi"],
        "Oanda.RestV20.Client": ["*.py", "*.pyi"],
        "Oanda.RestV20.Model": ["*.py", "*.pyi"],
        "Oanda.RestV20.Session": ["*.py", "*.pyi"],
        "QuantConnect": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Framework": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Framework.Alphas": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Framework.Alphas.Analysis": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Framework.Alphas.Analysis.Functions": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Framework.Alphas.Analysis.Providers": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Framework.Alphas.Serialization": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Framework.Execution": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Framework.Portfolio": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Framework.Risk": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Framework.Selection": ["*.py", "*.pyi"],
        "QuantConnect.Algorithm.Selection": ["*.py", "*.pyi"],
        "QuantConnect.AlgorithmFactory": ["*.py", "*.pyi"],
        "QuantConnect.AlgorithmFactory.Python": ["*.py", "*.pyi"],
        "QuantConnect.AlgorithmFactory.Python.Wrappers": ["*.py", "*.pyi"],
        "QuantConnect.Api": ["*.py", "*.pyi"],
        "QuantConnect.Api.Serialization": ["*.py", "*.pyi"],
        "QuantConnect.Benchmarks": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Backtesting": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Binance": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Binance.Messages": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Bitfinex": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Bitfinex.Converters": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Bitfinex.Messages": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.GDAX": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.GDAX.Messages": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.InteractiveBrokers": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.InteractiveBrokers.Client": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.InteractiveBrokers.FinancialAdvisor": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Oanda": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Paper": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Tradier": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Zerodha": ["*.py", "*.pyi"],
        "QuantConnect.Brokerages.Zerodha.Messages": ["*.py", "*.pyi"],
        "QuantConnect.Configuration": ["*.py", "*.pyi"],
        "QuantConnect.Data": ["*.py", "*.pyi"],
        "QuantConnect.Data.Auxiliary": ["*.py", "*.pyi"],
        "QuantConnect.Data.Consolidators": ["*.py", "*.pyi"],
        "QuantConnect.Data.Custom": ["*.py", "*.pyi"],
        "QuantConnect.Data.Custom.IconicTypes": ["*.py", "*.pyi"],
        "QuantConnect.Data.Custom.Intrinio": ["*.py", "*.pyi"],
        "QuantConnect.Data.Custom.Tiingo": ["*.py", "*.pyi"],
        "QuantConnect.Data.Fundamental": ["*.py", "*.pyi"],
        "QuantConnect.Data.Market": ["*.py", "*.pyi"],
        "QuantConnect.Data.Shortable": ["*.py", "*.pyi"],
        "QuantConnect.Data.UniverseSelection": ["*.py", "*.pyi"],
        "QuantConnect.DataSource": ["*.py", "*.pyi"],
        "QuantConnect.Exceptions": ["*.py", "*.pyi"],
        "QuantConnect.Indicators": ["*.py", "*.pyi"],
        "QuantConnect.Indicators.CandlestickPatterns": ["*.py", "*.pyi"],
        "QuantConnect.Interfaces": ["*.py", "*.pyi"],
        "QuantConnect.Lean": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.Alpha": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.Alphas": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.DataFeeds": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.DataFeeds.Enumerators": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.DataFeeds.Enumerators.Factories": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.DataFeeds.Queues": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.DataFeeds.Transport": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.DataFeeds.WorkScheduling": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.HistoricalData": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.RealTime": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.Results": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.Server": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.Setup": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.Storage": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Engine.TransactionHandlers": ["*.py", "*.pyi"],
        "QuantConnect.Lean.Launcher": ["*.py", "*.pyi"],
        "QuantConnect.Logging": ["*.py", "*.pyi"],
        "QuantConnect.Messaging": ["*.py", "*.pyi"],
        "QuantConnect.Notifications": ["*.py", "*.pyi"],
        "QuantConnect.Optimizer": ["*.py", "*.pyi"],
        "QuantConnect.Optimizer.Launcher": ["*.py", "*.pyi"],
        "QuantConnect.Optimizer.Objectives": ["*.py", "*.pyi"],
        "QuantConnect.Optimizer.Parameters": ["*.py", "*.pyi"],
        "QuantConnect.Optimizer.Strategies": ["*.py", "*.pyi"],
        "QuantConnect.Orders": ["*.py", "*.pyi"],
        "QuantConnect.Orders.Fees": ["*.py", "*.pyi"],
        "QuantConnect.Orders.Fills": ["*.py", "*.pyi"],
        "QuantConnect.Orders.OptionExercise": ["*.py", "*.pyi"],
        "QuantConnect.Orders.Serialization": ["*.py", "*.pyi"],
        "QuantConnect.Orders.Slippage": ["*.py", "*.pyi"],
        "QuantConnect.Orders.TimeInForces": ["*.py", "*.pyi"],
        "QuantConnect.Packets": ["*.py", "*.pyi"],
        "QuantConnect.Parameters": ["*.py", "*.pyi"],
        "QuantConnect.Python": ["*.py", "*.pyi"],
        "QuantConnect.Queues": ["*.py", "*.pyi"],
        "QuantConnect.Report": ["*.py", "*.pyi"],
        "QuantConnect.Report.ReportElements": ["*.py", "*.pyi"],
        "QuantConnect.Research": ["*.py", "*.pyi"],
        "QuantConnect.Scheduling": ["*.py", "*.pyi"],
        "QuantConnect.Securities": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Cfd": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Crypto": ["*.py", "*.pyi"],
        "QuantConnect.Securities.CurrencyConversion": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Equity": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Forex": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Future": ["*.py", "*.pyi"],
        "QuantConnect.Securities.FutureOption": ["*.py", "*.pyi"],
        "QuantConnect.Securities.FutureOption.Api": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Index": ["*.py", "*.pyi"],
        "QuantConnect.Securities.IndexOption": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Interfaces": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Option": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Option.StrategyMatcher": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Positions": ["*.py", "*.pyi"],
        "QuantConnect.Securities.Volatility": ["*.py", "*.pyi"],
        "QuantConnect.Statistics": ["*.py", "*.pyi"],
        "QuantConnect.Storage": ["*.py", "*.pyi"],
        "QuantConnect.Util": ["*.py", "*.pyi"],
        "QuantConnect.Util.RateLimit": ["*.py", "*.pyi"],
        "System": ["*.py", "*.pyi"],
        "System.Buffers": ["*.py", "*.pyi"],
        "System.Buffers.Binary": ["*.py", "*.pyi"],
        "System.Buffers.Text": ["*.py", "*.pyi"],
        "System.CodeDom": ["*.py", "*.pyi"],
        "System.CodeDom.Compiler": ["*.py", "*.pyi"],
        "System.Collections": ["*.py", "*.pyi"],
        "System.Collections.Concurrent": ["*.py", "*.pyi"],
        "System.Collections.Generic": ["*.py", "*.pyi"],
        "System.Collections.Immutable": ["*.py", "*.pyi"],
        "System.Collections.ObjectModel": ["*.py", "*.pyi"],
        "System.Collections.Specialized": ["*.py", "*.pyi"],
        "System.ComponentModel": ["*.py", "*.pyi"],
        "System.ComponentModel.DataAnnotations": ["*.py", "*.pyi"],
        "System.ComponentModel.DataAnnotations.Schema": ["*.py", "*.pyi"],
        "System.ComponentModel.Design": ["*.py", "*.pyi"],
        "System.ComponentModel.Design.Serialization": ["*.py", "*.pyi"],
        "System.Configuration": ["*.py", "*.pyi"],
        "System.Configuration.Assemblies": ["*.py", "*.pyi"],
        "System.Diagnostics": ["*.py", "*.pyi"],
        "System.Diagnostics.CodeAnalysis": ["*.py", "*.pyi"],
        "System.Diagnostics.Contracts": ["*.py", "*.pyi"],
        "System.Diagnostics.SymbolStore": ["*.py", "*.pyi"],
        "System.Diagnostics.Tracing": ["*.py", "*.pyi"],
        "System.Drawing": ["*.py", "*.pyi"],
        "System.Globalization": ["*.py", "*.pyi"],
        "System.IO": ["*.py", "*.pyi"],
        "System.IO.Enumeration": ["*.py", "*.pyi"],
        "System.IO.Strategies": ["*.py", "*.pyi"],
        "System.Linq": ["*.py", "*.pyi"],
        "System.Net": ["*.py", "*.pyi"],
        "System.Net.Cache": ["*.py", "*.pyi"],
        "System.Net.NetworkInformation": ["*.py", "*.pyi"],
        "System.Net.Security": ["*.py", "*.pyi"],
        "System.Net.Sockets": ["*.py", "*.pyi"],
        "System.Numerics": ["*.py", "*.pyi"],
        "System.Numerics.Hashing": ["*.py", "*.pyi"],
        "System.Reflection": ["*.py", "*.pyi"],
        "System.Reflection.Emit": ["*.py", "*.pyi"],
        "System.Reflection.Metadata": ["*.py", "*.pyi"],
        "System.Resources": ["*.py", "*.pyi"],
        "System.Runtime": ["*.py", "*.pyi"],
        "System.Runtime.CompilerServices": ["*.py", "*.pyi"],
        "System.Runtime.ConstrainedExecution": ["*.py", "*.pyi"],
        "System.Runtime.ExceptionServices": ["*.py", "*.pyi"],
        "System.Runtime.InteropServices": ["*.py", "*.pyi"],
        "System.Runtime.InteropServices.ComTypes": ["*.py", "*.pyi"],
        "System.Runtime.InteropServices.ObjectiveC": ["*.py", "*.pyi"],
        "System.Runtime.Intrinsics": ["*.py", "*.pyi"],
        "System.Runtime.Intrinsics.Arm": ["*.py", "*.pyi"],
        "System.Runtime.Intrinsics.X86": ["*.py", "*.pyi"],
        "System.Runtime.Loader": ["*.py", "*.pyi"],
        "System.Runtime.Remoting": ["*.py", "*.pyi"],
        "System.Runtime.Serialization": ["*.py", "*.pyi"],
        "System.Runtime.Versioning": ["*.py", "*.pyi"],
        "System.Security": ["*.py", "*.pyi"],
        "System.Security.Authentication": ["*.py", "*.pyi"],
        "System.Security.Authentication.ExtendedProtection": ["*.py", "*.pyi"],
        "System.Security.Cryptography": ["*.py", "*.pyi"],
        "System.Security.Permissions": ["*.py", "*.pyi"],
        "System.Security.Principal": ["*.py", "*.pyi"],
        "System.Text": ["*.py", "*.pyi"],
        "System.Text.Unicode": ["*.py", "*.pyi"],
        "System.Threading": ["*.py", "*.pyi"],
        "System.Threading.Tasks": ["*.py", "*.pyi"],
        "System.Threading.Tasks.Sources": ["*.py", "*.pyi"],
        "System.Timers": ["*.py", "*.pyi"],
        "System.Windows": ["*.py", "*.pyi"],
        "System.Windows.Input": ["*.py", "*.pyi"],
        "System.Windows.Markup": ["*.py", "*.pyi"]
    }
)
