from typing import ClassVar, Dict, Iterator, List, Sequence, Optional, Union
from numpy.typing import ArrayLike as _ArrayLike
from logging import Logger

class ArrayStruct:
    def __init__(self) -> None: ...

class BalanceType:
    __members__: ClassVar[Dict[str, BalanceType]] = ...  # read-only
    PROPORTIONAL_TO_CONFORM_LOAD: ClassVar[BalanceType] = ...
    PROPORTIONAL_TO_GENERATION_P: ClassVar[BalanceType] = ...
    PROPORTIONAL_TO_GENERATION_P_MAX: ClassVar[BalanceType] = ...
    PROPORTIONAL_TO_LOAD: ClassVar[BalanceType] = ...
    PROPORTIONAL_TO_GENERATION_REMAINING_MARGIN: ClassVar[BalanceType] = ...
    PROPORTIONAL_TO_GENERATION_PARTICIPATION_FACTOR: ClassVar[BalanceType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class ConnectedComponentMode:
    __members__: ClassVar[Dict[str, ConnectedComponentMode]] = ...  # read-only
    ALL: ClassVar[ConnectedComponentMode] = ...
    MAIN: ClassVar[ConnectedComponentMode] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class ContingencyContextType:
    __members__: ClassVar[Dict[str, ContingencyContextType]] = ...  # read-only
    ALL: ClassVar[ContingencyContextType] = ...
    NONE: ClassVar[ContingencyContextType] = ...
    SPECIFIC: ClassVar[ContingencyContextType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class PostContingencyResult:
    @property
    def contingency_id(self) -> str: ...
    @property
    def limit_violations(self) -> LimitViolationArray: ...
    @property
    def status(self) -> PostContingencyComputationStatus: ...

class PreContingencyResult:
    @property
    def limit_violations(self) -> LimitViolationArray: ...
    @property
    def status(self) -> LoadFlowComponentStatus: ...

class PostContingencyResultArray:
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class ElementType:
    __members__: ClassVar[Dict[str, ElementType]] = ...  # read-only
    ALIAS: ClassVar[ElementType] = ...
    BATTERY: ClassVar[ElementType] = ...
    BRANCH: ClassVar[ElementType] = ...
    BUS: ClassVar[ElementType] = ...
    BUSBAR_SECTION: ClassVar[ElementType] = ...
    DANGLING_LINE: ClassVar[ElementType] = ...
    TIE_LINE: ClassVar[ElementType] = ...
    GENERATOR: ClassVar[ElementType] = ...
    HVDC_LINE: ClassVar[ElementType] = ...
    IDENTIFIABLE: ClassVar[ElementType] = ...
    INJECTION: ClassVar[ElementType] = ...
    LCC_CONVERTER_STATION: ClassVar[ElementType] = ...
    OPERATIONAL_LIMITS: ClassVar[ElementType] = ...
    LINE: ClassVar[ElementType] = ...
    LINEAR_SHUNT_COMPENSATOR_SECTION: ClassVar[ElementType] = ...
    LOAD: ClassVar[ElementType] = ...
    MINMAX_REACTIVE_LIMITS: ClassVar[ElementType] = ...
    NON_LINEAR_SHUNT_COMPENSATOR_SECTION: ClassVar[ElementType] = ...
    PHASE_TAP_CHANGER: ClassVar[ElementType] = ...
    PHASE_TAP_CHANGER_STEP: ClassVar[ElementType] = ...
    RATIO_TAP_CHANGER: ClassVar[ElementType] = ...
    RATIO_TAP_CHANGER_STEP: ClassVar[ElementType] = ...
    REACTIVE_CAPABILITY_CURVE_POINT: ClassVar[ElementType] = ...
    SHUNT_COMPENSATOR: ClassVar[ElementType] = ...
    STATIC_VAR_COMPENSATOR: ClassVar[ElementType] = ...
    SUBSTATION: ClassVar[ElementType] = ...
    SWITCH: ClassVar[ElementType] = ...
    TERMINAL: ClassVar[ElementType] = ...
    THREE_WINDINGS_TRANSFORMER: ClassVar[ElementType] = ...
    TWO_WINDINGS_TRANSFORMER: ClassVar[ElementType] = ...
    VOLTAGE_LEVEL: ClassVar[ElementType] = ...
    VSC_CONVERTER_STATION: ClassVar[ElementType] = ...
    SUB_NETWORK: ClassVar[ElementType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class NetworkModificationType:
    __members__: ClassVar[Dict[str, NetworkModificationType]] = ...  # read-only
    VOLTAGE_LEVEL_TOPOLOGY_CREATION: ClassVar[NetworkModificationType] = ...
    CREATE_COUPLING_DEVICE: ClassVar[NetworkModificationType] = ...
    CREATE_FEEDER_BAY: ClassVar[NetworkModificationType] = ...
    CREATE_LINE_FEEDER: ClassVar[NetworkModificationType] = ...
    CREATE_TWO_WINDINGS_TRANSFORMER_FEEDER: ClassVar[NetworkModificationType] = ...
    CREATE_LINE_ON_LINE: ClassVar[NetworkModificationType] = ...
    REVERT_CREATE_LINE_ON_LINE: ClassVar[NetworkModificationType] = ...
    CONNECT_VOLTAGE_LEVEL_ON_LINE: ClassVar[NetworkModificationType] = ...
    REVERT_CONNECT_VOLTAGE_LEVEL_ON_LINE: ClassVar[NetworkModificationType] = ...
    REPLACE_TEE_POINT_BY_VOLTAGE_LEVEL_ON_LINE: ClassVar[NetworkModificationType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class RemoveModificationType:
    __members__: ClassVar[Dict[str, RemoveModificationType]] = ...  # read-only
    REMOVE_FEEDER: ClassVar[RemoveModificationType] = ...
    REMOVE_VOLTAGE_LEVEL: ClassVar[RemoveModificationType] = ...
    REMOVE_HVDC_LINE: ClassVar[RemoveModificationType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class FilterAttributesType:
    __members__: ClassVar[Dict[str, FilterAttributesType]] = ...  # read-only
    ALL_ATTRIBUTES: ClassVar[FilterAttributesType] = ...
    DEFAULT_ATTRIBUTES: ClassVar[FilterAttributesType] = ...
    SELECTION_ATTRIBUTES: ClassVar[FilterAttributesType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class JavaHandle:
    ...

class Dataframe:
    ...

class SldParameters:
    use_name: bool
    center_name: bool
    diagonal_label: bool
    nodes_infos: bool
    topological_coloring: bool
    component_library: str
    def __init__(self) -> None: ...

class LimitType:
    __members__: ClassVar[Dict[str, LimitType]] = ...  # read-only
    CURRENT: ClassVar[LimitType] = ...
    HIGH_VOLTAGE: ClassVar[LimitType] = ...
    LOW_VOLTAGE: ClassVar[LimitType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class LimitViolation:
    @property
    def acceptable_duration(self) -> int: ...
    @property
    def limit(self) -> float: ...
    @property
    def limit_name(self) -> str: ...
    @property
    def limit_reduction(self) -> float: ...
    @property
    def limit_type(self) -> LimitType: ...
    @property
    def side(self) -> Side: ...
    @property
    def subject_id(self) -> str: ...
    @property
    def subject_name(self) -> str: ...
    @property
    def value(self) -> float: ...

class LimitViolationArray:
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class LoadFlowComponentResult:
    @property
    def connected_component_num(self) -> int: ...
    @property
    def iteration_count(self) -> int: ...
    @property
    def slack_bus_active_power_mismatch(self) -> float: ...
    @property
    def distributed_active_power(self) -> float: ...
    @property
    def slack_bus_id(self) -> str: ...
    @property
    def status(self) -> LoadFlowComponentStatus: ...
    @property
    def synchronous_component_num(self) -> int: ...

class LoadFlowComponentResultArray:
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class LoadFlowComponentStatus:
    __members__: ClassVar[Dict[str, LoadFlowComponentStatus]] = ...  # read-only
    CONVERGED: ClassVar[LoadFlowComponentStatus] = ...
    FAILED: ClassVar[LoadFlowComponentStatus] = ...
    MAX_ITERATION_REACHED: ClassVar[LoadFlowComponentStatus] = ...
    SOLVER_FAILED: ClassVar[LoadFlowComponentStatus] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class PostContingencyComputationStatus:
    __members__: ClassVar[Dict[str, PostContingencyComputationStatus]] = ...  # read-only
    CONVERGED: ClassVar[PostContingencyComputationStatus] = ...
    FAILED: ClassVar[PostContingencyComputationStatus] = ...
    MAX_ITERATION_REACHED: ClassVar[PostContingencyComputationStatus] = ...
    SOLVER_FAILED: ClassVar[PostContingencyComputationStatus] = ...
    NO_IMPACT: ClassVar[PostContingencyComputationStatus] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class LoadFlowParameters:
    balance_type: BalanceType
    connected_component_mode: ConnectedComponentMode
    countries_to_balance: Sequence[str]
    dc_use_transformer_ratio: bool
    distributed_slack: bool
    no_generator_reactive_limits: bool
    phase_shifter_regulation_on: bool
    read_slack_bus: bool
    simul_shunt: bool
    transformer_voltage_control_on: bool
    twt_split_shunt_admittance: bool
    voltage_init_mode: VoltageInitMode
    write_slack_bus: bool
    provider_parameters_keys: List[str]
    provider_parameters_values: List[str]
    def __init__(self) -> None: ...

class LoadFlowValidationParameters:
    threshold: float
    verbose: bool
    loadflow_name: str
    epsilon_x: float
    apply_reactance_correction: bool
    loadflow_parameters: LoadFlowParameters
    ok_missing_values: bool
    no_requirement_if_reactive_bound_inversion: bool
    compare_results: bool
    check_main_component_only: bool
    no_requirement_if_setpoint_outside_power_bounds: bool
    def __init__(self) -> None: ...

class SecurityAnalysisParameters:
    loadflow_parameters: LoadFlowParameters
    flow_proportional_threshold: float
    low_voltage_proportional_threshold: float
    low_voltage_absolute_threshold: float
    high_voltage_proportional_threshold: float
    high_voltage_absolute_threshold: float
    provider_parameters_keys: List[str]
    provider_parameters_values: List[str]
    def __init__(self) -> None: ...

class SensitivityAnalysisParameters:
    loadflow_parameters: LoadFlowParameters
    provider_parameters_keys: List[str]
    provider_parameters_values: List[str]
    def __init__(self) -> None: ...

class Matrix:
    ...

class NetworkMetadata:
    @property
    def case_date(self) -> float: ...
    @property
    def forecast_distance(self) -> int: ...
    @property
    def id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def source_format(self) -> str: ...

class PyPowsyblError(Exception): ...

class Series:
    @property
    def data(self) -> object: ...
    @property
    def index(self) -> bool: ...
    @property
    def name(self) -> str: ...

class SeriesArray:
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class SeriesMetadata:
    def __init__(self, arg0: str, arg1: int, arg2: bool, arg3: bool, arg4: bool) -> None: ...
    @property
    def is_index(self) -> bool: ...
    @property
    def is_modifiable(self) -> bool: ...
    @property
    def is_default(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> int: ...

class Side:
    __members__: ClassVar[Dict[str, Side]] = ...  # read-only
    NONE: ClassVar[Side] = ...
    ONE: ClassVar[Side] = ...
    TWO: ClassVar[Side] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class ValidationLevel:
    __members__: ClassVar[Dict[str, ValidationLevel]] = ...  # read-only
    EQUIPMENT: ClassVar[ValidationLevel] = ...
    STEADY_STATE_HYPOTHESIS: ClassVar[ValidationLevel] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class ValidationType:
    __members__: ClassVar[Dict[str, ValidationType]] = ...  # read-only
    ALL: ClassVar[list] = ...
    BUSES: ClassVar[ValidationType] = ...
    FLOWS: ClassVar[ValidationType] = ...
    GENERATORS: ClassVar[ValidationType] = ...
    SHUNTS: ClassVar[ValidationType] = ...
    SVCS: ClassVar[ValidationType] = ...
    TWTS: ClassVar[ValidationType] = ...
    TWTS3W: ClassVar[ValidationType] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class VoltageInitMode:
    __members__: ClassVar[Dict[str, VoltageInitMode]] = ...  # read-only
    DC_VALUES: ClassVar[VoltageInitMode] = ...
    PREVIOUS_VALUES: ClassVar[VoltageInitMode] = ...
    UNIFORM_VALUES: ClassVar[VoltageInitMode] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class Zone:
    def __init__(self, id: str, injections_ids: List[str], injections_shift_keys: List[float]) -> None: ...

class FlowDecompositionParameters:
    enable_losses_compensation: bool
    losses_compensation_epsilon: float
    sensitivity_epsilon: float
    rescale_enabled: bool
    dc_fallback_enabled_after_ac_divergence: bool
    sensitivity_variable_batch_size: int
    def __init__(self) -> None: ...


class BranchSide:
    __members__: ClassVar[Dict[str, BranchSide]] = ...  # read-only
    ONE: ClassVar[BranchSide] = ...
    TWO: ClassVar[BranchSide] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class DynamicMappingType:
    __members__: ClassVar[Dict[str, DynamicMappingType]] = ...  # read-only
    ALPHA_BETA_LOAD: ClassVar[DynamicMappingType] = ...
    ONE_TRANSFORMER_LOAD: ClassVar[DynamicMappingType] = ...
    OMEGA_REF: ClassVar[DynamicMappingType] = ...
    GENERATOR_SYNCHRONOUS: ClassVar[DynamicMappingType] = ...
    GENERATOR_SYNCHRONOUS_THREE_WINDINGS: ClassVar[DynamicMappingType] = ...
    GENERATOR_SYNCHRONOUS_THREE_WINDINGS_PROPORTIONAL_REGULATIONS: ClassVar[
        DynamicMappingType] = ...
    GENERATOR_SYNCHRONOUS_FOUR_WINDINGS: ClassVar[DynamicMappingType] = ...
    GENERATOR_SYNCHRONOUS_FOUR_WINDINGS_PROPORTIONAL_REGULATIONS: ClassVar[
        DynamicMappingType] = ...
    CURRENT_LIMIT_AUTOMATON: ClassVar[DynamicMappingType] = ...


class VoltageInitializerStatus:
    __members__: ClassVar[Dict[str,
                               VoltageInitializerStatus]] = ...  # read-only
    OK: ClassVar[VoltageInitializerStatus] = ...
    NOT_OK: ClassVar[VoltageInitializerStatus] = ...


class VoltageInitializerObjective:
    __members__: ClassVar[Dict[str,
                               VoltageInitializerObjective]] = ...  # read-only
    MIN_GENERATION: ClassVar[VoltageInitializerObjective] = ...
    BETWEEN_HIGH_AND_LOW_VOLTAGE_LIMIT: ClassVar[VoltageInitializerObjective] = ...
    SPECIFIC_VOLTAGE_PROFILE: ClassVar[VoltageInitializerObjective] = ...

class DefaultXnecProvider:
    __members__: ClassVar[Dict[str, DefaultXnecProvider]] = ...  # read-only
    GT_5_PERC_ZONE_TO_ZONE_PTDF: ClassVar[DefaultXnecProvider] = ...
    ALL_BRANCHES: ClassVar[DefaultXnecProvider] = ...
    INTERCONNECTIONS: ClassVar[DefaultXnecProvider] = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, arg0: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, arg0: object) -> bool: ...
    def __setstate__(self, arg0: int) -> None: ...
    @property
    def name(self) -> str: ...

class ShortCircuitStudyType:
    __members__: ClassVar[Dict[str, ShortCircuitStudyType]] = ...  # read-only
    SUB_TRANSIENT: ClassVar[ShortCircuitStudyType] = ...
    TRANSIENT: ClassVar[ShortCircuitStudyType] = ...
    STEADY_STATE: ClassVar[ShortCircuitStudyType] = ...

class ShortCircuitFaultType:
    __members__: ClassVar[Dict[str, ShortCircuitFaultType]] = ...  # read-only
    BUS_FAULT: ClassVar[ShortCircuitFaultType] = ...
    BRANCH_FAULT: ClassVar[ShortCircuitFaultType] = ...

class ShortCircuitAnalysisParameters:
    with_voltage_result: bool
    with_feeder_result: bool
    with_limit_violations: bool
    study_type: ShortCircuitStudyType
    with_fortescue_result: bool
    min_voltage_drop_proportional_threshold: float
    provider_parameters_keys: List[str]
    provider_parameters_values: List[str]
    def __init__(self) -> None: ...


def add_contingency(analysis_context: JavaHandle, contingency_id: str, elements_ids: List[str]) -> None: ...
def add_monitored_elements(security_analysis_context: JavaHandle, contingency_context_type: ContingencyContextType, branch_ids: List[str], voltage_level_ids: List[str], three_windings_transformer_ids: List[str], contingency_ids: List[str]) -> None: ...
def clone_variant(network: JavaHandle, src: str, variant: str, may_overwrite: bool) -> None: ...
def create_dataframe(columns_values: list, columns_names: List[str], columns_types: List[int], is_index: List[bool]) -> Dataframe: ...
def create_element(network: JavaHandle, dataframes: List[Optional[Dataframe]], element_type: ElementType) -> None: ...
def create_exporter_parameters_series_array(format: str) -> SeriesArray: ...
def create_importer_parameters_series_array(format: str) -> SeriesArray: ...
def create_network(name: str, id: str) -> JavaHandle: ...
def create_network_elements_series_array(network: JavaHandle, element_type: ElementType, filter_attributes_type: FilterAttributesType, attributes: List[str], array: Optional[Dataframe]) -> SeriesArray: ...
def create_network_elements_extension_series_array(network: JavaHandle, extension_name: str, table_name: str) -> SeriesArray: ...
def get_extensions_names() -> List[str]: ...
def get_extensions_information() -> SeriesArray: ...
def create_security_analysis() -> JavaHandle: ...
def create_sensitivity_analysis() -> JavaHandle: ...
def save_network(network: JavaHandle, file: str, format: str, parameters: Dict[str,str], report: Optional[JavaHandle]) -> None: ...
def save_network_to_string(network: JavaHandle, format: str, parameters: Dict[str,str], report: Optional[JavaHandle]) -> str: ...
def save_network_to_binary_buffer(network: JavaHandle, format: str, parameters: Dict[str,str], report: Optional[JavaHandle]) -> bytes: ...
def get_branch_flows_sensitivity_matrix(sensitivity_analysis_result_context: JavaHandle, matrix_id: str, contingency_id: str) -> Matrix: ...
def get_branch_results(result: JavaHandle) -> SeriesArray: ...
def get_bus_breaker_view_buses(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_bus_breaker_view_elements(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_bus_breaker_view_switches(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_bus_results(result: JavaHandle) -> SeriesArray: ...
def get_bus_voltages_sensitivity_matrix(sensitivity_analysis_result_context: JavaHandle, contingency_id: str) -> Matrix: ...
def get_loadflow_provider_parameters_names(provider: str) -> List[str]: ...
def create_loadflow_provider_parameters_series_array(provider: str) -> SeriesArray: ...
def get_security_analysis_provider_parameters_names(provider: str) -> List[str]: ...
def get_sensitivity_analysis_provider_parameters_names(provider: str) -> List[str]: ...
def get_limit_violations(result: JavaHandle) -> SeriesArray: ...
def get_network_area_diagram_svg(network: JavaHandle, voltage_level_ids:  Union[str, List[str]], depth: int, high_nominal_voltage_bound: float, low_nominal_voltage_bound: float, edge_name_displayed: bool) -> str: ...
def get_network_area_diagram_displayed_voltage_levels(network: JavaHandle, voltage_level_ids:  Union[str, List[str]], depth: int) -> List[str]: ...
def get_network_elements_ids(network: JavaHandle, element_type: ElementType, nominal_voltages: List[float], countries: List[str], main_connected_component: bool, main_synchronous_component: bool, not_connected_to_same_bus_at_both_sides: bool) -> List[str]: ...
def get_network_export_formats() -> List[str]: ...
def get_network_import_formats() -> List[str]: ...
def get_loadflow_provider_names() -> List[str]: ...
def get_security_analysis_provider_names() -> List[str]: ...
def get_sensitivity_analysis_provider_names() -> List[str]: ...
def get_network_metadata(network: JavaHandle) -> NetworkMetadata: ...
def get_node_breaker_view_internal_connections(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_node_breaker_view_nodes(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_node_breaker_view_switches(network: JavaHandle, voltage_level: str) -> SeriesArray: ...
def get_reference_flows(sensitivity_analysis_result_context: JavaHandle, matrix_id: str, contingency_id: str) -> Matrix: ...
def get_reference_voltages(sensitivity_analysis_result_context: JavaHandle, contingency_id: str) -> Matrix: ...
def get_post_contingency_results(result: JavaHandle) -> PostContingencyResultArray: ...
def get_pre_contingency_result(result: JavaHandle) -> PreContingencyResult: ...
def get_network_elements_dataframe_metadata(element_type: ElementType) -> List[SeriesMetadata]: ...
def get_network_elements_creation_dataframes_metadata(element_type: ElementType) -> List[List[SeriesMetadata]]: ...
def get_single_line_diagram_svg(network: JavaHandle, container_id: str) -> str: ...
def get_single_line_diagram_svg_and_metadata(network: JavaHandle, container_id: str, parameters: SldParameters   ) -> List[str]: ...
def get_three_windings_transformer_results(result: JavaHandle) -> SeriesArray: ...
def get_validation_level(network: JavaHandle) -> ValidationLevel: ...
def get_variant_ids(network: JavaHandle) -> List[str]: ...
def get_version_table() -> str: ...
def get_working_variant_id(network: JavaHandle) -> str: ...
def add_branch_flow_factor_matrix(sensitivity_analysis_context: JavaHandle, matrix_id: str, branches_ids: List[str], variables_ids: List[str]) -> None: ...
def add_precontingency_branch_flow_factor_matrix(sensitivity_analysis_context: JavaHandle, matrix_id: str, branches_ids: List[str], variables_ids: List[str]) -> None: ...
def add_postcontingency_branch_flow_factor_matrix(sensitivity_analysis_context: JavaHandle, matrix_id: str, branches_ids: List[str], variables_ids: List[str], contingencies_ids: List[str]) -> None: ...
def is_config_read() -> bool: ...
def get_default_loadflow_provider() -> str: ...
def get_default_security_analysis_provider() -> str: ...
def get_default_sensitivity_analysis_provider() -> str: ...
def load_network(file: str, parameters: Dict[str,str], report: Optional[JavaHandle]) -> JavaHandle: ...
def load_network_from_string(file_name: str, file_content: str, parameters: Dict[str,str], report: Optional[JavaHandle]) -> JavaHandle: ...
def load_network_from_binary_buffers(file_content: List[memoryview], parameters: Dict[str,str], report: Optional[JavaHandle]) -> JavaHandle: ...
def merge(networks: List[JavaHandle]) -> JavaHandle: ...
def get_sub_network(network: JavaHandle, sub_network_id: str) -> JavaHandle: ...
def detach_sub_network(network: JavaHandle) -> JavaHandle: ...
def reduce_network(network: JavaHandle, v_min: float, v_max: float, ids: List[str], vls: List[str], depths: List[int], with_dangling_lines: bool) -> None: ...
def remove_elements(network: JavaHandle, element_ids: List[str]) -> None: ...
def remove_variant(network: JavaHandle, variant: str) -> None: ...
def run_loadflow(network: JavaHandle, dc: bool, parameters: LoadFlowParameters, provider: str, report: Optional[JavaHandle]) -> LoadFlowComponentResultArray: ...
def run_loadflow_validation(network: JavaHandle, validation_type: ValidationType, validation_parameters: LoadFlowValidationParameters) -> SeriesArray: ...
def run_security_analysis(security_analysis_context: JavaHandle, network: JavaHandle, parameters: SecurityAnalysisParameters, provider: str, dc: bool, report: Optional[JavaHandle]) -> JavaHandle: ...
def run_sensitivity_analysis(sensitivity_analysis_context: JavaHandle, network: JavaHandle, dc: bool, parameters: SensitivityAnalysisParameters, provider: str, report: Optional[JavaHandle]) -> JavaHandle: ...
def set_branch_flow_factor_matrix(sensitivity_analysis_context: JavaHandle, branches_ids: List[str], variables_ids: List[str]) -> None: ...
def set_bus_voltage_factor_matrix(sensitivity_analysis_context: JavaHandle, bus_ids: List[str], target_voltage_ids: List[str]) -> None: ...
def set_config_read(arg0: bool) -> None: ...
def set_logger(logger: Logger) -> None: ...
def set_default_loadflow_provider(provider: str) -> None: ...
def set_default_security_analysis_provider(provider: str) -> None: ...
def set_default_sensitivity_analysis_provider(provider: str) -> None: ...
def set_java_library_path(arg0: str) -> None: ...
def set_min_validation_level(network: JavaHandle, validation_level: ValidationLevel) -> None: ...
def set_working_variant(network: JavaHandle, variant: str) -> None: ...
def set_zones(sensitivity_analysis_context: JavaHandle, zones: List[Zone]) -> None: ...
def get_logger() -> Logger: ...
def update_connectable_status(arg0: JavaHandle, arg1: str, arg2: bool) -> bool: ...
def update_network_elements_with_series(network: JavaHandle, array: Dataframe, element_type: ElementType) -> None: ...
def update_switch_position(arg0: JavaHandle, arg1: str, arg2: bool) -> bool: ...
def validate(network: JavaHandle) -> ValidationLevel: ...
def write_network_area_diagram_svg(network: JavaHandle, svg_file: str, voltage_level_ids:  Union[str, List[str]], depth: int, high_nominal_voltage_bound: float, low_nominal_voltage_bound: float, edge_name_displayed: bool) -> None: ...
def write_single_line_diagram_svg(network: JavaHandle, container_id: str, svg_file: str, metadata_file: str, parameters: SldParameters) -> None: ...
def add_network_element_properties(network: JavaHandle, dataframe: Dataframe) -> None: ...
def remove_network_element_properties(network: JavaHandle, ids: List[str], properties: List[str]) -> None: ...
def get_network_extensions_dataframe_metadata(name: str, table_name: str) -> List[SeriesMetadata]: ...
def remove_extensions(network: JavaHandle, name: str, ids: List[str]) -> None: ...
def update_extensions(network: JavaHandle, name: str, table_name: str, dataframe: Dataframe) -> None: ...
def get_network_extensions_creation_dataframes_metadata(name: str) -> List[List[SeriesMetadata]]: ...
def create_extensions(network: JavaHandle, dataframes: List[Optional[Dataframe]], name: str) -> None: ...
def create_reporter_model(task_key: str, default_name: str) -> JavaHandle: ...
def print_report(reporter_model: JavaHandle) -> str: ...
def json_report(reporter_model: JavaHandle) -> str: ...
def create_glsk_document(file: str) -> JavaHandle: ...
def get_glsk_factors_start_timestamp(importer: JavaHandle) -> int: ...
def get_glsk_factors_end_timestamp(importer: JavaHandle) -> int: ...
def get_glsk_countries(importer: JavaHandle) -> List[str]: ...
def get_glsk_injection_keys(network: JavaHandle, importer: JavaHandle, country: str, timestamp: int) -> List[str]: ...
def get_glsk_factors(network: JavaHandle, importer: JavaHandle, country: str, timestamp: int) -> List[float]: ...
def create_flow_decomposition() -> JavaHandle: ...
def add_contingency_for_flow_decomposition(flow_decomposition_context: JavaHandle, contingency_id: str, elements_ids: List[str]) -> None: ...
def add_precontingency_monitored_elements_for_flow_decomposition(flow_decomposition_context: JavaHandle, branch_ids: List[str]) -> None: ...
def add_postcontingency_monitored_elements_for_flow_decomposition(flow_decomposition_context: JavaHandle, branch_ids: List[str], contingency_ids: List[str]) -> None: ...
def add_additional_xnec_provider_for_flow_decomposition(flow_decomposition_context: JavaHandle, default_xnec_provider: DefaultXnecProvider) -> None: ...
def run_flow_decomposition(flow_decomposition_context: JavaHandle, network: JavaHandle, flow_decomposition_parameters: FlowDecompositionParameters, load_flow_parameter: LoadFlowParameters) -> SeriesArray: ...
def connect_voltage_level_on_line(network: JavaHandle, bbs_or_bus_id: str, line_id: str, line1_id: str, line1_name: str, line2_id: str, line2_name: str, position_percent: float) -> None: ...
def revert_connect_voltage_level_on_line(network: JavaHandle, line1_id: str, line2_id: str, line_id: str, line_name: str) -> None: ...
def get_connectables_order_positions(network: JavaHandle, voltage_level_id: str) -> SeriesArray: ...
def get_unused_order_positions(network: JavaHandle, busbar_section_id: str, before_or_after: str) -> List[int]: ...
def remove_aliases(network: JavaHandle, dataframe: Dataframe) -> None: ...
def close() -> None: ...
def create_dynamic_simulation_context() -> JavaHandle: ...
def create_dynamic_model_mapping() -> JavaHandle: ...
def create_timeseries_mapping() -> JavaHandle: ...
def create_event_mapping() -> JavaHandle: ...
def run_dynamic_model(dynamic_model: JavaHandle, network: JavaHandle, dynamic_mapping: JavaHandle, event_mapping: JavaHandle, timeseries_mapping: JavaHandle, start: int, stop: int) -> JavaHandle: ...
def add_all_dynamic_mappings(dynamic_mapping_handle: JavaHandle, mapping_type: DynamicMappingType, mapping_df: Dataframe) -> None: ...
def get_dynamic_mappings_meta_data(mapping_type: DynamicMappingType) -> List[SeriesMetadata]: ...
def add_curve(curve_mapping_handle: JavaHandle, dynamic_id: str, variable: str) -> None: ...
def add_event_branch_disconnection(event_mapping_handle: JavaHandle, static_id: str, event_time: float, disconnect_origin: bool, disconnect_extremity: bool) -> None: ...
def add_event_injection_disconnection(event_mapping_handle: JavaHandle, static_id: str, event_time: float, state_event: bool) -> None: ...
def set_powsybl_config_location(absolute_path_to_config:str, config_file_name: str) -> None: ...
def get_dynamic_simulation_results_status(result_handle: JavaHandle) -> str: ...
def get_dynamic_curve(report_handle: JavaHandle, curve_name: str) -> SeriesArray: ...
def get_all_dynamic_curves_ids(report_handle: JavaHandle) -> List[str]: ...
def remove_elements_modification(network: JavaHandle, connectable_ids: List[str], dataframe: Optional[Dataframe], remove_modification_type: RemoveModificationType, raise_exception: Optional[bool], reporter: Optional[JavaHandle]) -> None: ...
def get_network_modification_metadata(network_modification_type: NetworkModificationType) -> List[SeriesMetadata]: ...
def get_network_modification_metadata_with_element_type(network_modification_type: NetworkModificationType, element_type: ElementType) -> List[List[SeriesMetadata]]: ...
def create_network_modification(network: JavaHandle, dataframes: List[Optional[Dataframe]], network_modification_type: NetworkModificationType, raise_exception: Optional[bool], reporter: Optional[JavaHandle]) -> None: ...
def get_single_line_diagram_component_library_names() -> List[str]: ...
def set_faults(short_circuit_analysis: JavaHandle, dfs: Optional[Dataframe], fault_type: ShortCircuitFaultType) -> None: ...
def get_fault_results(result: JavaHandle) -> SeriesArray: ...
def get_feeder_results(result: JavaHandle) -> SeriesArray: ...
def get_short_circuit_limit_violations(result: JavaHandle) -> SeriesArray: ...
def get_short_circuit_bus_results(result: JavaHandle) -> SeriesArray: ...
def get_faults_dataframes_metadata(faultType: ShortCircuitFaultType) -> List[SeriesMetadata]: ...
def run_shortcircuit_analysis(context: JavaHandle, network: JavaHandle, parameters: ShortCircuitAnalysisParameters, provider: str, reporter: Optional[JavaHandle]) -> JavaHandle: ...
def create_shortcircuit_analysis() -> JavaHandle: ...
def set_default_shortcircuit_analysis_provider(provider: str) -> None: ...
def get_default_shortcircuit_analysis_provider() -> str: ...
def get_shortcircuit_provider_names() -> List[str]: ...
def get_shortcircuit_provider_parameters_names(provider: str) -> List[str]: ...

def create_voltage_initializer_params() -> JavaHandle: ...


def voltage_initializer_add_variable_shunt_compensators(
    params_handle: JavaHandle, id_ptr: str) -> None: ...


def voltage_initializer_add_constant_q_generators(
    params_handle: JavaHandle, id_ptr: str) -> None: ...


def voltage_initializer_add_variable_two_windings_transformers(
    params_handle: JavaHandle, id_ptr: str) -> None: ...


def voltage_initializer_add_specific_low_voltage_limits(
        params_handle: JavaHandle, voltage_level_id: str, is_relative: bool, limit: float) -> None: ...

def voltage_initializer_add_specific_high_voltage_limits(
        params_handle: JavaHandle, voltage_level_id: str, is_relative: bool, limit: float) -> None: ...

def voltage_initializer_add_algorithm_param(
    params_handle: JavaHandle, key_ptr: str, value_ptr: str) -> None: ...


def voltage_initializer_set_objective(
    params_handle: JavaHandle, objective: VoltageInitializerObjective) -> None: ...


def voltage_initializer_set_objective_distance(
    params_handle: JavaHandle, dist: float) -> None: ...


def run_voltage_initializer(
    debug: bool, network_handle: JavaHandle, params_handle: JavaHandle) -> JavaHandle: ...


def voltage_initializer_apply_all_modifications(
    result_handle: JavaHandle, network_handle: JavaHandle) -> None: ...


def voltage_initializer_get_status(
    result_handle: JavaHandle) -> VoltageInitializerStatus: ...


def voltage_initializer_get_indicators(
    result_handle: JavaHandle) -> Dict[str, str]: ...
