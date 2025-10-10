from ._measure_code_complexity.validate_input_files import validate_input_files
from ._measure_code_complexity.read_source_file import read_source_file
from ._measure_code_complexity.parse_source_code import parse_source_code
from ._measure_code_complexity.calculate_complexity_metric import calculate_complexity_metric
from ._measure_code_complexity.calculate_cyclomatic_complexity import calculate_cyclomatic_complexity

from pydantic import BaseModel, Field
from typing import List


class CollectSourceCodeOutput(BaseModel):
    """Pydantic model for collect_source_code node outputs."""
    source_code_files: List[str] = (
        Field(..., description="List of paths to source code files")
    )


class MeasureCodeComplexityOutput(BaseModel):
    """Pydantic model for measure_code_complexity node outputs."""
    complexity_metrics: List[float] = (
        Field(..., description="List of complexity metrics for each file.")
    )
    cyclomatic_complexity: List[int] = (
        Field(..., description="Cyclomatic complexity values for each file.")
    )


def measure_code_complexity(collect_source_code_input: CollectSourceCodeOutput, **kwargs) -> MeasureCodeComplexityOutput:
    """
    Calculates code complexity metrics for a list of source code files.

    Parameters
    ----------
    source_code_files : List[str]
        List of paths to source code files as provided by the
        'collect_source_code' node.

    Returns
    -------
    Tuple[List[float], List[int]]
        A tuple containing two lists: the first list contains complexity
        metrics for each file, and the second list contains cyclomatic
        complexity values for each file.

    Raises
    ------
    FileNotFoundError
        If any of the source code files listed in 'source_code_files' do not
        exist.
    ValueError
        If the input 'source_code_files' is empty or not a list.

    Examples
    --------
    >>> source_code_files = ['/path/to/file1.py', '/path/to/file2.py']
    >>> complexity_metrics, cyclomatic_complexity =
    measure_code_complexity(source_code_files)
    [0.5, 0.7]
    [3, 5]

    >>> source_code_files = ['/path/to/file3.py']
    >>> complexity_metrics, cyclomatic_complexity =
    measure_code_complexity(source_code_files)
    [0.3]
    [2]

    """
    source_files: List[str] = collect_source_code_input.source_code_files
    
    validate_input_files(source_files=source_files)
    
    complexity_metrics: List[float] = []
    cyclomatic_complexity: List[int] = []
    
    for file_path in source_files:
        file_content: str = read_source_file(file_path=file_path)
        parsed_ast = parse_source_code(content=file_content)
        
        complexity_metric: float = calculate_complexity_metric(ast=parsed_ast)
        cyclomatic_value: int = calculate_cyclomatic_complexity(ast=parsed_ast)
        
        complexity_metrics.append(complexity_metric)
        cyclomatic_complexity.append(cyclomatic_value)
    
    return MeasureCodeComplexityOutput(
        complexity_metrics=complexity_metrics,
        cyclomatic_complexity=cyclomatic_complexity
    )