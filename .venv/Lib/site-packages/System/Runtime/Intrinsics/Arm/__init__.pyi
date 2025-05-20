from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Numerics
import System.Runtime.Intrinsics
import System.Runtime.Intrinsics.Arm


class ArmBase(System.Object, metaclass=abc.ABCMeta):
    """Provides access to the ARM base hardware instructions via intrinsics."""

    class Arm64(System.Object, metaclass=abc.ABCMeta):
        """Provides access to the ARM base hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def leading_sign_count(value: int) -> int:
            """A64: CLS Wd, Wn"""
            ...

        @staticmethod
        def leading_zero_count(value: int) -> int:
            """A64: CLZ Xd, Xn"""
            ...

        @staticmethod
        def multiply_high(left: int, right: int) -> int:
            """A64: SMULH Xd, Xn, Xm"""
            ...

        @staticmethod
        def reverse_element_bits(value: int) -> int:
            """A64: RBIT Xd, Xn"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def leading_zero_count(value: int) -> int:
        """A32: CLZ Rd, Rm  A64: CLZ Wd, Wn"""
        ...

    @staticmethod
    def reverse_element_bits(value: int) -> int:
        """A32: RBIT Rd, Rm  A64: RBIT Wd, Wn"""
        ...

    @staticmethod
    def Yield() -> None:
        """A32: YIELD  A64: YIELD"""
        ...


