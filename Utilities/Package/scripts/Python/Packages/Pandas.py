# coding: utf-8



get_ipython().run_line_magic('run', '"../Configuration/PackageLoader.ipynb"')


# # [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)

# # 10 minutes to pandas

# ## Basic data structures in pandas

# - Series
# - Dataframe

# ## Object creation



# Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s




# DataFrame
dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df




df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }, 
)

df2




df2.dtypes


# ## Viewing data



df.head()




df.tail()




df.index




df.columns




df.to_numpy()




df2.dtypes




df2.to_numpy()




df.describe()




df.T




df.sort_index(axis = 1, ascending = False)




df.sort_values(by = "B")


# ## Selection

# ### Getitem ([])



df['A']




df[0:3]




df["20130102":"20130104"]


# ### Selection by label



df.loc[dates[0]]




df.loc[:, ["A", "B"]]




df.loc["20130102":"20130104", ["A", "B"]]




df.loc[dates[0], "A"]




df.at[dates[0], "A"]


# ### Selection by position



df.iloc[3]




df.iloc[3:5, 0:2]




df.iloc[[1, 2, 4], [0, 2]]




df.iloc[1:3, :]




df.iloc[:, 1:3]




df.iloc[1, 1]




df.iat[1, 1]


# ### Boolean indexing



df[df["A"] > 0]




df[df > 0]




df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
df2[df2["E"].isin(["two", "four"])]


# ### Setting



s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
df["F"] = s1
df




df.at[dates[0], "A"] = 0
df




df.iat[0, 1] = 0
df




df.loc[:, "D"] = np.array([5] * len(df))
df




df2 = df.copy()
df2[df2 > 0] = -df2
df2


# ## Missing data






# ## Operations






# ## Merge






# ## Grouping






# ## Reshaping






# ## Time series






# ## Categoricals






# ## Plotting






# ## Importing and exporting data






# ## Gotchas






# # Intro to data structures

# ## Series






# ## DataFrame






# # Essential basic functionality

# ## Head and tail






# ## Attributes and underlying data






# ## Accelerated operations






# ## Flexible binary operations






# ## Descriptive statistics






# ## Function application






# ## Reindexing and altering labels






# ## Iteration






# ## .dt accessor






# ## Vectorized string methods






# ## Sorting






# ## Copying






# ## dtypes






# ## Selecting columns based on dtype






# # IO tools (text, CSV, HDF5, …)

# ## CSV & text files






# ## JSON






# ## HTML






# ## LaTeX






# ## XML






# ## Excel files






# ## OpenDocument Spreadsheets






# ## Binary Excel (.xlsb) files






# ## Calamine (Excel and ODS files)






# ## Clipboard






# ## Pickling






# ## msgpack






# ## HDF5 (PyTables)






# ## Feather






# ## Parquet






# ## ORC






# ## SQL queries






# ## Google BigQuery






# ## Stata format






# ## SAS formats






# ## SPSS formats






# ## Other file formats






# ## Performance considerations






# # PyArrow Functionality

# ## Data Structure Integration






# ## Operations






# ## I/O Reading






# # Indexing and selecting data

# ## Different choices for indexing






# ## Basics






# ## Attribute access






# ## Slicing ranges






# ## Selection by label






# ## Selection by position






# ## Selection by callable






# ## Combining positional and label-based indexing






# ## Selecting random samples






# ## Setting with enlargement






# ## Fast scalar value getting and setting






# ## Boolean indexing






# ## Indexing with isin






# ## The where() Method and Masking






# ## Setting with enlargement conditionally using numpy()






# ## The query() Method






# ## Duplicate data






# ## Dictionary-like get() method






# ## Looking up values by index/column labels






# ## Index objects






# ## Set / reset index






# ## Returning a view versus a copy






# # MultiIndex / advanced indexing

# # Hierarchical indexing (MultiIndex)






# # Advanced indexing with hierarchical index






# # Sorting a MultiIndex






# # Take methods






# # Index types






# # Miscellaneous indexing FAQ






# # Copy-on-Write (CoW)

# ## Previous behavior






# ## Migrating to Copy-on-Write






# ## Description






# ## Chained Assignment






# ## Read-only NumPy arrays






# ## Patterns to avoid






# ## Copy-on-Write optimizations






# ## How to enable CoW






# # Merge, join, concatenate and compare

# ## concat()






# ## merge()






# ## DataFrame.join()






# ## merge_ordered()






# ## merge_asof()






# ## compare()