class AdvSimd(System.Runtime.Intrinsics.Arm.ArmBase, metaclass=abc.ABCMeta):
    """Provides access to the ARM AdvSIMD hardware instructions via intrinsics."""

    class Arm64(System.Runtime.Intrinsics.Arm.ArmBase.Arm64, metaclass=abc.ABCMeta):
        """Provides access to the ARM AdvSIMD hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        @overload
        def abs(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vabsq_f64 (float64x2_t a)  A64: FABS Vd.2D, Vn.2D"""
            ...

        @staticmethod
        @overload
        def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vabsq_s64 (int64x2_t a)  A64: ABS Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def absolute_compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """uint64x2_t vcagtq_f64 (float64x2_t a, float64x2_t b)  A64: FACGT Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def absolute_compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """uint64x2_t vcageq_f64 (float64x2_t a, float64x2_t b)  A64: FACGE Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def absolute_compare_greater_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """uint64x1_t vcage_f64 (float64x1_t a, float64x1_t b)  A64: FACGE Dd, Dn, Dm"""
            ...

        @staticmethod
        def absolute_compare_greater_than_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """uint64x1_t vcagt_f64 (float64x1_t a, float64x1_t b)  A64: FACGT Dd, Dn, Dm"""
            ...

        @staticmethod
        def absolute_compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """uint64x2_t vcaltq_f64 (float64x2_t a, float64x2_t b)  A64: FACGT Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def absolute_compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """uint64x2_t vcaleq_f64 (float64x2_t a, float64x2_t b)  A64: FACGE Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def absolute_compare_less_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """uint64x1_t vcale_f64 (float64x1_t a, float64x1_t b)  A64: FACGE Dd, Dn, Dm"""
            ...

        @staticmethod
        def absolute_compare_less_than_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """uint64x1_t vcalt_f64 (float64x1_t a, float64x1_t b)  A64: FACGT Dd, Dn, Dm"""
            ...

        @staticmethod
        def absolute_difference(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vabdq_f64 (float64x2_t a, float64x2_t b)  A64: FABD Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def absolute_difference_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64x1_t vabd_f64 (float64x1_t a, float64x1_t b)  A64: FABD Dd, Dn, Dm"""
            ...

        @staticmethod
        def abs_saturate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vqabsq_s64 (int64x2_t a)  A64: SQABS Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def abs_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqabsh_s16 (int16_t a)  A64: SQABS Hd, Hn"""
            ...

        @staticmethod
        def abs_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int64x1_t vabs_s64 (int64x1_t a)  A64: ABS Dd, Dn"""
            ...

        @staticmethod
        def add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vaddq_f64 (float64x2_t a, float64x2_t b)  A64: FADD Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def add_across(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vaddv_u8 (uint8x8_t a)  A64: ADDV Bd, Vn.8B"""
            ...

        @staticmethod
        @overload
        def add_across(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vaddvq_u8 (uint8x16_t a)  A64: ADDV Bd, Vn.16B"""
            ...

        @staticmethod
        @overload
        def add_across_widening(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint16_t vaddlv_u8 (uint8x8_t a)  A64: UADDLV Hd, Vn.8B"""
            ...

        @staticmethod
        @overload
        def add_across_widening(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint16_t vaddlvq_u8 (uint8x16_t a)  A64: UADDLV Hd, Vn.16B"""
            ...

        @staticmethod
        @overload
        def add_pairwise(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vpaddq_u8 (uint8x16_t a, uint8x16_t b)  A64: ADDP Vd.16B, Vn.16B, Vm.16B"""
            ...

        @staticmethod
        @overload
        def add_pairwise(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vpaddq_f64 (float64x2_t a, float64x2_t b)  A64: FADDP Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def add_pairwise_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vpadds_f32 (float32x2_t a)  A64: FADDP Sd, Vn.2S"""
            ...

        @staticmethod
        @overload
        def add_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64_t vpaddd_f64 (float64x2_t a)  A64: FADDP Dd, Vn.2D"""
            ...

        @staticmethod
        @overload
        def add_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int64_t vpaddd_s64 (int64x2_t a)  A64: ADDP Dd, Vn.2D"""
            ...

        @staticmethod
        @overload
        def add_saturate(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8x8_t vsqadd_u8 (uint8x8_t a, int8x8_t b)  A64: USQADD Vd.8B, Vn.8B"""
            ...

        @staticmethod
        @overload
        def add_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vsqaddq_u8 (uint8x16_t a, int8x16_t b)  A64: USQADD Vd.16B, Vn.16B"""
            ...

        @staticmethod
        def add_saturate_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqaddb_u8 (uint8_t a, uint8_t b)  A64: UQADD Bd, Bn, Bm"""
            ...

        @staticmethod
        def ceiling(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrndpq_f64 (float64x2_t a)  A64: FRINTP Vd.2D, Vn.2D"""
            ...

        @staticmethod
        @overload
        def compare_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """uint64x2_t vceqq_f64 (float64x2_t a, float64x2_t b)  A64: FCMEQ Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vceqq_s64 (int64x2_t a, int64x2_t b)  A64: CMEQ Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_equal_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """uint64x1_t vceq_f64 (float64x1_t a, float64x1_t b)  A64: FCMEQ Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def compare_equal_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vceq_s64 (int64x1_t a, int64x1_t b)  A64: CMEQ Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """uint64x2_t vcgtq_f64 (float64x2_t a, float64x2_t b)  A64: FCMGT Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vcgtq_s64 (int64x2_t a, int64x2_t b)  A64: CMGT Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """uint64x2_t vcgeq_f64 (float64x2_t a, float64x2_t b)  A64: FCMGE Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vcgeq_s64 (int64x2_t a, int64x2_t b)  A64: CMGE Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """uint64x1_t vcge_f64 (float64x1_t a, float64x1_t b)  A64: FCMGE Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vcge_s64 (int64x1_t a, int64x1_t b)  A64: CMGE Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def compare_greater_than_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """uint64x1_t vcgt_f64 (float64x1_t a, float64x1_t b)  A64: FCMGT Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def compare_greater_than_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vcgt_s64 (int64x1_t a, int64x1_t b)  A64: CMGT Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """uint64x2_t vcltq_f64 (float64x2_t a, float64x2_t b)  A64: FCMGT Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vcltq_s64 (int64x2_t a, int64x2_t b)  A64: CMGT Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """uint64x2_t vcleq_f64 (float64x2_t a, float64x2_t b)  A64: FCMGE Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vcleq_s64 (int64x2_t a, int64x2_t b)  A64: CMGE Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """uint64x1_t vcle_f64 (float64x1_t a, float64x1_t b)  A64: FCMGE Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vcle_s64 (int64x1_t a, int64x1_t b)  A64: CMGE Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def compare_less_than_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """uint64x1_t vclt_f64 (float64x1_t a, float64x1_t b)  A64: FCMGT Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def compare_less_than_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vclt_s64 (int64x1_t a, int64x1_t b)  A64: CMGT Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def compare_test(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """uint64x2_t vtstq_f64 (float64x2_t a, float64x2_t b)  A64: CMTST Vd.2D, Vn.2D, Vm.2DThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
            ...

        @staticmethod
        @overload
        def compare_test(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vtstq_s64 (int64x2_t a, int64x2_t b)  A64: CMTST Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def compare_test_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """uint64x1_t vtst_f64 (float64x1_t a, float64x1_t b)  A64: CMTST Dd, Dn, DmThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
            ...

        @staticmethod
        @overload
        def compare_test_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vtst_s64 (int64x1_t a, int64x1_t b)  A64: CMTST Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def convert_to_double(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vcvt_f64_f32 (float32x2_t a)  A64: FCVTL Vd.2D, Vn.2S"""
            ...

        @staticmethod
        @overload
        def convert_to_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vcvtq_f64_s64 (int64x2_t a)  A64: SCVTF Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_double_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64x1_t vcvt_f64_s64 (int64x1_t a)  A64: SCVTF Dd, Dn"""
            ...

        @staticmethod
        def convert_to_double_upper(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vcvt_high_f64_f32 (float32x4_t a)  A64: FCVTL2 Vd.2D, Vn.4S"""
            ...

        @staticmethod
        def convert_to_int_64_round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vcvtaq_s64_f64 (float64x2_t a)  A64: FCVTAS Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_int_64_round_away_from_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int64x1_t vcvta_s64_f64 (float64x1_t a)  A64: FCVTAS Dd, Dn"""
            ...

        @staticmethod
        def convert_to_int_64_round_to_even(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vcvtnq_s64_f64 (float64x2_t a)  A64: FCVTNS Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_int_64_round_to_even_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int64x1_t vcvtn_s64_f64 (float64x1_t a)  A64: FCVTNS Dd, Dn"""
            ...

        @staticmethod
        def convert_to_int_64_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vcvtmq_s64_f64 (float64x2_t a)  A64: FCVTMS Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_int_64_round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int64x1_t vcvtm_s64_f64 (float64x1_t a)  A64: FCVTMS Dd, Dn"""
            ...

        @staticmethod
        def convert_to_int_64_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vcvtpq_s64_f64 (float64x2_t a)  A64: FCVTPS Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_int_64_round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int64x1_t vcvtp_s64_f64 (float64x1_t a)  A64: FCVTPS Dd, Dn"""
            ...

        @staticmethod
        def convert_to_int_64_round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vcvtq_s64_f64 (float64x2_t a)  A64: FCVTZS Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_int_64_round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int64x1_t vcvt_s64_f64 (float64x1_t a)  A64: FCVTZS Dd, Dn"""
            ...

        @staticmethod
        def convert_to_single_lower(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vcvt_f32_f64 (float64x2_t a)  A64: FCVTN Vd.2S, Vn.2D"""
            ...

        @staticmethod
        def convert_to_single_round_to_odd_lower(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vcvtx_f32_f64 (float64x2_t a)  A64: FCVTXN Vd.2S, Vn.2D"""
            ...

        @staticmethod
        def convert_to_single_round_to_odd_upper(lower: System.Runtime.Intrinsics.Vector64[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float32x4_t vcvtx_high_f32_f64 (float32x2_t r, float64x2_t a)  A64: FCVTXN2 Vd.4S, Vn.2D"""
            ...

        @staticmethod
        def convert_to_single_upper(lower: System.Runtime.Intrinsics.Vector64[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float32x4_t vcvt_high_f32_f64 (float32x2_t r, float64x2_t a)  A64: FCVTN2 Vd.4S, Vn.2D"""
            ...

        @staticmethod
        def convert_to_u_int_64_round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vcvtaq_u64_f64 (float64x2_t a)  A64: FCVTAU Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_u_int_64_round_away_from_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vcvta_u64_f64 (float64x1_t a)  A64: FCVTAU Dd, Dn"""
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_even(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vcvtnq_u64_f64 (float64x2_t a)  A64: FCVTNU Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_even_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vcvtn_u64_f64 (float64x1_t a)  A64: FCVTNU Dd, Dn"""
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vcvtmq_u64_f64 (float64x2_t a)  A64: FCVTMU Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vcvtm_u64_f64 (float64x1_t a)  A64: FCVTMU Dd, Dn"""
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vcvtpq_u64_f64 (float64x2_t a)  A64: FCVTPU Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vcvtp_u64_f64 (float64x1_t a)  A64: FCVTPU Dd, Dn"""
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint64x2_t vcvtq_u64_f64 (float64x2_t a)  A64: FCVTZU Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint64x1_t vcvt_u64_f64 (float64x1_t a)  A64: FCVTZU Dd, Dn"""
            ...

        @staticmethod
        @overload
        def divide(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vdiv_f32 (float32x2_t a, float32x2_t b)  A64: FDIV Vd.2S, Vn.2S, Vm.2S"""
            ...

        @staticmethod
        @overload
        def divide(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vdivq_f64 (float64x2_t a, float64x2_t b)  A64: FDIV Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vdupq_laneq_f64 (float64x2_t vec, const int lane)  A64: DUP Vd.2D, Vn.D[index]"""
            ...

        @staticmethod
        @overload
        def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vdupq_laneq_s64 (int64x2_t vec, const int lane)  A64: DUP Vd.2D, Vn.D[index]"""
            ...

        @staticmethod
        @overload
        def duplicate_to_vector_128(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vdupq_n_f64 (float64_t value)  A64: DUP Vd.2D, Vn.D[0]"""
            ...

        @staticmethod
        @overload
        def duplicate_to_vector_128(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vdupq_n_s64 (int64_t value)  A64: DUP Vd.2D, Rn"""
            ...

        @staticmethod
        def extract_narrowing_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqmovnh_u16 (uint16_t a)  A64: UQXTN Bd, Hn"""
            ...

        @staticmethod
        def extract_narrowing_saturate_unsigned_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqmovunh_s16 (int16_t a)  A64: SQXTUN Bd, Hn"""
            ...

        @staticmethod
        def floor(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrndmq_f64 (float64x2_t a)  A64: FRINTM Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def fused_multiply_add(addend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vfmaq_f64 (float64x2_t a, float64x2_t b, float64x2_t c)  A64: FMLA Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vfma_n_f32 (float32x2_t a, float32x2_t b, float32_t n)  A64: FMLA Vd.2S, Vn.2S, Vm.S[0]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_scalar(addend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vfmaq_n_f64 (float64x2_t a, float64x2_t b, float64_t n)  A64: FMLA Vd.2D, Vn.2D, Vm.D[0]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vfma_lane_f32 (float32x2_t a, float32x2_t b, float32x2_t v, const int lane)  A64: FMLA Vd.2S, Vn.2S, Vm.S[lane]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vfma_laneq_f32 (float32x2_t a, float32x2_t b, float32x4_t v, const int lane)  A64: FMLA Vd.2S, Vn.2S, Vm.S[lane]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vfmaq_laneq_f64 (float64x2_t a, float64x2_t b, float64x2_t v, const int lane)  A64: FMLA Vd.2D, Vn.2D, Vm.D[lane]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """float32x4_t vfmaq_lane_f32 (float32x4_t a, float32x4_t b, float32x2_t v, const int lane)  A64: FMLA Vd.4S, Vn.4S, Vm.S[lane]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_add_scalar_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64_t vfmad_laneq_f64 (float64_t a, float64_t b, float64x2_t v, const int lane)  A64: FMLA Dd, Dn, Vm.D[lane]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_add_scalar_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vfmas_lane_f32 (float32_t a, float32_t b, float32x2_t v, const int lane)  A64: FMLA Sd, Sn, Vm.S[lane]"""
            ...

        @staticmethod
        def fused_multiply_subtract(minuend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vfmsq_f64 (float64x2_t a, float64x2_t b, float64x2_t c)  A64: FMLS Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vfms_n_f32 (float32x2_t a, float32x2_t b, float32_t n)  A64: FMLS Vd.2S, Vn.2S, Vm.S[0]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_scalar(minuend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vfmsq_n_f64 (float64x2_t a, float64x2_t b, float64_t n)  A64: FMLS Vd.2D, Vn.2D, Vm.D[0]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vfms_lane_f32 (float32x2_t a, float32x2_t b, float32x2_t v, const int lane)  A64: FMLS Vd.2S, Vn.2S, Vm.S[lane]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vfms_laneq_f32 (float32x2_t a, float32x2_t b, float32x4_t v, const int lane)  A64: FMLS Vd.2S, Vn.2S, Vm.S[lane]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vfmsq_laneq_f64 (float64x2_t a, float64x2_t b, float64x2_t v, const int lane)  A64: FMLS Vd.2D, Vn.2D, Vm.D[lane]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """float32x4_t vfmsq_lane_f32 (float32x4_t a, float32x4_t b, float32x2_t v, const int lane)  A64: FMLS Vd.4S, Vn.4S, Vm.S[lane]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_scalar_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64_t vfmsd_laneq_f64 (float64_t a, float64_t b, float64x2_t v, const int lane)  A64: FMLS Dd, Dn, Vm.D[lane]"""
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_scalar_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vfmss_lane_f32 (float32_t a, float32_t b, float32x2_t v, const int lane)  A64: FMLS Sd, Sn, Vm.S[lane]"""
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector64[int], result_index: int, value: System.Runtime.Intrinsics.Vector64[int], value_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8x8_t vcopy_lane_u8 (uint8x8_t a, const int lane1, uint8x8_t b, const int lane2)  A64: INS Vd.B[lane1], Vn.B[lane2]"""
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector64[int], result_index: int, value: System.Runtime.Intrinsics.Vector128[int], value_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8x8_t vcopy_laneq_u8 (uint8x8_t a, const int lane1, uint8x16_t b, const int lane2)  A64: INS Vd.B[lane1], Vn.B[lane2]"""
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector64[float], result_index: int, value: System.Runtime.Intrinsics.Vector64[float], value_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vcopy_lane_f32 (float32x2_t a, const int lane1, float32x2_t b, const int lane2)  A64: INS Vd.S[lane1], Vn.S[lane2]"""
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector64[float], result_index: int, value: System.Runtime.Intrinsics.Vector128[float], value_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vcopy_laneq_f32 (float32x2_t a, const int lane1, float32x4_t b, const int lane2)  A64: INS Vd.S[lane1], Vn.S[lane2]"""
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector128[int], result_index: int, value: System.Runtime.Intrinsics.Vector64[int], value_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vcopyq_lane_u8 (uint8x16_t a, const int lane1, uint8x8_t b, const int lane2)  A64: INS Vd.B[lane1], Vn.B[lane2]"""
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector128[int], result_index: int, value: System.Runtime.Intrinsics.Vector128[int], value_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vcopyq_laneq_u8 (uint8x16_t a, const int lane1, uint8x16_t b, const int lane2)  A64: INS Vd.B[lane1], Vn.B[lane2]"""
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector128[float], result_index: int, value: System.Runtime.Intrinsics.Vector128[float], value_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vcopyq_laneq_f64 (float64x2_t a, const int lane1, float64x2_t b, const int lane2)  A64: INS Vd.D[lane1], Vn.D[lane2]"""
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector128[float], result_index: int, value: System.Runtime.Intrinsics.Vector64[float], value_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """float32x4_t vcopyq_lane_f32 (float32x4_t a, const int lane1, float32x2_t b, const int lane2)  A64: INS Vd.S[lane1], Vn.S[lane2]"""
            ...

        @staticmethod
        def load_2_x_vector_128(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD1 { Vn.16B, Vn+1.16B }, [Xn]"""
            ...

        @staticmethod
        def load_2_x_vector_128_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD2 { Vn.16B, Vn+1.16B }, [Xn]"""
            ...

        @staticmethod
        def load_3_x_vector_128(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD1 { Vn.16B, Vn+1.16B, Vn+2.16B }, [Xn]"""
            ...

        @staticmethod
        def load_3_x_vector_128_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD3 { Vn.16B, Vn+1.16B, Vn+2.16B }, [Xn]"""
            ...

        @staticmethod
        def load_4_x_vector_128(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD1 { Vn.16B, Vn+1.16B, Vn+2.16B, Vn+3.16B }, [Xn]"""
            ...

        @staticmethod
        def load_4_x_vector_128_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD4 { Vn.16B, Vn+1.16B, Vn+2.16B, Vn+3.16B }, [Xn]"""
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD2 { Vn.16B, Vn+1.16B }[Vm], [Xn]"""
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]:
            """A64: LD2 { Vn.4S, Vn+1.4S }[Vm], [Xn]"""
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD3 { Vn.16B, Vn+1.16B, Vn+2.16B }[Vm], [Xn]"""
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]:
            """A64: LD3 { Vn.4S, Vn+1.4S, Vn+2.4S }[Vm], [Xn]"""
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD4 { Vn.16B, Vn+1.16B, Vn+2.16B, Vn+3.16B }[Vm], [Xn]"""
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]:
            """A64: LD4 { Vn.4S, Vn+1.4S, Vn+2.4S, Vn+3.4S }[Vm], [Xn]"""
            ...

        @staticmethod
        def load_and_replicate_to_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vld1q_dup_f64 (float64_t const * ptr)  A64: LD1R { Vt.2D }, [Xn]"""
            ...

        @staticmethod
        def load_and_replicate_to_vector_128x_2(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD2R { Vn.16B, Vn+1.16B }, [Xn]"""
            ...

        @staticmethod
        def load_and_replicate_to_vector_128x_3(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD3R { Vn.16B, Vn+1.16B, Vn+2.16B }, [Xn]"""
            ...

        @staticmethod
        def load_and_replicate_to_vector_128x_4(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LD4R { Vn.16B, Vn+1.16B, Vn+2.16B, Vn+3.16B }, [Xn]"""
            ...

        @staticmethod
        def load_pair_scalar_vector_64(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
            """A64: LDP St1, St2, [Xn]"""
            ...

        @staticmethod
        def load_pair_scalar_vector_64_non_temporal(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
            """A64: LDNP St1, St2, [Xn]"""
            ...

        @staticmethod
        def load_pair_vector_128(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LDP Qt1, Qt2, [Xn]"""
            ...

        @staticmethod
        def load_pair_vector_128_non_temporal(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            """A64: LDNP Qt1, Qt2, [Xn]"""
            ...

        @staticmethod
        def load_pair_vector_64(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
            """A64: LDP Dt1, Dt2, [Xn]"""
            ...

        @staticmethod
        def load_pair_vector_64_non_temporal(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
            """A64: LDNP Dt1, Dt2, [Xn]"""
            ...

        @staticmethod
        def max(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vmaxq_f64 (float64x2_t a, float64x2_t b)  A64: FMAX Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def max_across(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vmaxv_u8 (uint8x8_t a)  A64: UMAXV Bd, Vn.8B"""
            ...

        @staticmethod
        @overload
        def max_across(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vmaxvq_u8 (uint8x16_t a)  A64: UMAXV Bd, Vn.16B"""
            ...

        @staticmethod
        @overload
        def max_across(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vmaxvq_f32 (float32x4_t a)  A64: FMAXV Sd, Vn.4S"""
            ...

        @staticmethod
        def max_number(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vmaxnmq_f64 (float64x2_t a, float64x2_t b)  A64: FMAXNM Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def max_number_across(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vmaxnmvq_f32 (float32x4_t a)  A64: FMAXNMV Sd, Vn.4S"""
            ...

        @staticmethod
        @overload
        def max_number_pairwise(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vpmaxnm_f32 (float32x2_t a, float32x2_t b)  A64: FMAXNMP Vd.2S, Vn.2S, Vm.2S"""
            ...

        @staticmethod
        @overload
        def max_number_pairwise(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vpmaxnmq_f64 (float64x2_t a, float64x2_t b)  A64: FMAXNMP Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def max_number_pairwise_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vpmaxnms_f32 (float32x2_t a)  A64: FMAXNMP Sd, Vn.2S"""
            ...

        @staticmethod
        @overload
        def max_number_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64_t vpmaxnmqd_f64 (float64x2_t a)  A64: FMAXNMP Dd, Vn.2D"""
            ...

        @staticmethod
        @overload
        def max_pairwise(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vpmaxq_u8 (uint8x16_t a, uint8x16_t b)  A64: UMAXP Vd.16B, Vn.16B, Vm.16B"""
            ...

        @staticmethod
        @overload
        def max_pairwise(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vpmaxq_f64 (float64x2_t a, float64x2_t b)  A64: FMAXP Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def max_pairwise_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vpmaxs_f32 (float32x2_t a)  A64: FMAXP Sd, Vn.2S"""
            ...

        @staticmethod
        @overload
        def max_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64_t vpmaxqd_f64 (float64x2_t a)  A64: FMAXP Dd, Vn.2D"""
            ...

        @staticmethod
        def max_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64x1_t vmax_f64 (float64x1_t a, float64x1_t b)  A64: FMAX Dd, Dn, Dm"""
            ...

        @staticmethod
        def min(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vminq_f64 (float64x2_t a, float64x2_t b)  A64: FMIN Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def min_across(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vminv_u8 (uint8x8_t a)  A64: UMINV Bd, Vn.8B"""
            ...

        @staticmethod
        @overload
        def min_across(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vminvq_u8 (uint8x16_t a)  A64: UMINV Bd, Vn.16B"""
            ...

        @staticmethod
        @overload
        def min_across(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vminvq_f32 (float32x4_t a)  A64: FMINV Sd, Vn.4S"""
            ...

        @staticmethod
        def min_number(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vminnmq_f64 (float64x2_t a, float64x2_t b)  A64: FMINNM Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def min_number_across(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vminnmvq_f32 (float32x4_t a)  A64: FMINNMV Sd, Vn.4S"""
            ...

        @staticmethod
        @overload
        def min_number_pairwise(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vpminnm_f32 (float32x2_t a, float32x2_t b)  A64: FMINNMP Vd.2S, Vn.2S, Vm.2S"""
            ...

        @staticmethod
        @overload
        def min_number_pairwise(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vpminnmq_f64 (float64x2_t a, float64x2_t b)  A64: FMINNMP Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def min_number_pairwise_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vpminnms_f32 (float32x2_t a)  A64: FMINNMP Sd, Vn.2S"""
            ...

        @staticmethod
        @overload
        def min_number_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64_t vpminnmqd_f64 (float64x2_t a)  A64: FMINNMP Dd, Vn.2D"""
            ...

        @staticmethod
        @overload
        def min_pairwise(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vpminq_u8 (uint8x16_t a, uint8x16_t b)  A64: UMINP Vd.16B, Vn.16B, Vm.16B"""
            ...

        @staticmethod
        @overload
        def min_pairwise(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vpminq_f64 (float64x2_t a, float64x2_t b)  A64: FMINP Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def min_pairwise_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vpmins_f32 (float32x2_t a)  A64: FMINP Sd, Vn.2S"""
            ...

        @staticmethod
        @overload
        def min_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64_t vpminqd_f64 (float64x2_t a)  A64: FMINP Dd, Vn.2D"""
            ...

        @staticmethod
        def min_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64x1_t vmin_f64 (float64x1_t a, float64x1_t b)  A64: FMIN Dd, Dn, Dm"""
            ...

        @staticmethod
        def multiply(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vmulq_f64 (float64x2_t a, float64x2_t b)  A64: FMUL Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def multiply_by_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vmulq_n_f64 (float64x2_t a, float64_t b)  A64: FMUL Vd.2D, Vn.2D, Vm.D[0]"""
            ...

        @staticmethod
        def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vmulq_laneq_f64 (float64x2_t a, float64x2_t v, const int lane)  A64: FMUL Vd.2D, Vn.2D, Vm.D[lane]"""
            ...

        @staticmethod
        def multiply_doubling_saturate_high_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqdmulhh_s16 (int16_t a, int16_t b)  A64: SQDMULH Hd, Hn, Hm"""
            ...

        @staticmethod
        @overload
        def multiply_doubling_scalar_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqdmulhh_lane_s16 (int16_t a, int16x4_t v, const int lane)  A64: SQDMULH Hd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_doubling_scalar_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqdmulhh_laneq_s16 (int16_t a, int16x8_t v, const int lane)  A64: SQDMULH Hd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        def multiply_doubling_widening_and_add_saturate_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int32_t vqdmlalh_s16 (int32_t a, int16_t b, int16_t c)  A64: SQDMLAL Sd, Hn, Hm"""
            ...

        @staticmethod
        def multiply_doubling_widening_and_subtract_saturate_scalar(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int32_t vqdmlslh_s16 (int32_t a, int16_t b, int16_t c)  A64: SQDMLSL Sd, Hn, Hm"""
            ...

        @staticmethod
        def multiply_doubling_widening_saturate_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int32_t vqdmullh_s16 (int16_t a, int16_t b)  A64: SQDMULL Sd, Hn, Hm"""
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_saturate_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int32_t vqdmullh_lane_s16 (int16_t a, int16x4_t v, const int lane)  A64: SQDMULL Sd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_saturate_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int32_t vqdmullh_laneq_s16 (int16_t a, int16x8_t v, const int lane)  A64: SQDMULL Sd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_scalar_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int32_t vqdmlalh_lane_s16 (int32_t a, int16_t b, int16x4_t v, const int lane)  A64: SQDMLAL Sd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_scalar_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int32_t vqdmlalh_laneq_s16 (int32_t a, int16_t b, int16x8_t v, const int lane)  A64: SQDMLAL Sd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_scalar_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int32_t vqdmlslh_lane_s16 (int32_t a, int16_t b, int16x4_t v, const int lane)  A64: SQDMLSL Sd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_scalar_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int32_t vqdmlslh_laneq_s16 (int32_t a, int16_t b, int16x8_t v, const int lane)  A64: SQDMLSL Sd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_extended(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vmulx_f32 (float32x2_t a, float32x2_t b)  A64: FMULX Vd.2S, Vn.2S, Vm.2S"""
            ...

        @staticmethod
        @overload
        def multiply_extended(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vmulxq_f64 (float64x2_t a, float64x2_t b)  A64: FMULX Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def multiply_extended_by_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vmulxq_lane_f64 (float64x2_t a, float64x1_t v, const int lane)  A64: FMULX Vd.2D, Vn.2D, Vm.D[0]"""
            ...

        @staticmethod
        @overload
        def multiply_extended_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vmulx_lane_f32 (float32x2_t a, float32x2_t v, const int lane)  A64: FMULX Vd.2S, Vn.2S, Vm.S[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_extended_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vmulx_laneq_f32 (float32x2_t a, float32x4_t v, const int lane)  A64: FMULX Vd.2S, Vn.2S, Vm.S[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_extended_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vmulxq_laneq_f64 (float64x2_t a, float64x2_t v, const int lane)  A64: FMULX Vd.2D, Vn.2D, Vm.D[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_extended_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """float32x4_t vmulxq_lane_f32 (float32x4_t a, float32x2_t v, const int lane)  A64: FMULX Vd.4S, Vn.4S, Vm.S[lane]"""
            ...

        @staticmethod
        def multiply_extended_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64x1_t vmulx_f64 (float64x1_t a, float64x1_t b)  A64: FMULX Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def multiply_extended_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64_t vmulxd_laneq_f64 (float64_t a, float64x2_t v, const int lane)  A64: FMULX Dd, Dn, Vm.D[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_extended_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32_t vmulxs_lane_f32 (float32_t a, float32x2_t v, const int lane)  A64: FMULX Sd, Sn, Vm.S[lane]"""
            ...

        @staticmethod
        def multiply_rounded_doubling_saturate_high_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrdmulhh_s16 (int16_t a, int16_t b)  A64: SQRDMULH Hd, Hn, Hm"""
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrdmulhh_lane_s16 (int16_t a, int16x4_t v, const int lane)  A64: SQRDMULH Hd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrdmulhh_laneq_s16 (int16_t a, int16x8_t v, const int lane)  A64: SQRDMULH Hd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        def multiply_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64_t vmuld_laneq_f64 (float64_t a, float64x2_t v, const int lane)  A64: FMUL Dd, Dn, Vm.D[lane]"""
            ...

        @staticmethod
        @overload
        def negate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vnegq_f64 (float64x2_t a)  A64: FNEG Vd.2D, Vn.2D"""
            ...

        @staticmethod
        @overload
        def negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vnegq_s64 (int64x2_t a)  A64: NEG Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def negate_saturate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """int64x2_t vqnegq_s64 (int64x2_t a)  A64: SQNEG Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def negate_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqnegh_s16 (int16_t a)  A64: SQNEG Hd, Hn"""
            ...

        @staticmethod
        def negate_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int64x1_t vneg_s64 (int64x1_t a)  A64: NEG Dd, Dn"""
            ...

        @staticmethod
        def reciprocal_estimate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrecpeq_f64 (float64x2_t a)  A64: FRECPE Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def reciprocal_estimate_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64x1_t vrecpe_f64 (float64x1_t a)  A64: FRECPE Dd, Dn"""
            ...

        @staticmethod
        def reciprocal_exponent_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64_t vrecpxd_f64 (float64_t a)  A64: FRECPX Dd, Dn"""
            ...

        @staticmethod
        def reciprocal_square_root_estimate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrsqrteq_f64 (float64x2_t a)  A64: FRSQRTE Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def reciprocal_square_root_estimate_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64x1_t vrsqrte_f64 (float64x1_t a)  A64: FRSQRTE Dd, Dn"""
            ...

        @staticmethod
        def reciprocal_square_root_step(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrsqrtsq_f64 (float64x2_t a, float64x2_t b)  A64: FRSQRTS Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def reciprocal_square_root_step_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64x1_t vrsqrts_f64 (float64x1_t a, float64x1_t b)  A64: FRSQRTS Dd, Dn, Dm"""
            ...

        @staticmethod
        def reciprocal_step(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrecpsq_f64 (float64x2_t a, float64x2_t b)  A64: FRECPS Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def reciprocal_step_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float64x1_t vrecps_f64 (float64x1_t a, float64x1_t b)  A64: FRECPS Dd, Dn, Dm"""
            ...

        @staticmethod
        @overload
        def reverse_element_bits(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8x8_t vrbit_u8 (uint8x8_t a)  A64: RBIT Vd.8B, Vn.8B"""
            ...

        @staticmethod
        @overload
        def reverse_element_bits(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vrbitq_u8 (uint8x16_t a)  A64: RBIT Vd.16B, Vn.16B"""
            ...

        @staticmethod
        def round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrndaq_f64 (float64x2_t a)  A64: FRINTA Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def round_to_nearest(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrndnq_f64 (float64x2_t a)  A64: FRINTN Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrndmq_f64 (float64x2_t a)  A64: FRINTM Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrndpq_f64 (float64x2_t a)  A64: FRINTP Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vrndq_f64 (float64x2_t a)  A64: FRINTZ Vd.2D, Vn.2D"""
            ...

        @staticmethod
        def shift_arithmetic_rounded_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrshlh_s16 (int16_t a, int16_t b)  A64: SQRSHL Hd, Hn, Hm"""
            ...

        @staticmethod
        def shift_arithmetic_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqshlh_s16 (int16_t a, int16_t b)  A64: SQSHL Hd, Hn, Hm"""
            ...

        @staticmethod
        def shift_left_logical_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqshlb_n_u8 (uint8_t a, const int n)  A64: UQSHL Bd, Bn, #n"""
            ...

        @staticmethod
        def shift_left_logical_saturate_unsigned_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint16_t vqshluh_n_s16 (int16_t a, const int n)  A64: SQSHLU Hd, Hn, #n"""
            ...

        @staticmethod
        def shift_logical_rounded_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqrshlb_u8 (uint8_t a, int8_t b)  A64: UQRSHL Bd, Bn, Bm"""
            ...

        @staticmethod
        def shift_logical_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqshlb_u8 (uint8_t a, int8_t b)  A64: UQSHL Bd, Bn, Bm"""
            ...

        @staticmethod
        def shift_right_arithmetic_narrowing_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqshrns_n_s32 (int32_t a, const int n)  A64: SQSHRN Hd, Sn, #n"""
            ...

        @staticmethod
        def shift_right_arithmetic_narrowing_saturate_unsigned_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqshrunh_n_s16 (int16_t a, const int n)  A64: SQSHRUN Bd, Hn, #n"""
            ...

        @staticmethod
        def shift_right_arithmetic_rounded_narrowing_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrshrns_n_s32 (int32_t a, const int n)  A64: SQRSHRN Hd, Sn, #n"""
            ...

        @staticmethod
        def shift_right_arithmetic_rounded_narrowing_saturate_unsigned_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqrshrunh_n_s16 (int16_t a, const int n)  A64: SQRSHRUN Bd, Hn, #n"""
            ...

        @staticmethod
        def shift_right_logical_narrowing_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqshrnh_n_u16 (uint16_t a, const int n)  A64: UQSHRN Bd, Hn, #n"""
            ...

        @staticmethod
        def shift_right_logical_rounded_narrowing_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqrshrnh_n_u16 (uint16_t a, const int n)  A64: UQRSHRN Bd, Hn, #n"""
            ...

        @staticmethod
        @overload
        def sqrt(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vsqrt_f32 (float32x2_t a)  A64: FSQRT Vd.2S, Vn.2S"""
            ...

        @staticmethod
        @overload
        def sqrt(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vsqrtq_f64 (float64x2_t a)  A64: FSQRT Vd.2D, Vn.2D"""
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            """A64: ST1 { Vn.16B, Vn+1.16B }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            """A64: ST1 { Vn.4S, Vn+1.4S }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            """A64: ST1 { Vn.16B, Vn+1.16B, Vn+2.16B }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            """A64: ST1 { Vn.4S, Vn+1.4S, Vn+2.4S }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            """A64: ST1 { Vn.16B, Vn+1.16B, Vn+2.16B, Vn+3.16B }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            """A64: ST1 { Vn.4S, Vn+1.4S, Vn+2.4S, Vn+3.4S }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[int], value_2: System.Runtime.Intrinsics.Vector64[int]) -> None:
            """A64: STP Dt1, Dt2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[float], value_2: System.Runtime.Intrinsics.Vector64[float]) -> None:
            """A64: STP Dt1, Dt2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector128[int], value_2: System.Runtime.Intrinsics.Vector128[int]) -> None:
            """A64: STP Qt1, Qt2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector128[float], value_2: System.Runtime.Intrinsics.Vector128[float]) -> None:
            """A64: STP Qt1, Qt2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[int], value_2: System.Runtime.Intrinsics.Vector64[int]) -> None:
            """A64: STNP Dt1, Dt2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[float], value_2: System.Runtime.Intrinsics.Vector64[float]) -> None:
            """A64: STNP Dt1, Dt2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector128[int], value_2: System.Runtime.Intrinsics.Vector128[int]) -> None:
            """A64: STNP Qt1, Qt2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector128[float], value_2: System.Runtime.Intrinsics.Vector128[float]) -> None:
            """A64: STNP Qt1, Qt2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair_scalar(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[int], value_2: System.Runtime.Intrinsics.Vector64[int]) -> None:
            """A64: STP St1, St2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair_scalar(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[float], value_2: System.Runtime.Intrinsics.Vector64[float]) -> None:
            """A64: STP St1, St2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair_scalar_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[int], value_2: System.Runtime.Intrinsics.Vector64[int]) -> None:
            """A64: STNP St1, St2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_pair_scalar_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[float], value_2: System.Runtime.Intrinsics.Vector64[float]) -> None:
            """A64: STNP St1, St2, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int) -> None:
            """void vst2_lane_s8 (int8_t * ptr, int8x16x2_t val, const int lane)  A64: ST2 { Vt.16B, Vt+1.16B }[index], [Xn]"""
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int) -> None:
            """void vst2_lane_f32 (float32_t * ptr, float32x2x2_t val, const int lane)  A64: ST2 { Vt.4S, Vt+1.4S }[index], [Xn]"""
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int) -> None:
            """void vst3_lane_s8 (int8_t * ptr, int8x16x3_t val, const int lane)  A64: ST3 { Vt.16B, Vt+1.16B, Vt+2.16B }[index], [Xn]"""
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int) -> None:
            """void vst3_lane_f32 (float32_t * ptr, float32x2x3_t val, const int lane)  A64: ST3 { Vt.4S, Vt+1.4S, Vt+2.4S }[index], [Xn]"""
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int) -> None:
            """void vst4_lane_s8 (int8_t * ptr, int8x16x4_t val, const int lane)  A64: ST4 { Vt.16B, Vt+1.16B, Vt+2.16B, Vt+3.16B }[index], [Xn]"""
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int) -> None:
            """void vst4_lane_f32 (float32_t * ptr, float32x2x4_t val, const int lane)  A64: ST4 { Vt.4S, Vt+1.4S, Vt+2.4S, Vt+3.4S }[index], [Xn]"""
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            """A64: ST2 { Vn.16B, Vn+1.16B }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            """A64: ST2 { Vn.4S, Vn+1.4S }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            """A64: ST3 { Vn.16B, Vn+1.16B, Vn+2.16B }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            """A64: ST3 { Vn.4S, Vn+1.4S, Vn+2.4S }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            """A64: ST4 { Vn.16B, Vn+1.16B, Vn+2.16B, Vn+3.16B }, [Xn]"""
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            """A64: ST4 { Vn.4S, Vn+1.4S, Vn+2.4S, Vn+3.4S }, [Xn]"""
            ...

        @staticmethod
        def subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vsubq_f64 (float64x2_t a, float64x2_t b)  A64: FSUB Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        def subtract_saturate_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8_t vqsubb_u8 (uint8_t a, uint8_t b)  A64: UQSUB Bd, Bn, Bm"""
            ...

        @staticmethod
        @overload
        def transpose_even(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8x8_t vtrn1_u8(uint8x8_t a, uint8x8_t b)  A64: TRN1 Vd.8B, Vn.8B, Vm.8B"""
            ...

        @staticmethod
        @overload
        def transpose_even(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vtrn1_f32(float32x2_t a, float32x2_t b)  A64: TRN1 Vd.2S, Vn.2S, Vm.2S"""
            ...

        @staticmethod
        @overload
        def transpose_even(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vtrn1q_u8(uint8x16_t a, uint8x16_t b)  A64: TRN1 Vd.16B, Vn.16B, Vm.16B"""
            ...

        @staticmethod
        @overload
        def transpose_even(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vtrn1q_f64(float64x2_t a, float64x2_t b)  A64: TRN1 Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def transpose_odd(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8x8_t vtrn2_u8(uint8x8_t a, uint8x8_t b)  A64: TRN2 Vd.8B, Vn.8B, Vm.8B"""
            ...

        @staticmethod
        @overload
        def transpose_odd(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vtrn2_f32(float32x2_t a, float32x2_t b)  A64: TRN2 Vd.2S, Vn.2S, Vm.2S"""
            ...

        @staticmethod
        @overload
        def transpose_odd(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vtrn2q_u8(uint8x16_t a, uint8x16_t b)  A64: TRN2 Vd.16B, Vn.16B, Vm.16B"""
            ...

        @staticmethod
        @overload
        def transpose_odd(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vtrn2q_f64(float64x2_t a, float64x2_t b)  A64: TRN2 Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def unzip_even(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8x8_t vuzp1_u8(uint8x8_t a, uint8x8_t b)  A64: UZP1 Vd.8B, Vn.8B, Vm.8B"""
            ...

        @staticmethod
        @overload
        def unzip_even(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vuzp1_f32(float32x2_t a, float32x2_t b)  A64: UZP1 Vd.2S, Vn.2S, Vm.2S"""
            ...

        @staticmethod
        @overload
        def unzip_even(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vuzp1q_u8(uint8x16_t a, uint8x16_t b)  A64: UZP1 Vd.16B, Vn.16B, Vm.16B"""
            ...

        @staticmethod
        @overload
        def unzip_even(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vuzp1q_f64(float64x2_t a, float64x2_t b)  A64: UZP1 Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def unzip_odd(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8x8_t vuzp2_u8(uint8x8_t a, uint8x8_t b)  A64: UZP2 Vd.8B, Vn.8B, Vm.8B"""
            ...

        @staticmethod
        @overload
        def unzip_odd(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vuzp2_f32(float32x2_t a, float32x2_t b)  A64: UZP2 Vd.2S, Vn.2S, Vm.2S"""
            ...

        @staticmethod
        @overload
        def unzip_odd(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vuzp2q_u8(uint8x16_t a, uint8x16_t b)  A64: UZP2 Vd.16B, Vn.16B, Vm.16B"""
            ...

        @staticmethod
        @overload
        def unzip_odd(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vuzp2q_f64(float64x2_t a, float64x2_t b)  A64: UZP2 Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def vector_table_lookup(table: System.Runtime.Intrinsics.Vector128[int], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vqvtbl1q_u8(uint8x16_t t, uint8x16_t idx)  A64: TBL Vd.16B, {Vn.16B}, Vm.16B"""
            ...

        @staticmethod
        @overload
        def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vqtbl2q_u8(uint8x16x2_t t, uint8x16_t idx)  A64: TBL Vd.16B, {Vn.16B, Vn+1.16B}, Vm.16B"""
            ...

        @staticmethod
        @overload
        def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vqtbl3q_u8(uint8x16x3_t t, uint8x16_t idx)  A64: TBL Vd.16B, {Vn.16B, Vn+1.16B, Vn+2.16B}, Vm.16B"""
            ...

        @staticmethod
        @overload
        def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vqtbl4q_u8(uint8x16x4_t t, uint8x16_t idx)  A64: TBL Vd.16B, {Vn.16B, Vn+1.16B, Vn+2.16B, Vn+3.16B}, Vm.16B"""
            ...

        @staticmethod
        @overload
        def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector128[int], table: System.Runtime.Intrinsics.Vector128[int], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vqvtbx1q_u8(uint8x16_t r, int8x16_t t, uint8x16_t idx)  A64: TBX Vd.16B, {Vn.16B}, Vm.16B"""
            ...

        @staticmethod
        @overload
        def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector128[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vqtbx2q_u8(uint8x16x2_t t, uint8x16_t idx)  A64: TBX Vd.16B, {Vn.16B, Vn+1.16B}, Vm.16B"""
            ...

        @staticmethod
        @overload
        def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector128[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vqtbx3q_u8(uint8x16x3_t t, uint8x16_t idx)  A64: TBX Vd.16B, {Vn.16B, Vn+1.16B, Vn+2.16B}, Vm.16B"""
            ...

        @staticmethod
        @overload
        def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector128[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vqtbx4q_u8(uint8x16x4_t t, uint8x16_t idx)  A64: TBX Vd.16B, {Vn.16B, Vn+1.16B, Vn+2.16B, Vn+3.16B}, Vm.16B"""
            ...

        @staticmethod
        @overload
        def zip_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8x8_t vzip2_u8(uint8x8_t a, uint8x8_t b)  A64: ZIP2 Vd.8B, Vn.8B, Vm.8B"""
            ...

        @staticmethod
        @overload
        def zip_high(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vzip2_f32(float32x2_t a, float32x2_t b)  A64: ZIP2 Vd.2S, Vn.2S, Vm.2S"""
            ...

        @staticmethod
        @overload
        def zip_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vzip2q_u8(uint8x16_t a, uint8x16_t b)  A64: ZIP2 Vd.16B, Vn.16B, Vm.16B"""
            ...

        @staticmethod
        @overload
        def zip_high(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vzip2q_f64(float64x2_t a, float64x2_t b)  A64: ZIP2 Vd.2D, Vn.2D, Vm.2D"""
            ...

        @staticmethod
        @overload
        def zip_low(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """uint8x8_t vzip1_u8(uint8x8_t a, uint8x8_t b)  A64: ZIP1 Vd.8B, Vn.8B, Vm.8B"""
            ...

        @staticmethod
        @overload
        def zip_low(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            """float32x2_t vzip1_f32(float32x2_t a, float32x2_t b)  A64: ZIP1 Vd.2S, Vn.2S, Vm.2S"""
            ...

        @staticmethod
        @overload
        def zip_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """uint8x16_t vzip1q_u8(uint8x16_t a, uint8x16_t b)  A64: ZIP1 Vd.16B, Vn.16B, Vm.16B"""
            ...

        @staticmethod
        @overload
        def zip_low(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """float64x2_t vzip1q_f64(float64x2_t a, float64x2_t b)  A64: ZIP1 Vd.2D, Vn.2D, Vm.2D"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vabs_s16 (int16x4_t a)  A32: VABS.S16 Dd, Dm  A64: ABS Vd.4H, Vn.4H"""
        ...

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vabs_f32 (float32x2_t a)  A32: VABS.F32 Dd, Dm  A64: FABS Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vabsq_s16 (int16x8_t a)  A32: VABS.S16 Qd, Qm  A64: ABS Vd.8H, Vn.8H"""
        ...

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vabsq_f32 (float32x4_t a)  A32: VABS.F32 Qd, Qm  A64: FABS Vd.4S, Vn.4S"""
        ...

    @staticmethod
    @overload
    def absolute_compare_greater_than(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """uint32x2_t vcagt_f32 (float32x2_t a, float32x2_t b)  A32: VACGT.F32 Dd, Dn, Dm  A64: FACGT Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def absolute_compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """uint32x4_t vcagtq_f32 (float32x4_t a, float32x4_t b)  A32: VACGT.F32 Qd, Qn, Qm  A64: FACGT Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def absolute_compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """uint32x2_t vcage_f32 (float32x2_t a, float32x2_t b)  A32: VACGE.F32 Dd, Dn, Dm  A64: FACGE Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def absolute_compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """uint32x4_t vcageq_f32 (float32x4_t a, float32x4_t b)  A32: VACGE.F32 Qd, Qn, Qm  A64: FACGE Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def absolute_compare_less_than(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """uint32x2_t vcalt_f32 (float32x2_t a, float32x2_t b)  A32: VACLT.F32 Dd, Dn, Dm  A64: FACGT Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def absolute_compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """uint32x4_t vcaltq_f32 (float32x4_t a, float32x4_t b)  A32: VACLT.F32 Qd, Qn, Qm  A64: FACGT Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def absolute_compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """uint32x2_t vcale_f32 (float32x2_t a, float32x2_t b)  A32: VACLE.F32 Dd, Dn, Dm  A64: FACGE Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def absolute_compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """uint32x4_t vcaleq_f32 (float32x4_t a, float32x4_t b)  A32: VACLE.F32 Qd, Qn, Qm  A64: FACGE Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vabd_u8 (uint8x8_t a, uint8x8_t b)  A32: VABD.U8 Dd, Dn, Dm  A64: UABD Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vabd_f32 (float32x2_t a, float32x2_t b)  A32: VABD.F32 Dd, Dn, Dm  A64: FABD Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vabdq_u8 (uint8x16_t a, uint8x16_t b)  A32: VABD.U8 Qd, Qn, Qm  A64: UABD Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vabdq_f32 (float32x4_t a, float32x4_t b)  A32: VABD.F32 Qd, Qn, Qm  A64: FABD Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def absolute_difference_add(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vaba_u8 (uint8x8_t a, uint8x8_t b, uint8x8_t c)  A32: VABA.U8 Dd, Dn, Dm  A64: UABA Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def absolute_difference_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vabaq_u8 (uint8x16_t a, uint8x16_t b, uint8x16_t c)  A32: VABA.U8 Qd, Qn, Qm  A64: UABA Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    def absolute_difference_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vabdl_u8 (uint8x8_t a, uint8x8_t b)  A32: VABDL.U8 Qd, Dn, Dm  A64: UABDL Vd.8H, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    def absolute_difference_widening_lower_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vabal_u8 (uint16x8_t a, uint8x8_t b, uint8x8_t c)  A32: VABAL.U8 Qd, Dn, Dm  A64: UABAL Vd.8H, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    def absolute_difference_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vabdl_high_u8 (uint8x16_t a, uint8x16_t b)  A32: VABDL.U8 Qd, Dn+1, Dm+1  A64: UABDL2 Vd.8H, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    def absolute_difference_widening_upper_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vabal_high_u8 (uint16x8_t a, uint8x16_t b, uint8x16_t c)  A32: VABAL.U8 Qd, Dn+1, Dm+1  A64: UABAL2 Vd.8H, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def abs_saturate(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqabs_s16 (int16x4_t a)  A32: VQABS.S16 Dd, Dm  A64: SQABS Vd.4H, Vn.4H"""
        ...

    @staticmethod
    @overload
    def abs_saturate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqabsq_s16 (int16x8_t a)  A32: VQABS.S16 Qd, Qm  A64: SQABS Vd.8H, Vn.8H"""
        ...

    @staticmethod
    def abs_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vabs_f64 (float64x1_t a)  A32: VABS.F64 Dd, Dm  A64: FABS Dd, Dn"""
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vadd_u8 (uint8x8_t a, uint8x8_t b)  A32: VADD.I8 Dd, Dn, Dm  A64: ADD Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vadd_f32 (float32x2_t a, float32x2_t b)  A32: VADD.F32 Dd, Dn, Dm  A64: FADD Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vaddq_u8 (uint8x16_t a, uint8x16_t b)  A32: VADD.I8 Qd, Qn, Qm  A64: ADD Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vaddq_f32 (float32x4_t a, float32x4_t b)  A32: VADD.F32 Qd, Qn, Qm  A64: FADD Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    def add_high_narrowing_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vaddhn_u16 (uint16x8_t a, uint16x8_t b)  A32: VADDHN.I16 Dd, Qn, Qm  A64: ADDHN Vd.8B, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def add_high_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vaddhn_high_u16 (uint8x8_t r, uint16x8_t a, uint16x8_t b)  A32: VADDHN.I16 Dd+1, Qn, Qm  A64: ADDHN2 Vd.16B, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    @overload
    def add_pairwise(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vpadd_u8 (uint8x8_t a, uint8x8_t b)  A32: VPADD.I8 Dd, Dn, Dm  A64: ADDP Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def add_pairwise(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vpadd_f32 (float32x2_t a, float32x2_t b)  A32: VPADD.F32 Dd, Dn, Dm  A64: FADDP Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def add_pairwise_widening(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint16x4_t vpaddl_u8 (uint8x8_t a)  A32: VPADDL.U8 Dd, Dm  A64: UADDLP Vd.4H, Vn.8B"""
        ...

    @staticmethod
    @overload
    def add_pairwise_widening(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vpaddlq_u8 (uint8x16_t a)  A32: VPADDL.U8 Qd, Qm  A64: UADDLP Vd.8H, Vn.16B"""
        ...

    @staticmethod
    @overload
    def add_pairwise_widening_and_add(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint16x4_t vpadal_u8 (uint16x4_t a, uint8x8_t b)  A32: VPADAL.U8 Dd, Dm  A64: UADALP Vd.4H, Vn.8B"""
        ...

    @staticmethod
    @overload
    def add_pairwise_widening_and_add(addend: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vpadalq_u8 (uint16x8_t a, uint8x16_t b)  A32: VPADAL.U8 Qd, Qm  A64: UADALP Vd.8H, Vn.16B"""
        ...

    @staticmethod
    def add_pairwise_widening_and_add_scalar(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vpadal_s32 (int64x1_t a, int32x2_t b)  A32: VPADAL.S32 Dd, Dm  A64: SADALP Vd.1D, Vn.2S"""
        ...

    @staticmethod
    def add_pairwise_widening_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vpaddl_s32 (int32x2_t a)  A32: VPADDL.S32 Dd, Dm  A64: SADDLP Dd, Vn.2S"""
        ...

    @staticmethod
    def add_rounded_high_narrowing_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vraddhn_u16 (uint16x8_t a, uint16x8_t b)  A32: VRADDHN.I16 Dd, Qn, Qm  A64: RADDHN Vd.8B, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def add_rounded_high_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vraddhn_high_u16 (uint8x8_t r, uint16x8_t a, uint16x8_t b)  A32: VRADDHN.I16 Dd+1, Qn, Qm  A64: RADDHN2 Vd.16B, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    @overload
    def add_saturate(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqadd_u8 (uint8x8_t a, uint8x8_t b)  A32: VQADD.U8 Dd, Dn, Dm  A64: UQADD Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def add_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqaddq_u8 (uint8x16_t a, uint8x16_t b)  A32: VQADD.U8 Qd, Qn, Qm  A64: UQADD Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    def add_saturate_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vqadd_s64 (int64x1_t a, int64x1_t b)  A32: VQADD.S64 Dd, Dn, Dm  A64: SQADD Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def add_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vadd_f64 (float64x1_t a, float64x1_t b)  A32: VADD.F64 Dd, Dn, Dm  A64: FADD Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def add_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vadd_s64 (int64x1_t a, int64x1_t b)  A32: VADD.I64 Dd, Dn, Dm  A64: ADD Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def add_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vaddl_u8 (uint8x8_t a, uint8x8_t b)  A32: VADDL.U8 Qd, Dn, Dm  A64: UADDL Vd.8H, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def add_widening_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vaddw_s8 (int16x8_t a, int8x8_t b)  A32: VADDW.S8 Qd, Qn, Dm  A64: SADDW Vd.8H, Vn.8H, Vm.8B"""
        ...

    @staticmethod
    def add_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vaddl_high_u8 (uint8x16_t a, uint8x16_t b)  A32: VADDL.U8 Qd, Dn+1, Dm+1  A64: UADDL2 Vd.8H, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vand_u8 (uint8x8_t a, uint8x8_t b)  A32: VAND Dd, Dn, Dm  A64: AND Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vand_f64 (float64x1_t a, float64x1_t b)  A32: VAND Dd, Dn, Dm  A64: AND Vd.8B, Vn.8B, Vm.8BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vandq_u8 (uint8x16_t a, uint8x16_t b)  A32: VAND Qd, Qn, Qm  A64: AND Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t vandq_f64 (float64x2_t a, float64x2_t b)  A32: VAND Qd, Qn, Qm  A64: AND Vd.16B, Vn.16B, Vm.16BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def bitwise_clear(value: System.Runtime.Intrinsics.Vector64[int], mask: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vbic_u8 (uint8x8_t a, uint8x8_t b)  A32: VBIC Dd, Dn, Dm  A64: BIC Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def bitwise_clear(value: System.Runtime.Intrinsics.Vector64[float], mask: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vbic_f64 (float64x1_t a, float64x1_t b)  A32: VBIC Dd, Dn, Dm  A64: BIC Vd.8B, Vn.8B, Vm.8BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def bitwise_clear(value: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vbicq_u8 (uint8x16_t a, uint8x16_t b)  A32: VBIC Qd, Qn, Qm  A64: BIC Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def bitwise_clear(value: System.Runtime.Intrinsics.Vector128[float], mask: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t vbicq_f64 (float64x2_t a, float64x2_t b)  A32: VBIC Qd, Qn, Qm  A64: BIC Vd.16B, Vn.16B, Vm.16BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def bitwise_select(select: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vbsl_u8 (uint8x8_t a, uint8x8_t b, uint8x8_t c)  A32: VBSL Dd, Dn, Dm  A64: BSL Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def bitwise_select(select: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vbsl_f64 (uint64x1_t a, float64x1_t b, float64x1_t c)  A32: VBSL Dd, Dn, Dm  A64: BSL Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def bitwise_select(select: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vbslq_u8 (uint8x16_t a, uint8x16_t b, uint8x16_t c)  A32: VBSL Qd, Qn, Qm  A64: BSL Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def bitwise_select(select: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t vbslq_f64 (uint64x2_t a, float64x2_t b, float64x2_t c)  A32: VBSL Qd, Qn, Qm  A64: BSL Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def ceiling(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrndp_f32 (float32x2_t a)  A32: VRINTP.F32 Dd, Dm  A64: FRINTP Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def ceiling(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrndpq_f32 (float32x4_t a)  A32: VRINTP.F32 Qd, Qm  A64: FRINTP Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def ceiling_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vrndp_f64 (float64x1_t a)  A32: VRINTP.F64 Dd, Dm  A64: FRINTP Dd, Dn"""
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vceq_u8 (uint8x8_t a, uint8x8_t b)  A32: VCEQ.I8 Dd, Dn, Dm  A64: CMEQ Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """uint32x2_t vceq_f32 (float32x2_t a, float32x2_t b)  A32: VCEQ.F32 Dd, Dn, Dm  A64: FCMEQ Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vceqq_u8 (uint8x16_t a, uint8x16_t b)  A32: VCEQ.I8 Qd, Qn, Qm  A64: CMEQ Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """uint32x4_t vceqq_f32 (float32x4_t a, float32x4_t b)  A32: VCEQ.F32 Qd, Qn, Qm  A64: FCMEQ Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vcgt_u8 (uint8x8_t a, uint8x8_t b)  A32: VCGT.U8 Dd, Dn, Dm  A64: CMHI Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """uint32x2_t vcgt_f32 (float32x2_t a, float32x2_t b)  A32: VCGT.F32 Dd, Dn, Dm  A64: FCMGT Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vcgtq_u8 (uint8x16_t a, uint8x16_t b)  A32: VCGT.U8 Qd, Qn, Qm  A64: CMHI Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """uint32x4_t vcgtq_f32 (float32x4_t a, float32x4_t b)  A32: VCGT.F32 Qd, Qn, Qm  A64: FCMGT Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vcge_u8 (uint8x8_t a, uint8x8_t b)  A32: VCGE.U8 Dd, Dn, Dm  A64: CMHS Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """uint32x2_t vcge_f32 (float32x2_t a, float32x2_t b)  A32: VCGE.F32 Dd, Dn, Dm  A64: FCMGE Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vcgeq_u8 (uint8x16_t a, uint8x16_t b)  A32: VCGE.U8 Qd, Qn, Qm  A64: CMHS Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """uint32x4_t vcgeq_f32 (float32x4_t a, float32x4_t b)  A32: VCGE.F32 Qd, Qn, Qm  A64: FCMGE Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vclt_u8 (uint8x8_t a, uint8x8_t b)  A32: VCLT.U8 Dd, Dn, Dm  A64: CMHI Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """uint32x2_t vclt_f32 (float32x2_t a, float32x2_t b)  A32: VCLT.F32 Dd, Dn, Dm  A64: FCMGT Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vcltq_u8 (uint8x16_t a, uint8x16_t b)  A32: VCLT.U8 Qd, Qn, Qm  A64: CMHI Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """uint32x4_t vcltq_f32 (float32x4_t a, float32x4_t b)  A32: VCLT.F32 Qd, Qn, Qm  A64: FCMGT Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vcle_u8 (uint8x8_t a, uint8x8_t b)  A32: VCLE.U8 Dd, Dn, Dm  A64: CMHS Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """uint32x2_t vcle_f32 (float32x2_t a, float32x2_t b)  A32: VCLE.F32 Dd, Dn, Dm  A64: FCMGE Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vcleq_u8 (uint8x16_t a, uint8x16_t b)  A32: VCLE.U8 Qd, Qn, Qm  A64: CMHS Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """uint32x4_t vcleq_f32 (float32x4_t a, float32x4_t b)  A32: VCLE.F32 Qd, Qn, Qm  A64: FCMGE Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def compare_test(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vtst_u8 (uint8x8_t a, uint8x8_t b)  A32: VTST.8 Dd, Dn, Dm  A64: CMTST Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def compare_test(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """uint32x2_t vtst_f32 (float32x2_t a, float32x2_t b)  A32: VTST.32 Dd, Dn, Dm  A64: CMTST Vd.2S, Vn.2S, Vm.2SThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def compare_test(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vtstq_u8 (uint8x16_t a, uint8x16_t b)  A32: VTST.8 Qd, Qn, Qm  A64: CMTST Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def compare_test(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """uint32x4_t vtstq_f32 (float32x4_t a, float32x4_t b)  A32: VTST.32 Qd, Qn, Qm  A64: CMTST Vd.4S, Vn.4S, Vm.4SThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_away_from_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32x2_t vcvta_s32_f32 (float32x2_t a)  A32: VCVTA.S32.F32 Dd, Dm  A64: FCVTAS Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vcvtaq_s32_f32 (float32x4_t a)  A32: VCVTA.S32.F32 Qd, Qm  A64: FCVTAS Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_int_32_round_away_from_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32_t vcvtas_s32_f32 (float32_t a)  A32: VCVTA.S32.F32 Sd, Sm  A64: FCVTAS Sd, Sn"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_even(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32x2_t vcvtn_s32_f32 (float32x2_t a)  A32: VCVTN.S32.F32 Dd, Dm  A64: FCVTNS Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_even(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vcvtnq_s32_f32 (float32x4_t a)  A32: VCVTN.S32.F32 Qd, Qm  A64: FCVTNS Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_int_32_round_to_even_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32_t vcvtns_s32_f32 (float32_t a)  A32: VCVTN.S32.F32 Sd, Sm  A64: FCVTNS Sd, Sn"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32x2_t vcvtm_s32_f32 (float32x2_t a)  A32: VCVTM.S32.F32 Dd, Dm  A64: FCVTMS Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vcvtmq_s32_f32 (float32x4_t a)  A32: VCVTM.S32.F32 Qd, Qm  A64: FCVTMS Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_int_32_round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32_t vcvtms_s32_f32 (float32_t a)  A32: VCVTM.S32.F32 Sd, Sm  A64: FCVTMS Sd, Sn"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32x2_t vcvtp_s32_f32 (float32x2_t a)  A32: VCVTP.S32.F32 Dd, Dm  A64: FCVTPS Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vcvtpq_s32_f32 (float32x4_t a)  A32: VCVTP.S32.F32 Qd, Qm  A64: FCVTPS Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_int_32_round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32_t vcvtps_s32_f32 (float32_t a)  A32: VCVTP.S32.F32 Sd, Sm  A64: FCVTPS Sd, Sn"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32x2_t vcvt_s32_f32 (float32x2_t a)  A32: VCVT.S32.F32 Dd, Dm  A64: FCVTZS Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vcvtq_s32_f32 (float32x4_t a)  A32: VCVT.S32.F32 Qd, Qm  A64: FCVTZS Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_int_32_round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32_t vcvts_s32_f32 (float32_t a)  A32: VCVT.S32.F32 Sd, Sm  A64: FCVTZS Sd, Sn"""
        ...

    @staticmethod
    @overload
    def convert_to_single(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vcvt_f32_s32 (int32x2_t a)  A32: VCVT.F32.S32 Dd, Dm  A64: SCVTF Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vcvtq_f32_s32 (int32x4_t a)  A32: VCVT.F32.S32 Qd, Qm  A64: SCVTF Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_single_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32_t vcvts_f32_s32 (int32_t a)  A32: VCVT.F32.S32 Sd, Sm  A64: SCVTF Sd, Sn"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_away_from_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32x2_t vcvta_u32_f32 (float32x2_t a)  A32: VCVTA.U32.F32 Dd, Dm  A64: FCVTAU Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vcvtaq_u32_f32 (float32x4_t a)  A32: VCVTA.U32.F32 Qd, Qm  A64: FCVTAU Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_u_int_32_round_away_from_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32_t vcvtas_u32_f32 (float32_t a)  A32: VCVTA.U32.F32 Sd, Sm  A64: FCVTAU Sd, Sn"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_even(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32x2_t vcvtn_u32_f32 (float32x2_t a)  A32: VCVTN.U32.F32 Dd, Dm  A64: FCVTNU Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_even(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vcvtnq_u32_f32 (float32x4_t a)  A32: VCVTN.U32.F32 Qd, Qm  A64: FCVTNU Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_u_int_32_round_to_even_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32_t vcvtns_u32_f32 (float32_t a)  A32: VCVTN.U32.F32 Sd, Sm  A64: FCVTNU Sd, Sn"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32x2_t vcvtm_u32_f32 (float32x2_t a)  A32: VCVTM.U32.F32 Dd, Dm  A64: FCVTMU Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vcvtmq_u32_f32 (float32x4_t a)  A32: VCVTM.U32.F32 Qd, Qm  A64: FCVTMU Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_u_int_32_round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32_t vcvtms_u32_f32 (float32_t a)  A32: VCVTM.U32.F32 Sd, Sm  A64: FCVTMU Sd, Sn"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32x2_t vcvtp_u32_f32 (float32x2_t a)  A32: VCVTP.U32.F32 Dd, Dm  A64: FCVTPU Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vcvtpq_u32_f32 (float32x4_t a)  A32: VCVTP.U32.F32 Qd, Qm  A64: FCVTPU Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_u_int_32_round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32_t vcvtps_u32_f32 (float32_t a)  A32: VCVTP.U32.F32 Sd, Sm  A64: FCVTPU Sd, Sn"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32x2_t vcvt_u32_f32 (float32x2_t a)  A32: VCVT.U32.F32 Dd, Dm  A64: FCVTZU Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vcvtq_u32_f32 (float32x4_t a)  A32: VCVT.U32.F32 Qd, Qm  A64: FCVTZU Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def convert_to_u_int_32_round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32_t vcvts_u32_f32 (float32_t a)  A32: VCVT.U32.F32 Sd, Sm  A64: FCVTZU Sd, Sn"""
        ...

    @staticmethod
    def divide_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vdiv_f64 (float64x1_t a, float64x1_t b)  A32: VDIV.F64 Dd, Dn, Dm  A64: FDIV Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector64[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vdupq_lane_u8 (uint8x8_t vec, const int lane)  A32: VDUP.8 Qd, Dm[index]  A64: DUP Vd.16B, Vn.B[index]"""
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector64[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vdupq_lane_f32 (float32x2_t vec, const int lane)  A32: VDUP.32 Qd, Dm[index]  A64: DUP Vd.4S, Vn.S[index]"""
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vdupq_lane_u8 (uint8x16_t vec, const int lane)  A32: VDUP.8 Qd, Dm[index]  A64: DUP Vd.16B, Vn.B[index]"""
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vdupq_lane_f32 (float32x4_t vec, const int lane)  A32: VDUP.32 Qd, Dm[index]  A64: DUP Vd.4S, Vn.S[index]"""
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_64(value: System.Runtime.Intrinsics.Vector64[int], index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vdup_lane_u8 (uint8x8_t vec, const int lane)  A32: VDUP.8 Dd, Dm[index]  A64: DUP Vd.8B, Vn.B[index]"""
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_64(value: System.Runtime.Intrinsics.Vector64[float], index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vdup_lane_f32 (float32x2_t vec, const int lane)  A32: VDUP.32 Dd, Dm[index]  A64: DUP Vd.2S, Vn.S[index]"""
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_64(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vdup_laneq_u8 (uint8x16_t vec, const int lane)  A32: VDUP.8 Dd, Dm[index]  A64: DUP Vd.8B, Vn.B[index]"""
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_64(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vdup_laneq_f32 (float32x4_t vec, const int lane)  A32: VDUP.32 Dd, Dm[index]  A64: DUP Vd.2S, Vn.S[index]"""
        ...

    @staticmethod
    @overload
    def duplicate_to_vector_128(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vdupq_n_u8 (uint8_t value)  A32: VDUP.8 Qd, Rt  A64: DUP Vd.16B, Rn"""
        ...

    @staticmethod
    @overload
    def duplicate_to_vector_128(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vdupq_n_f32 (float32_t value)  A32: VDUP Qd, Dm[0]  A64: DUP Vd.4S, Vn.S[0]"""
        ...

    @staticmethod
    @overload
    def duplicate_to_vector_64(value: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vdup_n_u8 (uint8_t value)  A32: VDUP.8 Dd, Rt  A64: DUP Vd.8B, Rn"""
        ...

    @staticmethod
    @overload
    def duplicate_to_vector_64(value: float) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vdup_n_f32 (float32_t value)  A32: VDUP Dd, Dm[0]  A64: DUP Vd.2S, Vn.S[0]"""
        ...

    @staticmethod
    @overload
    def extract(vector: System.Runtime.Intrinsics.Vector64[int], index: int) -> int:
        """uint8_t vget_lane_u8 (uint8x8_t v, const int lane)  A32: VMOV.U8 Rt, Dn[lane]  A64: UMOV Wd, Vn.B[lane]"""
        ...

    @staticmethod
    @overload
    def extract(vector: System.Runtime.Intrinsics.Vector64[float], index: int) -> float:
        """float32_t vget_lane_f32 (float32x2_t v, const int lane)  A32: VMOV.F32 Sd, Sm  A64: DUP Sd, Vn.S[lane]"""
        ...

    @staticmethod
    @overload
    def extract(vector: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        """uint8_t vgetq_lane_u8 (uint8x16_t v, const int lane)  A32: VMOV.U8 Rt, Dn[lane]  A64: UMOV Wd, Vn.B[lane]"""
        ...

    @staticmethod
    @overload
    def extract(vector: System.Runtime.Intrinsics.Vector128[float], index: int) -> float:
        """float64_t vgetq_lane_f64 (float64x2_t v, const int lane)  A32: VMOV.F64 Dd, Dm  A64: DUP Dd, Vn.D[lane]"""
        ...

    @staticmethod
    def extract_narrowing_lower(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vmovn_u16 (uint16x8_t a)  A32: VMOVN.I16 Dd, Qm  A64: XTN Vd.8B, Vn.8H"""
        ...

    @staticmethod
    def extract_narrowing_saturate_lower(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqmovn_u16 (uint16x8_t a)  A32: VQMOVN.U16 Dd, Qm  A64: UQXTN Vd.8B, Vn.8H"""
        ...

    @staticmethod
    def extract_narrowing_saturate_unsigned_lower(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqmovun_s16 (int16x8_t a)  A32: VQMOVUN.S16 Dd, Qm  A64: SQXTUN Vd.8B, Vn.8H"""
        ...

    @staticmethod
    def extract_narrowing_saturate_unsigned_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqmovun_high_s16 (uint8x8_t r, int16x8_t a)  A32: VQMOVUN.S16 Dd+1, Qm  A64: SQXTUN2 Vd.16B, Vn.8H"""
        ...

    @staticmethod
    def extract_narrowing_saturate_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqmovn_high_u16 (uint8x8_t r, uint16x8_t a)  A32: VQMOVN.U16 Dd+1, Qm  A64: UQXTN2 Vd.16B, Vn.8H"""
        ...

    @staticmethod
    def extract_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vmovn_high_u16 (uint8x8_t r, uint16x8_t a)  A32: VMOVN.I16 Dd+1, Qm  A64: XTN2 Vd.16B, Vn.8H"""
        ...

    @staticmethod
    @overload
    def extract_vector_128(upper: System.Runtime.Intrinsics.Vector128[int], lower: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vextq_s8 (uint8x16_t a, uint8x16_t b, const int n)  A32: VEXT.8 Qd, Qn, Qm, #n  A64: EXT Vd.16B, Vn.16B, Vm.16B, #n"""
        ...

    @staticmethod
    @overload
    def extract_vector_128(upper: System.Runtime.Intrinsics.Vector128[float], lower: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t vextq_f64 (float64x2_t a, float64x2_t b, const int n)  A32: VEXT.8 Qd, Qn, Qm, #(n*8)  A64: EXT Vd.16B, Vn.16B, Vm.16B, #(n*8)"""
        ...

    @staticmethod
    @overload
    def extract_vector_64(upper: System.Runtime.Intrinsics.Vector64[int], lower: System.Runtime.Intrinsics.Vector64[int], index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vext_s8 (uint8x8_t a, uint8x8_t b, const int n)  A32: VEXT.8 Dd, Dn, Dm, #n  A64: EXT Vd.8B, Vn.8B, Vm.8B, #n"""
        ...

    @staticmethod
    @overload
    def extract_vector_64(upper: System.Runtime.Intrinsics.Vector64[float], lower: System.Runtime.Intrinsics.Vector64[float], index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vext_f32 (float32x2_t a, float32x2_t b, const int n)  A32: VEXT.8 Dd, Dn, Dm, #(n*4)  A64: EXT Vd.8B, Vn.8B, Vm.8B, #(n*4)"""
        ...

    @staticmethod
    @overload
    def floor(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrndm_f32 (float32x2_t a)  A32: VRINTM.F32 Dd, Dm  A64: FRINTM Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def floor(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrndmq_f32 (float32x4_t a)  A32: VRINTM.F32 Qd, Qm  A64: FRINTM Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def floor_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vrndm_f64 (float64x1_t a)  A32: VRINTM.F64 Dd, Dm  A64: FRINTM Dd, Dn"""
        ...

    @staticmethod
    @overload
    def fused_add_halving(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vhadd_u8 (uint8x8_t a, uint8x8_t b)  A32: VHADD.U8 Dd, Dn, Dm  A64: UHADD Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def fused_add_halving(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vhaddq_u8 (uint8x16_t a, uint8x16_t b)  A32: VHADD.U8 Qd, Qn, Qm  A64: UHADD Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def fused_add_rounded_halving(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vrhadd_u8 (uint8x8_t a, uint8x8_t b)  A32: VRHADD.U8 Dd, Dn, Dm  A64: URHADD Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def fused_add_rounded_halving(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vrhaddq_u8 (uint8x16_t a, uint8x16_t b)  A32: VRHADD.U8 Qd, Qn, Qm  A64: URHADD Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def fused_multiply_add(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vfma_f32 (float32x2_t a, float32x2_t b, float32x2_t c)  A32: VFMA.F32 Dd, Dn, Dm  A64: FMLA Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def fused_multiply_add(addend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vfmaq_f32 (float32x4_t a, float32x4_t b, float32x4_t c)  A32: VFMA.F32 Qd, Qn, Qm  A64: FMLA Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    def fused_multiply_add_negated_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vfnma_f64 (float64x1_t a, float64x1_t b, float64x1_t c)  A32: VFNMA.F64 Dd, Dn, Dm  A64: FNMADD Dd, Dn, Dm, DaThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    def fused_multiply_add_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vfma_f64 (float64x1_t a, float64x1_t b, float64x1_t c)  A32: VFMA.F64 Dd, Dn, Dm  A64: FMADD Dd, Dn, Dm, Da"""
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vfms_f32 (float32x2_t a, float32x2_t b, float32x2_t c)  A32: VFMS.F32 Dd, Dn, Dm  A64: FMLS Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract(minuend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vfmsq_f32 (float32x4_t a, float32x4_t b, float32x4_t c)  A32: VFMS.F32 Qd, Qn, Qm  A64: FMLS Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    def fused_multiply_subtract_negated_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vfnms_f64 (float64x1_t a, float64x1_t b, float64x1_t c)  A32: VFNMS.F64 Dd, Dn, Dm  A64: FNMSUB Dd, Dn, Dm, DaThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    def fused_multiply_subtract_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vfms_f64 (float64x1_t a, float64x1_t b, float64x1_t c)  A32: VFMS.F64 Dd, Dn, Dm  A64: FMSUB Dd, Dn, Dm, Da"""
        ...

    @staticmethod
    @overload
    def fused_subtract_halving(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vhsub_u8 (uint8x8_t a, uint8x8_t b)  A32: VHSUB.U8 Dd, Dn, Dm  A64: UHSUB Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def fused_subtract_halving(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vhsubq_u8 (uint8x16_t a, uint8x16_t b)  A32: VHSUB.U8 Qd, Qn, Qm  A64: UHSUB Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def insert(vector: System.Runtime.Intrinsics.Vector64[int], index: int, data: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vset_lane_u8 (uint8_t a, uint8x8_t v, const int lane)  A32: VMOV.8 Dd[lane], Rt  A64: INS Vd.B[lane], Wn"""
        ...

    @staticmethod
    @overload
    def insert(vector: System.Runtime.Intrinsics.Vector64[float], index: int, data: float) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vset_lane_f32 (float32_t a, float32x2_t v, const int lane)  A32: VMOV.F32 Sd, Sm  A64: INS Vd.S[lane], Vn.S[0]"""
        ...

    @staticmethod
    @overload
    def insert(vector: System.Runtime.Intrinsics.Vector128[int], index: int, data: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vsetq_lane_u8 (uint8_t a, uint8x16_t v, const int lane)  A32: VMOV.8 Dd[lane], Rt  A64: INS Vd.B[lane], Wn"""
        ...

    @staticmethod
    @overload
    def insert(vector: System.Runtime.Intrinsics.Vector128[float], index: int, data: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t vsetq_lane_f64 (float64_t a, float64x2_t v, const int lane)  A32: VMOV.F64 Dd, Dm  A64: INS Vd.D[lane], Vn.D[0]"""
        ...

    @staticmethod
    @overload
    def insert_scalar(result: System.Runtime.Intrinsics.Vector128[float], result_index: int, value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t vcopyq_lane_f64 (float64x2_t a, const int lane1, float64x1_t b, const int lane2)  A32: VMOV.F64 Dd, Dm  A64: INS Vd.D[lane1], Vn.D[0]"""
        ...

    @staticmethod
    @overload
    def insert_scalar(result: System.Runtime.Intrinsics.Vector128[int], result_index: int, value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int64x2_t vcopyq_lane_s64 (int64x2_t a, const int lane1, int64x1_t b, const int lane2)  A32: VMOV Dd, Dm  A64: INS Vd.D[lane1], Vn.D[0]"""
        ...

    @staticmethod
    @overload
    def leading_sign_count(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vcls_s16 (int16x4_t a)  A32: VCLS.S16 Dd, Dm  A64: CLS Vd.4H, Vn.4H"""
        ...

    @staticmethod
    @overload
    def leading_sign_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vclsq_s16 (int16x8_t a)  A32: VCLS.S16 Qd, Qm  A64: CLS Vd.8H, Vn.8H"""
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vclz_u8 (uint8x8_t a)  A32: VCLZ.I8 Dd, Dm  A64: CLZ Vd.8B, Vn.8B"""
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vclzq_u8 (uint8x16_t a)  A32: VCLZ.I8 Qd, Qm  A64: CLZ Vd.16B, Vn.16B"""
        ...

    @staticmethod
    def load_2_x_vector_64(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD1 { Vn.8B, Vn+1.8B }, [Xn]"""
        ...

    @staticmethod
    def load_2_x_vector_64_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD2 { Vn.8B, Vn+1.8B }, [Xn]"""
        ...

    @staticmethod
    def load_3_x_vector_64(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD1 { Vn.8B, Vn+1.8B, Vn+2.8B }, [Xn]"""
        ...

    @staticmethod
    def load_3_x_vector_64_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD3 { Vn.8B, Vn+1.8B, Vn+2.8B }, [Xn]"""
        ...

    @staticmethod
    def load_4_x_vector_64(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD1 { Vn.8B, Vn+1.8B, Vn+2.8B, Vn+3.8B }, [Xn]"""
        ...

    @staticmethod
    def load_4_x_vector_64_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD4 { Vn.8B, Vn+1.8B, Vn+2.8B, Vn+3.8B }, [Xn]"""
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(value: System.Runtime.Intrinsics.Vector64[int], index: int, address: typing.Any) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vld1_lane_u8 (uint8_t const * ptr, uint8x8_t src, const int lane)  A32: VLD1.8 { Dd[index] }, [Rn]  A64: LD1 { Vt.B }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(value: System.Runtime.Intrinsics.Vector64[float], index: int, address: typing.Any) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vld1_lane_f32 (float32_t const * ptr, float32x2_t src, const int lane)  A32: VLD1.32 { Dd[index] }, [Rn]  A64: LD1 { Vt.S }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(value: System.Runtime.Intrinsics.Vector128[int], index: int, address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vld1q_lane_u8 (uint8_t const * ptr, uint8x16_t src, const int lane)  A32: VLD1.8 { Dd[index] }, [Rn]  A64: LD1 { Vt.B }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(value: System.Runtime.Intrinsics.Vector128[float], index: int, address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t vld1q_lane_f64 (float64_t const * ptr, float64x2_t src, const int lane)  A32: VLDR.64 Dd, [Rn]  A64: LD1 { Vt.D }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD2 { Vn.8B, Vn+1.8B }[Vm], [Xn]"""
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]:
        """A64: LD2 { Vn.2S, Vn+1.2S }[Vm], [Xn]"""
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD3 { Vn.8B, Vn+1.8B, Vn+2.8B }[Vm], [Xn]"""
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]:
        """A64: LD3 { Vn.2S, Vn+1.2S, Vn+2.2S }[Vm], [Xn]"""
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD4 { Vn.8B, Vn+1.8B, Vn+2.8B, Vn+3.8B }[Vm], [Xn]"""
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]:
        """A64: LD4 { Vn.2S, Vn+1.2S, Vn+2.2S, Vn+3.2S }[Vm], [Xn]"""
        ...

    @staticmethod
    def load_and_replicate_to_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vld1q_dup_u8 (uint8_t const * ptr)  A32: VLD1.8 { Dd[], Dd+1[] }, [Rn]  A64: LD1R { Vt.16B }, [Xn]"""
        ...

    @staticmethod
    def load_and_replicate_to_vector_64(address: typing.Any) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vld1_dup_u8 (uint8_t const * ptr)  A32: VLD1.8 { Dd[] }, [Rn]  A64: LD1R { Vt.8B }, [Xn]"""
        ...

    @staticmethod
    def load_and_replicate_to_vector_64x_2(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD2R { Vn.8B, Vn+1.8B }, [Xn]"""
        ...

    @staticmethod
    def load_and_replicate_to_vector_64x_3(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD3R { Vn.8B, Vn+1.8B, Vn+2.8B }, [Xn]"""
        ...

    @staticmethod
    def load_and_replicate_to_vector_64x_4(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """A64: LD4R { Vn.8B, Vn+1.8B, Vn+2.8B, Vn+3.8B }, [Xn]"""
        ...

    @staticmethod
    def load_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vld1q_u8 (uint8_t const * ptr)  A32: VLD1.8 Dd, Dd+1, [Rn]  A64: LD1 Vt.16B, [Xn]"""
        ...

    @staticmethod
    def load_vector_64(address: typing.Any) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vld1_u8 (uint8_t const * ptr)  A32: VLD1.8 Dd, [Rn]  A64: LD1 Vt.8B, [Xn]"""
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vmax_u8 (uint8x8_t a, uint8x8_t b)  A32: VMAX.U8 Dd, Dn, Dm  A64: UMAX Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vmax_f32 (float32x2_t a, float32x2_t b)  A32: VMAX.F32 Dd, Dn, Dm  A64: FMAX Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vmaxq_u8 (uint8x16_t a, uint8x16_t b)  A32: VMAX.U8 Qd, Qn, Qm  A64: UMAX Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vmaxq_f32 (float32x4_t a, float32x4_t b)  A32: VMAX.F32 Qd, Qn, Qm  A64: FMAX Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def max_number(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vmaxnm_f32 (float32x2_t a, float32x2_t b)  A32: VMAXNM.F32 Dd, Dn, Dm  A64: FMAXNM Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def max_number(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vmaxnmq_f32 (float32x4_t a, float32x4_t b)  A32: VMAXNM.F32 Qd, Qn, Qm  A64: FMAXNM Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    def max_number_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vmaxnm_f64 (float64x1_t a, float64x1_t b)  A32: VMAXNM.F64 Dd, Dn, Dm  A64: FMAXNM Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def max_pairwise(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vpmax_u8 (uint8x8_t a, uint8x8_t b)  A32: VPMAX.U8 Dd, Dn, Dm  A64: UMAXP Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def max_pairwise(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vpmax_f32 (float32x2_t a, float32x2_t b)  A32: VPMAX.F32 Dd, Dn, Dm  A64: FMAXP Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vmin_u8 (uint8x8_t a, uint8x8_t b)  A32: VMIN.U8 Dd, Dn, Dm  A64: UMIN Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vmin_f32 (float32x2_t a, float32x2_t b)  A32: VMIN.F32 Dd, Dn, Dm  A64: FMIN Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vminq_u8 (uint8x16_t a, uint8x16_t b)  A32: VMIN.U8 Qd, Qn, Qm  A64: UMIN Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vminq_f32 (float32x4_t a, float32x4_t b)  A32: VMIN.F32 Qd, Qn, Qm  A64: FMIN Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def min_number(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vminnm_f32 (float32x2_t a, float32x2_t b)  A32: VMINNM.F32 Dd, Dn, Dm  A64: FMINNM Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def min_number(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vminnmq_f32 (float32x4_t a, float32x4_t b)  A32: VMINNM.F32 Qd, Qn, Qm  A64: FMINNM Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    def min_number_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vminnm_f64 (float64x1_t a, float64x1_t b)  A32: VMINNM.F64 Dd, Dn, Dm  A64: FMINNM Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def min_pairwise(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vpmin_u8 (uint8x8_t a, uint8x8_t b)  A32: VPMIN.U8 Dd, Dn, Dm  A64: UMINP Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def min_pairwise(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vpmin_f32 (float32x2_t a, float32x2_t b)  A32: VPMIN.F32 Dd, Dn, Dm  A64: FMINP Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vmul_u8 (uint8x8_t a, uint8x8_t b)  A32: VMUL.I8 Dd, Dn, Dm  A64: MUL Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vmul_f32 (float32x2_t a, float32x2_t b)  A32: VMUL.F32 Dd, Dn, Dm  A64: FMUL Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vmulq_u8 (uint8x16_t a, uint8x16_t b)  A32: VMUL.I8 Qd, Qn, Qm  A64: MUL Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vmulq_f32 (float32x4_t a, float32x4_t b)  A32: VMUL.F32 Qd, Qn, Qm  A64: FMUL Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def multiply_add(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vmla_u8 (uint8x8_t a, uint8x8_t b, uint8x8_t c)  A32: VMLA.I8 Dd, Dn, Dm  A64: MLA Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def multiply_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vmlaq_u8 (uint8x16_t a, uint8x16_t b, uint8x16_t c)  A32: VMLA.I8 Qd, Qn, Qm  A64: MLA Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def multiply_add_by_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vmla_n_s16 (int16x4_t a, int16x4_t b, int16_t c)  A32: VMLA.I16 Dd, Dn, Dm[0]  A64: MLA Vd.4H, Vn.4H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_add_by_scalar(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vmlaq_n_s16 (int16x8_t a, int16x8_t b, int16_t c)  A32: VMLA.I16 Qd, Qn, Dm[0]  A64: MLA Vd.8H, Vn.8H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vmla_lane_s16 (int16x4_t a, int16x4_t b, int16x4_t v, const int lane)  A32: VMLA.I16 Dd, Dn, Dm[lane]  A64: MLA Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vmla_laneq_s16 (int16x4_t a, int16x4_t b, int16x8_t v, const int lane)  A32: VMLA.I16 Dd, Dn, Dm[lane]  A64: MLA Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vmlaq_lane_s16 (int16x8_t a, int16x8_t b, int16x4_t v, const int lane)  A32: VMLA.I16 Qd, Qn, Dm[lane]  A64: MLA Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vmlaq_laneq_s16 (int16x8_t a, int16x8_t b, int16x8_t v, const int lane)  A32: VMLA.I16 Qd, Qn, Dm[lane]  A64: MLA Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vmul_n_s16 (int16x4_t a, int16_t b)  A32: VMUL.I16 Dd, Dn, Dm[0]  A64: MUL Vd.4H, Vn.4H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_by_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vmul_n_f32 (float32x2_t a, float32_t b)  A32: VMUL.F32 Dd, Dn, Dm[0]  A64: FMUL Vd.2S, Vn.2S, Vm.S[0]"""
        ...

    @staticmethod
    @overload
    def multiply_by_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vmulq_n_s16 (int16x8_t a, int16_t b)  A32: VMUL.I16 Qd, Qn, Dm[0]  A64: MUL Vd.8H, Vn.8H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_by_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vmulq_n_f32 (float32x4_t a, float32_t b)  A32: VMUL.F32 Qd, Qn, Dm[0]  A64: FMUL Vd.4S, Vn.4S, Vm.S[0]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vmul_lane_s16 (int16x4_t a, int16x4_t v, const int lane)  A32: VMUL.I16 Dd, Dn, Dm[lane]  A64: MUL Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vmul_laneq_s16 (int16x4_t a, int16x8_t v, const int lane)  A32: VMUL.I16 Dd, Dn, Dm[lane]  A64: MUL Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vmul_lane_f32 (float32x2_t a, float32x2_t v, const int lane)  A32: VMUL.F32 Dd, Dn, Dm[lane]  A64: FMUL Vd.2S, Vn.2S, Vm.S[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vmul_laneq_f32 (float32x2_t a, float32x4_t v, const int lane)  A32: VMUL.F32 Dd, Dn, Dm[lane]  A64: FMUL Vd.2S, Vn.2S, Vm.S[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vmulq_lane_s16 (int16x8_t a, int16x4_t v, const int lane)  A32: VMUL.I16 Qd, Qn, Dm[lane]  A64: MUL Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vmulq_laneq_s16 (int16x8_t a, int16x8_t v, const int lane)  A32: VMUL.I16 Qd, Qn, Dm[lane]  A64: MUL Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vmulq_lane_f32 (float32x4_t a, float32x2_t v, const int lane)  A32: VMUL.F32 Qd, Qn, Dm[lane]  A64: FMUL Vd.4S, Vn.4S, Vm.S[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vmulq_laneq_f32 (float32x4_t a, float32x4_t v, const int lane)  A32: VMUL.F32 Qd, Qn, Dm[lane]  A64: FMUL Vd.4S, Vn.4S, Vm.S[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmull_lane_s16 (int16x4_t a, int16x4_t v, const int lane)  A32: VMULL.S16 Qd, Dn, Dm[lane]  A64: SMULL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmull_laneq_s16 (int16x4_t a, int16x8_t v, const int lane)  A32: VMULL.S16 Qd, Dn, Dm[lane]  A64: SMULL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmlal_lane_s16 (int32x4_t a, int16x4_t b, int16x4_t v, const int lane)  A32: VMLAL.S16 Qd, Dn, Dm[lane]  A64: SMLAL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmlal_laneq_s16 (int32x4_t a, int16x4_t b, int16x8_t v, const int lane)  A32: VMLAL.S16 Qd, Dn, Dm[lane]  A64: SMLAL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmlsl_lane_s16 (int32x4_t a, int16x4_t b, int16x4_t v, const int lane)  A32: VMLSL.S16 Qd, Dn, Dm[lane]  A64: SMLSL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmlsl_laneq_s16 (int32x4_t a, int16x4_t b, int16x8_t v, const int lane)  A32: VMLSL.S16 Qd, Dn, Dm[lane]  A64: SMLSL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmull_high_lane_s16 (int16x8_t a, int16x4_t v, const int lane)  A32: VMULL.S16 Qd, Dn+1, Dm[lane]  A64: SMULL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmull_high_laneq_s16 (int16x8_t a, int16x8_t v, const int lane)  A32: VMULL.S16 Qd, Dn+1, Dm[lane]  A64: SMULL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmlal_high_lane_s16 (int32x4_t a, int16x8_t b, int16x4_t v, const int lane)  A32: VMLAL.S16 Qd, Dn+1, Dm[lane]  A64: SMLAL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmlal_high_laneq_s16 (int32x4_t a, int16x8_t b, int16x8_t v, const int lane)  A32: VMLAL.S16 Qd, Dn+1, Dm[lane]  A64: SMLAL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmlsl_high_lane_s16 (int32x4_t a, int16x8_t b, int16x4_t v, const int lane)  A32: VMLSL.S16 Qd, Dn+1, Dm[lane]  A64: SMLSL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmlsl_high_laneq_s16 (int32x4_t a, int16x8_t b, int16x8_t v, const int lane)  A32: VMLSL.S16 Qd, Dn+1, Dm[lane]  A64: SMLSL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqdmulh_n_s16 (int16x4_t a, int16_t b)  A32: VQDMULH.S16 Dd, Dn, Dm[0]  A64: SQDMULH Vd.4H, Vn.4H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqdmulhq_n_s16 (int16x8_t a, int16_t b)  A32: VQDMULH.S16 Qd, Qn, Dm[0]  A64: SQDMULH Vd.8H, Vn.8H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqdmulh_lane_s16 (int16x4_t a, int16x4_t v, const int lane)  A32: VQDMULH.S16 Dd, Dn, Dm[lane]  A64: SQDMULH Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqdmulh_laneq_s16 (int16x4_t a, int16x8_t v, const int lane)  A32: VQDMULH.S16 Dd, Dn, Dm[lane]  A64: SQDMULH Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqdmulhq_lane_s16 (int16x8_t a, int16x4_t v, const int lane)  A32: VQDMULH.S16 Qd, Qn, Dm[lane]  A64: SQDMULH Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqdmulhq_laneq_s16 (int16x8_t a, int16x8_t v, const int lane)  A32: VQDMULH.S16 Qd, Qn, Dm[lane]  A64: SQDMULH Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqdmulh_s16 (int16x4_t a, int16x4_t b)  A32: VQDMULH.S16 Dd, Dn, Dm  A64: SQDMULH Vd.4H, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqdmulhq_s16 (int16x8_t a, int16x8_t b)  A32: VQDMULH.S16 Qd, Qn, Qm  A64: SQDMULH Vd.8H, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def multiply_doubling_widening_lower_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlal_s16 (int32x4_t a, int16x4_t b, int16x4_t c)  A32: VQDMLAL.S16 Qd, Dn, Dm  A64: SQDMLAL Vd.4S, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    def multiply_doubling_widening_lower_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlsl_s16 (int32x4_t a, int16x4_t b, int16x4_t c)  A32: VQDMLSL.S16 Qd, Dn, Dm  A64: SQDMLSL Vd.4S, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    def multiply_doubling_widening_lower_by_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlal_n_s16 (int32x4_t a, int16x4_t b, int16_t c)  A32: VQDMLAL.S16 Qd, Dn, Dm[0]  A64: SQDMLAL Vd.4S, Vn.4H, Vm.H[0]"""
        ...

    @staticmethod
    def multiply_doubling_widening_lower_by_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlsl_n_s16 (int32x4_t a, int16x4_t b, int16_t c)  A32: VQDMLSL.S16 Qd, Dn, Dm[0]  A64: SQDMLSL Vd.4S, Vn.4H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_lower_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlal_lane_s16 (int32x4_t a, int16x4_t b, int16x4_t v, const int lane)  A32: VQDMLAL.S16 Qd, Dn, Dm[lane]  A64: SQDMLAL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_lower_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlal_laneq_s16 (int32x4_t a, int16x4_t b, int16x8_t v, const int lane)  A32: VQDMLAL.S16 Qd, Dn, Dm[lane]  A64: SQDMLAL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_lower_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlsl_lane_s16 (int32x4_t a, int16x4_t b, int16x4_t v, const int lane)  A32: VQDMLSL.S16 Qd, Dn, Dm[lane]  A64: SQDMLSL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_lower_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlsl_laneq_s16 (int32x4_t a, int16x4_t b, int16x8_t v, const int lane)  A32: VQDMLSL.S16 Qd, Dn, Dm[lane]  A64: SQDMLSL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmull_s16 (int16x4_t a, int16x4_t b)  A32: VQDMULL.S16 Qd, Dn, Dm  A64: SQDMULL Vd.4S, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_lower_by_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmull_n_s16 (int16x4_t a, int16_t b)  A32: VQDMULL.S16 Qd, Dn, Dm[0]  A64: SQDMULL Vd.4S, Vn.4H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_saturate_lower_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmull_lane_s16 (int16x4_t a, int16x4_t v, const int lane)  A32: VQDMULL.S16 Qd, Dn, Dm[lane]  A64: SQDMULL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_saturate_lower_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmull_laneq_s16 (int16x4_t a, int16x8_t v, const int lane)  A32: VQDMULL.S16 Qd, Dn, Dm[lane]  A64: SQDMULL Vd.4S, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmull_high_s16 (int16x8_t a, int16x8_t b)  A32: VQDMULL.S16 Qd, Dn+1, Dm+1  A64: SQDMULL2 Vd.4S, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_upper_by_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmull_high_n_s16 (int16x8_t a, int16_t b)  A32: VQDMULL.S16 Qd, Dn+1, Dm[0]  A64: SQDMULL2 Vd.4S, Vn.8H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_saturate_upper_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmull_high_lane_s16 (int16x8_t a, int16x4_t v, const int lane)  A32: VQDMULL.S16 Qd, Dn+1, Dm[lane]  A64: SQDMULL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_saturate_upper_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmull_high_laneq_s16 (int16x8_t a, int16x8_t v, const int lane)  A32: VQDMULL.S16 Qd, Dn+1, Dm[lane]  A64: SQDMULL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    def multiply_doubling_widening_upper_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlal_high_s16 (int32x4_t a, int16x8_t b, int16x8_t c)  A32: VQDMLAL.S16 Qd, Dn+1, Dm+1  A64: SQDMLAL2 Vd.4S, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def multiply_doubling_widening_upper_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlsl_high_s16 (int32x4_t a, int16x8_t b, int16x8_t c)  A32: VQDMLSL.S16 Qd, Dn+1, Dm+1  A64: SQDMLSL2 Vd.4S, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def multiply_doubling_widening_upper_by_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlal_high_n_s16 (int32x4_t a, int16x8_t b, int16_t c)  A32: VQDMLAL.S16 Qd, Dn+1, Dm[0]  A64: SQDMLAL2 Vd.4S, Vn.8H, Vm.H[0]"""
        ...

    @staticmethod
    def multiply_doubling_widening_upper_by_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlsl_high_n_s16 (int32x4_t a, int16x8_t b, int16_t c)  A32: VQDMLSL.S16 Qd, Dn+1, Dm[0]  A64: SQDMLSL2 Vd.4S, Vn.8H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_upper_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlal_high_lane_s16 (int32x4_t a, int16x8_t b, int16x4_t v, const int lane)  A32: VQDMLAL.S16 Qd, Dn+1, Dm[lane]  A64: SQDMLAL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_upper_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlal_high_laneq_s16 (int32x4_t a, int16x8_t b, int16x8_t v, const int lane)  A32: VQDMLAL.S16 Qd, Dn+1, Dm[lane]  A64: SQDMLAL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_upper_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlsl_high_lane_s16 (int32x4_t a, int16x8_t b, int16x4_t v, const int lane)  A32: VQDMLSL.S16 Qd, Dn+1, Dm[lane]  A64: SQDMLSL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_upper_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vqdmlsl_high_laneq_s16 (int32x4_t a, int16x8_t b, int16x8_t v, const int lane)  A32: VQDMLSL.S16 Qd, Dn+1, Dm[lane]  A64: SQDMLSL2 Vd.4S, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrdmulh_n_s16 (int16x4_t a, int16_t b)  A32: VQRDMULH.S16 Dd, Dn, Dm[0]  A64: SQRDMULH Vd.4H, Vn.4H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrdmulhq_n_s16 (int16x8_t a, int16_t b)  A32: VQRDMULH.S16 Qd, Qn, Dm[0]  A64: SQRDMULH Vd.8H, Vn.8H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrdmulh_lane_s16 (int16x4_t a, int16x4_t v, const int lane)  A32: VQRDMULH.S16 Dd, Dn, Dm[lane]  A64: SQRDMULH Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrdmulh_laneq_s16 (int16x4_t a, int16x8_t v, const int lane)  A32: VQRDMULH.S16 Dd, Dn, Dm[lane]  A64: SQRDMULH Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrdmulhq_lane_s16 (int16x8_t a, int16x4_t v, const int lane)  A32: VQRDMULH.S16 Qd, Qn, Dm[lane]  A64: SQRDMULH Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrdmulhq_laneq_s16 (int16x8_t a, int16x8_t v, const int lane)  A32: VQRDMULH.S16 Qd, Qn, Dm[lane]  A64: SQRDMULH Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrdmulh_s16 (int16x4_t a, int16x4_t b)  A32: VQRDMULH.S16 Dd, Dn, Dm  A64: SQRDMULH Vd.4H, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrdmulhq_s16 (int16x8_t a, int16x8_t b)  A32: VQRDMULH.S16 Qd, Qn, Qm  A64: SQRDMULH Vd.8H, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def multiply_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vmul_f64 (float64x1_t a, float64x1_t b)  A32: VMUL.F64 Dd, Dn, Dm  A64: FMUL Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def multiply_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32_t vmuls_lane_f32 (float32_t a, float32x2_t v, const int lane)  A32: VMUL.F32 Sd, Sn, Dm[lane]  A64: FMUL Sd, Sn, Vm.S[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32_t vmuls_laneq_f32 (float32_t a, float32x4_t v, const int lane)  A32: VMUL.F32 Sd, Sn, Dm[lane]  A64: FMUL Sd, Sn, Vm.S[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_subtract(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vmls_u8 (uint8x8_t a, uint8x8_t b, uint8x8_t c)  A32: VMLS.I8 Dd, Dn, Dm  A64: MLS Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def multiply_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vmlsq_u8 (uint8x16_t a, uint8x16_t b, uint8x16_t c)  A32: VMLS.I8 Qd, Qn, Qm  A64: MLS Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_scalar(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vmls_n_s16 (int16x4_t a, int16x4_t b, int16_t c)  A32: VMLS.I16 Dd, Dn, Dm[0]  A64: MLS Vd.4H, Vn.4H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_scalar(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vmlsq_n_s16 (int16x8_t a, int16x8_t b, int16_t c)  A32: VMLS.I16 Qd, Qn, Dm[0]  A64: MLS Vd.8H, Vn.8H, Vm.H[0]"""
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vmls_lane_s16 (int16x4_t a, int16x4_t b, int16x4_t v, const int lane)  A32: VMLS.I16 Dd, Dn, Dm[lane]  A64: MLS Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vmls_laneq_s16 (int16x4_t a, int16x4_t b, int16x8_t v, const int lane)  A32: VMLS.I16 Dd, Dn, Dm[lane]  A64: MLS Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vmlsq_lane_s16 (int16x8_t a, int16x8_t b, int16x4_t v, const int lane)  A32: VMLS.I16 Qd, Qn, Dm[lane]  A64: MLS Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vmlsq_laneq_s16 (int16x8_t a, int16x8_t b, int16x8_t v, const int lane)  A32: VMLS.I16 Qd, Qn, Dm[lane]  A64: MLS Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    def multiply_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vmull_u8 (uint8x8_t a, uint8x8_t b)  A32: VMULL.U8 Qd, Dn, Dm  A64: UMULL Vd.8H, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    def multiply_widening_lower_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vmlal_u8 (uint16x8_t a, uint8x8_t b, uint8x8_t c)  A32: VMLAL.U8 Qd, Dn, Dm  A64: UMLAL Vd.8H, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    def multiply_widening_lower_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vmlsl_u8 (uint16x8_t a, uint8x8_t b, uint8x8_t c)  A32: VMLSL.U8 Qd, Dn, Dm  A64: UMLSL Vd.8H, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    def multiply_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vmull_high_u8 (uint8x16_t a, uint8x16_t b)  A32: VMULL.U8 Qd, Dn+1, Dm+1  A64: UMULL2 Vd.8H, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    def multiply_widening_upper_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vmlal_high_u8 (uint16x8_t a, uint8x16_t b, uint8x16_t c)  A32: VMLAL.U8 Qd, Dn+1, Dm+1  A64: UMLAL2 Vd.8H, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    def multiply_widening_upper_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vmlsl_high_u8 (uint16x8_t a, uint8x16_t b, uint8x16_t c)  A32: VMLSL.U8 Qd, Dn+1, Dm+1  A64: UMLSL2 Vd.8H, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vneg_s16 (int16x4_t a)  A32: VNEG.S16 Dd, Dm  A64: NEG Vd.4H, Vn.4H"""
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vneg_f32 (float32x2_t a)  A32: VNEG.F32 Dd, Dm  A64: FNEG Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vnegq_s16 (int16x8_t a)  A32: VNEG.S16 Qd, Qm  A64: NEG Vd.8H, Vn.8H"""
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vnegq_f32 (float32x4_t a)  A32: VNEG.F32 Qd, Qm  A64: FNEG Vd.4S, Vn.4S"""
        ...

    @staticmethod
    @overload
    def negate_saturate(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqneg_s16 (int16x4_t a)  A32: VQNEG.S16 Dd, Dm  A64: SQNEG Vd.4H, Vn.4H"""
        ...

    @staticmethod
    @overload
    def negate_saturate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqnegq_s16 (int16x8_t a)  A32: VQNEG.S16 Qd, Qm  A64: SQNEG Vd.8H, Vn.8H"""
        ...

    @staticmethod
    def negate_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vneg_f64 (float64x1_t a)  A32: VNEG.F64 Dd, Dm  A64: FNEG Dd, Dn"""
        ...

    @staticmethod
    @overload
    def Not(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vmvn_u8 (uint8x8_t a)  A32: VMVN Dd, Dm  A64: MVN Vd.8B, Vn.8B"""
        ...

    @staticmethod
    @overload
    def Not(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vmvn_f64 (float64x1_t a)  A32: VMVN Dd, Dm  A64: MVN Vd.8B, Vn.8BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def Not(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vmvnq_u8 (uint8x16_t a)  A32: VMVN Qd, Qm  A64: MVN Vd.16B, Vn.16B"""
        ...

    @staticmethod
    @overload
    def Not(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t vmvnq_f64 (float64x2_t a)  A32: VMVN Qd, Qm  A64: MVN Vd.16B, Vn.16BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vorr_u8 (uint8x8_t a, uint8x8_t b)  A32: VORR Dd, Dn, Dm  A64: ORR Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vorr_f64 (float64x1_t a, float64x1_t b)  A32: VORR Dd, Dn, Dm  A64: ORR Vd.8B, Vn.8B, Vm.8BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vorrq_u8 (uint8x16_t a, uint8x16_t b)  A32: VORR Qd, Qn, Qm  A64: ORR Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t vorrq_f64 (float64x2_t a, float64x2_t b)  A32: VORR Qd, Qn, Qm  A64: ORR Vd.16B, Vn.16B, Vm.16BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def or_not(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vorn_u8 (uint8x8_t a, uint8x8_t b)  A32: VORN Dd, Dn, Dm  A64: ORN Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def or_not(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vorn_f64 (float64x1_t a, float64x1_t b)  A32: VORN Dd, Dn, Dm  A64: ORN Vd.8B, Vn.8B, Vm.8BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def or_not(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vornq_u8 (uint8x16_t a, uint8x16_t b)  A32: VORN Qd, Qn, Qm  A64: ORN Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def or_not(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t vornq_f64 (float64x2_t a, float64x2_t b)  A32: VORN Qd, Qn, Qm  A64: ORN Vd.16B, Vn.16B, Vm.16BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def polynomial_multiply(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """poly8x8_t vmul_p8 (poly8x8_t a, poly8x8_t b)  A32: VMUL.P8 Dd, Dn, Dm  A64: PMUL Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def polynomial_multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """poly8x16_t vmulq_p8 (poly8x16_t a, poly8x16_t b)  A32: VMUL.P8 Qd, Qn, Qm  A64: PMUL Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    def polynomial_multiply_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """poly16x8_t vmull_p8 (poly8x8_t a, poly8x8_t b)  A32: VMULL.P8 Qd, Dn, Dm  A64: PMULL Vd.16B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    def polynomial_multiply_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """poly16x8_t vmull_high_p8 (poly8x16_t a, poly8x16_t b)  A32: VMULL.P8 Qd, Dn+1, Dm+1  A64: PMULL2 Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def pop_count(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vcnt_u8 (uint8x8_t a)  A32: VCNT.I8 Dd, Dm  A64: CNT Vd.8B, Vn.8B"""
        ...

    @staticmethod
    @overload
    def pop_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vcntq_u8 (uint8x16_t a)  A32: VCNT.I8 Qd, Qm  A64: CNT Vd.16B, Vn.16B"""
        ...

    @staticmethod
    @overload
    def reciprocal_estimate(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrecpe_f32 (float32x2_t a)  A32: VRECPE.F32 Dd, Dm  A64: FRECPE Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def reciprocal_estimate(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32x2_t vrecpe_u32 (uint32x2_t a)  A32: VRECPE.U32 Dd, Dm  A64: URECPE Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def reciprocal_estimate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrecpeq_f32 (float32x4_t a)  A32: VRECPE.F32 Qd, Qm  A64: FRECPE Vd.4S, Vn.4S"""
        ...

    @staticmethod
    @overload
    def reciprocal_estimate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vrecpeq_u32 (uint32x4_t a)  A32: VRECPE.U32 Qd, Qm  A64: URECPE Vd.4S, Vn.4S"""
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_estimate(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrsqrte_f32 (float32x2_t a)  A32: VRSQRTE.F32 Dd, Dm  A64: FRSQRTE Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_estimate(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32x2_t vrsqrte_u32 (uint32x2_t a)  A32: VRSQRTE.U32 Dd, Dm  A64: URSQRTE Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_estimate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrsqrteq_f32 (float32x4_t a)  A32: VRSQRTE.F32 Qd, Qm  A64: FRSQRTE Vd.4S, Vn.4S"""
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_estimate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vrsqrteq_u32 (uint32x4_t a)  A32: VRSQRTE.U32 Qd, Qm  A64: URSQRTE Vd.4S, Vn.4S"""
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_step(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrsqrts_f32 (float32x2_t a, float32x2_t b)  A32: VRSQRTS.F32 Dd, Dn, Dm  A64: FRSQRTS Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_step(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrsqrtsq_f32 (float32x4_t a, float32x4_t b)  A32: VRSQRTS.F32 Qd, Qn, Qm  A64: FRSQRTS Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def reciprocal_step(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrecps_f32 (float32x2_t a, float32x2_t b)  A32: VRECPS.F32 Dd, Dn, Dm  A64: FRECPS Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def reciprocal_step(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrecpsq_f32 (float32x4_t a, float32x4_t b)  A32: VRECPS.F32 Qd, Qn, Qm  A64: FRECPS Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    @overload
    def reverse_element_16(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vrev32_s16 (int16x4_t vec)  A32: VREV32.16 Dd, Dm  A64: REV32 Vd.4H, Vn.4H"""
        ...

    @staticmethod
    @overload
    def reverse_element_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vrev32q_s16 (int16x8_t vec)  A32: VREV32.16 Qd, Qm  A64: REV32 Vd.8H, Vn.8H"""
        ...

    @staticmethod
    @overload
    def reverse_element_32(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32x2_t vrev64_s32 (int32x2_t vec)  A32: VREV64.32 Dd, Dm  A64: REV64 Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def reverse_element_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vrev64q_s32 (int32x4_t vec)  A32: VREV64.32 Qd, Qm  A64: REV64 Vd.4S, Vn.4S"""
        ...

    @staticmethod
    @overload
    def reverse_element_8(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int8x8_t vrev16_s8 (int8x8_t vec)  A32: VREV16.8 Dd, Dm  A64: REV16 Vd.8B, Vn.8B"""
        ...

    @staticmethod
    @overload
    def reverse_element_8(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int8x16_t vrev16q_s8 (int8x16_t vec)  A32: VREV16.8 Qd, Qm  A64: REV16 Vd.16B, Vn.16B"""
        ...

    @staticmethod
    @overload
    def round_away_from_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrnda_f32 (float32x2_t a)  A32: VRINTA.F32 Dd, Dm  A64: FRINTA Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrndaq_f32 (float32x4_t a)  A32: VRINTA.F32 Qd, Qm  A64: FRINTA Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def round_away_from_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vrnda_f64 (float64x1_t a)  A32: VRINTA.F64 Dd, Dm  A64: FRINTA Dd, Dn"""
        ...

    @staticmethod
    @overload
    def round_to_nearest(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrndn_f32 (float32x2_t a)  A32: VRINTN.F32 Dd, Dm  A64: FRINTN Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def round_to_nearest(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrndnq_f32 (float32x4_t a)  A32: VRINTN.F32 Qd, Qm  A64: FRINTN Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def round_to_nearest_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vrndn_f64 (float64x1_t a)  A32: VRINTN.F64 Dd, Dm  A64: FRINTN Dd, Dn"""
        ...

    @staticmethod
    @overload
    def round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrndm_f32 (float32x2_t a)  A32: VRINTM.F32 Dd, Dm  A64: FRINTM Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrndmq_f32 (float32x4_t a)  A32: VRINTM.F32 Qd, Qm  A64: FRINTM Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vrndm_f64 (float64x1_t a)  A32: VRINTM.F64 Dd, Dm  A64: FRINTM Dd, Dn"""
        ...

    @staticmethod
    @overload
    def round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrndp_f32 (float32x2_t a)  A32: VRINTP.F32 Dd, Dm  A64: FRINTP Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrndpq_f32 (float32x4_t a)  A32: VRINTP.F32 Qd, Qm  A64: FRINTP Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vrndp_f64 (float64x1_t a)  A32: VRINTP.F64 Dd, Dm  A64: FRINTP Dd, Dn"""
        ...

    @staticmethod
    @overload
    def round_to_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vrnd_f32 (float32x2_t a)  A32: VRINTZ.F32 Dd, Dm  A64: FRINTZ Vd.2S, Vn.2S"""
        ...

    @staticmethod
    @overload
    def round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vrndq_f32 (float32x4_t a)  A32: VRINTZ.F32 Qd, Qm  A64: FRINTZ Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vrnd_f64 (float64x1_t a)  A32: VRINTZ.F64 Dd, Dm  A64: FRINTZ Dd, Dn"""
        ...

    @staticmethod
    @overload
    def shift_arithmetic(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vshl_s16 (int16x4_t a, int16x4_t b)  A32: VSHL.S16 Dd, Dn, Dm  A64: SSHL Vd.4H, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    @overload
    def shift_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vshlq_s16 (int16x8_t a, int16x8_t b)  A32: VSHL.S16 Qd, Qn, Qm  A64: SSHL Vd.8H, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    @overload
    def shift_arithmetic_rounded(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vrshl_s16 (int16x4_t a, int16x4_t b)  A32: VRSHL.S16 Dd, Dn, Dm  A64: SRSHL Vd.4H, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    @overload
    def shift_arithmetic_rounded(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vrshlq_s16 (int16x8_t a, int16x8_t b)  A32: VRSHL.S16 Qd, Qn, Qm  A64: SRSHL Vd.8H, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    @overload
    def shift_arithmetic_rounded_saturate(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrshl_s16 (int16x4_t a, int16x4_t b)  A32: VQRSHL.S16 Dd, Dn, Dm  A64: SQRSHL Vd.4H, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    @overload
    def shift_arithmetic_rounded_saturate(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrshlq_s16 (int16x8_t a, int16x8_t b)  A32: VQRSHL.S16 Qd, Qn, Qm  A64: SQRSHL Vd.8H, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def shift_arithmetic_rounded_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vqrshl_s64 (int64x1_t a, int64x1_t b)  A32: VQRSHL.S64 Dd, Dn, Dm  A64: SQRSHL Dd, Dn, Dm"""
        ...

    @staticmethod
    def shift_arithmetic_rounded_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vrshl_s64 (int64x1_t a, int64x1_t b)  A32: VRSHL.S64 Dd, Dn, Dm  A64: SRSHL Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def shift_arithmetic_saturate(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqshl_s16 (int16x4_t a, int16x4_t b)  A32: VQSHL.S16 Dd, Dn, Dm  A64: SQSHL Vd.4H, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    @overload
    def shift_arithmetic_saturate(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqshlq_s16 (int16x8_t a, int16x8_t b)  A32: VQSHL.S16 Qd, Qn, Qm  A64: SQSHL Vd.8H, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def shift_arithmetic_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vqshl_s64 (int64x1_t a, int64x1_t b)  A32: VQSHL.S64 Dd, Dn, Dm  A64: SQSHL Dd, Dn, Dm"""
        ...

    @staticmethod
    def shift_arithmetic_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vshl_s64 (int64x1_t a, int64x1_t b)  A32: VSHL.S64 Dd, Dn, Dm  A64: SSHL Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def shift_left_and_insert(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], shift: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vsli_n_u8(uint8x8_t a, uint8x8_t b, __builtin_constant_p(n))  A32: VSLI.8 Dd, Dm, #n  A64: SLI Vd.8B, Vn.8B, #n"""
        ...

    @staticmethod
    @overload
    def shift_left_and_insert(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], shift: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vsliq_n_u8(uint8x16_t a, uint8x16_t b, __builtin_constant_p(n))  A32: VSLI.8 Qd, Qm, #n  A64: SLI Vd.16B, Vn.16B, #n"""
        ...

    @staticmethod
    def shift_left_and_insert_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], shift: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64_t vslid_n_s64(int64_t a, int64_t b, __builtin_constant_p(n))  A32: VSLI.64 Dd, Dm, #n  A64: SLI Dd, Dn, #n"""
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vshl_n_u8 (uint8x8_t a, const int n)  A32: VSHL.I8 Dd, Dm, #n  A64: SHL Vd.8B, Vn.8B, #n"""
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vshlq_n_u8 (uint8x16_t a, const int n)  A32: VSHL.I8 Qd, Qm, #n  A64: SHL Vd.16B, Vn.16B, #n"""
        ...

    @staticmethod
    @overload
    def shift_left_logical_saturate(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqshl_n_u8 (uint8x8_t a, const int n)  A32: VQSHL.U8 Dd, Dm, #n  A64: UQSHL Vd.8B, Vn.8B, #n"""
        ...

    @staticmethod
    @overload
    def shift_left_logical_saturate(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqshlq_n_u8 (uint8x16_t a, const int n)  A32: VQSHL.U8 Qd, Qm, #n  A64: UQSHL Vd.16B, Vn.16B, #n"""
        ...

    @staticmethod
    def shift_left_logical_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vqshl_n_s64 (int64x1_t a, const int n)  A32: VQSHL.S64 Dd, Dm, #n  A64: SQSHL Dd, Dn, #n"""
        ...

    @staticmethod
    @overload
    def shift_left_logical_saturate_unsigned(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint16x4_t vqshlu_n_s16 (int16x4_t a, const int n)  A32: VQSHLU.S16 Dd, Dm, #n  A64: SQSHLU Vd.4H, Vn.4H, #n"""
        ...

    @staticmethod
    @overload
    def shift_left_logical_saturate_unsigned(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vqshluq_n_s16 (int16x8_t a, const int n)  A32: VQSHLU.S16 Qd, Qm, #n  A64: SQSHLU Vd.8H, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_left_logical_saturate_unsigned_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint64x1_t vqshlu_n_s64 (int64x1_t a, const int n)  A32: VQSHLU.S64 Dd, Dm, #n  A64: SQSHLU Dd, Dn, #n"""
        ...

    @staticmethod
    def shift_left_logical_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vshl_n_s64 (int64x1_t a, const int n)  A32: VSHL.I64 Dd, Dm, #n  A64: SHL Dd, Dn, #n"""
        ...

    @staticmethod
    def shift_left_logical_widening_lower(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vshll_n_u8 (uint8x8_t a, const int n)  A32: VSHLL.U8 Qd, Dm, #n  A64: USHLL Vd.8H, Vn.8B, #n"""
        ...

    @staticmethod
    def shift_left_logical_widening_upper(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vshll_high_n_u8 (uint8x16_t a, const int n)  A32: VSHLL.U8 Qd, Dm+1, #n  A64: USHLL2 Vd.8H, Vn.16B, #n"""
        ...

    @staticmethod
    @overload
    def shift_logical(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vshl_u8 (uint8x8_t a, int8x8_t b)  A32: VSHL.U8 Dd, Dn, Dm  A64: USHL Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def shift_logical(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vshlq_u8 (uint8x16_t a, int8x16_t b)  A32: VSHL.U8 Qd, Qn, Qm  A64: USHL Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def shift_logical_rounded(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vrshl_u8 (uint8x8_t a, int8x8_t b)  A32: VRSHL.U8 Dd, Dn, Dm  A64: URSHL Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def shift_logical_rounded(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vrshlq_u8 (uint8x16_t a, int8x16_t b)  A32: VRSHL.U8 Qd, Qn, Qm  A64: URSHL Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def shift_logical_rounded_saturate(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqrshl_u8 (uint8x8_t a, int8x8_t b)  A32: VQRSHL.U8 Dd, Dn, Dm  A64: UQRSHL Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def shift_logical_rounded_saturate(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqrshlq_u8 (uint8x16_t a, int8x16_t b)  A32: VQRSHL.U8 Qd, Qn, Qm  A64: UQRSHL Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    def shift_logical_rounded_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint64x1_t vqrshl_u64 (uint64x1_t a, int64x1_t b)  A32: VQRSHL.U64 Dd, Dn, Dm  A64: UQRSHL Dd, Dn, Dm"""
        ...

    @staticmethod
    def shift_logical_rounded_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint64x1_t vrshl_u64 (uint64x1_t a, int64x1_t b)  A32: VRSHL.U64 Dd, Dn, Dm  A64: URSHL Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def shift_logical_saturate(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqshl_u8 (uint8x8_t a, int8x8_t b)  A32: VQSHL.U8 Dd, Dn, Dm  A64: UQSHL Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def shift_logical_saturate(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqshlq_u8 (uint8x16_t a, int8x16_t b)  A32: VQSHL.U8 Qd, Qn, Qm  A64: UQSHL Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    def shift_logical_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint64x1_t vqshl_u64 (uint64x1_t a, int64x1_t b)  A32: VQSHL.U64 Dd, Dn, Dm  A64: UQSHL Dd, Dn, Dm"""
        ...

    @staticmethod
    def shift_logical_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint64x1_t vshl_u64 (uint64x1_t a, int64x1_t b)  A32: VSHL.U64 Dd, Dn, Dm  A64: USHL Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def shift_right_and_insert(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], shift: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vsri_n_u8(uint8x8_t a, uint8x8_t b, __builtin_constant_p(n))  A32: VSRI.8 Dd, Dm, #n  A64: SRI Vd.8B, Vn.8B, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_and_insert(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], shift: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vsriq_n_u8(uint8x16_t a, uint8x16_t b, __builtin_constant_p(n))  A32: VSRI.8 Qd, Qm, #n  A64: SRI Vd.16B, Vn.16B, #n"""
        ...

    @staticmethod
    def shift_right_and_insert_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], shift: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64_t vsrid_n_s64(int64_t a, int64_t b, __builtin_constant_p(n))  A32: VSRI.64 Dd, Dm, #n  A64: SRI Dd, Dn, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vshr_n_s16 (int16x4_t a, const int n)  A32: VSHR.S16 Dd, Dm, #n  A64: SSHR Vd.4H, Vn.4H, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vshrq_n_s16 (int16x8_t a, const int n)  A32: VSHR.S16 Qd, Qm, #n  A64: SSHR Vd.8H, Vn.8H, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_add(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vsra_n_s16 (int16x4_t a, int16x4_t b, const int n)  A32: VSRA.S16 Dd, Dm, #n  A64: SSRA Vd.4H, Vn.4H, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_add(addend: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vsraq_n_s16 (int16x8_t a, int16x8_t b, const int n)  A32: VSRA.S16 Qd, Qm, #n  A64: SSRA Vd.8H, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_add_scalar(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vsra_n_s64 (int64x1_t a, int64x1_t b, const int n)  A32: VSRA.S64 Dd, Dm, #n  A64: SSRA Dd, Dn, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqshrn_n_s32 (int32x4_t a, const int n)  A32: VQSHRN.S32 Dd, Qm, #n  A64: SQSHRN Vd.4H, Vn.4S, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_unsigned_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqshrun_n_s16 (int16x8_t a, const int n)  A32: VQSHRUN.S16 Dd, Qm, #n  A64: SQSHRUN Vd.8B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_unsigned_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqshrun_high_n_s16 (uint8x8_t r, int16x8_t a, const int n)  A32: VQSHRUN.S16 Dd+1, Dn, #n  A64: SQSHRUN2 Vd.16B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqshrn_high_n_s32 (int16x4_t r, int32x4_t a, const int n)  A32: VQSHRN.S32 Dd+1, Qm, #n  A64: SQSHRN2 Vd.8H, Vn.4S, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_rounded(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vrshr_n_s16 (int16x4_t a, const int n)  A32: VRSHR.S16 Dd, Dm, #n  A64: SRSHR Vd.4H, Vn.4H, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_rounded(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vrshrq_n_s16 (int16x8_t a, const int n)  A32: VRSHR.S16 Qd, Qm, #n  A64: SRSHR Vd.8H, Vn.8H, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_rounded_add(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vrsra_n_s16 (int16x4_t a, int16x4_t b, const int n)  A32: VRSRA.S16 Dd, Dm, #n  A64: SRSRA Vd.4H, Vn.4H, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_rounded_add(addend: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vrsraq_n_s16 (int16x8_t a, int16x8_t b, const int n)  A32: VRSRA.S16 Qd, Qm, #n  A64: SRSRA Vd.8H, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_add_scalar(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vrsra_n_s64 (int64x1_t a, int64x1_t b, const int n)  A32: VRSRA.S64 Dd, Dm, #n  A64: SRSRA Dd, Dn, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrshrn_n_s32 (int32x4_t a, const int n)  A32: VQRSHRN.S32 Dd, Qm, #n  A64: SQRSHRN Vd.4H, Vn.4S, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_unsigned_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqrshrun_n_s16 (int16x8_t a, const int n)  A32: VQRSHRUN.S16 Dd, Qm, #n  A64: SQRSHRUN Vd.8B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_unsigned_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqrshrun_high_n_s16 (uint8x8_t r, int16x8_t a, const int n)  A32: VQRSHRUN.S16 Dd+1, Dn, #n  A64: SQRSHRUN2 Vd.16B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrshrn_high_n_s32 (int16x4_t r, int32x4_t a, const int n)  A32: VQRSHRN.S32 Dd+1, Dn, #n  A64: SQRSHRN2 Vd.8H, Vn.4S, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vrshr_n_s64 (int64x1_t a, const int n)  A32: VRSHR.S64 Dd, Dm, #n  A64: SRSHR Dd, Dn, #n"""
        ...

    @staticmethod
    def shift_right_arithmetic_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vshr_n_s64 (int64x1_t a, const int n)  A32: VSHR.S64 Dd, Dm, #n  A64: SSHR Dd, Dn, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vshr_n_u8 (uint8x8_t a, const int n)  A32: VSHR.U8 Dd, Dm, #n  A64: USHR Vd.8B, Vn.8B, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vshrq_n_u8 (uint8x16_t a, const int n)  A32: VSHR.U8 Qd, Qm, #n  A64: USHR Vd.16B, Vn.16B, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_logical_add(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vsra_n_u8 (uint8x8_t a, uint8x8_t b, const int n)  A32: VSRA.U8 Dd, Dm, #n  A64: USRA Vd.8B, Vn.8B, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_logical_add(addend: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vsraq_n_u8 (uint8x16_t a, uint8x16_t b, const int n)  A32: VSRA.U8 Qd, Qm, #n  A64: USRA Vd.16B, Vn.16B, #n"""
        ...

    @staticmethod
    def shift_right_logical_add_scalar(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint64x1_t vsra_n_u64 (uint64x1_t a, uint64x1_t b, const int n)  A32: VSRA.U64 Dd, Dm, #n  A64: USRA Dd, Dn, #n"""
        ...

    @staticmethod
    def shift_right_logical_narrowing_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vshrn_n_u16 (uint16x8_t a, const int n)  A32: VSHRN.I16 Dd, Qm, #n  A64: SHRN Vd.8B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_logical_narrowing_saturate_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqshrn_n_u16 (uint16x8_t a, const int n)  A32: VQSHRN.U16 Dd, Qm, #n  A64: UQSHRN Vd.8B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_logical_narrowing_saturate_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqshrn_high_n_u16 (uint8x8_t r, uint16x8_t a, const int n)  A32: VQSHRN.U16 Dd+1, Qm, #n  A64: UQSHRN2 Vd.16B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_logical_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vshrn_high_n_u16 (uint8x8_t r, uint16x8_t a, const int n)  A32: VSHRN.I16 Dd+1, Qm, #n  A64: SHRN2 Vd.16B, Vn.8H, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_logical_rounded(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vrshr_n_u8 (uint8x8_t a, const int n)  A32: VRSHR.U8 Dd, Dm, #n  A64: URSHR Vd.8B, Vn.8B, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_logical_rounded(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vrshrq_n_u8 (uint8x16_t a, const int n)  A32: VRSHR.U8 Qd, Qm, #n  A64: URSHR Vd.16B, Vn.16B, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_logical_rounded_add(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vrsra_n_u8 (uint8x8_t a, uint8x8_t b, const int n)  A32: VRSRA.U8 Dd, Dm, #n  A64: URSRA Vd.8B, Vn.8B, #n"""
        ...

    @staticmethod
    @overload
    def shift_right_logical_rounded_add(addend: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vrsraq_n_u8 (uint8x16_t a, uint8x16_t b, const int n)  A32: VRSRA.U8 Qd, Qm, #n  A64: URSRA Vd.16B, Vn.16B, #n"""
        ...

    @staticmethod
    def shift_right_logical_rounded_add_scalar(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint64x1_t vrsra_n_u64 (uint64x1_t a, uint64x1_t b, const int n)  A32: VRSRA.U64 Dd, Dm, #n  A64: URSRA Dd, Dn, #n"""
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vrshrn_n_u16 (uint16x8_t a, const int n)  A32: VRSHRN.I16 Dd, Qm, #n  A64: RSHRN Vd.8B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_saturate_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqrshrn_n_u16 (uint16x8_t a, const int n)  A32: VQRSHRN.U16 Dd, Qm, #n  A64: UQRSHRN Vd.8B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_saturate_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqrshrn_high_n_u16 (uint8x8_t r, uint16x8_t a, const int n)  A32: VQRSHRN.U16 Dd+1, Dn, #n  A64: UQRSHRN2 Vd.16B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vrshrn_high_n_u16 (uint8x8_t r, uint16x8_t a, const int n)  A32: VRSHRN.I16 Dd+1, Qm, #n  A64: RSHRN2 Vd.16B, Vn.8H, #n"""
        ...

    @staticmethod
    def shift_right_logical_rounded_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint64x1_t vrshr_n_u64 (uint64x1_t a, const int n)  A32: VRSHR.U64 Dd, Dm, #n  A64: URSHR Dd, Dn, #n"""
        ...

    @staticmethod
    def shift_right_logical_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint64x1_t vshr_n_u64 (uint64x1_t a, const int n)  A32: VSHR.U64 Dd, Dm, #n  A64: USHR Dd, Dn, #n"""
        ...

    @staticmethod
    def sign_extend_widening_lower(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmovl_s16 (int16x4_t a)  A32: VMOVL.S16 Qd, Dm  A64: SXTL Vd.4S, Vn.4H"""
        ...

    @staticmethod
    def sign_extend_widening_upper(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vmovl_high_s16 (int16x8_t a)  A32: VMOVL.S16 Qd, Dm+1  A64: SXTL2 Vd.4S, Vn.8H"""
        ...

    @staticmethod
    def sqrt_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vsqrt_f64 (float64x1_t a)  A32: VSQRT.F64 Dd, Dm  A64: FSQRT Dd, Dn"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector64[int]) -> None:
        """void vst1_u8 (uint8_t * ptr, uint8x8_t val)  A32: VST1.8 { Dd }, [Rn]  A64: ST1 { Vt.8B }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector64[float]) -> None:
        """void vst1_f64 (float64_t * ptr, float64x1_t val)  A32: VST1.64 { Dd }, [Rn]  A64: ST1 { Vt.1D }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        """void vst1q_u8 (uint8_t * ptr, uint8x16_t val)  A32: VST1.8 { Dd, Dd+1 }, [Rn]  A64: ST1 { Vt.16B }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void vst1q_f64 (float64_t * ptr, float64x2_t val)  A32: VST1.64 { Dd, Dd+1 }, [Rn]  A64: ST1 { Vt.2D }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        """A64: ST1 { Vn.8B, Vn+1.8B }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        """A64: ST1 { Vn.2S, Vn+1.2S }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        """A64: ST1 { Vn.8B, Vn+1.8B, Vn+2.8B }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        """A64: ST1 { Vn.2S, Vn+1.2S, Vn+2.2S }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        """A64: ST1 { Vn.8B, Vn+1.8B, Vn+2.8B, Vn+3.8B }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        """A64: ST1 { Vn.2S, Vn+1.2S, Vn+2.2S, Vn+3.2S }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.Runtime.Intrinsics.Vector64[int], index: int) -> None:
        """void vst1_lane_u8 (uint8_t * ptr, uint8x8_t val, const int lane)  A32: VST1.8 { Dd[index] }, [Rn]  A64: ST1 { Vt.B }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.Runtime.Intrinsics.Vector64[float], index: int) -> None:
        """void vst1_lane_f32 (float32_t * ptr, float32x2_t val, const int lane)  A32: VST1.32 { Dd[index] }, [Rn]  A64: ST1 { Vt.S }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.Runtime.Intrinsics.Vector128[int], index: int) -> None:
        """void vst1q_lane_u8 (uint8_t * ptr, uint8x16_t val, const int lane)  A32: VST1.8 { Dd[index] }, [Rn]  A64: ST1 { Vt.B }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.Runtime.Intrinsics.Vector128[float], index: int) -> None:
        """void vst1q_lane_f64 (float64_t * ptr, float64x2_t val, const int lane)  A32: VSTR.64 Dd, [Rn]  A64: ST1 { Vt.D }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int) -> None:
        """A64: ST2 { Vt.8B, Vt+1.8B }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int) -> None:
        """A64: ST2 { Vt.2S, Vt+1.2S }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int) -> None:
        """A64: ST3 { Vt.8B, Vt+1.8B, Vt+2.8B }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int) -> None:
        """A64: ST2 { Vt.2S, Vt+1.2S, Vt+2.2S }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int) -> None:
        """A64: ST4 { Vt.8B, Vt+1.8B, Vt+2.8B, Vt+3.8B }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int) -> None:
        """A64: ST4 { Vt.2S, Vt+1.2S, Vt+2.2S, Vt+3.2S }[index], [Xn]"""
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        """A64: ST2 { Vn.8B, Vn+1.8B }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        """A64: ST2 { Vn.2S, Vn+1.2S }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        """A64: ST3 { Vn.8B, Vn+1.8B, Vn+2.8B }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        """A64: ST3 { Vn.2S, Vn+1.2S, Vn+2.2S }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        """A64: ST4 { Vn.8B, Vn+1.8B, Vn+2.8B, Vn+3.8B }, [Xn]"""
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        """A64: ST4 { Vn.2S, Vn+1.2S, Vn+2.2S, Vn+3.2S }, [Xn]"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vsub_u8 (uint8x8_t a, uint8x8_t b)  A32: VSUB.I8 Dd, Dn, Dm  A64: SUB Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float32x2_t vsub_f32 (float32x2_t a, float32x2_t b)  A32: VSUB.F32 Dd, Dn, Dm  A64: FSUB Vd.2S, Vn.2S, Vm.2S"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vsubq_u8 (uint8x16_t a, uint8x16_t b)  A32: VSUB.I8 Qd, Qn, Qm  A64: SUB Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float32x4_t vsubq_f32 (float32x4_t a, float32x4_t b)  A32: VSUB.F32 Qd, Qn, Qm  A64: FSUB Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    def subtract_high_narrowing_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vsubhn_u16 (uint16x8_t a, uint16x8_t b)  A32: VSUBHN.I16 Dd, Qn, Qm  A64: SUBHN Vd.8B, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def subtract_high_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vsubhn_high_u16 (uint8x8_t r, uint16x8_t a, uint16x8_t b)  A32: VSUBHN.I16 Dd+1, Qn, Qm  A64: SUBHN2 Vd.16B, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def subtract_rounded_high_narrowing_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vrsubhn_u16 (uint16x8_t a, uint16x8_t b)  A32: VRSUBHN.I16 Dd, Qn, Qm  A64: RSUBHN Vd.8B, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    def subtract_rounded_high_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vrsubhn_high_u16 (uint8x8_t r, uint16x8_t a, uint16x8_t b)  A32: VRSUBHN.I16 Dd+1, Qn, Qm  A64: RSUBHN2 Vd.16B, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    @overload
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqsub_u8 (uint8x8_t a, uint8x8_t b)  A32: VQSUB.U8 Dd, Dn, Dm  A64: UQSUB Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vqsubq_u8 (uint8x16_t a, uint8x16_t b)  A32: VQSUB.U8 Qd, Qn, Qm  A64: UQSUB Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    def subtract_saturate_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vqsub_s64 (int64x1_t a, int64x1_t b)  A32: VQSUB.S64 Dd, Dn, Dm  A64: SQSUB Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t vsub_f64 (float64x1_t a, float64x1_t b)  A32: VSUB.F64 Dd, Dn, Dm  A64: FSUB Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int64x1_t vsub_s64 (int64x1_t a, int64x1_t b)  A32: VSUB.I64 Dd, Dn, Dm  A64: SUB Dd, Dn, Dm"""
        ...

    @staticmethod
    @overload
    def subtract_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vsubl_u8 (uint8x8_t a, uint8x8_t b)  A32: VSUBL.U8 Qd, Dn, Dm  A64: USUBL Vd.8H, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def subtract_widening_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vsubw_s8 (int16x8_t a, int8x8_t b)  A32: VSUBW.S8 Qd, Qn, Dm  A64: SSUBW Vd.8H, Vn.8H, Vm.8B"""
        ...

    @staticmethod
    def subtract_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vsubl_high_u8 (uint8x16_t a, uint8x16_t b)  A32: VSUBL.U8 Qd, Dn+1, Dm+1  A64: USUBL2 Vd.8H, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def vector_table_lookup(table: System.Runtime.Intrinsics.Vector128[int], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqvtbl1_u8(uint8x16_t t, uint8x8_t idx)  A32: VTBL Dd, {Dn, Dn+1}, Dm  A64: TBL Vd.8B, {Vn.16B}, Vm.8B"""
        ...

    @staticmethod
    @overload
    def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqtbl2q_u8(uint8x16x2_t t, uint8x8_t idx)  A64: TBL Vd.8B, {Vn.16B, Vn+1.16B}, Vm.8B"""
        ...

    @staticmethod
    @overload
    def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqtbl3q_u8(uint8x16x3_t t, uint8x8_t idx)  A64: TBL Vd.8B, {Vn.16B, Vn+1.16B, Vn+2.16B}, Vm.8B"""
        ...

    @staticmethod
    @overload
    def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqtbl4q_u8(uint8x16x4_t t, uint8x8_t idx)  A64: TBL Vd.8B, {Vn.16B, Vn+1.16B, Vn+2.16B, Vn+3.16B}, Vm.8B"""
        ...

    @staticmethod
    @overload
    def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector64[int], table: System.Runtime.Intrinsics.Vector128[int], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqvtbx1_u8(uint8x8_t r, uint8x16_t t, uint8x8_t idx)  A32: VTBX Dd, {Dn, Dn+1}, Dm  A64: TBX Vd.8B, {Vn.16B}, Vm.8B"""
        ...

    @staticmethod
    @overload
    def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector64[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqtbx2q_u8(uint8x16x2_t t, uint8x8_t idx)  A64: TBX Vd.8B, {Vn.16B, Vn+1.16B}, Vm.8B"""
        ...

    @staticmethod
    @overload
    def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector64[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqtbx3q_u8(uint8x16x3_t t, uint8x8_t idx)  A64: TBX Vd.8B, {Vn.16B, Vn+1.16B, Vn+2.16B}, Vm.8B"""
        ...

    @staticmethod
    @overload
    def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector64[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t vqtbx4q_u8(uint8x16x4_t t, uint8x8_t idx)  A64: TBX Vd.8B, {Vn.16B, Vn+1.16B, Vn+2.16B, Vn+3.16B}, Vm.8B"""
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint8x8_t veor_u8 (uint8x8_t a, uint8x8_t b)  A32: VEOR Dd, Dn, Dm  A64: EOR Vd.8B, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """float64x1_t veor_f64 (float64x1_t a, float64x1_t b)  A32: VEOR Dd, Dn, Dm  A64: EOR Vd.8B, Vn.8B, Vm.8BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t veorq_u8 (uint8x16_t a, uint8x16_t b)  A32: VEOR Qd, Qn, Qm  A64: EOR Vd.16B, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """float64x2_t veorq_f64 (float64x2_t a, float64x2_t b)  A32: VEOR Qd, Qn, Qm  A64: EOR Vd.16B, Vn.16B, Vm.16BThe above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    def zero_extend_widening_lower(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vmovl_u8 (uint8x8_t a)  A32: VMOVL.U8 Qd, Dm  A64: UXTL Vd.8H, Vn.8B"""
        ...

    @staticmethod
    def zero_extend_widening_upper(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint16x8_t vmovl_high_u8 (uint8x16_t a)  A32: VMOVL.U8 Qd, Dm+1  A64: UXTL2 Vd.8H, Vn.16B"""
        ...


class SveMaskPattern(Enum):
    """This class has no documentation."""

    LARGEST_POWER_OF_2 = 0
    """POW2"""

    VECTOR_COUNT_1 = 1
    """VL1"""

    VECTOR_COUNT_2 = 2
    """VL2"""

    VECTOR_COUNT_3 = 3
    """VL3"""

    VECTOR_COUNT_4 = 4
    """VL4"""

    VECTOR_COUNT_5 = 5
    """VL5"""

    VECTOR_COUNT_6 = 6
    """VL6"""

    VECTOR_COUNT_7 = 7
    """VL7"""

    VECTOR_COUNT_8 = 8
    """VL8"""

    VECTOR_COUNT_16 = 9
    """VL16"""

    VECTOR_COUNT_32 = 10
    """VL32"""

    VECTOR_COUNT_64 = 11
    """VL64"""

    VECTOR_COUNT_128 = 12
    """VL128"""

    VECTOR_COUNT_256 = 13
    """VL256"""

    LARGEST_MULTIPLE_OF_4 = 29
    """MUL4"""

    LARGEST_MULTIPLE_OF_3 = 30
    """MUL3"""

    ALL = 31
    """ALL"""


class SvePrefetchType(Enum):
    """This class has no documentation."""

    LOAD_L_1_TEMPORAL = 0
    """PLDL1KEEP"""

    LOAD_L_1_NON_TEMPORAL = 1
    """PLDL1STRM"""

    LOAD_L_2_TEMPORAL = 2
    """PLDL2KEEP"""

    LOAD_L_2_NON_TEMPORAL = 3
    """PLDL2STRM"""

    LOAD_L_3_TEMPORAL = 4
    """PLDL3KEEP"""

    LOAD_L_3_NON_TEMPORAL = 5
    """PLDL3STRM"""

    STORE_L_1_TEMPORAL = 8
    """PSTL1KEEP"""

    STORE_L_1_NON_TEMPORAL = 9
    """PSTL1STRM"""

    STORE_L_2_TEMPORAL = 10
    """PSTL2KEEP"""

    STORE_L_2_NON_TEMPORAL = 11
    """PSTL2STRM"""

    STORE_L_3_TEMPORAL = 12
    """PSTL3KEEP"""

    STORE_L_3_NON_TEMPORAL = 13
    """PSTL3STRM"""


class Sve(System.Runtime.Intrinsics.Arm.AdvSimd, metaclass=abc.ABCMeta):
    """Provides access to the ARM SVE hardware instructions via intrinsics."""

    class Arm64(System.Runtime.Intrinsics.Arm.AdvSimd.Arm64, metaclass=abc.ABCMeta):
        """Provides access to the ARM SVE hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    @overload
    def abs(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svabs[_f64]_m(svfloat64_t inactive, svbool_t pg, svfloat64_t op)svfloat64_t svabs[_f64]_x(svbool_t pg, svfloat64_t op)svfloat64_t svabs[_f64]_z(svbool_t pg, svfloat64_t op)  FABS Ztied.D, Pg/M, Zop.D  FABS Ztied.D, Pg/M, Ztied.D"""
        ...

    @staticmethod
    @overload
    def abs(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint16_t svabs[_s16]_m(svint16_t inactive, svbool_t pg, svint16_t op)svint16_t svabs[_s16]_x(svbool_t pg, svint16_t op)svint16_t svabs[_s16]_z(svbool_t pg, svint16_t op)  ABS Zresult.H, Pg/M, Zop.H"""
        ...

    @staticmethod
    def absolute_compare_greater_than(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svacgt[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FACGT Presult.D, Pg/Z, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def absolute_compare_greater_than_or_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svacge[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FACGE Presult.D, Pg/Z, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def absolute_compare_less_than(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svaclt[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FACLT Presult.D, Pg/Z, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def absolute_compare_less_than_or_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svacle[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FACLE Presult.D, Pg/Z, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svabd[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svabd[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)  UABD Ztied1.B, Pg/M, Ztied1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svabd[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svabd[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svabd[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FABD Ztied1.D, Pg/M, Ztied1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def add(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svadd[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svadd[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svadd[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  ADD Zresult.B, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def add(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svadd[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svadd[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svadd[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FADD Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def add_across(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """float64_t svaddv[_f64](svbool_t pg, svfloat64_t op)  FADDV Dresult, Pg, Zop.D"""
        ...

    @staticmethod
    @overload
    def add_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """int64_t svaddv[_s16](svbool_t pg, svint16_t op)  SADDV Dresult, Pg, Zop.H"""
        ...

    @staticmethod
    def add_rotate_complex(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], rotation: int) -> System.Numerics.Vector[float]:
        """svfloat64_t svcadd[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2, uint64_t imm_rotation)svfloat64_t svcadd[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2, uint64_t imm_rotation)svfloat64_t svcadd[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2, uint64_t imm_rotation)  FCADD Ztied1.D, Pg/M, Ztied1.D, Zop2.D, #imm_rotation"""
        ...

    @staticmethod
    def add_saturate(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svqadd[_u8](svuint8_t op1, svuint8_t op2)  UQADD Zresult.B, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    def add_sequential_across(initial: System.Numerics.Vector[float], value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """float64_t svadda[_f64](svbool_t pg, float64_t initial, svfloat64_t op)  FADDA Dtied, Pg, Dtied, Zop.D"""
        ...

    @staticmethod
    def And(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svand[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svand[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svand[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  AND Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def and_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """uint8_t svandv[_u8](svbool_t pg, svuint8_t op)  ANDV Bresult, Pg, Zop.B"""
        ...

    @staticmethod
    def bitwise_clear(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svbic[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svbic[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svbic[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  BIC Ztied1.B, Pg/M, Ztied1.B, Zop2.B  BIC Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def boolean_not(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svcnot[_u8]_m(svuint8_t inactive, svbool_t pg, svuint8_t op)svuint8_t svcnot[_u8]_x(svbool_t pg, svuint8_t op)svuint8_t svcnot[_u8]_z(svbool_t pg, svuint8_t op)  CNOT Zresult.B, Pg/M, Zop.B"""
        ...

    @staticmethod
    @overload
    def compact(mask: System.Numerics.Vector[float], value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svcompact[_f64](svbool_t pg, svfloat64_t op)  COMPACT Zresult.D, Pg, Zop.D"""
        ...

    @staticmethod
    @overload
    def compact(mask: System.Numerics.Vector[int], value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svcompact[_s32](svbool_t pg, svint32_t op)  COMPACT Zresult.S, Pg, Zop.S"""
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svcmpeq[_u8](svbool_t pg, svuint8_t op1, svuint8_t op2)  CMPEQ Presult.B, Pg/Z, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svcmpeq[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FCMEQ Presult.D, Pg/Z, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svcmpgt[_u8](svbool_t pg, svuint8_t op1, svuint8_t op2)  CMPHI Presult.B, Pg/Z, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svcmpgt[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FCMGT Presult.D, Pg/Z, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svcmpge[_u8](svbool_t pg, svuint8_t op1, svuint8_t op2)  CMPHS Presult.B, Pg/Z, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svcmpge[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FCMGE Presult.D, Pg/Z, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svcmplt[_u8](svbool_t pg, svuint8_t op1, svuint8_t op2)  CMPHI Presult.B, Pg/Z, Zop2.B, Zop1.B"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svcmplt[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FCMGT Presult.D, Pg/Z, Zop2.D, Zop1.D"""
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svcmple[_u8](svbool_t pg, svuint8_t op1, svuint8_t op2)  CMPHS Presult.B, Pg/Z, Zop2.B, Zop1.B"""
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svcmple[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FCMGE Presult.D, Pg/Z, Zop2.D, Zop1.D"""
        ...

    @staticmethod
    @overload
    def compare_not_equal_to(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svcmpne[_u8](svbool_t pg, svuint8_t op1, svuint8_t op2)  CMPNE Presult.B, Pg/Z, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def compare_not_equal_to(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svcmpne[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FCMNE Presult.D, Pg/Z, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def compare_unordered(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svbool_t svcmpuo[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FCMUO Presult.D, Pg/Z, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def compute_16_bit_addresses(bases: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint32_t svadrh[_u32base]_[s32]index(svuint32_t bases, svint32_t indices)  ADR Zresult.S, [Zbases.S, Zindices.S, LSL #1]"""
        ...

    @staticmethod
    def compute_32_bit_addresses(bases: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint32_t svadrw[_u32base]_[s32]index(svuint32_t bases, svint32_t indices)  ADR Zresult.S, [Zbases.S, Zindices.S, LSL #2]"""
        ...

    @staticmethod
    def compute_64_bit_addresses(bases: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint32_t svadrd[_u32base]_[s32]index(svuint32_t bases, svint32_t indices)  ADR Zresult.S, [Zbases.S, Zindices.S, LSL #3]"""
        ...

    @staticmethod
    def compute_8_bit_addresses(bases: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint32_t svadrb[_u32base]_[s32]offset(svuint32_t bases, svint32_t offsets)  ADR Zresult.S, [Zbases.S, Zoffsets.S]"""
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element(mask: System.Numerics.Vector[int], default_value: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svclasta[_u8](svbool_t pg, svuint8_t fallback, svuint8_t data)  CLASTA Btied, Pg, Btied, Zdata.B"""
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element(mask: System.Numerics.Vector[int], default_values: int, data: System.Numerics.Vector[int]) -> int:
        """uint8_t svclasta[_n_u8](svbool_t pg, uint8_t fallback, svuint8_t data)  CLASTA Wtied, Pg, Wtied, Zdata.B"""
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element(mask: System.Numerics.Vector[float], default_value: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svclasta[_f64](svbool_t pg, svfloat64_t fallback, svfloat64_t data)  CLASTA Dtied, Pg, Dtied, Zdata.D"""
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element(mask: System.Numerics.Vector[float], default_values: float, data: System.Numerics.Vector[float]) -> float:
        """float64_t svclasta[_n_f64](svbool_t pg, float64_t fallback, svfloat64_t data)  CLASTA Dtied, Pg, Dtied, Zdata.D"""
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element_and_replicate(mask: System.Numerics.Vector[int], default_scalar: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svclasta[_u8](svbool_t pg, svuint8_t fallback, svuint8_t data)  CLASTA Ztied.B, Pg, Ztied.B, Zdata.B"""
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element_and_replicate(mask: System.Numerics.Vector[float], default_scalar: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svclasta[_f64](svbool_t pg, svfloat64_t fallback, svfloat64_t data)  CLASTA Ztied.D, Pg, Ztied.D, Zdata.D"""
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element(mask: System.Numerics.Vector[int], default_value: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svclastb[_u8](svbool_t pg, svuint8_t fallback, svuint8_t data)  CLASTB Btied, Pg, Btied, Zdata.B"""
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element(mask: System.Numerics.Vector[int], default_values: int, data: System.Numerics.Vector[int]) -> int:
        """uint8_t svclastb[_n_u8](svbool_t pg, uint8_t fallback, svuint8_t data)  CLASTB Wtied, Pg, Wtied, Zdata.B"""
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element(mask: System.Numerics.Vector[float], default_value: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svclastb[_f64](svbool_t pg, svfloat64_t fallback, svfloat64_t data)  CLASTB Dtied, Pg, Dtied, Zdata.D"""
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element(mask: System.Numerics.Vector[float], default_values: float, data: System.Numerics.Vector[float]) -> float:
        """float64_t svclastb[_n_f64](svbool_t pg, float64_t fallback, svfloat64_t data)  CLASTB Dtied, Pg, Dtied, Zdata.D"""
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element_and_replicate(mask: System.Numerics.Vector[int], fallback: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svclastb[_u8](svbool_t pg, svuint8_t fallback, svuint8_t data)  CLASTB Ztied.B, Pg, Ztied.B, Zdata.B"""
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element_and_replicate(mask: System.Numerics.Vector[float], fallback: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svclastb[_f64](svbool_t pg, svfloat64_t fallback, svfloat64_t data)  CLASTB Ztied.D, Pg, Ztied.D, Zdata.D"""
        ...

    @staticmethod
    @overload
    def conditional_select(mask: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svsel[_u8](svbool_t pg, svuint8_t op1, svuint8_t op2)svbool_t svsel[_b](svbool_t pg, svbool_t op1, svbool_t op2)  SEL Zresult.B, Pg, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def conditional_select(mask: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svsel[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  SEL Zresult.D, Pg, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def convert_to_double(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svcvt_f64[_s32]_m(svfloat64_t inactive, svbool_t pg, svint32_t op)svfloat64_t svcvt_f64[_s32]_x(svbool_t pg, svint32_t op)svfloat64_t svcvt_f64[_s32]_z(svbool_t pg, svint32_t op)  SCVTF Zresult.D, Pg/M, Zop.S"""
        ...

    @staticmethod
    @overload
    def convert_to_double(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svcvt_f64[_f32]_m(svfloat64_t inactive, svbool_t pg, svfloat32_t op)svfloat64_t svcvt_f64[_f32]_x(svbool_t pg, svfloat32_t op)svfloat64_t svcvt_f64[_f32]_z(svbool_t pg, svfloat32_t op)  FCVT Zresult.D, Pg/M, Zop.S"""
        ...

    @staticmethod
    def convert_to_int_32(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """svint32_t svcvt_s32[_f64]_m(svint32_t inactive, svbool_t pg, svfloat64_t op)svint32_t svcvt_s32[_f64]_x(svbool_t pg, svfloat64_t op)svint32_t svcvt_s32[_f64]_z(svbool_t pg, svfloat64_t op)  FCVTZS Zresult.S, Pg/M, Zop.D"""
        ...

    @staticmethod
    def convert_to_int_64(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """svint64_t svcvt_s64[_f64]_m(svint64_t inactive, svbool_t pg, svfloat64_t op)svint64_t svcvt_s64[_f64]_x(svbool_t pg, svfloat64_t op)svint64_t svcvt_s64[_f64]_z(svbool_t pg, svfloat64_t op)  FCVTZS Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    @overload
    def convert_to_single(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat32_t svcvt_f32[_f64]_m(svfloat32_t inactive, svbool_t pg, svfloat64_t op)svfloat32_t svcvt_f32[_f64]_x(svbool_t pg, svfloat64_t op)svfloat32_t svcvt_f32[_f64]_z(svbool_t pg, svfloat64_t op)  FCVT Zresult.S, Pg/M, Zop.D"""
        ...

    @staticmethod
    @overload
    def convert_to_single(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat32_t svcvt_f32[_s32]_m(svfloat32_t inactive, svbool_t pg, svint32_t op)svfloat32_t svcvt_f32[_s32]_x(svbool_t pg, svint32_t op)svfloat32_t svcvt_f32[_s32]_z(svbool_t pg, svint32_t op)  SCVTF Zresult.S, Pg/M, Zop.S"""
        ...

    @staticmethod
    def convert_to_u_int_32(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """svuint32_t svcvt_u32[_f64]_m(svuint32_t inactive, svbool_t pg, svfloat64_t op)svuint32_t svcvt_u32[_f64]_x(svbool_t pg, svfloat64_t op)svuint32_t svcvt_u32[_f64]_z(svbool_t pg, svfloat64_t op)  FCVTZU Zresult.S, Pg/M, Zop.D"""
        ...

    @staticmethod
    def convert_to_u_int_64(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """svuint64_t svcvt_u64[_f64]_m(svuint64_t inactive, svbool_t pg, svfloat64_t op)svuint64_t svcvt_u64[_f64]_x(svbool_t pg, svfloat64_t op)svuint64_t svcvt_u64[_f64]_z(svbool_t pg, svfloat64_t op)  FCVTZU Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    def count_16_bit_elements(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """uint64_t svcnth_pat(enum svpattern pattern)  CNTH Xresult, pattern"""
        ...

    @staticmethod
    def count_32_bit_elements(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """uint64_t svcntw_pat(enum svpattern pattern)  CNTW Xresult, pattern"""
        ...

    @staticmethod
    def count_64_bit_elements(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """uint64_t svcntd_pat(enum svpattern pattern)  CNTD Xresult, pattern"""
        ...

    @staticmethod
    def count_8_bit_elements(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """uint64_t svcntb_pat(enum svpattern pattern)  CNTB Xresult, pattern"""
        ...

    @staticmethod
    def create_break_after_mask(mask: System.Numerics.Vector[int], src_mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svbrka[_b]_z(svbool_t pg, svbool_t op)  BRKA Presult.B, Pg/Z, Pop.B"""
        ...

    @staticmethod
    def create_break_after_propagate_mask(mask: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svbrkpa[_b]_z(svbool_t pg, svbool_t op1, svbool_t op2)  BRKPA Presult.B, Pg/Z, Pop1.B, Pop2.B"""
        ...

    @staticmethod
    def create_break_before_mask(mask: System.Numerics.Vector[int], src_mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svbrkb[_b]_z(svbool_t pg, svbool_t op)  BRKB Presult.B, Pg/Z, Pop.B"""
        ...

    @staticmethod
    def create_break_before_propagate_mask(mask: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svbrkpb[_b]_z(svbool_t pg, svbool_t op1, svbool_t op2)  BRKPB Presult.B, Pg/Z, Pop1.B, Pop2.B"""
        ...

    @staticmethod
    def create_break_propagate_mask(total_mask: System.Numerics.Vector[int], from_mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svbrkn[_b]_z(svbool_t pg, svbool_t op1, svbool_t op2)  BRKN Ptied2.B, Pg/Z, Pop1.B, Ptied2.B"""
        ...

    @staticmethod
    def create_false_mask_byte() -> System.Numerics.Vector[int]:
        """svbool_t svpfalse[_b]()  PFALSE Presult.B"""
        ...

    @staticmethod
    def create_false_mask_double() -> System.Numerics.Vector[float]:
        """svbool_t svpfalse[_b]()  PFALSE Presult.B"""
        ...

    @staticmethod
    def create_false_mask_int_16() -> System.Numerics.Vector[int]:
        """svbool_t svpfalse[_b]()  PFALSE Presult.B"""
        ...

    @staticmethod
    def create_false_mask_int_32() -> System.Numerics.Vector[int]:
        """svbool_t svpfalse[_b]()  PFALSE Presult.B"""
        ...

    @staticmethod
    def create_false_mask_int_64() -> System.Numerics.Vector[int]:
        """svbool_t svpfalse[_b]()  PFALSE Presult.B"""
        ...

    @staticmethod
    def create_false_mask_s_byte() -> System.Numerics.Vector[int]:
        """svbool_t svpfalse[_b]()  PFALSE Presult.B"""
        ...

    @staticmethod
    def create_false_mask_single() -> System.Numerics.Vector[float]:
        """svbool_t svpfalse[_b]()  PFALSE Presult.B"""
        ...

    @staticmethod
    def create_false_mask_u_int_16() -> System.Numerics.Vector[int]:
        """svbool_t svpfalse[_b]()  PFALSE Presult.B"""
        ...

    @staticmethod
    def create_false_mask_u_int_32() -> System.Numerics.Vector[int]:
        """svbool_t svpfalse[_b]()  PFALSE Presult.B"""
        ...

    @staticmethod
    def create_false_mask_u_int_64() -> System.Numerics.Vector[int]:
        """svbool_t svpfalse[_b]()  PFALSE Presult.B"""
        ...

    @staticmethod
    def create_mask_for_first_active_element(mask: System.Numerics.Vector[int], src_mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svpfirst[_b](svbool_t pg, svbool_t op)  PFIRST Ptied.B, Pg, Ptied.B"""
        ...

    @staticmethod
    def create_mask_for_next_active_element(mask: System.Numerics.Vector[int], src_mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svbool_t svpnext_b8(svbool_t pg, svbool_t op)  PNEXT Ptied.B, Pg, Ptied.B"""
        ...

    @staticmethod
    def create_true_mask_byte(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svbool_t svptrue_pat_b8(enum svpattern pattern)  PTRUE Presult.B, pattern"""
        ...

    @staticmethod
    def create_true_mask_double(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[float]:
        """svbool_t svptrue_pat_b8(enum svpattern pattern)  PTRUE Presult.B, pattern"""
        ...

    @staticmethod
    def create_true_mask_int_16(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svbool_t svptrue_pat_b8(enum svpattern pattern)  PTRUE Presult.B, pattern"""
        ...

    @staticmethod
    def create_true_mask_int_32(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svbool_t svptrue_pat_b8(enum svpattern pattern)  PTRUE Presult.B, pattern"""
        ...

    @staticmethod
    def create_true_mask_int_64(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svbool_t svptrue_pat_b8(enum svpattern pattern)  PTRUE Presult.B, pattern"""
        ...

    @staticmethod
    def create_true_mask_s_byte(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svbool_t svptrue_pat_b8(enum svpattern pattern)  PTRUE Presult.B, pattern"""
        ...

    @staticmethod
    def create_true_mask_single(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[float]:
        """svbool_t svptrue_pat_b8(enum svpattern pattern)  PTRUE Presult.B, pattern"""
        ...

    @staticmethod
    def create_true_mask_u_int_16(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svbool_t svptrue_pat_b16(enum svpattern pattern)  PTRUE Presult.H, pattern"""
        ...

    @staticmethod
    def create_true_mask_u_int_32(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svbool_t svptrue_pat_b32(enum svpattern pattern)  PTRUE Presult.S, pattern"""
        ...

    @staticmethod
    def create_true_mask_u_int_64(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svbool_t svptrue_pat_b64(enum svpattern pattern)  PTRUE Presult.D, pattern"""
        ...

    @staticmethod
    def create_while_less_than_mask_16_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        """svbool_t svwhilelt_b16[_s32](int32_t op1, int32_t op2)  WHILELT Presult.H, Wop1, Wop2"""
        ...

    @staticmethod
    def create_while_less_than_mask_32_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        """svbool_t svwhilelt_b32[_s32](int32_t op1, int32_t op2)  WHILELT Presult.S, Wop1, Wop2"""
        ...

    @staticmethod
    def create_while_less_than_mask_64_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        """svbool_t svwhilelt_b64[_s32](int32_t op1, int32_t op2)  WHILELT Presult.D, Wop1, Wop2"""
        ...

    @staticmethod
    def create_while_less_than_mask_8_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        """svbool_t svwhilelt_b8[_s32](int32_t op1, int32_t op2)  WHILELT Presult.B, Wop1, Wop2"""
        ...

    @staticmethod
    def create_while_less_than_or_equal_mask_16_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        """svbool_t svwhilele_b16[_s32](int32_t op1, int32_t op2)  WHILELE Presult.H, Wop1, Wop2"""
        ...

    @staticmethod
    def create_while_less_than_or_equal_mask_32_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        """svbool_t svwhilele_b32[_s32](int32_t op1, int32_t op2)  WHILELE Presult.S, Wop1, Wop2"""
        ...

    @staticmethod
    def create_while_less_than_or_equal_mask_64_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        """svbool_t svwhilele_b64[_s32](int32_t op1, int32_t op2)  WHILELE Presult.D, Wop1, Wop2"""
        ...

    @staticmethod
    def create_while_less_than_or_equal_mask_8_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        """svbool_t svwhilele_b8[_s32](int32_t op1, int32_t op2)  WHILELE Presult.B, Wop1, Wop2"""
        ...

    @staticmethod
    def divide(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svdiv[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svdiv[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svdiv[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FDIV Ztied1.D, Pg/M, Ztied1.D, Zop2.D"""
        ...

    @staticmethod
    def dot_product(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svdot[_s32](svint32_t op1, svint8_t op2, svint8_t op3)  SDOT Ztied1.S, Zop2.B, Zop3.B"""
        ...

    @staticmethod
    def dot_product_by_selected_scalar(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        """svint32_t svdot_lane[_s32](svint32_t op1, svint8_t op2, svint8_t op3, uint64_t imm_index)  SDOT Ztied1.S, Zop2.B, Zop3.B[imm_index]"""
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector(data: System.Numerics.Vector[int], index: int) -> System.Numerics.Vector[int]:
        """svuint8_t svdup_lane[_u8](svuint8_t data, uint8_t index)  DUP Zresult.B, Zdata.B[index]"""
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector(data: System.Numerics.Vector[float], index: int) -> System.Numerics.Vector[float]:
        """svfloat64_t svdup_lane[_f64](svfloat64_t data, uint64_t index)  DUP Zresult.D, Zdata.D[index]"""
        ...

    @staticmethod
    @overload
    def extract_vector(upper: System.Numerics.Vector[int], lower: System.Numerics.Vector[int], index: int) -> System.Numerics.Vector[int]:
        """svuint8_t svext[_u8](svuint8_t op1, svuint8_t op2, uint64_t imm3)  EXT Ztied1.B, Ztied1.B, Zop2.B, #imm3"""
        ...

    @staticmethod
    @overload
    def extract_vector(upper: System.Numerics.Vector[float], lower: System.Numerics.Vector[float], index: int) -> System.Numerics.Vector[float]:
        """svfloat64_t svext[_f64](svfloat64_t op1, svfloat64_t op2, uint64_t imm3)  EXT Ztied1.B, Ztied1.B, Zop2.B, #imm3 * 8"""
        ...

    @staticmethod
    def floating_point_exponential_accelerator(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svexpa[_f64](svuint64_t op)  FEXPA Zresult.D, Zop.D"""
        ...

    @staticmethod
    def fused_multiply_add(addend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svmla[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)svfloat64_t svmla[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)svfloat64_t svmla[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)  FMLA Ztied1.D, Pg/M, Zop2.D, Zop3.D"""
        ...

    @staticmethod
    def fused_multiply_add_by_selected_scalar(addend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], right_index: int) -> System.Numerics.Vector[float]:
        """svfloat64_t svmla_lane[_f64](svfloat64_t op1, svfloat64_t op2, svfloat64_t op3, uint64_t imm_index)  FMLA Ztied1.D, Zop2.D, Zop3.D[imm_index]"""
        ...

    @staticmethod
    def fused_multiply_add_negated(addend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svnmla[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)svfloat64_t svnmla[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)svfloat64_t svnmla[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)  FNMLA Ztied1.D, Pg/M, Zop2.D, Zop3.D"""
        ...

    @staticmethod
    def fused_multiply_subtract(minuend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svmls[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)svfloat64_t svmls[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)svfloat64_t svmls[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)  FMLS Ztied1.D, Pg/M, Zop2.D, Zop3.D"""
        ...

    @staticmethod
    def fused_multiply_subtract_by_selected_scalar(minuend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], right_index: int) -> System.Numerics.Vector[float]:
        """svfloat64_t svmls_lane[_f64](svfloat64_t op1, svfloat64_t op2, svfloat64_t op3, uint64_t imm_index)  FMLS Ztied1.D, Zop2.D, Zop3.D[imm_index]"""
        ...

    @staticmethod
    def fused_multiply_subtract_negated(minuend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svnmls[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)svfloat64_t svnmls[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)svfloat64_t svnmls[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3)  FNMLS Ztied1.D, Pg/M, Zop2.D, Zop3.D"""
        ...

    @staticmethod
    @overload
    def gather_prefetch_16_bit(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfh_gather_[s32]index(svbool_t pg, const void *base, svint32_t indices, enum svprfop op)  PRFH op, Pg, [Xbase, Zindices.S, SXTW #1]"""
        ...

    @staticmethod
    @overload
    def gather_prefetch_16_bit(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfh_gather[_u64base](svbool_t pg, svuint64_t bases, enum svprfop op)  PRFH op, Pg, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_prefetch_32_bit(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfw_gather_[s32]index(svbool_t pg, const void *base, svint32_t indices, enum svprfop op)  PRFW op, Pg, [Xbase, Zindices.S, SXTW #2]"""
        ...

    @staticmethod
    @overload
    def gather_prefetch_32_bit(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfw_gather[_u64base](svbool_t pg, svuint64_t bases, enum svprfop op)  PRFW op, Pg, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_prefetch_64_bit(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfd_gather_[s32]index(svbool_t pg, const void *base, svint32_t indices, enum svprfop op)  PRFD op, Pg, [Xbase, Zindices.S, SXTW #3]"""
        ...

    @staticmethod
    @overload
    def gather_prefetch_64_bit(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfd_gather[_u64base](svbool_t pg, svuint64_t bases, enum svprfop op)  PRFD op, Pg, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_prefetch_8_bit(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfb_gather_[s32]offset(svbool_t pg, const void *base, svint32_t offsets, enum svprfop op)  PRFB op, Pg, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    @overload
    def gather_prefetch_8_bit(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfb_gather[_u64base](svbool_t pg, svuint64_t bases, enum svprfop op)  PRFB op, Pg, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector(mask: System.Numerics.Vector[float], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svld1_gather_[s64]index[_f64](svbool_t pg, const float64_t *base, svint64_t indices)  LD1D Zresult.D, Pg/Z, [Xbase, Zindices.D, LSL #3]"""
        ...

    @staticmethod
    @overload
    def gather_vector(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svld1_gather_[s32]index[_s32](svbool_t pg, const int32_t *base, svint32_t indices)  LD1W Zresult.S, Pg/Z, [Xbase, Zindices.S, SXTW #2]"""
        ...

    @staticmethod
    @overload
    def gather_vector(mask: System.Numerics.Vector[float], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svld1_gather[_u64base]_f64(svbool_t pg, svuint64_t bases)  LD1D Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LD1D Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_byte_zero_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svld1ub_gather_[s32]offset_s32(svbool_t pg, const uint8_t *base, svint32_t offsets)  LD1B Zresult.S, Pg/Z, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    @overload
    def gather_vector_byte_zero_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1ub_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LD1B Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_byte_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svldff1ub_gather_[s32]offset_s32(svbool_t pg, const uint8_t *base, svint32_t offsets)  LDFF1B Zresult.S, Pg/Z, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    @overload
    def gather_vector_byte_zero_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1ub_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LDFF1B Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_first_faulting(mask: System.Numerics.Vector[float], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svldff1_gather_[s64]index[_f64](svbool_t pg, const float64_t *base, svint64_t indices)  LDFF1D Zresult.D, Pg/Z, [Xbase, Zindices.D, LSL #3]"""
        ...

    @staticmethod
    @overload
    def gather_vector_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svldff1_gather_[s32]index[_s32](svbool_t pg, const int32_t *base, svint32_t indices)  LDFF1W Zresult.S, Pg/Z, [Xbase, Zindices.S, SXTW #2]"""
        ...

    @staticmethod
    @overload
    def gather_vector_first_faulting(mask: System.Numerics.Vector[float], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svldff1_gather[_u64base]_f64(svbool_t pg, svuint64_t bases)  LDFF1D Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LDFF1D Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_int_16_sign_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svld1sh_gather_[s32]index_s32(svbool_t pg, const int16_t *base, svint32_t indices)  LD1SH Zresult.S, Pg/Z, [Xbase, Zindices.S, SXTW #1]"""
        ...

    @staticmethod
    @overload
    def gather_vector_int_16_sign_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1sh_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LD1SH Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_int_16_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svldff1sh_gather_[s32]index_s32(svbool_t pg, const int16_t *base, svint32_t indices)  LDFF1SH Zresult.S, Pg/Z, [Xbase, Zindices.S, SXTW #1]"""
        ...

    @staticmethod
    @overload
    def gather_vector_int_16_sign_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1sh_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LDFF1SH Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    def gather_vector_int_16_with_byte_offsets_sign_extend(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svld1sh_gather_[s32]offset_s32(svbool_t pg, const int16_t *base, svint32_t offsets)  LD1SH Zresult.S, Pg/Z, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    def gather_vector_int_16_with_byte_offsets_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svldff1sh_gather_[s32]offset_s32(svbool_t pg, const int16_t *base, svint32_t offsets)  LDFF1SH Zresult.S, Pg/Z, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    @overload
    def gather_vector_int_32_sign_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1sw_gather_[s64]index_s64(svbool_t pg, const int32_t *base, svint64_t indices)  LD1SW Zresult.D, Pg/Z, [Xbase, Zindices.D, LSL #2]"""
        ...

    @staticmethod
    @overload
    def gather_vector_int_32_sign_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1sw_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LD1SW Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_int_32_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1sw_gather_[s64]index_s64(svbool_t pg, const int32_t *base, svint64_t indices)  LDFF1SW Zresult.D, Pg/Z, [Xbase, Zindices.D, LSL #2]"""
        ...

    @staticmethod
    @overload
    def gather_vector_int_32_sign_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1sw_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LDFF1SW Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    def gather_vector_int_32_with_byte_offsets_sign_extend(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1sw_gather_[s64]offset_s64(svbool_t pg, const int32_t *base, svint64_t offsets)  LD1SW Zresult.D, Pg/Z, [Xbase, Zoffsets.D]"""
        ...

    @staticmethod
    def gather_vector_int_32_with_byte_offsets_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1sw_gather_[s64]offset_s64(svbool_t pg, const int32_t *base, svint64_t offsets)  LDFF1SW Zresult.D, Pg/Z, [Xbase, Zoffsets.D]"""
        ...

    @staticmethod
    @overload
    def gather_vector_s_byte_sign_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svld1sb_gather_[s32]offset_s32(svbool_t pg, const int8_t *base, svint32_t offsets)  LD1SB Zresult.S, Pg/Z, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    @overload
    def gather_vector_s_byte_sign_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1sb_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LD1SB Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_s_byte_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svldff1sb_gather_[s32]offset_s32(svbool_t pg, const int8_t *base, svint32_t offsets)  LDFF1SB Zresult.S, Pg/Z, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    @overload
    def gather_vector_s_byte_sign_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1sb_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LDFF1SB Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    def gather_vector_u_int_16_with_byte_offsets_zero_extend(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svld1uh_gather_[s32]offset_s32(svbool_t pg, const uint16_t *base, svint32_t offsets)  LD1H Zresult.S, Pg/Z, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    def gather_vector_u_int_16_with_byte_offsets_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svldff1uh_gather_[s32]offset_s32(svbool_t pg, const uint16_t *base, svint32_t offsets)  LDFF1H Zresult.S, Pg/Z, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_16_zero_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svld1uh_gather_[s32]index_s32(svbool_t pg, const uint16_t *base, svint32_t indices)  LD1H Zresult.S, Pg/Z, [Xbase, Zindices.S, SXTW #1]"""
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_16_zero_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1uh_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LD1H Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_16_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svldff1uh_gather_[s32]index_s32(svbool_t pg, const uint16_t *base, svint32_t indices)  LDFF1H Zresult.S, Pg/Z, [Xbase, Zindices.S, SXTW #1]"""
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_16_zero_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1uh_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LDFF1H Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    def gather_vector_u_int_32_with_byte_offsets_zero_extend(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1uw_gather_[s64]offset_s64(svbool_t pg, const uint32_t *base, svint64_t offsets)  LD1W Zresult.D, Pg/Z, [Xbase, Zoffsets.D]"""
        ...

    @staticmethod
    def gather_vector_u_int_32_with_byte_offsets_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1uw_gather_[s64]offset_s64(svbool_t pg, const uint32_t *base, svint64_t offsets)  LDFF1W Zresult.D, Pg/Z, [Xbase, Zoffsets.D]"""
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_32_zero_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1uw_gather_[s64]index_s64(svbool_t pg, const uint32_t *base, svint64_t indices)  LD1W Zresult.D, Pg/Z, [Xbase, Zindices.D, LSL #2]"""
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_32_zero_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svld1uw_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LD1W Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_32_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1uw_gather_[s64]index_s64(svbool_t pg, const uint32_t *base, svint64_t indices)  LDFF1W Zresult.D, Pg/Z, [Xbase, Zindices.D, LSL #2]"""
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_32_zero_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svldff1uw_gather[_u64base]_s64(svbool_t pg, svuint64_t bases)  LDFF1W Zresult.D, Pg/Z, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def gather_vector_with_byte_offset_first_faulting(mask: System.Numerics.Vector[float], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svldff1_gather_[s64]offset[_f64](svbool_t pg, const float64_t *base, svint64_t offsets)  LDFF1D Zresult.D, Pg/Z, [Xbase, Zoffsets.D]"""
        ...

    @staticmethod
    @overload
    def gather_vector_with_byte_offset_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svldff1_gather_[s32]offset[_s32](svbool_t pg, const int32_t *base, svint32_t offsets)  LDFF1W Zresult.S, Pg/Z, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    @overload
    def gather_vector_with_byte_offsets(mask: System.Numerics.Vector[float], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svld1_gather_[s64]offset[_f64](svbool_t pg, const float64_t *base, svint64_t offsets)  LD1D Zresult.D, Pg/Z, [Xbase, Zoffsets.D]"""
        ...

    @staticmethod
    @overload
    def gather_vector_with_byte_offsets(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svld1_gather_[s32]offset[_s32](svbool_t pg, const int32_t *base, svint32_t offsets)  LD1W Zresult.S, Pg/Z, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    @overload
    def get_active_element_count(mask: System.Numerics.Vector[int], _from: System.Numerics.Vector[int]) -> int:
        """uint64_t svcntp_b8(svbool_t pg, svbool_t op)  CNTP Xresult, Pg, Pop.B"""
        ...

    @staticmethod
    @overload
    def get_active_element_count(mask: System.Numerics.Vector[float], _from: System.Numerics.Vector[float]) -> int:
        """uint64_t svcntp_b8(svbool_t pg, svbool_t op)  CNTP Xresult, Pg, Pop.B"""
        ...

    @staticmethod
    def get_ffr_byte() -> System.Numerics.Vector[int]:
        """svbool_t svrdffr()  RDFFR Presult.B"""
        ...

    @staticmethod
    def get_ffr_int_16() -> System.Numerics.Vector[int]:
        """svbool_t svrdffr()  RDFFR Presult.B"""
        ...

    @staticmethod
    def get_ffr_int_32() -> System.Numerics.Vector[int]:
        """svbool_t svrdffr()  RDFFR Presult.B"""
        ...

    @staticmethod
    def get_ffr_int_64() -> System.Numerics.Vector[int]:
        """svbool_t svrdffr()  RDFFR Presult.B"""
        ...

    @staticmethod
    def get_ffr_s_byte() -> System.Numerics.Vector[int]:
        """svbool_t svrdffr()  RDFFR Presult.B"""
        ...

    @staticmethod
    def get_ffr_u_int_16() -> System.Numerics.Vector[int]:
        """svbool_t svrdffr()  RDFFR Presult.B"""
        ...

    @staticmethod
    def get_ffr_u_int_32() -> System.Numerics.Vector[int]:
        """svbool_t svrdffr()  RDFFR Presult.B"""
        ...

    @staticmethod
    def get_ffr_u_int_64() -> System.Numerics.Vector[int]:
        """svbool_t svrdffr()  RDFFR Presult.B"""
        ...

    @staticmethod
    @overload
    def insert_into_shifted_vector(left: System.Numerics.Vector[int], right: int) -> System.Numerics.Vector[int]:
        """svuint8_t svinsr[_n_u8](svuint8_t op1, uint8_t op2)  INSR Ztied1.B, Wop2  INSR Ztied1.B, Bop2"""
        ...

    @staticmethod
    @overload
    def insert_into_shifted_vector(left: System.Numerics.Vector[float], right: float) -> System.Numerics.Vector[float]:
        """svfloat64_t svinsr[_n_f64](svfloat64_t op1, float64_t op2)  INSR Ztied1.D, Xop2  INSR Ztied1.D, Dop2"""
        ...

    @staticmethod
    def leading_sign_count(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svcls[_s8]_m(svuint8_t inactive, svbool_t pg, svint8_t op)svuint8_t svcls[_s8]_x(svbool_t pg, svint8_t op)svuint8_t svcls[_s8]_z(svbool_t pg, svint8_t op)  CLS Zresult.B, Pg/M, Zop.B"""
        ...

    @staticmethod
    def leading_zero_count(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svclz[_s8]_m(svuint8_t inactive, svbool_t pg, svint8_t op)svuint8_t svclz[_s8]_x(svbool_t pg, svint8_t op)svuint8_t svclz[_s8]_z(svbool_t pg, svint8_t op)  CLZ Zresult.B, Pg/M, Zop.B"""
        ...

    @staticmethod
    @overload
    def load_2_x_vector_and_unzip(mask: System.Numerics.Vector[int], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int]]:
        """svuint8x2_t svld2[_u8](svbool_t pg, const uint8_t *base)  LD2B {Zresult0.B, Zresult1.B}, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_2_x_vector_and_unzip(mask: System.Numerics.Vector[float], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float]]:
        """svfloat64x2_t svld2[_f64](svbool_t pg, const float64_t *base)  LD2D {Zresult0.D, Zresult1.D}, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_3_x_vector_and_unzip(mask: System.Numerics.Vector[int], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int]]:
        """svuint8x3_t svld3[_u8](svbool_t pg, const uint8_t *base)  LD3B {Zresult0.B - Zresult2.B}, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_3_x_vector_and_unzip(mask: System.Numerics.Vector[float], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float]]:
        """svfloat64x3_t svld3[_f64](svbool_t pg, const float64_t *base)  LD3D {Zresult0.D - Zresult2.D}, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_4_x_vector_and_unzip(mask: System.Numerics.Vector[int], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int]]:
        """svuint8x4_t svld4[_u8](svbool_t pg, const uint8_t *base)  LD4B {Zresult0.B - Zresult3.B}, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_4_x_vector_and_unzip(mask: System.Numerics.Vector[float], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float]]:
        """svfloat64x4_t svld4[_f64](svbool_t pg, const float64_t *base)  LD4D {Zresult0.D - Zresult3.D}, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_vector(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint8_t svld1[_u8](svbool_t pg, const uint8_t *base)  LD1B Zresult.B, Pg/Z, [Xarray, Xindex]  LD1B Zresult.B, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_vector(mask: System.Numerics.Vector[float], address: typing.Any) -> System.Numerics.Vector[float]:
        """svfloat64_t svld1[_f64](svbool_t pg, const float64_t *base)  LD1D Zresult.D, Pg/Z, [Xarray, Xindex, LSL #3]  LD1D Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_vector_128_and_replicate_to_vector(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint8_t svld1rq[_u8](svbool_t pg, const uint8_t *base)  LD1RQB Zresult.B, Pg/Z, [Xbase, #0]"""
        ...

    @staticmethod
    @overload
    def load_vector_128_and_replicate_to_vector(mask: System.Numerics.Vector[float], address: typing.Any) -> System.Numerics.Vector[float]:
        """svfloat64_t svld1rq[_f64](svbool_t pg, const float64_t *base)  LD1RQD Zresult.D, Pg/Z, [Xbase, #0]"""
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_int_16(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint16_t svldnf1ub_s16(svbool_t pg, const uint8_t *base)  LDNF1B Zresult.H, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_int_32(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint32_t svldnf1ub_s32(svbool_t pg, const uint8_t *base)  LDNF1B Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svldnf1ub_s64(svbool_t pg, const uint8_t *base)  LDNF1B Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_u_int_16(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint16_t svldnf1ub_u16(svbool_t pg, const uint8_t *base)  LDNF1B Zresult.H, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_u_int_32(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint32_t svldnf1ub_u32(svbool_t pg, const uint8_t *base)  LDNF1B Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_u_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svldnf1ub_u64(svbool_t pg, const uint8_t *base)  LDNF1B Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint16_t svldff1ub_s16(svbool_t pg, const uint8_t *base)  LDFF1B Zresult.H, Pg/Z, [Xbase, XZR]"""
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint16_t svld1ub_s16(svbool_t pg, const uint8_t *base)  LD1B Zresult.H, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint32_t svld1ub_s32(svbool_t pg, const uint8_t *base)  LD1B Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svld1ub_s64(svbool_t pg, const uint8_t *base)  LD1B Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_u_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint16_t svld1ub_u16(svbool_t pg, const uint8_t *base)  LD1B Zresult.H, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint32_t svld1ub_u32(svbool_t pg, const uint8_t *base)  LD1B Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svld1ub_u64(svbool_t pg, const uint8_t *base)  LD1B Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_vector_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint8_t svldff1[_u8](svbool_t pg, const uint8_t *base)  LDFF1B Zresult.B, Pg/Z, [Xbase, XZR]"""
        ...

    @staticmethod
    @overload
    def load_vector_first_faulting(mask: System.Numerics.Vector[float], address: typing.Any) -> System.Numerics.Vector[float]:
        """svfloat64_t svldff1[_f64](svbool_t pg, const float64_t *base)  LDFF1D Zresult.D, Pg/Z, [Xbase, XZR, LSL #3]"""
        ...

    @staticmethod
    def load_vector_int_16_non_faulting_sign_extend_to_int_32(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint32_t svldnf1sh_s32(svbool_t pg, const int16_t *base)  LDNF1SH Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_16_non_faulting_sign_extend_to_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svldnf1sh_s64(svbool_t pg, const int16_t *base)  LDNF1SH Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_16_non_faulting_sign_extend_to_u_int_32(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint32_t svldnf1sh_u32(svbool_t pg, const int16_t *base)  LDNF1SH Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_16_non_faulting_sign_extend_to_u_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svldnf1sh_u64(svbool_t pg, const int16_t *base)  LDNF1SH Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_16_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint32_t svldff1sh_s32(svbool_t pg, const int16_t *base)  LDFF1SH Zresult.S, Pg/Z, [Xbase, XZR, LSL #1]"""
        ...

    @staticmethod
    def load_vector_int_16_sign_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint32_t svld1sh_s32(svbool_t pg, const int16_t *base)  LD1SH Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_16_sign_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svld1sh_s64(svbool_t pg, const int16_t *base)  LD1SH Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_16_sign_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint32_t svld1sh_u32(svbool_t pg, const int16_t *base)  LD1SH Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_16_sign_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svld1sh_u64(svbool_t pg, const int16_t *base)  LD1SH Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_32_non_faulting_sign_extend_to_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svldnf1sw_s64(svbool_t pg, const int32_t *base)  LDNF1SW Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_32_non_faulting_sign_extend_to_u_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svldnf1sw_u64(svbool_t pg, const int32_t *base)  LDNF1SW Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_32_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svldff1sw_s64(svbool_t pg, const int32_t *base)  LDFF1SW Zresult.D, Pg/Z, [Xbase, XZR, LSL #2]"""
        ...

    @staticmethod
    def load_vector_int_32_sign_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svld1sw_s64(svbool_t pg, const int32_t *base)  LD1SW Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_int_32_sign_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svld1sw_u64(svbool_t pg, const int32_t *base)  LD1SW Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_non_faulting(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint8_t svldnf1[_u8](svbool_t pg, const uint8_t *base)  LDNF1B Zresult.B, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_vector_non_temporal(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint8_t svldnt1[_u8](svbool_t pg, const uint8_t *base)  LDNT1B Zresult.B, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def load_vector_non_temporal(mask: System.Numerics.Vector[float], address: typing.Any) -> System.Numerics.Vector[float]:
        """svfloat64_t svldnt1[_f64](svbool_t pg, const float64_t *base)  LDNT1D Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_int_16(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint16_t svldnf1sb_s16(svbool_t pg, const int8_t *base)  LDNF1SB Zresult.H, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_int_32(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint32_t svldnf1sb_s32(svbool_t pg, const int8_t *base)  LDNF1SB Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svldnf1sb_s64(svbool_t pg, const int8_t *base)  LDNF1SB Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_u_int_16(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint16_t svldnf1sb_u16(svbool_t pg, const int8_t *base)  LDNF1SB Zresult.H, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_u_int_32(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint32_t svldnf1sb_u32(svbool_t pg, const int8_t *base)  LDNF1SB Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_u_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svldnf1sb_u64(svbool_t pg, const int8_t *base)  LDNF1SB Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint16_t svldff1sb_s16(svbool_t pg, const int8_t *base)  LDFF1SB Zresult.H, Pg/Z, [Xbase, XZR]"""
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint16_t svld1sb_s16(svbool_t pg, const int8_t *base)  LD1SB Zresult.H, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint32_t svld1sb_s32(svbool_t pg, const int8_t *base)  LD1SB Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svld1sb_s64(svbool_t pg, const int8_t *base)  LD1SB Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_u_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint16_t svld1sb_u16(svbool_t pg, const int8_t *base)  LD1SB Zresult.H, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint32_t svld1sb_u32(svbool_t pg, const int8_t *base)  LD1SB Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svld1sb_u64(svbool_t pg, const int8_t *base)  LD1SB Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_16_non_faulting_zero_extend_to_int_32(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint32_t svldnf1uh_s32(svbool_t pg, const uint16_t *base)  LDNF1H Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_16_non_faulting_zero_extend_to_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svldnf1uh_s64(svbool_t pg, const uint16_t *base)  LDNF1H Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_16_non_faulting_zero_extend_to_u_int_32(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint32_t svldnf1uh_u32(svbool_t pg, const uint16_t *base)  LDNF1H Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_16_non_faulting_zero_extend_to_u_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svldnf1uh_u64(svbool_t pg, const uint16_t *base)  LDNF1H Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_16_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint32_t svldff1uh_s32(svbool_t pg, const uint16_t *base)  LDFF1H Zresult.S, Pg/Z, [Xbase, XZR, LSL #1]"""
        ...

    @staticmethod
    def load_vector_u_int_16_zero_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint32_t svld1uh_s32(svbool_t pg, const uint16_t *base)  LD1H Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_16_zero_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svld1uh_s64(svbool_t pg, const uint16_t *base)  LD1H Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_16_zero_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint32_t svld1uh_u32(svbool_t pg, const uint16_t *base)  LD1H Zresult.S, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_16_zero_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svld1uh_u64(svbool_t pg, const uint16_t *base)  LD1H Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_32_non_faulting_zero_extend_to_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svldnf1uw_s64(svbool_t pg, const uint32_t *base)  LDNF1W Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_32_non_faulting_zero_extend_to_u_int_64(address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svldnf1uw_u64(svbool_t pg, const uint32_t *base)  LDNF1W Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_32_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svldff1uw_s64(svbool_t pg, const uint32_t *base)  LDFF1W Zresult.D, Pg/Z, [Xbase, XZR, LSL #2]"""
        ...

    @staticmethod
    def load_vector_u_int_32_zero_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svint64_t svld1uw_s64(svbool_t pg, const uint32_t *base)  LD1W Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def load_vector_u_int_32_zero_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        """svuint64_t svld1uw_u64(svbool_t pg, const uint32_t *base)  LD1W Zresult.D, Pg/Z, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def max(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svmax[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svmax[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svmax[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  UMAX Ztied1.B, Pg/M, Ztied1.B, Zop2.B  UMAX Ztied2.B, Pg/M, Ztied2.B, Zop1.B"""
        ...

    @staticmethod
    @overload
    def max(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svmax[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svmax[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svmax[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FMAX Ztied1.D, Pg/M, Ztied1.D, Zop2.D  FMAX Ztied2.D, Pg/M, Ztied2.D, Zop1.D"""
        ...

    @staticmethod
    @overload
    def max_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """uint8_t svmaxv[_u8](svbool_t pg, svuint8_t op)  UMAXV Bresult, Pg, Zop.B"""
        ...

    @staticmethod
    @overload
    def max_across(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """float64_t svmaxv[_f64](svbool_t pg, svfloat64_t op)  FMAXV Dresult, Pg, Zop.D"""
        ...

    @staticmethod
    def max_number(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svmaxnm[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svmaxnm[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svmaxnm[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FMAXNM Ztied1.D, Pg/M, Ztied1.D, Zop2.D  FMAXNM Ztied2.D, Pg/M, Ztied2.D, Zop1.D"""
        ...

    @staticmethod
    def max_number_across(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """float64_t svmaxnmv[_f64](svbool_t pg, svfloat64_t op)  FMAXNMV Dresult, Pg, Zop.D"""
        ...

    @staticmethod
    @overload
    def min(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svmin[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svmin[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svmin[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  UMIN Ztied1.B, Pg/M, Ztied1.B, Zop2.B  UMIN Ztied2.B, Pg/M, Ztied2.B, Zop1.B"""
        ...

    @staticmethod
    @overload
    def min(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svmin[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svmin[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svmin[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FMIN Ztied1.D, Pg/M, Ztied1.D, Zop2.D  FMIN Ztied2.D, Pg/M, Ztied2.D, Zop1.D"""
        ...

    @staticmethod
    @overload
    def min_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """uint8_t svminv[_u8](svbool_t pg, svuint8_t op)  UMINV Bresult, Pg, Zop.B"""
        ...

    @staticmethod
    @overload
    def min_across(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """float64_t svminv[_f64](svbool_t pg, svfloat64_t op)  FMINV Dresult, Pg, Zop.D"""
        ...

    @staticmethod
    def min_number(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svminnm[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svminnm[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svminnm[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FMINNM Ztied1.D, Pg/M, Ztied1.D, Zop2.D  FMINNM Ztied2.D, Pg/M, Ztied2.D, Zop1.D"""
        ...

    @staticmethod
    def min_number_across(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """float64_t svminnmv[_f64](svbool_t pg, svfloat64_t op)  FMINNMV Dresult, Pg, Zop.D"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svmul[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svmul[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svmul[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  MUL Ztied1.B, Pg/M, Ztied1.B, Zop2.B  MUL Ztied2.B, Pg/M, Ztied2.B, Zop1.Bsvuint8_t svmul[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svmul[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svmul[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svmul[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FMUL Ztied1.D, Pg/M, Ztied1.D, Zop2.D  FMUL Ztied2.D, Pg/M, Ztied2.D, Zop1.Dsvfloat64_t svmul[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)"""
        ...

    @staticmethod
    def multiply_add(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svmla[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2, svuint8_t op3)svuint8_t svmla[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2, svuint8_t op3)svuint8_t svmla[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2, svuint8_t op3)  MLA Ztied1.B, Pg/M, Zop2.B, Zop3.B"""
        ...

    @staticmethod
    def multiply_add_rotate_complex(addend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], rotation: int) -> System.Numerics.Vector[float]:
        """svfloat64_t svcmla[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3, uint64_t imm_rotation)svfloat64_t svcmla[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3, uint64_t imm_rotation)svfloat64_t svcmla[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2, svfloat64_t op3, uint64_t imm_rotation)  FCMLA Ztied1.D, Pg/M, Zop2.D, Zop3.D, #imm_rotation"""
        ...

    @staticmethod
    def multiply_add_rotate_complex_by_selected_scalar(addend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], right_index: int, rotation: int) -> System.Numerics.Vector[float]:
        """svfloat32_t svcmla_lane[_f32](svfloat32_t op1, svfloat32_t op2, svfloat32_t op3, uint64_t imm_index, uint64_t imm_rotation)  FCMLA Ztied1.S, Zop2.S, Zop3.S[imm_index], #imm_rotation"""
        ...

    @staticmethod
    def multiply_by_selected_scalar(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], right_index: int) -> System.Numerics.Vector[float]:
        """svfloat64_t svmul_lane[_f64](svfloat64_t op1, svfloat64_t op2, uint64_t imm_index)  FMUL Zresult.D, Zop1.D, Zop2.D[imm_index]"""
        ...

    @staticmethod
    def multiply_extended(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svmulx[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svmulx[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svmulx[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FMULX Ztied1.D, Pg/M, Ztied1.D, Zop2.D"""
        ...

    @staticmethod
    def multiply_subtract(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svmls[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2, svuint8_t op3)svuint8_t svmls[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2, svuint8_t op3)svuint8_t svmls[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2, svuint8_t op3)  MLS Ztied1.B, Pg/M, Zop2.B, Zop3.B"""
        ...

    @staticmethod
    @overload
    def negate(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svneg[_f64]_m(svfloat64_t inactive, svbool_t pg, svfloat64_t op)svfloat64_t svneg[_f64]_x(svbool_t pg, svfloat64_t op)svfloat64_t svneg[_f64]_z(svbool_t pg, svfloat64_t op)  FNEG Ztied.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    @overload
    def negate(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint16_t svneg[_s16]_m(svint16_t inactive, svbool_t pg, svint16_t op)svint16_t svneg[_s16]_x(svbool_t pg, svint16_t op)svint16_t svneg[_s16]_z(svbool_t pg, svint16_t op)  NEG Ztied.H, Pg/M, Zop.H"""
        ...

    @staticmethod
    def Not(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svnot[_u8]_m(svuint8_t inactive, svbool_t pg, svuint8_t op)svuint8_t svnot[_u8]_x(svbool_t pg, svuint8_t op)svuint8_t svnot[_u8]_z(svbool_t pg, svuint8_t op)svbool_t svnot[_b]_z(svbool_t pg, svbool_t op)  NOT Zresult.B, Pg/M, Zop.B"""
        ...

    @staticmethod
    def Or(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svorr[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svorr[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svorr[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  ORR Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def or_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """uint8_t svorv[_u8](svbool_t pg, svuint8_t op)  ORV Bresult, Pg, Zop.B"""
        ...

    @staticmethod
    @overload
    def pop_count(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svcnt[_s8]_m(svuint8_t inactive, svbool_t pg, svint8_t op)svuint8_t svcnt[_s8]_x(svbool_t pg, svint8_t op)svuint8_t svcnt[_s8]_z(svbool_t pg, svint8_t op)  CNT Zresult.B, Pg/M, Zop.B"""
        ...

    @staticmethod
    @overload
    def pop_count(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """svuint32_t svcnt[_f32]_m(svuint32_t inactive, svbool_t pg, svfloat32_t op)svuint32_t svcnt[_f32]_x(svbool_t pg, svfloat32_t op)svuint32_t svcnt[_f32]_z(svbool_t pg, svfloat32_t op)  CNT Zresult.S, Pg/M, Zop.S"""
        ...

    @staticmethod
    def prefetch_bytes(mask: System.Numerics.Vector[int], address: typing.Any, prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfb(svbool_t pg, const void *base, enum svprfop op)  PRFB op, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def prefetch_int_16(mask: System.Numerics.Vector[int], address: typing.Any, prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfh(svbool_t pg, const void *base, enum svprfop op)  PRFH op, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def prefetch_int_32(mask: System.Numerics.Vector[int], address: typing.Any, prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfw(svbool_t pg, const void *base, enum svprfop op)  PRFW op, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def prefetch_int_64(mask: System.Numerics.Vector[int], address: typing.Any, prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        """void svprfd(svbool_t pg, const void *base, enum svprfop op)  PRFD op, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def reciprocal_estimate(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrecpe[_f64](svfloat64_t op)  FRECPE Zresult.D, Zop.D"""
        ...

    @staticmethod
    def reciprocal_exponent(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrecpx[_f64]_m(svfloat64_t inactive, svbool_t pg, svfloat64_t op)svfloat64_t svrecpx[_f64]_x(svbool_t pg, svfloat64_t op)svfloat64_t svrecpx[_f64]_z(svbool_t pg, svfloat64_t op)  FRECPX Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrsqrte[_f64](svfloat64_t op)  FRSQRTE Zresult.D, Zop.D"""
        ...

    @staticmethod
    def reciprocal_sqrt_step(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrsqrts[_f64](svfloat64_t op1, svfloat64_t op2)  FRSQRTS Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def reciprocal_step(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrecps[_f64](svfloat64_t op1, svfloat64_t op2)  FRECPS Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def reverse_bits(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svrbit[_u8]_m(svuint8_t inactive, svbool_t pg, svuint8_t op)svuint8_t svrbit[_u8]_x(svbool_t pg, svuint8_t op)svuint8_t svrbit[_u8]_z(svbool_t pg, svuint8_t op)  RBIT Zresult.B, Pg/M, Zop.B"""
        ...

    @staticmethod
    @overload
    def reverse_element(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svrev[_u8](svuint8_t op)  REV Zresult.B, Zop.B"""
        ...

    @staticmethod
    @overload
    def reverse_element(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrev[_f64](svfloat64_t op)  REV Zresult.D, Zop.D"""
        ...

    @staticmethod
    def reverse_element_16(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svrevh[_s32]_m(svint32_t inactive, svbool_t pg, svint32_t op)svint32_t svrevh[_s32]_x(svbool_t pg, svint32_t op)svint32_t svrevh[_s32]_z(svbool_t pg, svint32_t op)  REVH Zresult.S, Pg/M, Zop.S"""
        ...

    @staticmethod
    def reverse_element_32(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svrevw[_s64]_m(svint64_t inactive, svbool_t pg, svint64_t op)svint64_t svrevw[_s64]_x(svbool_t pg, svint64_t op)svint64_t svrevw[_s64]_z(svbool_t pg, svint64_t op)  REVW Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    def reverse_element_8(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint16_t svrevb[_s16]_m(svint16_t inactive, svbool_t pg, svint16_t op)svint16_t svrevb[_s16]_x(svbool_t pg, svint16_t op)svint16_t svrevb[_s16]_z(svbool_t pg, svint16_t op)  REVB Zresult.H, Pg/M, Zop.H"""
        ...

    @staticmethod
    def round_away_from_zero(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrinta[_f64]_m(svfloat64_t inactive, svbool_t pg, svfloat64_t op)svfloat64_t svrinta[_f64]_x(svbool_t pg, svfloat64_t op)svfloat64_t svrinta[_f64]_z(svbool_t pg, svfloat64_t op)  FRINTA Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    def round_to_nearest(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrintn[_f64]_m(svfloat64_t inactive, svbool_t pg, svfloat64_t op)svfloat64_t svrintn[_f64]_x(svbool_t pg, svfloat64_t op)svfloat64_t svrintn[_f64]_z(svbool_t pg, svfloat64_t op)  FRINTN Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    def round_to_negative_infinity(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrintm[_f64]_m(svfloat64_t inactive, svbool_t pg, svfloat64_t op)svfloat64_t svrintm[_f64]_x(svbool_t pg, svfloat64_t op)svfloat64_t svrintm[_f64]_z(svbool_t pg, svfloat64_t op)  FRINTM Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    def round_to_positive_infinity(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrintp[_f64]_m(svfloat64_t inactive, svbool_t pg, svfloat64_t op)svfloat64_t svrintp[_f64]_x(svbool_t pg, svfloat64_t op)svfloat64_t svrintp[_f64]_z(svbool_t pg, svfloat64_t op)  FRINTP Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    def round_to_zero(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svrintz[_f64]_m(svfloat64_t inactive, svbool_t pg, svfloat64_t op)svfloat64_t svrintz[_f64]_x(svbool_t pg, svfloat64_t op)svfloat64_t svrintz[_f64]_z(svbool_t pg, svfloat64_t op)  FRINTZ Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_16_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """int32_t svqdech_pat[_n_s32](int32_t op, enum svpattern pattern, uint64_t imm_factor)  SQDECH Xtied, Wtied, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_16_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svint16_t svqdech_pat[_s16](svint16_t op, enum svpattern pattern, uint64_t imm_factor)  SQDECH Ztied.H, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_32_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """int32_t svqdecw_pat[_n_s32](int32_t op, enum svpattern pattern, uint64_t imm_factor)  SQDECW Xtied, Wtied, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_32_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svint32_t svqdecw_pat[_s32](svint32_t op, enum svpattern pattern, uint64_t imm_factor)  SQDECW Ztied.S, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_64_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """int32_t svqdecd_pat[_n_s32](int32_t op, enum svpattern pattern, uint64_t imm_factor)  SQDECD Xtied, Wtied, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_64_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svint64_t svqdecd_pat[_s64](svint64_t op, enum svpattern pattern, uint64_t imm_factor)  SQDECD Ztied.D, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    def saturating_decrement_by_8_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """int32_t svqdecb_pat[_n_s32](int32_t op, enum svpattern pattern, uint64_t imm_factor)  SQDECB Xtied, Wtied, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_active_element_count(value: int, _from: System.Numerics.Vector[int]) -> int:
        """int32_t svqdecp[_n_s32]_b8(int32_t op, svbool_t pg)  SQDECP Xtied, Pg.B, Wtied"""
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_active_element_count(value: System.Numerics.Vector[int], _from: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint16_t svqdecp[_s16](svint16_t op, svbool_t pg)  SQDECP Ztied.H, Pg"""
        ...

    @staticmethod
    @overload
    def saturating_increment_by_16_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """int32_t svqinch_pat[_n_s32](int32_t op, enum svpattern pattern, uint64_t imm_factor)  SQINCH Xtied, Wtied, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_increment_by_16_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svint16_t svqinch_pat[_s16](svint16_t op, enum svpattern pattern, uint64_t imm_factor)  SQINCH Ztied.H, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_increment_by_32_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """int32_t svqincw_pat[_n_s32](int32_t op, enum svpattern pattern, uint64_t imm_factor)  SQINCW Xtied, Wtied, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_increment_by_32_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svint32_t svqincw_pat[_s32](svint32_t op, enum svpattern pattern, uint64_t imm_factor)  SQINCW Ztied.S, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_increment_by_64_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """int32_t svqincd_pat[_n_s32](int32_t op, enum svpattern pattern, uint64_t imm_factor)  SQINCD Xtied, Wtied, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_increment_by_64_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        """svint64_t svqincd_pat[_s64](svint64_t op, enum svpattern pattern, uint64_t imm_factor)  SQINCD Ztied.D, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    def saturating_increment_by_8_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        """int32_t svqincb_pat[_n_s32](int32_t op, enum svpattern pattern, uint64_t imm_factor)  SQINCB Xtied, Wtied, pattern, MUL #imm_factor"""
        ...

    @staticmethod
    @overload
    def saturating_increment_by_active_element_count(value: int, _from: System.Numerics.Vector[int]) -> int:
        """int32_t svqincp[_n_s32]_b8(int32_t op, svbool_t pg)  SQINCP Xtied, Pg.B, Wtied"""
        ...

    @staticmethod
    @overload
    def saturating_increment_by_active_element_count(value: System.Numerics.Vector[int], _from: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint16_t svqincp[_s16](svint16_t op, svbool_t pg)  SQINCP Ztied.H, Pg"""
        ...

    @staticmethod
    def scale(left: System.Numerics.Vector[float], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svscale[_f64]_m(svbool_t pg, svfloat64_t op1, svint64_t op2)svfloat64_t svscale[_f64]_x(svbool_t pg, svfloat64_t op1, svint64_t op2)svfloat64_t svscale[_f64]_z(svbool_t pg, svfloat64_t op1, svint64_t op2)  FSCALE Ztied1.D, Pg/M, Ztied1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def scatter(mask: System.Numerics.Vector[float], address: typing.Any, indicies: System.Numerics.Vector[int], data: System.Numerics.Vector[float]) -> None:
        """void svst1_scatter_[s64]offset[_f64](svbool_t pg, float64_t *base, svint64_t offsets, svfloat64_t data)  ST1D Zdata.D, Pg, [Xbase, Zoffsets.D]"""
        ...

    @staticmethod
    @overload
    def scatter(mask: System.Numerics.Vector[int], address: typing.Any, indicies: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        """void svst1_scatter_[s32]offset[_s32](svbool_t pg, int32_t *base, svint32_t offsets, svint32_t data)  ST1W Zdata.S, Pg, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    @overload
    def scatter(mask: System.Numerics.Vector[float], addresses: System.Numerics.Vector[int], data: System.Numerics.Vector[float]) -> None:
        """void svst1_scatter[_u64base_f64](svbool_t pg, svuint64_t bases, svfloat64_t data)  ST1D Zdata.D, Pg, [Zbases.D, #0]"""
        ...

    @staticmethod
    @overload
    def scatter(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        """void svst1_scatter[_u64base_s64](svbool_t pg, svuint64_t bases, svint64_t data)  ST1D Zdata.D, Pg, [Zbases.D, #0]"""
        ...

    @staticmethod
    def scatter_16_bit_narrowing(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        """void svst1h_scatter[_u64base_s64](svbool_t pg, svuint64_t bases, svint64_t data)  ST1H Zdata.D, Pg, [Zbases.D, #0]"""
        ...

    @staticmethod
    def scatter_16_bit_with_byte_offsets_narrowing(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        """void svst1h_scatter_[s32]offset[_s32](svbool_t pg, int16_t *base, svint32_t offsets, svint32_t data)  ST1H Zdata.S, Pg, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    def scatter_32_bit_narrowing(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        """void svst1w_scatter[_u64base_s64](svbool_t pg, svuint64_t bases, svint64_t data)  ST1W Zdata.D, Pg, [Zbases.D, #0]"""
        ...

    @staticmethod
    def scatter_32_bit_with_byte_offsets_narrowing(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        """void svst1w_scatter_[s64]offset[_s64](svbool_t pg, int32_t *base, svint64_t offsets, svint64_t data)  ST1W Zdata.D, Pg, [Xbase, Zoffsets.D]"""
        ...

    @staticmethod
    def scatter_8_bit_narrowing(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        """void svst1b_scatter[_u64base_s64](svbool_t pg, svuint64_t bases, svint64_t data)  ST1B Zdata.D, Pg, [Zbases.D, #0]"""
        ...

    @staticmethod
    def scatter_8_bit_with_byte_offsets_narrowing(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        """void svst1b_scatter_[s32]offset[_s32](svbool_t pg, int8_t *base, svint32_t offsets, svint32_t data)  ST1B Zdata.S, Pg, [Xbase, Zoffsets.S, SXTW]"""
        ...

    @staticmethod
    def set_ffr(value: System.Numerics.Vector[int]) -> None:
        """void svwrffr(svbool_t op)  WRFFR Pop.B"""
        ...

    @staticmethod
    def shift_left_logical(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svlsl[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svlsl[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svlsl[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  LSL Ztied1.B, Pg/M, Ztied1.B, Zop2.B"""
        ...

    @staticmethod
    def shift_right_arithmetic(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint16_t svasr[_s16]_m(svbool_t pg, svint16_t op1, svuint16_t op2)svint16_t svasr[_s16]_x(svbool_t pg, svint16_t op1, svuint16_t op2)svint16_t svasr[_s16]_z(svbool_t pg, svint16_t op1, svuint16_t op2)  ASR Ztied1.H, Pg/M, Ztied1.H, Zop2.H"""
        ...

    @staticmethod
    def shift_right_arithmetic_for_divide(value: System.Numerics.Vector[int], control: int) -> System.Numerics.Vector[int]:
        """svint16_t svasrd[_n_s16]_m(svbool_t pg, svint16_t op1, uint64_t imm2)svint16_t svasrd[_n_s16]_x(svbool_t pg, svint16_t op1, uint64_t imm2)svint16_t svasrd[_n_s16]_z(svbool_t pg, svint16_t op1, uint64_t imm2)  ASRD Ztied1.H, Pg/M, Ztied1.H, #imm2"""
        ...

    @staticmethod
    def shift_right_logical(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svlsr[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svlsr[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svlsr[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  LSR Ztied1.B, Pg/M, Ztied1.B, Zop2.B"""
        ...

    @staticmethod
    def sign_extend_16(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint32_t svexth[_s32]_m(svint32_t inactive, svbool_t pg, svint32_t op)svint32_t svexth[_s32]_x(svbool_t pg, svint32_t op)svint32_t svexth[_s32]_z(svbool_t pg, svint32_t op)  SXTH Zresult.S, Pg/M, Zop.S"""
        ...

    @staticmethod
    def sign_extend_32(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint64_t svextw[_s64]_m(svint64_t inactive, svbool_t pg, svint64_t op)svint64_t svextw[_s64]_x(svbool_t pg, svint64_t op)svint64_t svextw[_s64]_z(svbool_t pg, svint64_t op)  SXTW Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    def sign_extend_8(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint16_t svextb[_s16]_m(svint16_t inactive, svbool_t pg, svint16_t op)svint16_t svextb[_s16]_x(svbool_t pg, svint16_t op)svint16_t svextb[_s16]_z(svbool_t pg, svint16_t op)  SXTB Zresult.H, Pg/M, Zop.H"""
        ...

    @staticmethod
    def sign_extend_widening_lower(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint16_t svunpklo[_s16](svint8_t op)  SUNPKLO Zresult.H, Zop.B"""
        ...

    @staticmethod
    def sign_extend_widening_upper(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svint16_t svunpkhi[_s16](svint8_t op)  SUNPKHI Zresult.H, Zop.B"""
        ...

    @staticmethod
    @overload
    def splice(mask: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svsplice[_u8](svbool_t pg, svuint8_t op1, svuint8_t op2)  SPLICE Ztied1.B, Pg, Ztied1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def splice(mask: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svsplice[_f64](svbool_t pg, svfloat64_t op1, svfloat64_t op2)  SPLICE Ztied1.D, Pg, Ztied1.D, Zop2.D"""
        ...

    @staticmethod
    def sqrt(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svsqrt[_f64]_m(svfloat64_t inactive, svbool_t pg, svfloat64_t op)svfloat64_t svsqrt[_f64]_x(svbool_t pg, svfloat64_t op)svfloat64_t svsqrt[_f64]_z(svbool_t pg, svfloat64_t op)  FSQRT Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[int], address: typing.Any, data: System.Numerics.Vector[int]) -> None:
        """void svst1[_u8](svbool_t pg, uint8_t *base, svuint8_t data)  ST1B Zdata.B, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[int], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int]]) -> None:
        """void svst2[_u8](svbool_t pg, uint8_t *base, svuint8x2_t data)  ST2B {Zdata0.B, Zdata1.B}, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[int], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int]]) -> None:
        """void svst3[_u8](svbool_t pg, uint8_t *base, svuint8x3_t data)  ST3B {Zdata0.B - Zdata2.B}, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[int], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int]]) -> None:
        """void svst4[_u8](svbool_t pg, uint8_t *base, svuint8x4_t data)  ST4B {Zdata0.B - Zdata3.B}, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[float], address: typing.Any, data: System.Numerics.Vector[float]) -> None:
        """void svst1[_f64](svbool_t pg, float64_t *base, svfloat64_t data)  ST1D Zdata.D, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[float], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float]]) -> None:
        """void svst2[_f64](svbool_t pg, float64_t *base, svfloat64x2_t data)  ST2D {Zdata0.D, Zdata1.D}, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[float], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float]]) -> None:
        """void svst3[_f64](svbool_t pg, float64_t *base, svfloat64x3_t data)  ST3D {Zdata0.D - Zdata2.D}, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[float], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float]]) -> None:
        """void svst4[_f64](svbool_t pg, float64_t *base, svfloat64x4_t data)  ST4D {Zdata0.D - Zdata3.D}, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    def store_narrowing(mask: System.Numerics.Vector[int], address: typing.Any, data: System.Numerics.Vector[int]) -> None:
        """void svst1b[_s16](svbool_t pg, int8_t *base, svint16_t data)  ST1B Zdata.H, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def store_non_temporal(mask: System.Numerics.Vector[int], address: typing.Any, data: System.Numerics.Vector[int]) -> None:
        """void svstnt1[_u8](svbool_t pg, uint8_t *base, svuint8_t data)  STNT1B Zdata.B, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def store_non_temporal(mask: System.Numerics.Vector[float], address: typing.Any, data: System.Numerics.Vector[float]) -> None:
        """void svstnt1[_f64](svbool_t pg, float64_t *base, svfloat64_t data)  STNT1D Zdata.D, Pg, [Xbase, #0, MUL VL]"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svsub[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svsub[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t svsub[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  SUB Ztied1.B, Pg/M, Ztied1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svsub[_f64]_m(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svsub[_f64]_x(svbool_t pg, svfloat64_t op1, svfloat64_t op2)svfloat64_t svsub[_f64]_z(svbool_t pg, svfloat64_t op1, svfloat64_t op2)  FSUB Ztied1.D, Pg/M, Ztied1.D, Zop2.D"""
        ...

    @staticmethod
    def subtract_saturate(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svqsub[_u8](svuint8_t op1, svuint8_t op2)  UQSUB Zresult.B, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    def test_any_true(mask: System.Numerics.Vector[int], src_mask: System.Numerics.Vector[int]) -> bool:
        """bool svptest_any(svbool_t pg, svbool_t op)  PTEST"""
        ...

    @staticmethod
    def test_first_true(mask: System.Numerics.Vector[int], src_mask: System.Numerics.Vector[int]) -> bool:
        """bool svptest_first(svbool_t pg, svbool_t op)  PTEST"""
        ...

    @staticmethod
    def test_last_true(mask: System.Numerics.Vector[int], src_mask: System.Numerics.Vector[int]) -> bool:
        """bool svptest_last(svbool_t pg, svbool_t op)  PTEST"""
        ...

    @staticmethod
    @overload
    def transpose_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svtrn1[_u8](svuint8_t op1, svuint8_t op2)  TRN1 Zresult.B, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def transpose_even(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svtrn1[_f64](svfloat64_t op1, svfloat64_t op2)  TRN1 Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def transpose_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svtrn2[_u8](svuint8_t op1, svuint8_t op2)  TRN2 Zresult.B, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def transpose_odd(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svtrn2[_f64](svfloat64_t op1, svfloat64_t op2)  TRN2 Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def trigonometric_multiply_add_coefficient(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], control: int) -> System.Numerics.Vector[float]:
        """svfloat64_t svtmad[_f64](svfloat64_t op1, svfloat64_t op2, uint64_t imm3)  FTMAD Ztied1.D, Ztied1.D, Zop2.D, #imm3"""
        ...

    @staticmethod
    def trigonometric_select_coefficient(value: System.Numerics.Vector[float], selector: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svtssel[_f64](svfloat64_t op1, svuint64_t op2)  FTSSEL Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    def trigonometric_starting_value(value: System.Numerics.Vector[float], sign: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svtsmul[_f64](svfloat64_t op1, svuint64_t op2)  FTSMUL Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def unzip_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svuzp1[_u8](svuint8_t op1, svuint8_t op2)  UZP1 Zresult.B, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def unzip_even(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svuzp1[_f64](svfloat64_t op1, svfloat64_t op2)  UZP1 Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def unzip_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svuzp2[_u8](svuint8_t op1, svuint8_t op2)  UZP2 Zresult.B, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def unzip_odd(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svuzp2[_f64](svfloat64_t op1, svfloat64_t op2)  UZP2 Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def vector_table_lookup(data: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svtbl[_u8](svuint8_t data, svuint8_t indices)  TBL Zresult.B, {Zdata.B}, Zindices.B"""
        ...

    @staticmethod
    @overload
    def vector_table_lookup(data: System.Numerics.Vector[float], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """svfloat64_t svtbl[_f64](svfloat64_t data, svuint64_t indices)  TBL Zresult.D, {Zdata.D}, Zindices.D"""
        ...

    @staticmethod
    def xor(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t sveor[_u8]_m(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t sveor[_u8]_x(svbool_t pg, svuint8_t op1, svuint8_t op2)svuint8_t sveor[_u8]_z(svbool_t pg, svuint8_t op1, svuint8_t op2)  EOR Ztied1.B, Pg/M, Ztied1.B, Zop2.B"""
        ...

    @staticmethod
    def xor_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """uint8_t sveorv[_u8](svbool_t pg, svuint8_t op)  EORV Bresult, Pg, Zop.B"""
        ...

    @staticmethod
    def zero_extend_16(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint32_t svexth[_u32]_m(svuint32_t inactive, svbool_t pg, svuint32_t op)svuint32_t svexth[_u32]_x(svbool_t pg, svuint32_t op)svuint32_t svexth[_u32]_z(svbool_t pg, svuint32_t op)  UXTH Zresult.S, Pg/M, Zop.S"""
        ...

    @staticmethod
    def zero_extend_32(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint64_t svextw[_u64]_m(svuint64_t inactive, svbool_t pg, svuint64_t op)svuint64_t svextw[_u64]_x(svbool_t pg, svuint64_t op)svuint64_t svextw[_u64]_z(svbool_t pg, svuint64_t op)  UXTW Zresult.D, Pg/M, Zop.D"""
        ...

    @staticmethod
    def zero_extend_8(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint16_t svextb[_u16]_m(svuint16_t inactive, svbool_t pg, svuint16_t op)svuint16_t svextb[_u16]_x(svbool_t pg, svuint16_t op)svuint16_t svextb[_u16]_z(svbool_t pg, svuint16_t op)  UXTB Zresult.H, Pg/M, Zop.H"""
        ...

    @staticmethod
    def zero_extend_widening_lower(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint16_t svunpklo[_u16](svuint8_t op)  UUNPKLO Zresult.H, Zop.B"""
        ...

    @staticmethod
    def zero_extend_widening_upper(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint16_t svunpkhi[_u16](svuint8_t op)  UUNPKHI Zresult.H, Zop.B"""
        ...

    @staticmethod
    @overload
    def zip_high(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svzip2[_u8](svuint8_t op1, svuint8_t op2)  ZIP2 Zresult.B, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def zip_high(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svzip2[_f64](svfloat64_t op1, svfloat64_t op2)  ZIP2 Zresult.D, Zop1.D, Zop2.D"""
        ...

    @staticmethod
    @overload
    def zip_low(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """svuint8_t svzip1[_u8](svuint8_t op1, svuint8_t op2)  ZIP1 Zresult.B, Zop1.B, Zop2.B"""
        ...

    @staticmethod
    @overload
    def zip_low(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """svfloat64_t svzip1[_f64](svfloat64_t op1, svfloat64_t op2)  ZIP1 Zresult.D, Zop1.D, Zop2.D"""
        ...


class Aes(System.Runtime.Intrinsics.Arm.ArmBase, metaclass=abc.ABCMeta):
    """Provides access to the ARM AES hardware instructions via intrinsics."""

    class Arm64(System.Runtime.Intrinsics.Arm.ArmBase.Arm64, metaclass=abc.ABCMeta):
        """Provides access to the ARM AES hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def decrypt(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vaesdq_u8 (uint8x16_t data, uint8x16_t key)  A32: AESD.8 Qd, Qm  A64: AESD Vd.16B, Vn.16B"""
        ...

    @staticmethod
    def encrypt(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vaeseq_u8 (uint8x16_t data, uint8x16_t key)  A32: AESE.8 Qd, Qm  A64: AESE Vd.16B, Vn.16B"""
        ...

    @staticmethod
    def inverse_mix_columns(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vaesimcq_u8 (uint8x16_t data)  A32: AESIMC.8 Qd, Qm  A64: AESIMC Vd.16B, Vn.16B"""
        ...

    @staticmethod
    def mix_columns(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint8x16_t vaesmcq_u8 (uint8x16_t data)  A32: AESMC.8 Qd, Qm  A64: AESMC V>.16B, Vn.16B"""
        ...

    @staticmethod
    def polynomial_multiply_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """poly128_t vmull_p64 (poly64_t a, poly64_t b)  A32: VMULL.P8 Qd, Dn, Dm  A64: PMULL Vd.1Q, Vn.1D, Vm.1D"""
        ...

    @staticmethod
    def polynomial_multiply_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """poly128_t vmull_high_p64 (poly64x2_t a, poly64x2_t b)  A32: VMULL.P8 Qd, Dn+1, Dm+1  A64: PMULL2 Vd.1Q, Vn.2D, Vm.2D"""
        ...


class Sha256(System.Runtime.Intrinsics.Arm.ArmBase, metaclass=abc.ABCMeta):
    """Provides access to the ARM SHA256 hardware instructions via intrinsics."""

    class Arm64(System.Runtime.Intrinsics.Arm.ArmBase.Arm64, metaclass=abc.ABCMeta):
        """Provides access to the ARM SHA256 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def hash_update_1(hash_abcd: System.Runtime.Intrinsics.Vector128[int], hash_efgh: System.Runtime.Intrinsics.Vector128[int], wk: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vsha256hq_u32 (uint32x4_t hash_abcd, uint32x4_t hash_efgh, uint32x4_t wk)  A32: SHA256H.32 Qd, Qn, Qm  A64: SHA256H Qd, Qn, Vm.4S"""
        ...

    @staticmethod
    def hash_update_2(hash_efgh: System.Runtime.Intrinsics.Vector128[int], hash_abcd: System.Runtime.Intrinsics.Vector128[int], wk: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vsha256h2q_u32 (uint32x4_t hash_efgh, uint32x4_t hash_abcd, uint32x4_t wk)  A32: SHA256H2.32 Qd, Qn, Qm  A64: SHA256H2 Qd, Qn, Vm.4S"""
        ...

    @staticmethod
    def schedule_update_0(w_0_3: System.Runtime.Intrinsics.Vector128[int], w_4_7: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vsha256su0q_u32 (uint32x4_t w_0_3, uint32x4_t w_4_7)  A32: SHA256SU0.32 Qd, Qm  A64: SHA256SU0 Vd.4S, Vn.4S"""
        ...

    @staticmethod
    def schedule_update_1(w_0_3: System.Runtime.Intrinsics.Vector128[int], w_8_11: System.Runtime.Intrinsics.Vector128[int], w_12_15: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vsha256su1q_u32 (uint32x4_t w_0_3, uint32x4_t w_8_11, uint32x4_t w_12_15)  A32: SHA256SU1.32 Qd, Qn, Qm  A64: SHA256SU1 Vd.4S, Vn.4S, Vm.4S"""
        ...


class Sha1(System.Runtime.Intrinsics.Arm.ArmBase, metaclass=abc.ABCMeta):
    """Provides access to the ARM SHA1 hardware instructions via intrinsics."""

    class Arm64(System.Runtime.Intrinsics.Arm.ArmBase.Arm64, metaclass=abc.ABCMeta):
        """Provides access to the ARM SHA1 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def fixed_rotate(hash_e: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """uint32_t vsha1h_u32 (uint32_t hash_e)  A32: SHA1H.32 Qd, Qm  A64: SHA1H Sd, Sn"""
        ...

    @staticmethod
    def hash_update_choose(hash_abcd: System.Runtime.Intrinsics.Vector128[int], hash_e: System.Runtime.Intrinsics.Vector64[int], wk: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vsha1cq_u32 (uint32x4_t hash_abcd, uint32_t hash_e, uint32x4_t wk)  A32: SHA1C.32 Qd, Qn, Qm  A64: SHA1C Qd, Sn, Vm.4S"""
        ...

    @staticmethod
    def hash_update_majority(hash_abcd: System.Runtime.Intrinsics.Vector128[int], hash_e: System.Runtime.Intrinsics.Vector64[int], wk: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vsha1mq_u32 (uint32x4_t hash_abcd, uint32_t hash_e, uint32x4_t wk)  A32: SHA1M.32 Qd, Qn, Qm  A64: SHA1M Qd, Sn, Vm.4S"""
        ...

    @staticmethod
    def hash_update_parity(hash_abcd: System.Runtime.Intrinsics.Vector128[int], hash_e: System.Runtime.Intrinsics.Vector64[int], wk: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vsha1pq_u32 (uint32x4_t hash_abcd, uint32_t hash_e, uint32x4_t wk)  A32: SHA1P.32 Qd, Qn, Qm  A64: SHA1P Qd, Sn, Vm.4S"""
        ...

    @staticmethod
    def schedule_update_0(w_0_3: System.Runtime.Intrinsics.Vector128[int], w_4_7: System.Runtime.Intrinsics.Vector128[int], w_8_11: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vsha1su0q_u32 (uint32x4_t w_0_3, uint32x4_t w_4_7, uint32x4_t w_8_11)  A32: SHA1SU0.32 Qd, Qn, Qm  A64: SHA1SU0 Vd.4S, Vn.4S, Vm.4S"""
        ...

    @staticmethod
    def schedule_update_1(tw_0_3: System.Runtime.Intrinsics.Vector128[int], w_12_15: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """uint32x4_t vsha1su1q_u32 (uint32x4_t tw_0_3, uint32x4_t w_12_15)  A32: SHA1SU1.32 Qd, Qm  A64: SHA1SU1 Vd.4S, Vn.4S"""
        ...


class Crc32(System.Runtime.Intrinsics.Arm.ArmBase, metaclass=abc.ABCMeta):
    """Provides access to the ARM Crc32 hardware instructions via intrinsics."""

    class Arm64(System.Runtime.Intrinsics.Arm.ArmBase.Arm64, metaclass=abc.ABCMeta):
        """Provides access to the ARM Crc32 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def compute_crc_32(crc: int, data: int) -> int:
            """uint32_t __crc32d (uint32_t a, uint64_t b)  A64: CRC32X Wd, Wn, Xm"""
            ...

        @staticmethod
        def compute_crc_32c(crc: int, data: int) -> int:
            """uint32_t __crc32cd (uint32_t a, uint64_t b)  A64: CRC32CX Wd, Wn, Xm"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def compute_crc_32(crc: int, data: int) -> int:
        """uint32_t __crc32b (uint32_t a, uint8_t b)  A32: CRC32B Rd, Rn, Rm  A64: CRC32B Wd, Wn, Wm"""
        ...

    @staticmethod
    def compute_crc_32c(crc: int, data: int) -> int:
        """uint32_t __crc32cb (uint32_t a, uint8_t b)  A32: CRC32CB Rd, Rn, Rm  A64: CRC32CB Wd, Wn, Wm"""
        ...


class Rdm(System.Runtime.Intrinsics.Arm.AdvSimd, metaclass=abc.ABCMeta):
    """Provides access to the ARMv8.1-RDMA hardware instructions via intrinsics."""

    class Arm64(System.Runtime.Intrinsics.Arm.AdvSimd.Arm64, metaclass=abc.ABCMeta):
        """Provides access to the ARMv8.1-RDMA hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def multiply_rounded_doubling_and_add_saturate_high_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrdmlahh_s16 (int16_t a, int16_t b, int16_t c)  A64: SQRDMLAH Hd, Hn, Hm"""
            ...

        @staticmethod
        def multiply_rounded_doubling_and_subtract_saturate_high_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrdmlshh_s16 (int16_t a, int16_t b, int16_t c)  A64: SQRDMLSH Hd, Hn, Hm"""
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrdmlahh_lane_s16 (int16_t a, int16_t b, int16x4_t v, const int lane)  A64: SQRDMLAH Hd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrdmlahh_laneq_s16 (int16_t a, int16_t b, int16x8_t v, const int lane)  A64: SQRDMLAH Hd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrdmlshh_lane_s16 (int16_t a, int16_t b, int16x4_t v, const int lane)  A64: SQRDMLSH Hd, Hn, Vm.H[lane]"""
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            """int16_t vqrdmlshh_laneq_s16 (int16_t a, int16_t b, int16x8_t v, const int lane)  A64: SQRDMLSH Hd, Hn, Vm.H[lane]"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    @overload
    def multiply_rounded_doubling_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrdmlah_s16 (int16x4_t a, int16x4_t b, int16x4_t c)  A32: VQRDMLAH.S16 Dd, Dn, Dm  A64: SQRDMLAH Vd.4H, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrdmlahq_s16 (int16x8_t a, int16x8_t b, int16x8_t c)  A32: VQRDMLAH.S16 Qd, Qn, Qm  A64: SQRDMLAH Vd.8H, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrdmlsh_s16 (int16x4_t a, int16x4_t b, int16x4_t c)  A32: VQRDMLSH.S16 Dd, Dn, Dm  A64: SQRDMLSH Vd.4H, Vn.4H, Vm.4H"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrdmlshq_s16 (int16x8_t a, int16x8_t b, int16x8_t c)  A32: VQRDMLSH.S16 Qd, Qn, Qm  A64: SQRDMLSH Vd.8H, Vn.8H, Vm.8H"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrdmlah_lane_s16 (int16x4_t a, int16x4_t b, int16x4_t v, const int lane)  A32: VQRDMLAH.S16 Dd, Dn, Dm[lane]  A64: SQRDMLAH Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrdmlah_laneq_s16 (int16x4_t a, int16x4_t b, int16x8_t v, const int lane)  A32: VQRDMLAH.S16 Dd, Dn, Dm[lane]  A64: SQRDMLAH Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrdmlahq_lane_s16 (int16x8_t a, int16x8_t b, int16x4_t v, const int lane)  A32: VQRDMLAH.S16 Qd, Qn, Dm[lane]  A64: SQRDMLAH Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrdmlahq_laneq_s16 (int16x8_t a, int16x8_t b, int16x8_t v, const int lane)  A32: VQRDMLAH.S16 Qd, Qn, Dm[lane]  A64: SQRDMLAH Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrdmlsh_lane_s16 (int16x4_t a, int16x4_t b, int16x4_t v, const int lane)  A32: VQRDMLSH.S16 Dd, Dn, Dm[lane]  A64: SQRDMLSH Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int16x4_t vqrdmlsh_laneq_s16 (int16x4_t a, int16x4_t b, int16x8_t v, const int lane)  A32: VQRDMLSH.S16 Dd, Dn, Dm[lane]  A64: SQRDMLSH Vd.4H, Vn.4H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrdmlshq_lane_s16 (int16x8_t a, int16x8_t b, int16x4_t v, const int lane)  A32: VQRDMLSH.S16 Qd, Qn, Dm[lane]  A64: SQRDMLSH Vd.8H, Vn.8H, Vm.H[lane]"""
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int16x8_t vqrdmlshq_laneq_s16 (int16x8_t a, int16x8_t b, int16x8_t v, const int lane)  A32: VQRDMLSH.S16 Qd, Qn, Dm[lane]  A64: SQRDMLSH Vd.8H, Vn.8H, Vm.H[lane]"""
        ...


class Dp(System.Runtime.Intrinsics.Arm.AdvSimd, metaclass=abc.ABCMeta):
    """Provides access to the ARMv8.2-DotProd hardware instructions via intrinsics."""

    class Arm64(System.Runtime.Intrinsics.Arm.AdvSimd.Arm64, metaclass=abc.ABCMeta):
        """Provides access to the ARMv8.2-DotProd hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    @overload
    def dot_product(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32x2_t vdot_s32 (int32x2_t r, int8x8_t a, int8x8_t b)  A32: VSDOT.S8 Dd, Dn, Dm  A64: SDOT Vd.2S, Vn.8B, Vm.8B"""
        ...

    @staticmethod
    @overload
    def dot_product(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vdotq_s32 (int32x4_t r, int8x16_t a, int8x16_t b)  A32: VSDOT.S8 Qd, Qn, Qm  A64: SDOT Vd.4S, Vn.16B, Vm.16B"""
        ...

    @staticmethod
    @overload
    def dot_product_by_selected_quadruplet(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_scaled_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32x2_t vdot_lane_s32 (int32x2_t r, int8x8_t a, int8x8_t b, const int lane)  A32: VSDOT.S8 Dd, Dn, Dm[lane]  A64: SDOT Vd.2S, Vn.8B, Vm.4B[lane]"""
        ...

    @staticmethod
    @overload
    def dot_product_by_selected_quadruplet(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_scaled_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """int32x2_t vdot_laneq_s32 (int32x2_t r, int8x8_t a, int8x16_t b, const int lane)  A32: VSDOT.S8 Dd, Dn, Dm[lane]  A64: SDOT Vd.2S, Vn.8B, Vm.4B[lane]"""
        ...

    @staticmethod
    @overload
    def dot_product_by_selected_quadruplet(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_scaled_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vdotq_laneq_s32 (int32x4_t r, int8x16_t a, int8x16_t b, const int lane)  A32: VSDOT.S8 Qd, Qn, Dm[lane]  A64: SDOT Vd.4S, Vn.16B, Vm.4B[lane]"""
        ...

    @staticmethod
    @overload
    def dot_product_by_selected_quadruplet(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_scaled_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """int32x4_t vdotq_lane_s32 (int32x4_t r, int8x16_t a, int8x8_t b, const int lane)  A32: VSDOT.S8 Qd, Qn, Dm[lane]  A64: SDOT Vd.4S, Vn.16B, Vm.4B[lane]"""
        ...