# # Reshaping and pivot tables

# ## pivot() and pivot_table()






# ## stack() and unstack()






# ## melt() and wide_to_long()






# ## get_dummies() and from_dummies()






# ## explode()






# ## crosstab()






# ## cut()






# ## factorize()






# # Working with text data

# ## Text data types






# ## String methods






# ## Splitting and replacing strings






# ## Concatenation






# ## Indexing with .str






# ## Extracting substrings






# ## Testing for strings that match or contain a pattern






# ## Creating indicator variables






# ## Method summary






# # Working with missing data

# ## Values considered “missing”






# ## NA semantics






# ## Inserting missing data






# ## Calculations with missing data






# ## Dropping missing data






# ## Filling missing data






# # Duplicate Labels

# ## Consequences of Duplicate Labels






# ## Duplicate Label Detection






# ## Disallowing Duplicate Labels






# # Categorical data

# ## Object creation






# ## CategoricalDtype






# ## Description






# ## Working with categories






# ## Sorting and order






# ## Comparisons






# ## Operations






# ## Data munging






# ## Getting data in/out






# ## Missing data






# ## Differences to R’s factor






# ## Gotchas






# # Nullable integer data type

# ## Construction






# ## Operations






# ## Scalar NA Value






# # Nullable Boolean data type

# ## Indexing with NA values






# ## Kleene logical operations






# # Chart visualization

# ## Basic plotting: plot






# ## Other plots






# ## Plotting with missing data






# ## Plotting tools






# ## Plot formatting






# ## Plotting directly with Matplotlib






# ## Plotting backends






# # Table Visualization

# ## Styler Object and Customising the Display






# ## Formatting the Display






# ## Styler Object and HTML






# ## Methods to Add Styles






# ## Table Styles






# ## Setting Classes and Linking to External CSS






# ## Styler Functions






# ## Tooltips and Captions






# ## Finer Control with Slicing






# ## Optimization






# ## Builtin Styles






# ## Sharing styles






# ## Limitations






# ## Other Fun and Useful Stuff






# ## Export to Excel






# ## Export to LaTeX






# ## More About CSS and HTML






# ## Extensibility






# # Group by: split-apply-combine

# ## Splitting an object into groups






# ## Iterating through groups






# ## Selecting a group






# ## Aggregation






# ## Transformation






# ## Filtration






# ## Flexible apply






# ## Numba Accelerated Routines






# ## Other useful features






# ## Examples






# # Windowing operations

# ## Overview






# ## Rolling window






# ## Weighted window






# ## Expanding window






# ## Exponentially weighted window






# # Time series / date functionality

# ## Overview






# ## Timestamps vs. time spans






# ## Converting to timestamps






# ## Generating ranges of timestamps






# ## Timestamp limitations






# ## Indexing






# ## Time/date components






# ## DateOffset objects






# ## Time Series-related instance methods






# ## Resampling






# ## Time span representation






# ## Converting between representations






# ## Representing out-of-bounds spans






# ## Time zone handling






# # Time deltas

# ## Parsing






# ## Operations






# ## Reductions






# ## Frequency conversion






# ## Attributes






# ## TimedeltaIndex






# ## Resampling






# # Options and settings

# ## Overview






# ## Available options






# ## Getting and setting options






# ## Setting startup options in Python/IPython environment






# ## Frequently used options






# ## Number formatting






# ## Unicode formatting






# ## Table schema display






# # Enhancing performance

# ## Cython (writing C extensions for pandas)






# ## Numba (JIT compilation)






# ## Expression evaluation via eval()






# # Scaling to large datasets

# ## Load less data






# ## Use efficient datatypes






# ## Use chunking






# ## Use Other Libraries






# # Sparse data structures

# ## SparseArray






# ## SparseDtype






# ## Sparse accessor






# ## Sparse calculation






# ## Interaction with scipy.sparse






# # Frequently Asked Questions (FAQ)

# ## DataFrame memory usage






# ## Using if/truth statements with pandas






# ## Mutating with User Defined Function (UDF) methods






# ## Missing value representation for NumPy types






# ## Differences with NumPy






# ## Thread-safety








Byte-ordering issues







# # Cookbook

# ## Idioms






# ## Selection






# ## Multiindexing






# ## Missing data






# ## Grouping






# ## Timeseries






# ## Merge






# ## Plotting






# ## Data in/out






# ## Computation






# ## Timedeltas






# ## Creating example data






# ## Constant series






# # Sandbox
