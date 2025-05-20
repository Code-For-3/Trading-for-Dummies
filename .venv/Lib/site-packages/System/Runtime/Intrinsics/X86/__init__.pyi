from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Runtime.Intrinsics
import System.Runtime.Intrinsics.X86


class X86Base(System.Object, metaclass=abc.ABCMeta):
    """Provides access to the x86 base hardware instructions via intrinsics."""

    class X64(System.Object, metaclass=abc.ABCMeta):
        """Provides access to the x86 base hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def div_rem(lower: int, upper: int, divisor: int) -> System.ValueTuple[int, int]:
            """unsigned __int64 _udiv128(unsigned __int64 highdividend, unsigned __int64 lowdividend, unsigned __int64 divisor, unsigned __int64* remainder)  DIV reg/m64"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def cpu_id(function_id: int, sub_function_id: int) -> System.ValueTuple[int, int, int, int]:
        """void __cpuidex (int cpuInfo[4], int function_id, int subfunction_id);  CPUID"""
        ...

    @staticmethod
    @overload
    def div_rem(lower: int, upper: int, divisor: int) -> System.ValueTuple[int, int]:
        """unsigned _udiv64(unsigned __int64 dividend, unsigned divisor, unsigned* remainder)  DIV reg/m32"""
        ...

    @staticmethod
    @overload
    def div_rem(lower: System.UIntPtr, upper: System.UIntPtr, divisor: System.UIntPtr) -> System.ValueTuple[System.UIntPtr, System.UIntPtr]:
        """IDIV reg/m"""
        ...

    @staticmethod
    @overload
    def div_rem(lower: System.UIntPtr, upper: System.IntPtr, divisor: System.IntPtr) -> System.ValueTuple[System.IntPtr, System.IntPtr]:
        """IDIV reg/m"""
        ...

    @staticmethod
    def pause() -> None:
        """void _mm_pause (void);  PAUSE"""
        ...


class Sse(System.Runtime.Intrinsics.X86.X86Base, metaclass=abc.ABCMeta):
    """Provides access to X86 SSE hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.X86Base.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 SSE hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_cvtsi64_ss (__m128 a, __int64 b)   CVTSI2SS xmm1,       r/m64  VCVTSI2SS xmm1, xmm2, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def convert_to_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            """__int64 _mm_cvtss_si64 (__m128 a)   CVTSS2SI r64, xmm1/m32  VCVTSS2SI r64, xmm1/m32This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def convert_to_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            """__int64 _mm_cvttss_si64 (__m128 a)   CVTTSS2SI r64, xmm1/m32  VCVTTSS2SI r64, xmm1/m32This intrinsic is only available on 64-bit processes"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_add_ps (__m128 a,  __m128 b)   ADDPS xmm1,               xmm2/m128  VADDPS xmm1,         xmm2, xmm3/m128  VADDPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def add_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_add_ss (__m128 a,  __m128 b)   ADDSS xmm1,               xmm2/m32  VADDSS xmm1,         xmm2, xmm3/m32  VADDSS xmm1 {k1}{z}, xmm2, xmm3/m32{er}"""
        ...

    @staticmethod
    def And(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_and_ps (__m128 a, __m128 b)   ANDPS xmm1,               xmm2/m128  VANDPS xmm1,         xmm2, xmm3/m128  VANDPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def and_not(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_andnot_ps (__m128 a, __m128 b)   ANDNPS xmm1,               xmm2/m128  VANDNPS xmm1,         xmm2, xmm3/m128  VANDNPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpeq_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(0)  VCMPPS xmm1, xmm2, xmm3/m128, imm8(0)"""
        ...

    @staticmethod
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpgt_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(1)   ; with swapped operands  VCMPPS xmm1, xmm2, xmm3/m128, imm8(1)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpge_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(2)   ; with swapped operands  VCMPPS xmm1, xmm2, xmm3/m128, imm8(2)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmplt_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(1)  VCMPPS xmm1, xmm2, xmm3/m128, imm8(1)"""
        ...

    @staticmethod
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmple_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(2)  VCMPPS xmm1, xmm2, xmm3/m128, imm8(2)"""
        ...

    @staticmethod
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpneq_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(4)  VCMPPS xmm1, xmm2, xmm3/m128, imm8(4)"""
        ...

    @staticmethod
    def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpngt_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(5)   ; with swapped operands  VCMPPS xmm1, xmm2, xmm3/m128, imm8(5)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpnge_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(6)   ; with swapped operands  VCMPPS xmm1, xmm2, xmm3/m128, imm8(6)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_not_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpnlt_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(5)  VCMPPS xmm1, xmm2, xmm3/m128, imm8(5)"""
        ...

    @staticmethod
    def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpnle_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(6)  VCMPPS xmm1, xmm2, xmm3/m128, imm8(6)"""
        ...

    @staticmethod
    def compare_ordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpord_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(7)  VCMPPS xmm1, xmm2, xmm3/m128, imm8(7)"""
        ...

    @staticmethod
    def compare_scalar_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpeq_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(0)  VCMPSS xmm1, xmm2, xmm3/m32, imm8(0)"""
        ...

    @staticmethod
    def compare_scalar_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpgt_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(1)   ; with swapped operands  VCMPSS xmm1, xmm2, xmm3/m32, imm8(1)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_scalar_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpge_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(2)   ; with swapped operands  VCMPSS xmm1, xmm2, xmm3/m32, imm8(2)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_scalar_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmplt_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(1)  VCMPSS xmm1, xmm2, xmm3/m32, imm8(1)"""
        ...

    @staticmethod
    def compare_scalar_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmple_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(2)  VCMPSS xmm1, xmm2, xmm3/m32, imm8(2)"""
        ...

    @staticmethod
    def compare_scalar_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpneq_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(4)  VCMPSS xmm1, xmm2, xmm3/m32, imm8(4)"""
        ...

    @staticmethod
    def compare_scalar_not_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpngt_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(5)   ; with swapped operands  VCMPSS xmm1, xmm2, xmm3/m32, imm8(5)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_scalar_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpnge_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(6)   ; with swapped operands  VCMPSS xmm1, xmm2, xmm3/m32, imm8(6)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_scalar_not_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpnlt_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(5)  VCMPSS xmm1, xmm2, xmm3/m32, imm8(5)"""
        ...

    @staticmethod
    def compare_scalar_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpnle_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(6)  VCMPSS xmm1, xmm2, xmm3/m32, imm8(6)"""
        ...

    @staticmethod
    def compare_scalar_ordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpord_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(7)  VCMPSS xmm1, xmm2, xmm3/m32, imm8(7)"""
        ...

    @staticmethod
    def compare_scalar_ordered_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comieq_ss (__m128 a, __m128 b)   COMISS xmm1, xmm2/m32        ; ZF=1 && PF=0  VCOMISS xmm1, xmm2/m32        ; ZF=1 && PF=0  VCOMISS xmm1, xmm2/m32{sae}   ; ZF=1 && PF=0"""
        ...

    @staticmethod
    def compare_scalar_ordered_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comigt_ss (__m128 a, __m128 b)   COMISS xmm1, xmm2/m32        ; ZF=0 && CF=0  VCOMISS xmm1, xmm2/m32        ; ZF=0 && CF=0  VCOMISS xmm1, xmm2/m32{sae}   ; ZF=0 && CF=0"""
        ...

    @staticmethod
    def compare_scalar_ordered_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comige_ss (__m128 a, __m128 b)   COMISS xmm1, xmm2/m32        ; CF=0  VCOMISS xmm1, xmm2/m32        ; CF=0  VCOMISS xmm1, xmm2/m32{sae}   ; CF=0"""
        ...

    @staticmethod
    def compare_scalar_ordered_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comilt_ss (__m128 a, __m128 b)   COMISS xmm1, xmm2/m32        ; PF=0 && CF=1  VCOMISS xmm1, xmm2/m32        ; PF=0 && CF=1  VCOMISS xmm1, xmm2/m32{sae}   ; PF=0 && CF=1"""
        ...

    @staticmethod
    def compare_scalar_ordered_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comile_ss (__m128 a, __m128 b)   COMISS xmm1, xmm2/m32        ; PF=0 && (ZF=1 || CF=1)  VCOMISS xmm1, xmm2/m32        ; PF=0 && (ZF=1 || CF=1)  VCOMISS xmm1, xmm2/m32{sae}   ; PF=0 && (ZF=1 || CF=1)"""
        ...

    @staticmethod
    def compare_scalar_ordered_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comineq_ss (__m128 a, __m128 b)   COMISS xmm1, xmm2/m32        ; ZF=0 || PF=1  VCOMISS xmm1, xmm2/m32        ; ZF=0 || PF=1  VCOMISS xmm1, xmm2/m32{sae}   ; ZF=0 || PF=1"""
        ...

    @staticmethod
    def compare_scalar_unordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpunord_ss (__m128 a,  __m128 b)   CMPSS xmm1,       xmm2/m32, imm8(3)  VCMPSS xmm1, xmm2, xmm3/m32, imm8(3)"""
        ...

    @staticmethod
    def compare_scalar_unordered_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomieq_ss (__m128 a, __m128 b)   UCOMISS xmm1, xmm2/m32       ; ZF=1 && PF=0  VUCOMISS xmm1, xmm2/m32       ; ZF=1 && PF=0  VUCOMISS xmm1, xmm2/m32{sae}  ; ZF=1 && PF=0"""
        ...

    @staticmethod
    def compare_scalar_unordered_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomigt_ss (__m128 a, __m128 b)   UCOMISS xmm1, xmm2/m32       ; ZF=0 && CF=0  VUCOMISS xmm1, xmm2/m32       ; ZF=0 && CF=0  VUCOMISS xmm1, xmm2/m32{sae}  ; ZF=0 && CF=0"""
        ...

    @staticmethod
    def compare_scalar_unordered_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomige_ss (__m128 a, __m128 b)   UCOMISS xmm1, xmm2/m32       ; CF=0  VUCOMISS xmm1, xmm2/m32       ; CF=0  VUCOMISS xmm1, xmm2/m32{sae}  ; CF=0"""
        ...

    @staticmethod
    def compare_scalar_unordered_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomilt_ss (__m128 a, __m128 b)   UCOMISS xmm1, xmm2/m32       ; PF=0 && CF=1  VUCOMISS xmm1, xmm2/m32       ; PF=0 && CF=1  VUCOMISS xmm1, xmm2/m32{sae}  ; PF=0 && CF=1"""
        ...

    @staticmethod
    def compare_scalar_unordered_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomile_ss (__m128 a, __m128 b)   UCOMISS xmm1, xmm2/m32       ; PF=0 && (ZF=1 || CF=1)  VUCOMISS xmm1, xmm2/m32       ; PF=0 && (ZF=1 || CF=1)  VUCOMISS xmm1, xmm2/m32{sae}  ; PF=0 && (ZF=1 || CF=1)"""
        ...

    @staticmethod
    def compare_scalar_unordered_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomineq_ss (__m128 a, __m128 b)   UCOMISS xmm1, xmm2/m32       ; ZF=0 || PF=1  VUCOMISS xmm1, xmm2/m32       ; ZF=0 || PF=1  VUCOMISS xmm1, xmm2/m32{sae}  ; ZF=0 || PF=1"""
        ...

    @staticmethod
    def compare_unordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmpunord_ps (__m128 a,  __m128 b)   CMPPS xmm1,       xmm2/m128, imm8(3)  VCMPPS xmm1, xmm2, xmm3/m128, imm8(3)"""
        ...

    @staticmethod
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvtsi32_ss (__m128 a, int b)   CVTSI2SS xmm1,       r/m32  VCVTSI2SS xmm1, xmm2, r/m32"""
        ...

    @staticmethod
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        """int _mm_cvtss_si32 (__m128 a)   CVTSS2SI r32, xmm1/m32  VCVTSS2SI r32, xmm1/m32"""
        ...

    @staticmethod
    def convert_to_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        """int _mm_cvttss_si32 (__m128 a)   CVTTSS2SI r32, xmm1/m32  VCVTTSS2SI r32, xmm1/m32"""
        ...

    @staticmethod
    def divide(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_div_ps (__m128 a,  __m128 b)   DIVPS xmm,                xmm2/m128  VDIVPS xmm1,         xmm2, xmm3/m128  VDIVPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def divide_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_div_ss (__m128 a,  __m128 b)   DIVSS xmm1,       xmm2/m32  VDIVSS xmm1, xmm2, xmm3/m32"""
        ...

    @staticmethod
    def load_aligned_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_load_ps (float const* mem_address)   MOVAPS xmm1,         m128  VMOVAPS xmm1,         m128  VMOVAPS xmm1 {k1}{z}, m128"""
        ...

    @staticmethod
    def load_high(lower: System.Runtime.Intrinsics.Vector128[float], address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_loadh_pi (__m128 a, __m64 const* mem_addr)   MOVHPS xmm1,       m64  VMOVHPS xmm1, xmm2, m64"""
        ...

    @staticmethod
    def load_low(upper: System.Runtime.Intrinsics.Vector128[float], address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_loadl_pi (__m128 a, __m64 const* mem_addr)   MOVLPS xmm1,       m64  VMOVLPS xmm1, xmm2, m64"""
        ...

    @staticmethod
    def load_scalar_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_load_ss (float const* mem_address)   MOVSS xmm1,      m32  VMOVSS xmm1,      m32  VMOVSS xmm1 {k1}, m32"""
        ...

    @staticmethod
    def load_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_loadu_ps (float const* mem_address)   MOVUPS xmm1,         m128  VMOVUPS xmm1,         m128  VMOVUPS xmm1 {k1}{z}, m128"""
        ...

    @staticmethod
    def max(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_max_ps (__m128 a,  __m128 b)   MAXPS xmm1,               xmm2/m128  VMAXPS xmm1,         xmm2, xmm3/m128  VMAXPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def max_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_max_ss (__m128 a,  __m128 b)   MAXSS xmm1,       xmm2/m32  VMAXSS xmm1, xmm2, xmm3/m32"""
        ...

    @staticmethod
    def min(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_min_ps (__m128 a,  __m128 b)   MINPS xmm1,               xmm2/m128  VMINPS xmm1,         xmm2, xmm3/m128  VMINPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def min_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_min_ss (__m128 a,  __m128 b)   MINSS xmm1,       xmm2/m32  VMINSS xmm1, xmm2, xmm3/m32"""
        ...

    @staticmethod
    def move_high_to_low(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_movehl_ps (__m128 a,  __m128 b)   MOVHLPS xmm1,       xmm2  VMOVHLPS xmm1, xmm2, xmm3"""
        ...

    @staticmethod
    def move_low_to_high(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_movelh_ps (__m128 a,  __m128 b)   MOVLHPS xmm1,       xmm2  VMOVLHPS xmm1, xmm2, xmm3"""
        ...

    @staticmethod
    def move_mask(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        """int _mm_movemask_ps (__m128 a)   MOVMSKPS r32, xmm1  VMOVMSKPS r32, xmm1"""
        ...

    @staticmethod
    def move_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_move_ss (__m128 a, __m128 b)   MOVSS xmm1,         xmm2  VMOVSS xmm1,         xmm2, xmm3  VMOVSS xmm1 {k1}{z}, xmm2, xmm3"""
        ...

    @staticmethod
    def multiply(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_mul_ps (__m128 a, __m128 b)   MULPS xmm1,               xmm2/m128  VMULPS xmm1,         xmm2, xmm3/m128  VMULPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def multiply_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_mul_ss (__m128 a, __m128 b)   MULSS xmm1,       xmm2/m32  VMULSS xmm1, xmm2, xmm3/m32"""
        ...

    @staticmethod
    def Or(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_or_ps (__m128 a,  __m128 b)   ORPS xmm1,               xmm2/m128  VORPS xmm1,         xmm2, xmm3/m128  VORPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def prefetch_0(address: typing.Any) -> None:
        """void _mm_prefetch(char* p, int i)  PREFETCHT0 m8"""
        ...

    @staticmethod
    def prefetch_1(address: typing.Any) -> None:
        """void _mm_prefetch(char* p, int i)  PREFETCHT1 m8"""
        ...

    @staticmethod
    def prefetch_2(address: typing.Any) -> None:
        """void _mm_prefetch(char* p, int i)  PREFETCHT2 m8"""
        ...

    @staticmethod
    def prefetch_non_temporal(address: typing.Any) -> None:
        """void _mm_prefetch(char* p, int i)  PREFETCHNTA m8"""
        ...

    @staticmethod
    def reciprocal(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_rcp_ps (__m128 a)   RCPPS xmm1, xmm2/m128  VRCPPS xmm1, xmm2/m128"""
        ...

    @staticmethod
    @overload
    def reciprocal_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_rcp_ss (__m128 a)   RCPSS xmm1,       xmm2/m32  VRCPSS xmm1, xmm2, xmm3/m32"""
        ...

    @staticmethod
    @overload
    def reciprocal_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_rcp_ss (__m128 a, __m128 b)   RCPSS xmm1,       xmm2/m32  VRCPSS xmm1, xmm2, xmm3/m32The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    def reciprocal_sqrt(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_rsqrt_ps (__m128 a)   RSQRTPS xmm1, xmm2/m128  VRSQRTPS xmm1, xmm2/m128"""
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_rsqrt_ss (__m128 a)   RSQRTSS xmm1,       xmm2/m32  VRSQRTSS xmm1, xmm2, xmm3/m32"""
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_rsqrt_ss (__m128 a, __m128 b)   RSQRTSS xmm1,       xmm2/m32  VRSQRTSS xmm1, xmm2, xmm3/m32The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    def shuffle(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_shuffle_ps (__m128 a,  __m128 b, unsigned int control)   SHUFPS xmm1,               xmm2/m128,         imm8  VSHUFPS xmm1,         xmm2, xmm3/m128,         imm8  VSHUFPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst, imm8"""
        ...

    @staticmethod
    def sqrt(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_sqrt_ps (__m128 a)   SQRTPS xmm1,         xmm2/m128  VSQRTPS xmm1,         xmm2/m128  VSQRTPS xmm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def sqrt_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_sqrt_ss (__m128 a)   SQRTSS xmm1,               xmm2/m32  VSQRTSS xmm1,         xmm2, xmm3/m32  VSQRTSS xmm1 {k1}{z}, xmm2, xmm3/m32{er}"""
        ...

    @staticmethod
    @overload
    def sqrt_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_sqrt_ss (__m128 a, __m128 b)   SQRTSS xmm1,               xmm2/m32  VSQRTSS xmm1,         xmm2, xmm3/m32  VSQRTSS xmm1 {k1}{z}, xmm2, xmm3/m32{er}The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_storeu_ps (float* mem_addr, __m128 a)   MOVUPS m128,         xmm1  VMOVUPS m128,         xmm1  VMOVUPS m128 {k1}{z}, xmm1"""
        ...

    @staticmethod
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_store_ps (float* mem_addr, __m128 a)   MOVAPS m128,         xmm1  VMOVAPS m128,         xmm1  VMOVAPS m128 {k1}{z}, xmm1"""
        ...

    @staticmethod
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_stream_ps (float* mem_addr, __m128 a)   MOVNTPS m128, xmm1  VMOVNTPS m128, xmm1"""
        ...

    @staticmethod
    def store_fence() -> None:
        """void _mm_sfence(void)  SFENCE"""
        ...

    @staticmethod
    def store_high(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_storeh_pi (__m64* mem_addr, __m128 a)   MOVHPS m64, xmm1  VMOVHPS m64, xmm1"""
        ...

    @staticmethod
    def store_low(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_storel_pi (__m64* mem_addr, __m128 a)   MOVLPS m64, xmm1  VMOVLPS m64, xmm1"""
        ...

    @staticmethod
    def store_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_store_ss (float* mem_addr, __m128 a)   MOVSS m32,      xmm1  VMOVSS m32,      xmm1  VMOVSS m32 {k1}, xmm1"""
        ...

    @staticmethod
    def subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_sub_ps (__m128d a, __m128d b)   SUBPS xmm1,               xmm2/m128  VSUBPS xmm1,         xmm2, xmm3/m128  VSUBPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_sub_ss (__m128 a, __m128 b)   SUBSS xmm1,               xmm2/m32  VSUBSS xmm1,         xmm2, xmm3/m32  VSUBSS xmm1 {k1}{z}, xmm2, xmm3/m32{er}"""
        ...

    @staticmethod
    def unpack_high(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_unpackhi_ps (__m128 a,  __m128 b)   UNPCKHPS xmm1,               xmm2/m128  VUNPCKHPS xmm1,         xmm2, xmm3/m128  VUNPCKHPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def unpack_low(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_unpacklo_ps (__m128 a,  __m128 b)   UNPCKLPS xmm1,               xmm2/m128  VUNPCKLPS xmm1,         xmm2, xmm3/m128  VUNPCKLPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def xor(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_xor_ps (__m128 a,  __m128 b)   XORPS xmm1,               xmm2/m128  VXORPS xmm1,         xmm2, xmm3/m128  VXORPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...


class Sse2(System.Runtime.Intrinsics.X86.Sse, metaclass=abc.ABCMeta):
    """Provides access to X86 SSE2 hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Sse.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 SSE2 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128d _mm_cvtsi64_sd (__m128d a, __int64 b)   CVTSI2SD xmm1,       r/m64  VCVTSI2SD xmm1, xmm2, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def convert_scalar_to_vector_128_int_64(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtsi64_si128 (__int64 a)   MOVQ xmm1, r/m64  VMOVQ xmm1, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def convert_scalar_to_vector_128_u_int_64(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtsi64_si128 (__int64 a)   MOVQ xmm1, r/m64  VMOVQ xmm1, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_to_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
            """__int64 _mm_cvtsi128_si64 (__m128i a)   MOVQ r/m64, xmm1  VMOVQ r/m64, xmm1This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_to_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            """__int64 _mm_cvtsd_si64 (__m128d a)   CVTSD2SI r64, xmm1/m64  VCVTSD2SI r64, xmm1/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def convert_to_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            """__int64 _mm_cvttsd_si64 (__m128d a)   CVTTSD2SI r64, xmm1/m64  VCVTTSD2SI r64, xmm1/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def convert_to_u_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
            """__int64 _mm_cvtsi128_si64 (__m128i a)   MOVQ r/m64, xmm1  VMOVQ r/m64, xmm1This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def store_non_temporal(address: typing.Any, value: int) -> None:
            """void _mm_stream_si64(__int64 *p, __int64 a)  MOVNTI m64, r64This intrinsic is only available on 64-bit processes"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_add_epi8 (__m128i a,  __m128i b)   PADDB xmm1,               xmm2/m128  VPADDB xmm1,         xmm2, xmm3/m128  VPADDB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_add_pd (__m128d a,  __m128d b)   ADDPD xmm1,               xmm2/m128  VADDPD xmm1,         xmm2, xmm3/m128  VADDPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    def add_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_adds_epi8 (__m128i a,  __m128i b)   PADDSB xmm1,               xmm2/m128  VPADDSB xmm1,         xmm2, xmm3/m128  VPADDSB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def add_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_add_sd (__m128d a,  __m128d b)   ADDSD xmm1,               xmm2/m64  VADDSD xmm1,         xmm2, xmm3/m64  VADDSD xmm1 {k1}{z}, xmm2, xmm3/m64{er}"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_and_si128 (__m128i a,  __m128i b)   PAND xmm1,       xmm2/m128  VPAND xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_and_pd (__m128d a, __m128d b)   ANDPD xmm1,               xmm2/m128  VANDPD xmm1,         xmm2, xmm3/m128  VANDPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def and_not(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_andnot_si128 (__m128i a,  __m128i b)   PANDN xmm1,       xmm2/m128  VPANDN xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def and_not(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_andnot_pd (__m128d a, __m128d b)   ANDNPD xmm1,               xmm2/m128  VANDNPD xmm1,         xmm2, xmm3/m128  VANDNPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    def average(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_avg_epu8 (__m128i a,  __m128i b)   PAVGB xmm1,               xmm2/m128  VPAVGB xmm1,         xmm2, xmm3/m128  VPAVGB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cmpeq_epi8 (__m128i a,  __m128i b)   PCMPEQB xmm1,       xmm2/m128  VPCMPEQB xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpeq_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(0)  VCMPPD xmm1, xmm2, xmm3/m128, imm8(0)"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cmpgt_epi8 (__m128i a,  __m128i b)   PCMPGTB xmm1,       xmm2/m128  VPCMPGTB xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpgt_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(1)   ; with swapped operands  VCMPPD xmm1, xmm2, xmm3/m128, imm8(1)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpge_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(2)   ; with swapped operands  VCMPPD xmm1, xmm2, xmm3/m128, imm8(2)   ; with swapped operands"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cmplt_epi8 (__m128i a,  __m128i b)   PCMPGTB xmm1,       xmm2/m128    ; with swapped operands  VPCMPGTB xmm1, xmm2, xmm3/m128    ; with swapped operands"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmplt_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(1)  VCMPPD xmm1, xmm2, xmm3/m128, imm8(1)"""
        ...

    @staticmethod
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmple_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(2)  VCMPPD xmm1, xmm2, xmm3/m128, imm8(2)"""
        ...

    @staticmethod
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpneq_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(4)  VCMPPD xmm1, xmm2, xmm3/m128, imm8(4)"""
        ...

    @staticmethod
    def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpngt_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(5)   ; with swapped operands  VCMPPD xmm1, xmm2, xmm3/m128, imm8(5)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpnge_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(6)   ; with swapped operands  VCMPPD xmm1, xmm2, xmm3/m128, imm8(6)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_not_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpnlt_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(5)  VCMPPD xmm1, xmm2, xmm3/m128, imm8(5)"""
        ...

    @staticmethod
    def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpnle_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(6)  VCMPPD xmm1, xmm2, xmm3/m128, imm8(6)"""
        ...

    @staticmethod
    def compare_ordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpord_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(7)  VCMPPD xmm1, xmm2, xmm3/m128, imm8(7)"""
        ...

    @staticmethod
    def compare_scalar_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpeq_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(0)  VCMPDS xmm1, xmm2, xmm3/m64, imm8(0)"""
        ...

    @staticmethod
    def compare_scalar_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpgt_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(1)   ; with swapped operands  VCMPDS xmm1, xmm2, xmm3/m64, imm8(1)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_scalar_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpge_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(2)   ; with swapped operands  VCMPDS xmm1, xmm2, xmm3/m64, imm8(2)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_scalar_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmplt_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(1)  VCMPDS xmm1, xmm2, xmm3/m64, imm8(1)"""
        ...

    @staticmethod
    def compare_scalar_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmple_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(2)  VCMPDS xmm1, xmm2, xmm3/m64, imm8(2)"""
        ...

    @staticmethod
    def compare_scalar_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpneq_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(4)  VCMPDS xmm1, xmm2, xmm3/m64, imm8(4)"""
        ...

    @staticmethod
    def compare_scalar_not_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpngt_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(5)   ; with swapped operands  VCMPDS xmm1, xmm2, xmm3/m64, imm8(5)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_scalar_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpnge_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(6)   ; with swapped operands  VCMPDS xmm1, xmm2, xmm3/m64, imm8(6)   ; with swapped operands"""
        ...

    @staticmethod
    def compare_scalar_not_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpnlt_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(5)  VCMPDS xmm1, xmm2, xmm3/m64, imm8(5)"""
        ...

    @staticmethod
    def compare_scalar_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpnle_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(6)  VCMPDS xmm1, xmm2, xmm3/m64, imm8(6)"""
        ...

    @staticmethod
    def compare_scalar_ordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpord_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(7)  VCMPDS xmm1, xmm2, xmm3/m64, imm8(7)"""
        ...

    @staticmethod
    def compare_scalar_ordered_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comieq_sd (__m128d a, __m128d b)   COMISD xmm1, xmm2/m64        ; ZF=1 && PF=0  VCOMISD xmm1, xmm2/m64        ; ZF=1 && PF=0  VCOMISD xmm1, xmm2/m64{sae}   ; ZF=1 && PF=0"""
        ...

    @staticmethod
    def compare_scalar_ordered_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comigt_sd (__m128d a, __m128d b)   COMISD xmm1, xmm2/m64        ; ZF=0 && CF=0  VCOMISD xmm1, xmm2/m64        ; ZF=0 && CF=0  VCOMISD xmm1, xmm2/m64{sae}   ; ZF=0 && CF=0"""
        ...

    @staticmethod
    def compare_scalar_ordered_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comige_sd (__m128d a, __m128d b)   COMISD xmm1, xmm2/m64        ; CF=0  VCOMISD xmm1, xmm2/m64        ; CF=0  VCOMISD xmm1, xmm2/m64{sae}   ; CF=0"""
        ...

    @staticmethod
    def compare_scalar_ordered_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comilt_sd (__m128d a, __m128d b)   COMISD xmm1, xmm2/m64        ; PF=0 && CF=1  VCOMISD xmm1, xmm2/m64        ; PF=0 && CF=1  VCOMISD xmm1, xmm2/m64{sae}   ; PF=0 && CF=1"""
        ...

    @staticmethod
    def compare_scalar_ordered_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comile_sd (__m128d a, __m128d b)   COMISD xmm1, xmm2/m64        ; PF=0 && (ZF=1 || CF=1)  VCOMISD xmm1, xmm2/m64        ; PF=0 && (ZF=1 || CF=1)  VCOMISD xmm1, xmm2/m64{sae}   ; PF=0 && (ZF=1 || CF=1)"""
        ...

    @staticmethod
    def compare_scalar_ordered_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_comineq_sd (__m128d a, __m128d b)   COMISD xmm1, xmm2/m64        ; ZF=0 || PF=1  VCOMISD xmm1, xmm2/m64        ; ZF=0 || PF=1  VCOMISD xmm1, xmm2/m64{sae}   ; ZF=0 || PF=1"""
        ...

    @staticmethod
    def compare_scalar_unordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpunord_sd (__m128d a,  __m128d b)   CMPDS xmm1,       xmm2/m64, imm8(3)  VCMPDS xmm1, xmm2, xmm3/m64, imm8(3)"""
        ...

    @staticmethod
    def compare_scalar_unordered_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomieq_sd (__m128d a, __m128d b)   UCOMISD xmm1, xmm2/m64       ; ZF=1 && PF=0  VUCOMISD xmm1, xmm2/m64       ; ZF=1 && PF=0  VUCOMISD xmm1, xmm2/m64{sae}  ; ZF=1 && PF=0"""
        ...

    @staticmethod
    def compare_scalar_unordered_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomigt_sd (__m128d a, __m128d b)   UCOMISD xmm1, xmm2/m64       ; ZF=0 && CF=0  VUCOMISD xmm1, xmm2/m64       ; ZF=0 && CF=0  VUCOMISD xmm1, xmm2/m64{sae}  ; ZF=0 && CF=0"""
        ...

    @staticmethod
    def compare_scalar_unordered_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomige_sd (__m128d a, __m128d b)   UCOMISD xmm1, xmm2/m64       ; CF=0  VUCOMISD xmm1, xmm2/m64       ; CF=0  VUCOMISD xmm1, xmm2/m64{sae}  ; CF=0"""
        ...

    @staticmethod
    def compare_scalar_unordered_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomilt_sd (__m128d a, __m128d b)   UCOMISD xmm1, xmm2/m64       ; PF=0 && CF=1  VUCOMISD xmm1, xmm2/m64       ; PF=0 && CF=1  VUCOMISD xmm1, xmm2/m64{sae}  ; PF=0 && CF=1"""
        ...

    @staticmethod
    def compare_scalar_unordered_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomile_sd (__m128d a, __m128d b)   UCOMISD xmm1, xmm2/m64       ; PF=0 && (ZF=1 || CF=1)  VUCOMISD xmm1, xmm2/m64       ; PF=0 && (ZF=1 || CF=1)  VUCOMISD xmm1, xmm2/m64{sae}  ; PF=0 && (ZF=1 || CF=1)"""
        ...

    @staticmethod
    def compare_scalar_unordered_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_ucomineq_sd (__m128d a, __m128d b)   UCOMISD xmm1, xmm2/m64       ; ZF=0 || PF=1  VUCOMISD xmm1, xmm2/m64       ; ZF=0 || PF=1  VUCOMISD xmm1, xmm2/m64{sae}  ; ZF=0 || PF=1"""
        ...

    @staticmethod
    def compare_unordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cmpunord_pd (__m128d a,  __m128d b)   CMPPD xmm1,       xmm2/m128, imm8(3)  VCMPPD xmm1, xmm2, xmm3/m128, imm8(3)"""
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cvtsi32_sd (__m128d a, int b)   CVTSI2SD xmm1,       r/m32  VCVTSI2SD xmm1, xmm2, r/m32"""
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cvtss_sd (__m128d a, __m128 b)   CVTSS2SD xmm1,       xmm2/m32  VCVTSS2SD xmm1, xmm2, xmm3/m32"""
        ...

    @staticmethod
    def convert_scalar_to_vector_128_int_32(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtsi32_si128 (int a)   MOVD xmm1, r/m32  VMOVD xmm1, r/m32"""
        ...

    @staticmethod
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvtsd_ss (__m128 a, __m128d b)   CVTSD2SS xmm1,       xmm2/m64  VCVTSD2SS xmm1, xmm2, xmm3/m64"""
        ...

    @staticmethod
    def convert_scalar_to_vector_128_u_int_32(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtsi32_si128 (int a)   MOVD xmm1, r/m32  VMOVD xmm1, r/m32"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """int _mm_cvtsi128_si32 (__m128i a)   MOVD r/m32, xmm1  VMOVD r/m32, xmm1"""
        ...

    @staticmethod
    @overload
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        """int _mm_cvtsd_si32 (__m128d a)   CVTSD2SI r32, xmm1/m64  VCVTSD2SI r32, xmm1/m64"""
        ...

    @staticmethod
    def convert_to_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        """int _mm_cvttsd_si32 (__m128d a)   CVTTSD2SI r32, xmm1/m64  VCVTTSD2SI r32, xmm1/m64"""
        ...

    @staticmethod
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """int _mm_cvtsi128_si32 (__m128i a)   MOVD r/m32, xmm1  VMOVD r/m32, xmm1"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cvtepi32_pd (__m128i a)   CVTDQ2PD xmm1,         xmm2/m64  VCVTDQ2PD xmm1,         xmm2/m64  VCVTDQ2PD xmm1 {k1}{z}, xmm2/m64/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_double(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cvtps_pd (__m128 a)   CVTPS2PD xmm1,         xmm2/m64  VCVTPS2PD xmm1,         xmm2/m64  VCVTPS2PD xmm1 {k1}{z}, xmm2/m64/m32bcst"""
        ...

    @staticmethod
    def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtps_epi32 (__m128 a)   CVTPS2DQ xmm1,         xmm2/m128  VCVTPS2DQ xmm1,         xmm2/m128  VCVTPS2DQ xmm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    def convert_to_vector_128_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvttps_epi32 (__m128 a)   CVTTPS2DQ xmm1,         xmm2/m128  VCVTTPS2DQ xmm1,         xmm2/m128  VCVTTPS2DQ xmm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvtepi32_ps (__m128i a)   CVTDQ2PS xmm1,         xmm2/m128  VCVTDQ2PS xmm1,         xmm2/m128  VCVTDQ2PS xmm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvtpd_ps (__m128d a)   CVTPD2PS xmm1,         xmm2/m128  VCVTPD2PS xmm1,         xmm2/m128  VCVTPD2PS xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    def divide(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_div_pd (__m128d a,  __m128d b)   DIVPD xmm1,               xmm2/m128  VDIVPD xmm1,         xmm2, xmm3/m128  VDIVPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    def divide_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_div_sd (__m128d a,  __m128d b)   DIVSD xmm1,       xmm2/m64  VDIVSD xmm1, xmm2, xmm3/m64"""
        ...

    @staticmethod
    def extract(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        """int _mm_extract_epi16 (__m128i a,  int immediate)   PEXTRW r/m16, xmm1, imm8  VPEXTRW r/m16, xmm1, imm8"""
        ...

    @staticmethod
    def insert(value: System.Runtime.Intrinsics.Vector128[int], data: int, index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_insert_epi16 (__m128i a,  int i, int immediate)   PINSRW xmm1,       r/m16, imm8  VPINSRW xmm1, xmm2, r/m16, imm8"""
        ...

    @staticmethod
    def load_aligned_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_load_si128 (__m128i const* mem_address)   MOVDQA   xmm1,         m128  VMOVDQA   xmm1,         m128  VMOVDQA32 xmm1 {k1}{z}, m128"""
        ...

    @staticmethod
    def load_fence() -> None:
        """void _mm_lfence(void)  LFENCE"""
        ...

    @staticmethod
    def load_high(lower: System.Runtime.Intrinsics.Vector128[float], address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_loadh_pd (__m128d a, double const* mem_addr)   MOVHPD xmm1,       m64  VMOVHPD xmm1, xmm2, m64"""
        ...

    @staticmethod
    def load_low(upper: System.Runtime.Intrinsics.Vector128[float], address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_loadl_pd (__m128d a, double const* mem_addr)   MOVLPD xmm1,       m64  VMOVLPD xmm1, xmm2, m64"""
        ...

    @staticmethod
    def load_scalar_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_loadu_si32 (void const* mem_addr)   MOVD xmm1, m32  VMOVD xmm1, m32"""
        ...

    @staticmethod
    def load_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_loadu_si128 (__m128i const* mem_address)   MOVDQU  xmm1,         m128  VMOVDQU  xmm1,         m128  VMOVDQU8 xmm1 {k1}{z}, m128"""
        ...

    @staticmethod
    def mask_move(source: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int], address: typing.Any) -> None:
        """void _mm_maskmoveu_si128 (__m128i a,  __m128i mask, char* mem_address)   MASKMOVDQU xmm1, xmm2    ; Address: EDI/RDI  VMASKMOVDQU xmm1, xmm2    ; Address: EDI/RDI"""
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_max_epu8 (__m128i a,  __m128i b)   PMAXUB xmm1,               xmm2/m128  VPMAXUB xmm1,         xmm2, xmm3/m128  VPMAXUB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_max_pd (__m128d a,  __m128d b)   MAXPD xmm1,               xmm2/m128  VMAXPD xmm1,         xmm2, xmm3/m128  VMAXPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    def max_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_max_sd (__m128d a,  __m128d b)   MAXSD xmm1,       xmm2/m64  VMAXSD xmm1, xmm2, xmm3/m64"""
        ...

    @staticmethod
    def memory_fence() -> None:
        """void _mm_mfence(void)  MFENCE"""
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_min_epu8 (__m128i a,  __m128i b)   PMINUB xmm1,               xmm2/m128  VPMINUB xmm1,         xmm2, xmm3/m128  VPMINUB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_min_pd (__m128d a,  __m128d b)   MINPD xmm1,               xmm2/m128  VMINPD xmm1,         xmm2, xmm3/m128  VMINPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    def min_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_min_sd (__m128d a,  __m128d b)   MINSD xmm1,       xmm2/m64  VMINSD xmm1, xmm2, xmm3/m64"""
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """int _mm_movemask_epi8 (__m128i a)   PMOVMSKB r32, xmm1  VPMOVMSKB r32, xmm1"""
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        """int _mm_movemask_pd (__m128d a)   MOVMSKPD r32, xmm1  VMOVMSKPD r32, xmm1"""
        ...

    @staticmethod
    @overload
    def move_scalar(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_move_epi64 (__m128i a)   MOVQ xmm1, xmm2  VMOVQ xmm1, xmm2"""
        ...

    @staticmethod
    @overload
    def move_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_move_sd (__m128d a, __m128d b)   MOVSD xmm1,               xmm2  VMOVSD xmm1,         xmm2, xmm3  VMOVSD xmm1 {k1}{z}, xmm2, xmm3"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_mul_epu32 (__m128i a,  __m128i b)   PMULUDQ xmm1,               xmm2/m128  VPMULUDQ xmm1,         xmm2, xmm3/m128  VPMULUDQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_mul_pd (__m128d a,  __m128d b)   MULPD xmm1,               xmm2/m128  VMULPD xmm1,         xmm2, xmm3/m128  VMULPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    def multiply_add_adjacent(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_madd_epi16 (__m128i a,  __m128i b)   PMADDWD xmm1,               xmm2/m128  VPMADDWD xmm1,         xmm2, xmm3/m128  VPMADDWD xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def multiply_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_mulhi_epi16 (__m128i a,  __m128i b)   PMULHW xmm1,               xmm2/m128  VPMULHW xmm1,         xmm2, xmm3/m128  VPMULHW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_mullo_epi16 (__m128i a,  __m128i b)   PMULLW xmm1,               xmm2/m128  VPMULLW xmm1,         xmm2, xmm3/m128  VPMULLW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def multiply_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_mul_sd (__m128d a,  __m128d b)   MULSD xmm1,       xmm2/m64  VMULSD xmm1, xmm2, xmm3/m64"""
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_or_si128 (__m128i a,  __m128i b)   POR xmm1,       xmm2/m128  VPOR xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_or_pd (__m128d a,  __m128d b)   ORPD xmm1,               xmm2/m128  VORPD xmm1,         xmm2, xmm3/m128  VORPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    def pack_signed_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_packs_epi16 (__m128i a,  __m128i b)   PACKSSWB xmm1,               xmm2/m128  VPACKSSWB xmm1,         xmm2, xmm3/m128  VPACKSSWB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def pack_unsigned_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_packus_epi16 (__m128i a,  __m128i b)   PACKUSWB xmm1,               xmm2/m128  VPACKUSWB xmm1,         xmm2, xmm3/m128  VPACKUSWB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_sll_epi16 (__m128i a, __m128i count)   PSLLW xmm1,               xmm2/m128  VPSLLW xmm1,         xmm2, xmm3/m128  VPSLLW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_slli_epi16 (__m128i a,  int immediate)   PSLLW xmm1,               imm8  VPSLLW xmm1,         xmm2, imm8  VPSLLW xmm1 {k1}{z}, xmm2, imm8"""
        ...

    @staticmethod
    def shift_left_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector128[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_bslli_si128 (__m128i a, int imm8)   PSLLDQ xmm1,            imm8  VPSLLDQ xmm1, xmm2/m128, imm8"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_sra_epi16 (__m128i a, __m128i count)   PSRAW xmm1,               xmm2/m128  VPSRAW xmm1,         xmm2, xmm3/m128  VPSRAW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_srai_epi16 (__m128i a,  int immediate)   PSRAW xmm1,               imm8  VPSRAW xmm1,         xmm2, imm8  VPSRAW xmm1 {k1}{z}, xmm2, imm8"""
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_srl_epi16 (__m128i a, __m128i count)   PSRLW xmm1,               xmm2/m128  VPSRLW xmm1,         xmm2, xmm3/m128  VPSRLW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_srli_epi16 (__m128i a,  int immediate)   PSRLW xmm1,               imm8  VPSRLW xmm1,         xmm2, imm8  VPSRLW xmm1 {k1}{z}, xmm2, imm8"""
        ...

    @staticmethod
    def shift_right_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector128[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_bsrli_si128 (__m128i a, int imm8)   PSRLDQ xmm1,            imm8  VPSRLDQ xmm1, xmm2/m128, imm8"""
        ...

    @staticmethod
    @overload
    def shuffle(value: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_shuffle_epi32 (__m128i a,  int immediate)   PSHUFD xmm1,         xmm2/m128,         imm8  VPSHUFD xmm1,         xmm2/m128,         imm8  VPSHUFD xmm1 {k1}{z}, xmm2/m128/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def shuffle(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_shuffle_pd (__m128d a,  __m128d b, int immediate)   SHUFPD xmm1,               xmm2/m128,         imm8  VSHUFPD xmm1,         xmm2, xmm3/m128,         imm8  VSHUFPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst, imm8"""
        ...

    @staticmethod
    def shuffle_high(value: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_shufflehi_epi16 (__m128i a,  int immediate)   PSHUFHW xmm1,         xmm2/m128, imm8  VPSHUFHW xmm1,         xmm2/m128, imm8  VPSHUFHW xmm1 {k1}{z}, xmm2/m128, imm8"""
        ...

    @staticmethod
    def shuffle_low(value: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_shufflelo_epi16 (__m128i a,  int control)   PSHUFLW xmm1,         xmm2/m128, imm8  VPSHUFLW xmm1,         xmm2/m128, imm8  VPSHUFLW xmm1 {k1}{z}, xmm2/m128, imm8"""
        ...

    @staticmethod
    def sqrt(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_sqrt_pd (__m128d a)   SQRTPD xmm1,         xmm2/m128  VSQRTPD xmm1,         xmm2/m128  VSQRTPD xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def sqrt_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_sqrt_sd (__m128d a)   SQRTSD xmm1,               xmm2/m64  VSQRTSD xmm1,         xmm2, xmm3/m64  VSQRTSD xmm1 {k1}{z}, xmm2, xmm3/m64{er}The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def sqrt_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_sqrt_sd (__m128d a, __m128d b)   SQRTSD xmm1,               xmm2/m64  VSQRTSD xmm1,         xmm2, xmm3/m64  VSQRTSD xmm1 {k1}{z}, xmm2, xmm3/m64{er}"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        """void _mm_storeu_si128 (__m128i* mem_addr, __m128i a)   MOVDQU  m128,         xmm1  VMOVDQU  m128,         xmm1  VMOVDQU8 m128 {k1}{z}, xmm1"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_storeu_pd (double* mem_addr, __m128d a)   MOVAPD m128,         xmm1  VMOVAPD m128,         xmm1  VMOVAPD m128 {k1}{z}, xmm1"""
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        """void _mm_store_si128 (__m128i* mem_addr, __m128i a)   MOVDQA   m128,         xmm1  VMOVDQA   m128,         xmm1  VMOVDQA32 m128 {k1}{z}, xmm1"""
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_store_pd (double* mem_addr, __m128d a)   MOVAPD m128,         xmm1  VMOVAPD m128,         xmm1  VMOVAPD m128 {k1}{z}, xmm1"""
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        """void _mm_stream_si128 (__m128i* mem_addr, __m128i a)   MOVNTDQ m128, xmm1  VMOVNTDQ m128, xmm1"""
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_stream_pd (double* mem_addr, __m128d a)   MOVNTPD m128, xmm1  VMOVNTPD m128, xmm1"""
        ...

    @staticmethod
    def store_high(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_storeh_pd (double* mem_addr, __m128d a)   MOVHPD m64, xmm1  VMOVHPD m64, xmm1"""
        ...

    @staticmethod
    def store_low(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_storel_pd (double* mem_addr, __m128d a)   MOVLPD m64, xmm1  VMOVLPD m64, xmm1"""
        ...

    @staticmethod
    def store_non_temporal(address: typing.Any, value: int) -> None:
        """void _mm_stream_si32(int *p, int a)  MOVNTI m32, r32"""
        ...

    @staticmethod
    @overload
    def store_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        """void _mm_storeu_si32 (void* mem_addr, __m128i a)   MOVD m32, xmm1  VMOVD m32, xmm1"""
        ...

    @staticmethod
    @overload
    def store_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_store_sd (double* mem_addr, __m128d a)   MOVSD m64,      xmm1  VMOVSD m64,      xmm1  VMOVSD m64 {k1}, xmm1"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_sub_epi8 (__m128i a,  __m128i b)   PSUBB xmm1,               xmm2/m128  VPSUBB xmm1,         xmm2, xmm3/m128  VPSUBB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_sub_pd (__m128d a, __m128d b)   SUBPD xmm1,               xmm2/m128  VSUBPD xmm1,         xmm2, xmm3/m128  VSUBPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_subs_epi8 (__m128i a,  __m128i b)   PSUBSB xmm1,               xmm2/m128  VPSUBSB xmm1,         xmm2, xmm3/m128  VPSUBSB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_sub_sd (__m128d a, __m128d b)   SUBSD xmm1,               xmm2/m64  VSUBSD xmm1,         xmm2, xmm3/m64  VSUBSD xmm1 {k1}{z}, xmm2, xmm3/m64{er}"""
        ...

    @staticmethod
    def sum_absolute_differences(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_sad_epu8 (__m128i a,  __m128i b)   PSADBW xmm1,               xmm2/m128  VPSADBW xmm1,         xmm2, xmm3/m128  VPSADBW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def unpack_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_unpackhi_epi8 (__m128i a,  __m128i b)   PUNPCKHBW xmm1,               xmm2/m128  VPUNPCKHBW xmm1,         xmm2, xmm3/m128  VPUNPCKHBW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def unpack_high(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_unpackhi_pd (__m128d a,  __m128d b)   UNPCKHPD xmm1,               xmm2/m128  VUNPCKHPD xmm1,         xmm2, xmm3/m128  VUNPCKHPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def unpack_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_unpacklo_epi8 (__m128i a,  __m128i b)   PUNPCKLBW xmm1,               xmm2/m128  VPUNPCKLBW xmm1,         xmm2, xmm3/m128  VPUNPCKLBW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def unpack_low(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_unpacklo_pd (__m128d a,  __m128d b)   UNPCKLPD xmm1,               xmm2/m128  VUNPCKLPD xmm1,         xmm2, xmm3/m128  VUNPCKLPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_xor_si128 (__m128i a,  __m128i b)   PXOR xmm1,       xmm2/m128  VPXOR xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_xor_pd (__m128d a,  __m128d b)   XORPD xmm1,               xmm2/m128  VXORPD xmm1,         xmm2, xmm3/m128  VXORPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...


class Pclmulqdq(System.Runtime.Intrinsics.X86.Sse2, metaclass=abc.ABCMeta):
    """Provides access to X86 CLMUL hardware instructions via intrinsics."""

    class V256(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def carryless_multiply(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_clmulepi64_epi128 (__m256i a, __m256i b, const int imm8)  VPCLMULQDQ ymm1, ymm2, ymm3/m256, imm8"""
            ...

    class V512(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def carryless_multiply(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_clmulepi64_epi128 (__m512i a, __m512i b, const int imm8)  VPCLMULQDQ zmm1, zmm2, zmm3/m512, imm8"""
            ...

    class X64(System.Runtime.Intrinsics.X86.Sse2.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 CLMUL hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def carryless_multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_clmulepi64_si128 (__m128i a, __m128i b, const int imm8)   PCLMULQDQ xmm1,       xmm2/m128, imm8  VPCLMULQDQ xmm1, xmm2, xmm3/m128, imm8"""
        ...


class Sse3(System.Runtime.Intrinsics.X86.Sse2, metaclass=abc.ABCMeta):
    """Provides access to X86 SSE3 hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Sse2.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 SSE3 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def add_subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_addsub_ps (__m128 a, __m128 b)   ADDSUBPS xmm1,       xmm2/m128  VADDSUBPS xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def horizontal_add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_hadd_ps (__m128 a, __m128 b)   HADDPS xmm1,       xmm2/m128  VHADDPS xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def horizontal_subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_hsub_ps (__m128 a, __m128 b)   HSUBPS xmm1,       xmm2/m128  VHSUBPS xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def load_and_duplicate_to_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_loaddup_pd (double const* mem_addr)   MOVDDUP xmm1,         m64  VMOVDDUP xmm1,         m64  VMOVDDUP xmm1 {k1}{z}, m64"""
        ...

    @staticmethod
    def load_dqu_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_lddqu_si128 (__m128i const* mem_addr)   LDDQU xmm1, m128  VLDDQU xmm1, m128"""
        ...

    @staticmethod
    def move_and_duplicate(source: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_movedup_pd (__m128d a)   MOVDDUP xmm1,         xmm2/m64  VMOVDDUP xmm1,         xmm2/m64  VMOVDDUP xmm1 {k1}{z}, xmm2/m64"""
        ...

    @staticmethod
    def move_high_and_duplicate(source: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_movehdup_ps (__m128 a)   MOVSHDUP xmm1,         xmm2/m128  VMOVSHDUP xmm1,         xmm2/m128  VMOVSHDUP xmm1 {k1}{z}, xmm2/m128"""
        ...

    @staticmethod
    def move_low_and_duplicate(source: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_moveldup_ps (__m128 a)   MOVSLDUP xmm1,         xmm2/m128  VMOVSLDUP xmm1,         xmm2/m128  VMOVSLDUP xmm1 {k1}{z}, xmm2/m128"""
        ...


class Ssse3(System.Runtime.Intrinsics.X86.Sse3, metaclass=abc.ABCMeta):
    """Provides access to X86 SSSE3 hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Sse3.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 SSSE3 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_abs_epi8 (__m128i a)   PABSB xmm1,         xmm2/m128  VPABSB xmm1,         xmm2/m128  VPABSB xmm1 {k1}{z}, xmm2/m128"""
        ...

    @staticmethod
    def align_right(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_alignr_epi8 (__m128i a, __m128i b, int count)   PALIGNR xmm1,               xmm2/m128, imm8  VPALIGNR xmm1,         xmm2, xmm3/m128, imm8  VPALIGNR xmm1 {k1}{z}, xmm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    def horizontal_add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_hadd_epi16 (__m128i a, __m128i b)   PHADDW xmm1,       xmm2/m128  VPHADDW xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def horizontal_add_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_hadds_epi16 (__m128i a, __m128i b)   PHADDSW xmm1,       xmm2/m128  VPHADDSW xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def horizontal_subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_hsub_epi16 (__m128i a, __m128i b)   PHSUBW xmm1,       xmm2/m128  VPHSUBW xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def horizontal_subtract_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_hsubs_epi16 (__m128i a, __m128i b)   PHSUBSW xmm1,       xmm2/m128  VPHSUBSW xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def multiply_add_adjacent(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_maddubs_epi16 (__m128i a, __m128i b)   PMADDUBSW xmm1,               xmm2/m128  VPMADDUBSW xmm1,         xmm2, xmm3/m128  VPMADDUBSW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def multiply_high_round_scale(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_mulhrs_epi16 (__m128i a, __m128i b)   PMULHRSW xmm1,               xmm2/m128  VPMULHRSW xmm1,         xmm2, xmm3/m128  VPMULHRSW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def shuffle(value: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_shuffle_epi8 (__m128i a, __m128i b)   PSHUFB xmm1,               xmm2/m128  VPSHUFB xmm1,         xmm2, xmm3/m128  VPSHUFB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def sign(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_sign_epi8 (__m128i a, __m128i b)   PSIGNB xmm1,       xmm2/m128  VPSIGNB xmm1, xmm2, xmm3/m128"""
        ...


class Sse41(System.Runtime.Intrinsics.X86.Ssse3, metaclass=abc.ABCMeta):
    """Provides access to X86 SSE4.1 hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Ssse3.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 SSE4.1 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def extract(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
            """__int64 _mm_extract_epi64 (__m128i a, const int imm8)   PEXTRQ r/m64, xmm1, imm8  VPEXTRQ r/m64, xmm1, imm8This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def insert(value: System.Runtime.Intrinsics.Vector128[int], data: int, index: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_insert_epi64 (__m128i a, __int64 i, const int imm8)   PINSRQ xmm1,       r/m64, imm8  VPINSRQ xmm1, xmm2, r/m64, imm8This intrinsic is only available on 64-bit processes"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    @overload
    def blend(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_blend_epi16 (__m128i a, __m128i b, const int imm8)   PBLENDW xmm1,       xmm2/m128 imm8  VPBLENDW xmm1, xmm2, xmm3/m128 imm8"""
        ...

    @staticmethod
    @overload
    def blend(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_blend_ps (__m128 a, __m128 b, const int imm8)   BLENDPS xmm1,       xmm2/m128, imm8  VBLENDPS xmm1, xmm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_blendv_epi8 (__m128i a, __m128i b, __m128i mask)   PBLENDVB xmm1,       xmm2/m128, <XMM0>  VPBLENDVB xmm1, xmm2, xmm3/m128, xmm4"""
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mask: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_blendv_ps (__m128 a, __m128 b, __m128 mask)   BLENDVPS xmm1,       xmm2/m128, <XMM0>  VBLENDVPS xmm1, xmm2, xmm3/m128, xmm4"""
        ...

    @staticmethod
    def ceiling(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_ceil_ps (__m128 a)   ROUNDPS xmm1, xmm2/m128, imm8(10)  VROUNDPS xmm1, xmm2/m128, imm8(10)"""
        ...

    @staticmethod
    @overload
    def ceiling_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_ceil_ss (__m128 a)   ROUNDSS xmm1,       xmm2/m128, imm8(10)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(10)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def ceiling_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_ceil_ss (__m128 a, __m128 b)   ROUNDSS xmm1,       xmm2/m128, imm8(10)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(10)"""
        ...

    @staticmethod
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cmpeq_epi64 (__m128i a, __m128i b)   PCMPEQQ xmm1,       xmm2/m128  VPCMPEQQ xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """PMOVSXBW xmm1,         m64  VPMOVSXBW xmm1,         m64  VPMOVSXBW xmm1 {k1}{z}, m64The native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtepi8_epi16 (__m128i a)   PMOVSXBW xmm1,         xmm2/m64  VPMOVSXBW xmm1,         xmm2/m64  VPMOVSXBW xmm1 {k1}{z}, xmm2/m64"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """PMOVSXBD xmm1,         m32  VPMOVSXBD xmm1,         m32  VPMOVSXBD xmm1 {k1}{z}, m32The native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtepi8_epi32 (__m128i a)   PMOVSXBD xmm1,         xmm2/m32  VPMOVSXBD xmm1,         xmm2/m32  VPMOVSXBD xmm1 {k1}{z}, xmm2/m32"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_64(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """PMOVSXBQ xmm1,         m16  VPMOVSXBQ xmm1,         m16  VPMOVSXBQ xmm1 {k1}{z}, m16The native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtepi8_epi64 (__m128i a)   PMOVSXBQ xmm1,         xmm2/m16  VPMOVSXBQ xmm1,         xmm2/m16  VPMOVSXBQ xmm1 {k1}{z}, xmm2/m16"""
        ...

    @staticmethod
    def dot_product(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_dp_ps (__m128 a, __m128 b, const int imm8)   DPPS xmm1,       xmm2/m128, imm8  VDPPS xmm1, xmm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    @overload
    def extract(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        """int _mm_extract_epi8 (__m128i a, const int imm8)   PEXTRB r/m8, xmm1, imm8  VPEXTRB r/m8, xmm1, imm8"""
        ...

    @staticmethod
    @overload
    def extract(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> float:
        """int _mm_extract_ps (__m128 a, const int imm8)   EXTRACTPS r/m32, xmm1, imm8  VEXTRACTPS r/m32, xmm1, imm8"""
        ...

    @staticmethod
    def floor(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_floor_ps (__m128 a)   ROUNDPS xmm1, xmm2/m128, imm8(9)  VROUNDPS xmm1, xmm2/m128, imm8(9)"""
        ...

    @staticmethod
    @overload
    def floor_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_floor_ss (__m128 a)   ROUNDSS xmm1,       xmm2/m128, imm8(9)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(9)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def floor_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_floor_ss (__m128 a, __m128 b)   ROUNDSS xmm1,       xmm2/m128, imm8(9)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(9)"""
        ...

    @staticmethod
    @overload
    def insert(value: System.Runtime.Intrinsics.Vector128[int], data: int, index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_insert_epi8 (__m128i a, int i, const int imm8)   PINSRB xmm1,       r/m8, imm8  VPINSRB xmm1, xmm2, r/m8, imm8"""
        ...

    @staticmethod
    @overload
    def insert(value: System.Runtime.Intrinsics.Vector128[float], data: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_insert_ps (__m128 a, __m128 b, const int imm8)   INSERTPS xmm1,       xmm2/m32, imm8  VINSERTPS xmm1, xmm2, xmm3/m32, imm8"""
        ...

    @staticmethod
    def load_aligned_vector_128_non_temporal(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_stream_load_si128 (const __m128i* mem_addr)   MOVNTDQA xmm1, m128  VMOVNTDQA xmm1, m128"""
        ...

    @staticmethod
    def max(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_max_epi8 (__m128i a, __m128i b)   PMAXSB xmm1,               xmm2/m128  VPMAXSB xmm1,         xmm2, xmm3/m128  VPMAXSB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def min(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_min_epi8 (__m128i a, __m128i b)   PMINSB xmm1,               xmm2/m128  VPMINSB xmm1,         xmm2, xmm3/m128  VPMINSB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def min_horizontal(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_minpos_epu16 (__m128i a)   PHMINPOSUW xmm1, xmm2/m128  VPHMINPOSUW xmm1, xmm2/m128"""
        ...

    @staticmethod
    def multiple_sum_absolute_differences(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_mpsadbw_epu8 (__m128i a, __m128i b, const int imm8)   MPSADBW xmm1,       xmm2/m128, imm8  VMPSADBW xmm1, xmm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    def multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_mul_epi32 (__m128i a, __m128i b)   PMULDQ xmm1,               xmm2/m128  VPMULDQ xmm1,         xmm2, xmm3/m128  VPMULDQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_mullo_epi32 (__m128i a, __m128i b)   PMULLD xmm1,               xmm2/m128  VPMULLD xmm1,         xmm2, xmm3/m128  VPMULLD xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def pack_unsigned_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_packus_epi32 (__m128i a, __m128i b)   PACKUSDW xmm1,               xmm2/m128  VPACKUSDW xmm1,         xmm2, xmm3/m128  VPACKUSDW xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    def round_current_direction(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ps (__m128 a, _MM_FROUND_CUR_DIRECTION)   ROUNDPS xmm1, xmm2/m128, imm8(4)  VROUNDPS xmm1, xmm2/m128, imm8(4)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def round_current_direction_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ss (__m128 a, _MM_FROUND_CUR_DIRECTION)   ROUNDSS xmm1,       xmm2/m128, imm8(4)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(4)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def round_current_direction_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ss (__m128 a, __m128 b, _MM_FROUND_CUR_DIRECTION)   ROUNDSS xmm1,       xmm2/m128, imm8(4)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(4)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    def round_to_nearest_integer(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ps (__m128 a, _MM_FROUND_TO_NEAREST_INT |_MM_FROUND_NO_EXC)   ROUNDPS xmm1, xmm2/m128, imm8(8)  VROUNDPS xmm1, xmm2/m128, imm8(8)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def round_to_nearest_integer_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ss (__m128 a, _MM_FROUND_TO_NEAREST_INT | _MM_FROUND_NO_EXC)   ROUNDSS xmm1,       xmm2/m128, imm8(8)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(8)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def round_to_nearest_integer_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ss (__m128 a, __m128 b, _MM_FROUND_TO_NEAREST_INT | _MM_FROUND_NO_EXC)   ROUNDSS xmm1,       xmm2/m128, imm8(8)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(8)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    def round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ps (__m128 a, _MM_FROUND_TO_NEG_INF |_MM_FROUND_NO_EXC)   ROUNDPS xmm1, xmm2/m128, imm8(9)  VROUNDPS xmm1, xmm2/m128, imm8(9)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ss (__m128 a, _MM_FROUND_TO_NEG_INF | _MM_FROUND_NO_EXC)   ROUNDSS xmm1,       xmm2/m128, imm8(9)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(9)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def round_to_negative_infinity_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ss (__m128 a, __m128 b, _MM_FROUND_TO_NEG_INF | _MM_FROUND_NO_EXC)   ROUNDSS xmm1,       xmm2/m128, imm8(9)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(9)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    def round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ps (__m128 a, _MM_FROUND_TO_POS_INF |_MM_FROUND_NO_EXC)   ROUNDPS xmm1, xmm2/m128, imm8(10)  VROUNDPS xmm1, xmm2/m128, imm8(10)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ss (__m128 a, _MM_FROUND_TO_POS_INF | _MM_FROUND_NO_EXC)   ROUNDSS xmm1,       xmm2/m128, imm8(10)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(10)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def round_to_positive_infinity_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ss (__m128 a, __m128 b, _MM_FROUND_TO_POS_INF | _MM_FROUND_NO_EXC)   ROUNDSS xmm1,       xmm2/m128, imm8(10)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(10)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    def round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ps (__m128 a, _MM_FROUND_TO_ZERO |_MM_FROUND_NO_EXC)   ROUNDPS xmm1, xmm2/m128, imm8(11)  VROUNDPS xmm1, xmm2/m128, imm8(11)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ss (__m128 a, _MM_FROUND_TO_ZERO | _MM_FROUND_NO_EXC)   ROUNDSS xmm1,       xmm2/m128, imm8(11)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(11)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    @overload
    def round_to_zero_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_round_ss (__m128 a, __m128 b, _MM_FROUND_TO_ZERO | _MM_FROUND_NO_EXC)   ROUNDSS xmm1,       xmm2/m128, imm8(11)  VROUNDSS xmm1, xmm2, xmm3/m128, imm8(11)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    def test_c(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> bool:
        """int _mm_testc_si128 (__m128i a, __m128i b)   PTEST xmm1, xmm2/m128    ; CF=1  VPTEST xmm1, xmm2/m128    ; CF=1"""
        ...

    @staticmethod
    def test_not_z_and_not_c(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> bool:
        """int _mm_testnzc_si128 (__m128i a, __m128i b)   PTEST xmm1, xmm2/m128    ; ZF=0 && CF=0  VPTEST xmm1, xmm2/m128    ; ZF=0 && CF=0"""
        ...

    @staticmethod
    def test_z(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> bool:
        """int _mm_testz_si128 (__m128i a, __m128i b)   PTEST xmm1, xmm2/m128    ; ZF=1  VPTEST xmm1, xmm2/m128    ; ZF=1"""
        ...


class Sse42(System.Runtime.Intrinsics.X86.Sse41, metaclass=abc.ABCMeta):
    """Provides access to X86 SSE4.2 hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Sse41.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 SSE4.2 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def crc_32(crc: int, data: int) -> int:
            """unsigned __int64 _mm_crc32_u64 (unsigned __int64 crc, unsigned __int64 v)  CRC32 r64, r/m64This intrinsic is only available on 64-bit processes"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cmpgt_epi64 (__m128i a, __m128i b)   PCMPGTQ xmm1,       xmm2/m128  VPCMPGTQ xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def crc_32(crc: int, data: int) -> int:
        """unsigned int _mm_crc32_u8 (unsigned int crc, unsigned char v)  CRC32 r32, r/m8"""
        ...


class FloatComparisonMode(Enum):
    """This class has no documentation."""

    ORDERED_EQUAL_NON_SIGNALING = 0
    """_CMP_EQ_OQ"""

    ORDERED_LESS_THAN_SIGNALING = 1
    """_CMP_LT_OS"""

    ORDERED_LESS_THAN_OR_EQUAL_SIGNALING = 2
    """_CMP_LE_OS"""

    UNORDERED_NON_SIGNALING = 3
    """_CMP_UNORD_Q"""

    UNORDERED_NOT_EQUAL_NON_SIGNALING = 4
    """_CMP_NEQ_UQ"""

    UNORDERED_NOT_LESS_THAN_SIGNALING = 5
    """_CMP_NLT_US"""

    UNORDERED_NOT_LESS_THAN_OR_EQUAL_SIGNALING = 6
    """_CMP_NLE_US"""

    ORDERED_NON_SIGNALING = 7
    """_CMP_ORD_Q"""

    UNORDERED_EQUAL_NON_SIGNALING = 8
    """_CMP_EQ_UQ"""

    UNORDERED_NOT_GREATER_THAN_OR_EQUAL_SIGNALING = 9
    """_CMP_NGE_US"""

    UNORDERED_NOT_GREATER_THAN_SIGNALING = 10
    """_CMP_NGT_US"""

    ORDERED_FALSE_NON_SIGNALING = 11
    """_CMP_FALSE_OQ"""

    ORDERED_NOT_EQUAL_NON_SIGNALING = 12
    """_CMP_NEQ_OQ"""

    ORDERED_GREATER_THAN_OR_EQUAL_SIGNALING = 13
    """_CMP_GE_OS"""

    ORDERED_GREATER_THAN_SIGNALING = 14
    """_CMP_GT_OS"""

    UNORDERED_TRUE_NON_SIGNALING = 15
    """_CMP_TRUE_UQ"""

    ORDERED_EQUAL_SIGNALING = 16
    """_CMP_EQ_OS"""

    ORDERED_LESS_THAN_NON_SIGNALING = 17
    """_CMP_LT_OQ"""

    ORDERED_LESS_THAN_OR_EQUAL_NON_SIGNALING = 18
    """_CMP_LE_OQ"""

    UNORDERED_SIGNALING = 19
    """_CMP_UNORD_S"""

    UNORDERED_NOT_EQUAL_SIGNALING = 20
    """_CMP_NEQ_US"""

    UNORDERED_NOT_LESS_THAN_NON_SIGNALING = 21
    """_CMP_NLT_UQ"""

    UNORDERED_NOT_LESS_THAN_OR_EQUAL_NON_SIGNALING = 22
    """_CMP_NLE_UQ"""

    ORDERED_SIGNALING = 23
    """_CMP_ORD_S"""

    UNORDERED_EQUAL_SIGNALING = 24
    """_CMP_EQ_US"""

    UNORDERED_NOT_GREATER_THAN_OR_EQUAL_NON_SIGNALING = 25
    """_CMP_NGE_UQ"""

    UNORDERED_NOT_GREATER_THAN_NON_SIGNALING = 26
    """_CMP_NGT_UQ"""

    ORDERED_FALSE_SIGNALING = 27
    """_CMP_FALSE_OS"""

    ORDERED_NOT_EQUAL_SIGNALING = 28
    """_CMP_NEQ_OS"""

    ORDERED_GREATER_THAN_OR_EQUAL_NON_SIGNALING = 29
    """_CMP_GE_OQ"""

    ORDERED_GREATER_THAN_NON_SIGNALING = 30
    """_CMP_GT_OQ"""

    UNORDERED_TRUE_SIGNALING = 31
    """_CMP_TRUE_US"""


class Avx(System.Runtime.Intrinsics.X86.Sse42, metaclass=abc.ABCMeta):
    """Provides access to X86 AVX hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Sse42.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def add(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_add_ps (__m256 a, __m256 b)  VADDPS ymm1,         ymm2, ymm3/m256  VADDPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def add_subtract(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_addsub_ps (__m256 a, __m256 b)  VADDSUBPS ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def And(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_and_ps (__m256 a, __m256 b)  VANDPS ymm1,         ymm2, ymm2/m256  VANDPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def and_not(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_andnot_ps (__m256 a, __m256 b)  VANDNPS ymm1,         ymm2, ymm2/m256  VANDNPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def blend(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_blend_ps (__m256 a, __m256 b, const int imm8)  VBLENDPS ymm1, ymm2, ymm3/m256, imm8"""
        ...

    @staticmethod
    def blend_variable(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], mask: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_blendv_ps (__m256 a, __m256 b, __m256 mask)  VBLENDVPS ymm1, ymm2, ymm3/m256, ymm4"""
        ...

    @staticmethod
    def broadcast_scalar_to_vector_128(source: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_broadcast_ss (float const * mem_addr)  VBROADCASTSS xmm1,         m32  VBROADCASTSS xmm1 {k1}{z}, m32"""
        ...

    @staticmethod
    def broadcast_scalar_to_vector_256(source: typing.Any) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_broadcast_ss (float const * mem_addr)  VBROADCASTSS ymm1,         m32  VBROADCASTSS ymm1 {k1}{z}, m32"""
        ...

    @staticmethod
    def broadcast_vector_128_to_vector_256(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_broadcast_ps (__m128 const * mem_addr)  VBROADCASTF128  ymm1,         m128  VBROADCASTF32x4 ymm1 {k1}{z}, m128"""
        ...

    @staticmethod
    def ceiling(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_ceil_ps (__m128 a)  VROUNDPS ymm1, ymm2/m256, imm8(10)"""
        ...

    @staticmethod
    @overload
    def compare(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmp_ps (__m128 a, __m128 b, const int imm8)  VCMPPS xmm1, xmm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    @overload
    def compare(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmp_ps (__m256 a, __m256 b, const int imm8)  VCMPPS ymm1, ymm2, ymm3/m256, imm8"""
        ...

    @staticmethod
    def compare_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmpeq_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(0)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmpgt_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(14)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmpge_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(13)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_less_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmplt_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(1)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmple_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(2)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmpneq_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(4)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmpngt_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(10)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmpnge_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(9)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_not_less_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmpnlt_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(5)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmpnle_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(6)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_ordered(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmpord_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(7)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cmp_ss (__m128 a, __m128 b, const int imm8)  VCMPSD xmm1, xmm2, xmm3/m64, imm8"""
        ...

    @staticmethod
    def compare_unordered(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cmpunord_ps (__m256 a,  __m256 b)  VCMPPS ymm1, ymm2/m256, imm8(3)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtpd_epi32 (__m256d a)  VCVTPD2DQ xmm1,         ymm2/m256  VCVTPD2DQ xmm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    def convert_to_vector_128_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvttpd_epi32 (__m256d a)  VCVTTPD2DQ xmm1,         ymm2/m256  VCVTTPD2DQ xmm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm256_cvtpd_ps (__m256d a)  VCVTPD2PS xmm1,         ymm2/m256  VCVTPD2PS xmm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_cvtepi32_pd (__m128i a)  VCVTDQ2PD ymm1,         xmm2/m128  VCVTDQ2PD ymm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_cvtps_pd (__m128 a)  VCVTPS2PD ymm1,         xmm2/m128  VCVTPS2PD ymm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    def convert_to_vector_256_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvtps_epi32 (__m256 a)  VCVTPS2DQ ymm1,         ymm2/m256  VCVTPS2DQ ymm1 {k1}{z}, ymm2/m256/m32bcst"""
        ...

    @staticmethod
    def convert_to_vector_256_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvttps_epi32 (__m256 a)  VCVTTPS2DQ ymm1,         ymm2/m256  VCVTTPS2DQ ymm1 {k1}{z}, ymm2/m256/m32bcst"""
        ...

    @staticmethod
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cvtepi32_ps (__m256i a)  VCVTDQ2PS ymm1,         ymm2/m256  VCVTDQ2PS ymm1 {k1}{z}, ymm2/m256/m32bcst"""
        ...

    @staticmethod
    def divide(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_div_ps (__m256 a, __m256 b)  VDIVPS ymm1,         ymm2, ymm3/m256  VDIVPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def dot_product(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_dp_ps (__m256 a, __m256 b, const int imm8)  VDPPS ymm, ymm, ymm/m256, imm8"""
        ...

    @staticmethod
    def duplicate_even_indexed(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_moveldup_ps (__m256 a)  VMOVSLDUP ymm1,         ymm2/m256  VMOVSLDUP ymm1 {k1}{z}, ymm2/m256"""
        ...

    @staticmethod
    def duplicate_odd_indexed(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_movehdup_ps (__m256 a)  VMOVSHDUP ymm1,         ymm2/m256  VMOVSHDUP ymm1 {k1}{z}, ymm2/m256"""
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector256[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_extractf128_si256 (__m256i a, const int imm8)  VEXTRACTF128  xmm1/m128,         ymm2, imm8  VEXTRACTF32x4 xmm1/m128 {k1}{z}, ymm2, imm8"""
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector256[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm256_extractf128_ps (__m256 a, const int imm8)  VEXTRACTF128  xmm1/m128,         ymm2, imm8  VEXTRACTF32x4 xmm1/m128 {k1}{z}, ymm2, imm8"""
        ...

    @staticmethod
    def floor(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_floor_ps (__m256 a)  VROUNDPS ymm1, ymm2/m256, imm8(9)"""
        ...

    @staticmethod
    def horizontal_add(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_hadd_ps (__m256 a, __m256 b)  VHADDPS ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def horizontal_subtract(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_hsub_ps (__m256 a, __m256 b)  VHSUBPS ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector256[int], data: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_insertf128_si256 (__m256i a, __m128i b, int imm8)  VINSERTF128  ymm1,         ymm2, xmm3/m128, imm8  VINSERTF32x4 ymm1 {k1}{z}, ymm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector256[float], data: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_insertf128_ps (__m256 a, __m128 b, int imm8)  VINSERTF128  ymm1,         ymm2, xmm3/m128, imm8  VINSERTF32x4 ymm1 {k1}{z}, ymm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    def load_aligned_vector_256(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_load_si256 (__m256i const * mem_addr)  VMOVDQA   ymm1,         m256  VMOVDQA32 ymm1 {k1}{z}, m256"""
        ...

    @staticmethod
    def load_dqu_vector_256(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_lddqu_si256 (__m256i const * mem_addr)  VLDDQU ymm1, m256"""
        ...

    @staticmethod
    def load_vector_256(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_loadu_si256 (__m256i const * mem_addr)  VMOVDQU  ymm1,         m256  VMOVDQU8 ymm1 {k1}{z}, m256"""
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_maskload_ps (float const * mem_addr, __m128i mask)  VMASKMOVPS xmm1, xmm2, m128"""
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_maskload_ps (float const * mem_addr, __m256i mask)  VMASKMOVPS ymm1, ymm2, m256"""
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        """void _mm_maskstore_ps (float * mem_addr, __m128i mask, __m128 a)  VMASKMOVPS m128, xmm1, xmm2"""
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        """void _mm256_maskstore_ps (float * mem_addr, __m256i mask, __m256 a)  VMASKMOVPS m256, ymm1, ymm2"""
        ...

    @staticmethod
    def max(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_max_ps (__m256 a, __m256 b)  VMAXPS ymm1,         ymm2, ymm3/m256  VMAXPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def min(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_min_ps (__m256 a, __m256 b)  VMINPS ymm1,         ymm2, ymm3/m256  VMINPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def move_mask(value: System.Runtime.Intrinsics.Vector256[float]) -> int:
        """int _mm256_movemask_ps (__m256 a)  VMOVMSKPS r32, ymm1"""
        ...

    @staticmethod
    def multiply(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_mul_ps (__m256 a, __m256 b)  VMULPS ymm1,         ymm2, ymm3/m256  VMULPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def Or(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_or_ps (__m256 a, __m256 b)  VORPS ymm1,         ymm2, ymm3/m256  VORPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def permute(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_permute_ps (__m128 a, int imm8)  VPERMILPS xmm1,         xmm2/m128,         imm8  VPERMILPS xmm1 {k1}{z}, xmm2/m128/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def permute(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_permute_ps (__m256 a, int imm8)  VPERMILPS ymm1,         ymm2/m256,         imm8  VPERMILPS ymm1 {k1}{z}, ymm2/m256/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def permute_2x_128(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permute2f128_si256 (__m256i a, __m256i b, int imm8)  VPERM2F128 ymm1, ymm2, ymm3/m256, imm8"""
        ...

    @staticmethod
    @overload
    def permute_2x_128(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_permute2f128_ps (__m256 a, __m256 b, int imm8)  VPERM2F128 ymm1, ymm2, ymm3/m256, imm8"""
        ...

    @staticmethod
    @overload
    def permute_var(left: System.Runtime.Intrinsics.Vector128[float], control: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_permutevar_ps (__m128 a, __m128i b)  VPERMILPS xmm1,         xmm2, xmm3/m128  VPERMILPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def permute_var(left: System.Runtime.Intrinsics.Vector256[float], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_permutevar_ps (__m256 a, __m256i b)  VPERMILPS ymm1,         ymm2, ymm3/m256  VPERMILPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def reciprocal(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_rcp_ps (__m256 a)  VRCPPS ymm1, ymm2/m256"""
        ...

    @staticmethod
    def reciprocal_sqrt(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_rsqrt_ps (__m256 a)  VRSQRTPS ymm1, ymm2/m256"""
        ...

    @staticmethod
    def round_current_direction(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_round_ps (__m256 a, _MM_FROUND_CUR_DIRECTION)  VROUNDPS ymm1, ymm2/m256, imm8(4)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    def round_to_nearest_integer(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_round_ps (__m256 a, _MM_FROUND_TO_NEAREST_INT)  VROUNDPS ymm1, ymm2/m256, imm8(8)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    def round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_round_ps (__m256 a, _MM_FROUND_TO_NEG_INF | _MM_FROUND_NO_EXC)  VROUNDPS ymm1, ymm2/m256, imm8(9)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    def round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_round_ps (__m256 a, _MM_FROUND_TO_POS_INF | _MM_FROUND_NO_EXC)  VROUNDPS ymm1, ymm2/m256, imm8(10)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    def round_to_zero(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_round_ps (__m256 a, _MM_FROUND_TO_ZERO | _MM_FROUND_NO_EXC)  VROUNDPS ymm1, ymm2/m256, imm8(11)The above native signature does not exist. We provide this additional overload for the recommended use case of this intrinsic."""
        ...

    @staticmethod
    def shuffle(value: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_shuffle_ps (__m256 a, __m256 b, const int imm8)  VSHUFPS ymm1,         ymm2, ymm3/m256,         imm8  VSHUFPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst, imm8"""
        ...

    @staticmethod
    def sqrt(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_sqrt_ps (__m256 a)  VSQRTPS ymm1,         ymm2/m256  VSQRTPS ymm1 {k1}{z}, ymm2/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        """void _mm256_storeu_si256 (__m256i * mem_addr, __m256i a)  VMOVDQU  m256,         ymm1  VMOVDQU8 m256 {k1}{z}, ymm1"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        """void _mm256_storeu_ps (float * mem_addr, __m256 a)  VMOVUPS m256,         ymm1  VMOVUPS m256 {k1}{z}, ymm1"""
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        """void _mm256_store_si256 (__m256i * mem_addr, __m256i a)  VMOVDQA   m256,         ymm1  VMOVDQA32 m256 {k1}{z}, ymm1"""
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        """void _mm256_store_ps (float * mem_addr, __m256 a)  VMOVAPS m256,         ymm1  VMOVAPS m256 {k1}{z}, ymm1"""
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        """void _mm256_stream_si256 (__m256i * mem_addr, __m256i a)  VMOVNTDQ m256, ymm1"""
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        """void _mm256_stream_ps (float * mem_addr, __m256 a)  VMOVNTPS m256, ymm1"""
        ...

    @staticmethod
    def subtract(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_sub_ps (__m256 a, __m256 b)  VSUBPS ymm1,         ymm2, ymm3/m256  VSUBPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def test_c(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_testc_ps (__m128 a, __m128 b)  VTESTPS xmm1, xmm2/m128    ; CF=1"""
        ...

    @staticmethod
    @overload
    def test_c(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> bool:
        """int _mm256_testc_si256 (__m256i a, __m256i b)  VPTEST ymm1, ymm2/m256    ; CF=1"""
        ...

    @staticmethod
    @overload
    def test_c(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> bool:
        """int _mm256_testc_ps (__m256 a, __m256 b)  VTESTPS ymm1, ymm2/m256    ; CF=1"""
        ...

    @staticmethod
    @overload
    def test_not_z_and_not_c(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_testnzc_ps (__m128 a, __m128 b)  VTESTPS xmm1, ymm2/m128    ; ZF=0 && CF=0"""
        ...

    @staticmethod
    @overload
    def test_not_z_and_not_c(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> bool:
        """int _mm256_testnzc_si256 (__m256i a, __m256i b)  VPTEST ymm1, ymm2/m256    ; ZF=0 && CF=0"""
        ...

    @staticmethod
    @overload
    def test_not_z_and_not_c(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> bool:
        """int _mm256_testnzc_ps (__m256 a, __m256 b)  VTESTPS ymm1, ymm2/m256    ; ZF=0 && CF=0"""
        ...

    @staticmethod
    @overload
    def test_z(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        """int _mm_testz_ps (__m128 a, __m128 b)  VTESTPS xmm1, xmm2/m128    ; ZF=1"""
        ...

    @staticmethod
    @overload
    def test_z(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> bool:
        """int _mm256_testz_si256 (__m256i a, __m256i b)  VPTEST ymm1, ymm2/m256    ; ZF=1"""
        ...

    @staticmethod
    @overload
    def test_z(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> bool:
        """int _mm256_testz_ps (__m256 a, __m256 b)  VTESTPS ymm1, ymm2/m256    ; ZF=1"""
        ...

    @staticmethod
    def unpack_high(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_unpackhi_ps (__m256 a, __m256 b)  VUNPCKHPS ymm1,         ymm2, ymm3/m256  VUNPCKHPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def unpack_low(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_unpacklo_ps (__m256 a, __m256 b)  VUNPCKLPS ymm1,         ymm2, ymm3/m256  VUNPCKLPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def xor(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_xor_ps (__m256 a, __m256 b)  VXORPS ymm1,         ymm2, ymm3/m256  VXORPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...


class Avx2(System.Runtime.Intrinsics.X86.Avx, metaclass=abc.ABCMeta):
    """Provides access to X86 AVX2 hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Avx.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX2 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def abs(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_abs_epi8 (__m256i a)  VPABSB ymm1,         ymm2/m256  VPABSB ymm1 {k1}{z}, ymm2/m256"""
        ...

    @staticmethod
    def add(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_add_epi8 (__m256i a, __m256i b)  VPADDB ymm1,         ymm2, ymm3/m256  VPADDB ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def add_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_adds_epi8 (__m256i a, __m256i b)  VPADDSB ymm1,         ymm2, ymm3/m256  VPADDSB ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def align_right(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_alignr_epi8 (__m256i a, __m256i b, const int count)  VPALIGNR ymm1,         ymm2, ymm3/m256, imm8  VPALIGNR ymm1 {k1}{z}, ymm2, ymm3/m256, imm8"""
        ...

    @staticmethod
    def And(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_and_si256 (__m256i a, __m256i b)  VPAND ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def and_not(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_andnot_si256 (__m256i a, __m256i b)  VPANDN ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def average(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_avg_epu8 (__m256i a, __m256i b)  VPAVGB ymm1,         ymm2, ymm3/m256  VPAVGB ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    @overload
    def blend(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_blend_epi32 (__m128i a, __m128i b, const int imm8)  VPBLENDD xmm1, xmm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    @overload
    def blend(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_blend_epi16 (__m256i a, __m256i b, const int imm8)  VPBLENDW ymm1, ymm2, ymm3/m256 imm8"""
        ...

    @staticmethod
    def blend_variable(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_blendv_epi8 (__m256i a, __m256i b, __m256i mask)  VPBLENDVB ymm1, ymm2, ymm3/m256, ymm4"""
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_128(source: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_broadcastb_epi8 (__m128i a)  VPBROADCASTB xmm1,         m8  VPBROADCASTB xmm1 {k1}{z}, m8The above native signature does not directly correspond to the managed signature."""
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_broadcastb_epi8 (__m128i a)  VPBROADCASTB xmm1,         xmm2/m8  VPBROADCASTB xmm1 {k1}{z}, xmm2/m8"""
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_broadcastss_ps (__m128 a)  VBROADCASTSS xmm1,         xmm2/m32  VBROADCASTSS xmm1 {k1}{z}, xmm2/m32"""
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_256(source: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_broadcastb_epi8 (__m128i a)  VPBROADCASTB ymm1,         m8  VPBROADCASTB ymm1 {k1}{z}, m8The above native signature does not directly correspond to the managed signature."""
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_broadcastb_epi8 (__m128i a)  VPBROADCASTB ymm1,         xmm2/m8  VPBROADCASTB ymm1 {k1}{z}, xmm2/m8"""
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_broadcastss_ps (__m128 a)  VBROADCASTSS ymm1,         xmm2/m32  VBROADCASTSS ymm1 {k1}{z}, xmm2/m32"""
        ...

    @staticmethod
    def broadcast_vector_128_to_vector_256(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_broadcastsi128_si256 (__m128i a)  VBROADCASTI128  ymm1,         m128  VBROADCASTI32x4 ymm1 {k1}{z}, m128The above native signature does not directly correspond to the managed signature."""
        ...

    @staticmethod
    def compare_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cmpeq_epi8 (__m256i a, __m256i b)  VPCMPEQB ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cmpgt_epi8 (__m256i a, __m256i b)  VPCMPGTB ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> int:
        """int _mm256_cvtsi256_si32 (__m256i a)  VMOVD r/m32, ymm1"""
        ...

    @staticmethod
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> int:
        """int _mm256_cvtsi256_si32 (__m256i a)  VMOVD r/m32, ymm1"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_16(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        """VPMOVSXBW ymm1,         m128  VPMOVSXBW ymm1 {k1}{z}, m128The native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvtepi8_epi16 (__m128i a)  VPMOVSXBW ymm1,         xmm2/m128  VPMOVSXBW ymm1 {k1}{z}, xmm2/m128"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_32(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        """VPMOVSXBD ymm1,         m64  VPMOVSXBD ymm1 {k1}{z}, m64The native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvtepi8_epi32 (__m128i a)  VPMOVSXBD ymm1,         xmm2/m64  VPMOVSXBD ymm1 {k1}{z}, xmm2/m64"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        """VPMOVSXBQ ymm1,         m32  VPMOVSXBQ ymm1 {k1}{z}, m32The native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvtepi8_epi64 (__m128i a)  VPMOVSXBQ ymm1,         xmm2/m32  VPMOVSXBQ ymm1 {k1}{z}, xmm2/m32"""
        ...

    @staticmethod
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector256[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_extracti128_si256 (__m256i a, const int imm8)  VEXTRACTI128  xmm1/m128,         ymm2, imm8  VEXTRACTI32x4 xmm1/m128 {k1}{z}, ymm2, imm8"""
        ...

    @staticmethod
    @overload
    def gather_mask_vector_128(source: System.Runtime.Intrinsics.Vector128[int], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int], scale: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_mask_i32gather_epi32 (__m128i src, int const* base_addr, __m128i vindex, __m128i mask, const int scale)  VPGATHERDD xmm1, vm32x, xmm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_mask_vector_128(source: System.Runtime.Intrinsics.Vector128[float], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[float], scale: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_mask_i32gather_ps (__m128 src, float const* base_addr, __m128i vindex, __m128 mask, const int scale)  VGATHERDPS xmm1, vm32x, xmm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_mask_vector_128(source: System.Runtime.Intrinsics.Vector128[int], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector128[int], scale: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_mask_i64gather_epi32 (__m128i src, int const* base_addr, __m256i vindex, __m128i mask, const int scale)  VPGATHERQD xmm1, vm32y, xmm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_mask_vector_128(source: System.Runtime.Intrinsics.Vector128[float], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector128[float], scale: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm256_mask_i64gather_ps (__m128 src, float const* base_addr, __m256i vindex, __m128 mask, const int scale)  VGATHERQPS xmm1, vm32y, xmm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_mask_vector_256(source: System.Runtime.Intrinsics.Vector256[int], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int], scale: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_mask_i32gather_epi32 (__m256i src, int const* base_addr, __m256i vindex, __m256i mask, const int scale)  VPGATHERDD ymm1, vm32y, ymm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_mask_vector_256(source: System.Runtime.Intrinsics.Vector256[int], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector256[int], scale: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_mask_i32gather_epi64 (__m256i src, __int64 const* base_addr, __m128i vindex, __m256i mask, const int scale)  VPGATHERDQ ymm1, vm32y, ymm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_mask_vector_256(source: System.Runtime.Intrinsics.Vector256[float], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[float], scale: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_mask_i32gather_ps (__m256 src, float const* base_addr, __m256i vindex, __m256 mask, const int scale)  VPGATHERDPS ymm1, vm32y, ymm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_mask_vector_256(source: System.Runtime.Intrinsics.Vector256[float], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector256[float], scale: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_mask_i32gather_pd (__m256d src, double const* base_addr, __m128i vindex, __m256d mask, const int scale)  VPGATHERDPD ymm1, vm32y, ymm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_vector_128(base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], scale: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_i32gather_epi32 (int const* base_addr, __m128i vindex, const int scale)  VPGATHERDD xmm1, vm32x, xmm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_vector_128(base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], scale: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_i64gather_epi32 (int const* base_addr, __m256i vindex, const int scale)  VPGATHERQD xmm1, vm64y, xmm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_vector_256(base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], scale: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_i32gather_epi32 (int const* base_addr, __m256i vindex, const int scale)  VPGATHERDD ymm1, vm32y, ymm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    @overload
    def gather_vector_256(base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], scale: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_i32gather_epi64 (__int64 const* base_addr, __m128i vindex, const int scale)  VPGATHERDQ ymm1, vm32y, ymm2The scale parameter should be 1, 2, 4 or 8, otherwise, ArgumentOutOfRangeException will be thrown."""
        ...

    @staticmethod
    def horizontal_add(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_hadd_epi16 (__m256i a, __m256i b)  VPHADDW ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def horizontal_add_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_hadds_epi16 (__m256i a, __m256i b)  VPHADDSW ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def horizontal_subtract(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_hsub_epi16 (__m256i a, __m256i b)  VPHSUBW ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def horizontal_subtract_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_hsubs_epi16 (__m256i a, __m256i b)  VPHSUBSW ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector256[int], data: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_inserti128_si256 (__m256i a, __m128i b, const int imm8)  VINSERTI128  ymm1,         ymm2, xmm3/m128, imm8  VINSERTI32x4 ymm1 {k1}{z}, ymm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    def load_aligned_vector_256_non_temporal(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_stream_load_si256 (__m256i const* mem_addr)  VMOVNTDQA ymm1, m256"""
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_maskload_epi32 (int const* mem_addr, __m128i mask)  VPMASKMOVD xmm1, xmm2, m128"""
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_maskload_epi32 (int const* mem_addr, __m256i mask)  VPMASKMOVD ymm1, ymm2, m256"""
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        """void _mm_maskstore_epi32 (int* mem_addr, __m128i mask, __m128i a)  VPMASKMOVD m128, xmm1, xmm2"""
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        """void _mm256_maskstore_epi32 (int* mem_addr, __m256i mask, __m256i a)  VPMASKMOVD m256, ymm1, ymm2"""
        ...

    @staticmethod
    def max(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_max_epi8 (__m256i a, __m256i b)  VPMAXSB ymm1,         ymm2, ymm3/m256  VPMAXSB ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def min(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_min_epi8 (__m256i a, __m256i b)  VPMINSB ymm1,         ymm2, ymm3/m256  VPMINSB ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def move_mask(value: System.Runtime.Intrinsics.Vector256[int]) -> int:
        """int _mm256_movemask_epi8 (__m256i a)  VPMOVMSKB r32, ymm1"""
        ...

    @staticmethod
    def multiple_sum_absolute_differences(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_mpsadbw_epu8 (__m256i a, __m256i b, const int imm8)  VMPSADBW ymm1, ymm2, ymm3/m256, imm8"""
        ...

    @staticmethod
    def multiply(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_mul_epi32 (__m256i a, __m256i b)  VPMULDQ ymm1,         ymm2, ymm3/m256  VPMULDQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    def multiply_add_adjacent(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_madd_epi16 (__m256i a, __m256i b)  VPMADDWD ymm1,         ymm2, ymm3/m256  VPMADDWD ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def multiply_high(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_mulhi_epi16 (__m256i a, __m256i b)  VPMULHW ymm1,         ymm2, ymm3/m256  VPMULHW ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def multiply_high_round_scale(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_mulhrs_epi16 (__m256i a, __m256i b)  VPMULHRSW ymm1,         ymm2, ymm3/m256  VPMULHRSW ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_mullo_epi16 (__m256i a, __m256i b)  VPMULLW ymm1,         ymm2, ymm3/m256  VPMULLW ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def Or(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_or_si256 (__m256i a, __m256i b)  VPOR ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def pack_signed_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_packs_epi16 (__m256i a, __m256i b)  VPACKSSWB ymm1,         ymm2, ymm3/m256  VPACKSSWB ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def pack_unsigned_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_packus_epi16 (__m256i a, __m256i b)  VPACKUSWB ymm1,         ymm2, ymm3/m256  VPACKUSWB ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def permute_2x_128(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permute2x128_si256 (__m256i a, __m256i b, const int imm8)  VPERM2I128 ymm1, ymm2, ymm3/m256, imm8"""
        ...

    @staticmethod
    @overload
    def permute_4x_64(value: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permute4x64_epi64 (__m256i a, const int imm8)  VPERMQ ymm1,         ymm2/m256,         imm8  VPERMQ ymm1 {k1}{z}, ymm2/m256/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def permute_4x_64(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_permute4x64_pd (__m256d a, const int imm8)  VPERMPD ymm1,         ymm2/m256,         imm8  VPERMPD ymm1 {k1}{z}, ymm2/m256/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def permute_var_8x_32(left: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permutevar8x32_epi32 (__m256i a, __m256i idx)  VPERMD ymm1,         ymm2/m256,         imm8  VPERMD ymm1 {k1}{z}, ymm2/m256/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def permute_var_8x_32(left: System.Runtime.Intrinsics.Vector256[float], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_permutevar8x32_ps (__m256 a, __m256i idx)  VPERMPS ymm1,         ymm2/m256,         imm8  VPERMPS ymm1 {k1}{z}, ymm2/m256/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_sll_epi16 (__m256i a, __m128i count)  VPSLLW ymm1,         ymm2, xmm3/m128  VPSLLW ymm1 {k1}{z}, ymm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_slli_epi16 (__m256i a, int imm8)  VPSLLW ymm1,         ymm2, imm8  VPSLLW ymm1 {k1}{z}, ymm2, imm8"""
        ...

    @staticmethod
    def shift_left_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector256[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_bslli_epi128 (__m256i a, const int imm8)  VPSLLDQ ymm1, ymm2/m256, imm8"""
        ...

    @staticmethod
    @overload
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_sllv_epi32 (__m128i a, __m128i count)  VPSLLVD xmm1,         xmm2, xmm3/m128  VPSLLVD xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_sllv_epi32 (__m256i a, __m256i count)  VPSLLVD ymm1,         ymm2, ymm3/m256  VPSLLVD ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """_mm256_sra_epi16 (__m256i a, __m128i count)  VPSRAW ymm1,         ymm2, xmm3/m128  VPSRAW ymm1 {k1}{z}, ymm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_srai_epi16 (__m256i a, int imm8)  VPSRAW ymm1,         ymm2, imm8  VPSRAW ymm1 {k1}{z}, ymm2, imm8"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_srav_epi32 (__m128i a, __m128i count)  VPSRAVD xmm1,         xmm2, xmm3/m128  VPSRAVD xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_srav_epi32 (__m256i a, __m256i count)  VPSRAVD ymm1,         ymm2, ymm3/m256  VPSRAVD ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_srl_epi16 (__m256i a, __m128i count)  VPSRLW ymm1,         ymm2, xmm3/m128  VPSRLW ymm1 {k1}{z}, ymm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_srli_epi16 (__m256i a, int imm8)  VPSRLW ymm1,         ymm2, imm8  VPSRLW ymm1 {k1}{z}, ymm2, imm8"""
        ...

    @staticmethod
    def shift_right_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector256[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_bsrli_epi128 (__m256i a, const int imm8)  VPSRLDQ ymm1, ymm2/m128, imm8"""
        ...

    @staticmethod
    @overload
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_srlv_epi32 (__m128i a, __m128i count)  VPSRLVD xmm1,         xmm2, xmm3/m128  VPSRLVD xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_srlv_epi32 (__m256i a, __m256i count)  VPSRLVD ymm1,         ymm2, ymm3/m256  VPSRLVD ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def shuffle(value: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_shuffle_epi8 (__m256i a, __m256i b)  VPSHUFB ymm1,         ymm2, ymm3/m256  VPSHUFB ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    @overload
    def shuffle(value: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_shuffle_epi32 (__m256i a, const int imm8)  VPSHUFD ymm1,         ymm2/m256,         imm8  VPSHUFD ymm1 {k1}{z}, ymm2/m256/m32bcst, imm8"""
        ...

    @staticmethod
    def shuffle_high(value: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_shufflehi_epi16 (__m256i a, const int imm8)  VPSHUFHW ymm1,         ymm2/m256, imm8  VPSHUFHW ymm1 {k1}{z}, ymm2/m256, imm8"""
        ...

    @staticmethod
    def shuffle_low(value: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_shufflelo_epi16 (__m256i a, const int imm8)  VPSHUFLW ymm1,         ymm2/m256, imm8  VPSHUFLW ymm1 {k1}{z}, ymm2/m256, imm8"""
        ...

    @staticmethod
    def sign(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_sign_epi8 (__m256i a, __m256i b)  VPSIGNB ymm1, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def subtract(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_sub_epi8 (__m256i a, __m256i b)  VPSUBB ymm1,         ymm2, ymm3/m256  VPSUBB ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_subs_epi8 (__m256i a, __m256i b)  VPSUBSB ymm1,         ymm2, ymm3/m128  VPSUBSB ymm1 {k1}{z}, ymm2, ymm3/m128"""
        ...

    @staticmethod
    def sum_absolute_differences(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_sad_epu8 (__m256i a, __m256i b)  VPSADBW ymm1,         ymm2, ymm3/m256  VPSADBW ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def unpack_high(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_unpackhi_epi8 (__m256i a, __m256i b)  VPUNPCKHBW ymm1,         ymm2, ymm3/m256  VPUNPCKHBW ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def unpack_low(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_unpacklo_epi8 (__m256i a, __m256i b)  VPUNPCKLBW ymm1,         ymm2, ymm3/m256  VPUNPCKLBW ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def xor(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_xor_si256 (__m256i a, __m256i b)  VPXOR ymm1, ymm2, ymm3/m256"""
        ...


class FloatRoundingMode(Enum):
    """This class has no documentation."""

    TO_EVEN = ...
    """_MM_FROUND_TO_NEAREST_INT | _MM_FROUND_NO_EXC"""

    TO_NEGATIVE_INFINITY = ...
    """_MM_FROUND_TO_NEG_INF | _MM_FROUND_NO_EXC"""

    TO_POSITIVE_INFINITY = ...
    """_MM_FROUND_TO_POS_INF | _MM_FROUND_NO_EXC"""

    TO_ZERO = ...
    """_MM_FROUND_TO_ZERO | _MM_FROUND_NO_EXC"""


class Avx512F(System.Runtime.Intrinsics.X86.Avx2, metaclass=abc.ABCMeta):
    """Provides access to X86 AVX512F hardware instructions via intrinsics."""

    class VL(System.Object, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX512F+VL hardware instructions via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        @overload
        def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_abs_epi64 (__m128i a)  VPABSQ xmm1 {k1}{z}, xmm2/m128/m64bcst"""
            ...

        @staticmethod
        @overload
        def abs(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_abs_epi64 (__m128i a)  VPABSQ ymm1 {k1}{z}, ymm2/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def align_right_32(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_alignr_epi32 (__m128i a, __m128i b, const int count)  VALIGND xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def align_right_32(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_alignr_epi32 (__m256i a, __m256i b, const int count)  VALIGND ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def align_right_64(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_alignr_epi64 (__m128i a, __m128i b, const int count)  VALIGNQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst, imm8"""
            ...

        @staticmethod
        @overload
        def align_right_64(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_alignr_epi64 (__m256i a, __m256i b, const int count)  VALIGNQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst, imm8"""
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cmpgt_epu32 (__m128i a, __m128i b)  VPCMPUD k1 {k2}, xmm2, xmm3/m128/m32bcst, imm8(6)"""
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cmpgt_epu32 (__m256i a, __m256i b)  VPCMPUD k1 {k2}, ymm2, ymm3/m256/m32bcst, imm8(6)"""
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cmpge_epi32 (__m128i a, __m128i b)  VPCMPD k1 {k2}, xmm2, xmm3/m128/m32bcst, imm8(5)"""
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cmpge_epi32 (__m256i a, __m256i b)  VPCMPD k1 {k2}, ymm2, ymm3/m256/m32bcst, imm8(5)"""
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cmplt_epi32 (__m128i a, __m128i b)  VPCMPD k1 {k2}, xmm2, xmm3/m128/m32bcst, imm8(1)"""
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cmplt_epi32 (__m256i a, __m256i b)  VPCMPD k1 {k2}, ymm2, ymm3/m256/m32bcst, imm8(1)"""
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cmple_epi32 (__m128i a, __m128i b)  VPCMPD k1 {k2}, xmm2, xmm3/m128/m32bcst, imm8(2)"""
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cmple_epi32 (__m256i a, __m256i b)  VPCMPD k1 {k2}, ymm2, ymm3/m256/m32bcst, imm8(2)"""
            ...

        @staticmethod
        @overload
        def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cmpne_epi32 (__m128i a, __m128i b)  VPCMPD k1 {k2}, xmm2, xmm3/m128/m32bcst, imm8(4)"""
            ...

        @staticmethod
        @overload
        def compare_not_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cmpne_epi32 (__m256i a, __m256i b)  VPCMPD k1 {k2}, ymm2, ymm3/m256/m32bcst, imm8(4)"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtepi32_epi8 (__m128i a)  VPMOVDB xmm1/m32 {k1}{z}, xmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtepi32_epi8 (__m256i a)  VPMOVDB xmm1/m64 {k1}{z}, ymm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtusepi32_epi8 (__m128i a)  VPMOVUSDB xmm1/m32 {k1}{z}, xmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtusepi32_epi8 (__m256i a)  VPMOVUSDB xmm1/m64 {k1}{z}, ymm2"""
            ...

        @staticmethod
        def convert_to_vector_128_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128d _mm_cvtepu32_pd (__m128i a)  VCVTUDQ2PD xmm1 {k1}{z}, xmm2/m64/m32bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtepi32_epi16 (__m128i a)  VPMOVDW xmm1/m64 {k1}{z}, zmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtepi32_epi16 (__m256i a)  VPMOVDW xmm1/m128 {k1}{z}, zmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtsepi32_epi16 (__m128i a)  VPMOVSDW xmm1/m64 {k1}{z}, zmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtsepi32_epi16 (__m256i a)  VPMOVSDW xmm1/m128 {k1}{z}, zmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtepi64_epi32 (__m128i a)  VPMOVQD xmm1/m64 {k1}{z}, xmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtepi64_epi32 (__m256i a)  VPMOVQD xmm1/m128 {k1}{z}, ymm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm128_cvtsepi64_epi32 (__m128i a)  VPMOVSQD xmm1/m64 {k1}{z}, xmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtsepi64_epi32 (__m256i a)  VPMOVSQD xmm1/m128 {k1}{z}, ymm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtepi32_epi8 (__m128i a)  VPMOVDB xmm1/m32 {k1}{z}, zmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtepi32_epi8 (__m256i a)  VPMOVDB xmm1/m64 {k1}{z}, zmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtsepi32_epi8 (__m128i a)  VPMOVSDB xmm1/m32 {k1}{z}, zmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtsepi32_epi8 (__m256i a)  VPMOVSDB xmm1/m64 {k1}{z}, zmm2"""
            ...

        @staticmethod
        def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_cvtepu32_ps (__m128i a)  VCVTUDQ2PS xmm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtepi32_epi16 (__m128i a)  VPMOVDW xmm1/m64 {k1}{z}, xmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtepi32_epi16 (__m256i a)  VPMOVDW xmm1/m128 {k1}{z}, ymm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtusepi32_epi16 (__m128i a)  VPMOVUSDW xmm1/m64 {k1}{z}, xmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtusepi32_epi16 (__m256i a)  VPMOVUSDW xmm1/m128 {k1}{z}, ymm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm128_cvtepi64_epi32 (__m128i a)  VPMOVQD xmm1/m128 {k1}{z}, xmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtps_epu32 (__m128 a)  VCVTPS2UDQ xmm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtepi64_epi32 (__m256i a)  VPMOVQD xmm1/m128 {k1}{z}, ymm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtpd_epu32 (__m256d a)  VCVTPD2UDQ xmm1 {k1}{z}, ymm2/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm128_cvtusepi64_epi32 (__m128i a)  VPMOVUSQD xmm1/m128 {k1}{z}, xmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtusepi64_epi32 (__m256i a)  VPMOVUSQD xmm1/m128 {k1}{z}, ymm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvttps_epu32 (__m128 a)  VCVTTPS2UDQ xmm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvttpd_epu32 (__m256d a)  VCVTTPD2UDQ xmm1 {k1}{z}, ymm2/m256/m64bcst"""
            ...

        @staticmethod
        def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256d _mm512_cvtepu32_pd (__m128i a)  VCVTUDQ2PD ymm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_cvtepu32_ps (__m256i a)  VCVTUDQ2PS ymm1 {k1}{z}, ymm2/m256/m32bcst"""
            ...

        @staticmethod
        def convert_to_vector_256_u_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cvtps_epu32 (__m256 a)  VCVTPS2UDQ ymm1 {k1}{z}, ymm2/m256/m32bcst"""
            ...

        @staticmethod
        def convert_to_vector_256_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cvttps_epu32 (__m256 a)  VCVTTPS2UDQ ymm1 {k1}{z}, ymm2/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def fixup(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], table: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_fixupimm_ps(__m128 a, __m128 b, __m128i tbl, int imm);  VFIXUPIMMPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def fixup(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], table: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_fixupimm_ps(__m256 a, __m256 b, __m256i tbl, int imm);  VFIXUPIMMPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def get_exponent(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_getexp_ps (__m128 a)  VGETEXPPS xmm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def get_exponent(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_getexp_ps (__m256 a)  VGETEXPPS ymm1 {k1}{z}, ymm2/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def get_mantissa(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_getmant_ps (__m128 a)  VGETMANTPS xmm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def get_mantissa(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_getmant_ps (__m256 a)  VGETMANTPS ymm1 {k1}{z}, ymm2/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def max(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_max_epi64 (__m128i a, __m128i b)  VPMAXSQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
            ...

        @staticmethod
        @overload
        def max(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_max_epi64 (__m256i a, __m256i b)  VPMAXSQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def min(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_min_epi64 (__m128i a, __m128i b)  VPMINSQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
            ...

        @staticmethod
        @overload
        def min(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_min_epi64 (__m256i a, __m256i b)  VPMINSQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def permute_var_2x_64x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_permutex2var_epi64 (__m128i a, __m128i idx, __m128i b)  VPERMI2Q xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst  VPERMT2Q xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
            ...

        @staticmethod
        @overload
        def permute_var_2x_64x_2(lower: System.Runtime.Intrinsics.Vector128[float], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128d _mm_permutex2var_pd (__m128d a, __m128i idx, __m128i b)  VPERMI2PD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst  VPERMT2PD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
            ...

        @staticmethod
        @overload
        def permute_var_4x_32x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_permutex2var_epi32 (__m128i a, __m128i idx, __m128i b)  VPERMI2D xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst  VPERMT2D xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def permute_var_4x_32x_2(lower: System.Runtime.Intrinsics.Vector128[float], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_permutex2var_ps (__m128 a, __m128i idx, __m128i b)  VPERMI2PS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst  VPERMT2PS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def permute_var_4x_64(value: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_permute4x64_epi64 (__m256i a, __m256i b)  VPERMQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def permute_var_4x_64(value: System.Runtime.Intrinsics.Vector256[float], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256d _mm256_permute4x64_pd (__m256d a, __m256i b)  VPERMPD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def permute_var_4x_64x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_permutex2var_epi64 (__m256i a, __m256i idx, __m256i b)  VPERMI2Q ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst  VPERMT2Q ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def permute_var_4x_64x_2(lower: System.Runtime.Intrinsics.Vector256[float], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256d _mm256_permutex2var_pd (__m256d a, __m256i idx, __m256i b)  VPERMI2PD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst  VPERMT2PD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def permute_var_8x_32x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_permutex2var_epi32 (__m256i a, __m256i idx, __m256i b)  VPERMI2D ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst  VPERMT2D ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def permute_var_8x_32x_2(lower: System.Runtime.Intrinsics.Vector256[float], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_permutex2var_ps (__m256 a, __m256i idx, __m256i b)  VPERMI2PS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst  VPERMT2PS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def reciprocal_14(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_rcp14_ps (__m128 a, __m128 b)  VRCP14PS xmm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def reciprocal_14(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_rcp14_ps (__m256 a, __m256 b)  VRCP14PS ymm1 {k1}{z}, ymm2/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def reciprocal_sqrt_14(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_rsqrt14_ps (__m128 a, __m128 b)  VRSQRT14PS xmm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def reciprocal_sqrt_14(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_rsqrt14_ps (__m256 a, __m256 b)  VRSQRT14PS ymm1 {k1}{z}, ymm2/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def rotate_left(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_rol_epi32 (__m128i a, int imm8)  VPROLD xmm1 {k1}{z}, xmm2/m128/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def rotate_left(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_rol_epi32 (__m256i a, int imm8)  VPROLD ymm1 {k1}{z}, ymm2/m256/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def rotate_left_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_rolv_epi32 (__m128i a, __m128i b)  VPROLDV xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def rotate_left_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_rolv_epi32 (__m256i a, __m256i b)  VPROLDV ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def rotate_right(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_ror_epi32 (__m128i a, int imm8)  VPRORD xmm1 {k1}{z}, xmm2/m128/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def rotate_right(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_ror_epi32 (__m256i a, int imm8)  VPRORD ymm1 {k1}{z}, ymm2/m256/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def rotate_right_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_rorv_epi32 (__m128i a, __m128i b)  VPRORDV xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def rotate_right_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_rorv_epi32 (__m256i a, __m256i b)  VPRORDV ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def round_scale(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_roundscale_ps (__m128 a, int imm)  VRNDSCALEPS xmm1 {k1}{z}, xmm2/m128/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def round_scale(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_roundscale_ps (__m256 a, int imm)  VRNDSCALEPS ymm1 {k1}{z}, ymm2/m256/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def scale(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_scalef_ps (__m128 a, int imm)  VSCALEFPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def scale(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_scalef_ps (__m256 a, int imm)  VSCALEFPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_sra_epi64 (__m128i a, __m128i count)  VPSRAQ xmm1 {k1}{z}, xmm2, xmm3/m128"""
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_sra_epi64 (__m256i a, __m128i count)  VPSRAQ ymm1 {k1}{z}, ymm2, xmm3/m128"""
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__128i _mm_srai_epi64 (__m128i a, int imm8)  VPSRAQ xmm1 {k1}{z}, xmm2, imm8"""
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_srai_epi64 (__m256i a, int imm8)  VPSRAQ ymm1 {k1}{z}, ymm2, imm8"""
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_srav_epi64 (__m128i a, __m128i count)  VPSRAVQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_srav_epi64 (__m256i a, __m256i count)  VPSRAVQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def shuffle_2x_128(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256d _mm256_shuffle_f64x2 (__m256d a, __m256d b, const int imm8)  VSHUFF64x2 ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst, imm8"""
            ...

        @staticmethod
        @overload
        def shuffle_2x_128(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_shuffle_i32x4 (__m256i a, __m256i b, const int imm8)  VSHUFI32x4 ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def ternary_logic(a: System.Runtime.Intrinsics.Vector128[int], b: System.Runtime.Intrinsics.Vector128[int], c: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_ternarylogic_si128 (__m128i a, __m128i b, __m128i c, byte imm)  VPTERNLOGD xmm1 {k1}{z}, xmm2, xmm3/m128, imm8The above native signature does not exist. We provide this additional overload for consistency with the other bitwise APIs."""
            ...

        @staticmethod
        @overload
        def ternary_logic(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_ternarylogic_ps (__m128 a, __m128 b, __m128 c, int imm)  VPTERNLOGD xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst, imm8The above native signature does not exist. We provide this additional overload for consistency with the other bitwise APIs."""
            ...

        @staticmethod
        @overload
        def ternary_logic(a: System.Runtime.Intrinsics.Vector256[int], b: System.Runtime.Intrinsics.Vector256[int], c: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_ternarylogic_si256 (__m256i a, __m256i b, __m256i c, byte imm)  VPTERNLOGD ymm1 {k1}{z}, ymm2, ymm3/m256, imm8The above native signature does not exist. We provide this additional overload for consistency with the other bitwise APIs."""
            ...

        @staticmethod
        @overload
        def ternary_logic(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_ternarylogic_ps (__m256 a, __m256 b, __m256 c, int imm)  VPTERNLOGD ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst, imm8The above native signature does not exist. We provide this additional overload for consistency with the other bitwise APIs."""
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx2.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX512F hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128d _mm_cvtsi64_sd (__m128d a, __int64 b)  VCVTUSI2SD xmm1, xmm2, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128d _mm_cvt_roundsi64_sd (__m128d a, __int64 b, int rounding)  VCVTSI2SD xmm1, xmm2, r64 {er}This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_cvt_roundi64_ss (__m128 a, __int64 b, int rounding)  VCVTSI2SS xmm1, xmm2, r64 {er}This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_cvtsi64_ss (__m128 a, __int64 b)  VCVTUSI2SS xmm1, xmm2, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def convert_to_int_64(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
            """__int64 _mm_cvt_roundss_i64 (__m128 a, int rounding)  VCVTSS2SI r64, xmm1 {er}This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_to_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            """unsigned __int64 _mm_cvtss_u64 (__m128 a)  VCVTSS2USI r64, xmm1/m32{er}This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_to_u_int_64(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
            """unsigned __int64 _mm_cvt_roundss_u64 (__m128 a, int rounding)  VCVTSS2USI r64, xmm1 {er}This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def convert_to_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            """unsigned __int64 _mm_cvttss_u64 (__m128 a)  VCVTTSS2USI r64, xmm1/m32{er}This intrinsic is only available on 64-bit processes"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def abs(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_abs_epi32 (__m512i a)  VPABSD zmm1 {k1}{z}, zmm2/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_add_epi32 (__m512i a, __m512i b)  VPADDD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_add_pd (__m512d a, __m512d b)  VADDPD zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst{er}"""
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_add_round_pd (__m512d a, __m512d b, int rounding)  VADDPD zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    def add_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_add_round_sd (__m128d a, __m128d b, int rounding)  VADDSD xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def align_right_32(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_alignr_epi32 (__m512i a, __m512i b, const int count)  VALIGND zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst, imm8"""
        ...

    @staticmethod
    def align_right_64(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_alignr_epi64 (__m512i a, __m512i b, const int count)  VALIGNQ zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst, imm8"""
        ...

    @staticmethod
    def And(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_and_si512 (__m512i a, __m512i b)  VPANDD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    def and_not(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_andnot_si512 (__m512i a, __m512i b)  VPANDND zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mask: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_blendv_pd (__m512d a, __m512d b, __m512d mask)  VBLENDMPD zmm1 {k1}, zmm2, zmm3/m512/m64bcst"""
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_blendv_epi32 (__m512i a, __m512i b, __m512i mask)  VPBLENDMD zmm1 {k1}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_broadcastd_epi32 (__m128i a)  VPBROADCASTD zmm1 {k1}{z}, xmm2/m32"""
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_broadcastss_ps (__m128 a)  VBROADCASTSS zmm1 {k1}{z}, xmm2/m32"""
        ...

    @staticmethod
    def broadcast_vector_128_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_broadcast_i32x4 (__m128i const * mem_addr)  VBROADCASTI32x4 zmm1 {k1}{z}, m128"""
        ...

    @staticmethod
    def broadcast_vector_256_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_broadcast_i64x4 (__m256i const * mem_addr)  VBROADCASTI64x4 zmm1 {k1}{z}, m256"""
        ...

    @staticmethod
    def compare(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmp_pd (__m512d a, __m512d b, const int imm8)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8"""
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmpeq_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(0)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmpeq_epi32 (__m512i a, __m512i b)  VPCMPEQD k1 {k2}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmpgt_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(14)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmpgt_epi32 (__m512i a, __m512i b)  VPCMPGTD k1 {k2}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmpge_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(13)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmpge_epi32 (__m512i a, __m512i b)  VPCMPD k1 {k2}, zmm2, zmm3/m512/m32bcst, imm8(5)"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmplt_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(1)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmplt_epi32 (__m512i a, __m512i b)  VPCMPD k1 {k2}, zmm2, zmm3/m512/m32bcst, imm8(1)"""
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmple_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(2)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmple_epi32 (__m512i a, __m512i b)  VPCMPD k1 {k2}, zmm2, zmm3/m512/m32bcst, imm8(2)"""
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmpneq_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(4)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmpne_epi32 (__m512i a, __m512i b)  VPCMPD k1 {k2}, zmm2, zmm3/m512/m32bcst, imm8(4)"""
        ...

    @staticmethod
    def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmpngt_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(10)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmpnge_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(9)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_not_less_than(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmpnlt_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(5)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmpnle_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(6)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_ordered(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmpord_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(7)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def compare_unordered(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cmpunord_pd (__m512d a,  __m512d b)  VCMPPD k1 {k2}, zmm2, zmm3/m512/m64bcst{sae}, imm8(3)The above native signature does not exist. We provide this additional overload for completeness."""
        ...

    @staticmethod
    def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cvtsi32_sd (__m128d a, int b)  VCVTUSI2SD xmm1, xmm2, r/m32"""
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvtsi32_ss (__m128 a, int b)  VCVTUSI2SS xmm1, xmm2, r/m32"""
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvt_roundi32_ss (__m128 a, int b, int rounding)VCVTUSI2SS xmm1, xmm2, r32 {er}"""
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvt_roundsd_ss (__m128 a, __m128d b, int rounding)VCVTSD2SS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
        """int _mm_cvt_roundss_i32 (__m128 a, int rounding)  VCVTSS2SIK r32, xmm1 {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        """unsigned int _mm_cvtss_u32 (__m128 a)  VCVTSS2USI r32, xmm1/m32{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
        """unsigned int _mm_cvt_roundss_u32 (__m128 a, int rounding)  VCVTSS2USI r32, xmm1 {er}"""
        ...

    @staticmethod
    def convert_to_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        """unsigned int _mm_cvttss_u32 (__m128 a)  VCVTTSS2USI r32, xmm1/m32{er}"""
        ...

    @staticmethod
    def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm512_cvtepi32_epi8 (__m512i a)  VPMOVDB xmm1/m128 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm512_cvtusepi32_epi8 (__m512i a)  VPMOVUSDB xmm1/m128 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm512_cvtepi64_epi16 (__m512i a)  VPMOVQW xmm1/m128 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_128_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm512_cvtsepi64_epi16 (__m512i a)  VPMOVSQW xmm1/m128 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm512_cvtepi32_epi8 (__m512i a)  VPMOVDB xmm1/m128 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm512_cvtsepi32_epi8 (__m512i a)  VPMOVSDB xmm1/m128 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_128_u_int_16(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm512_cvtepi64_epi16 (__m512i a)  VPMOVQW xmm1/m128 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_128_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm512_cvtusepi64_epi16 (__m512i a)  VPMOVUSQW xmm1/m128 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_256_int_16(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtepi32_epi16 (__m512i a)  VPMOVDW ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_256_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtsepi32_epi16 (__m512i a)  VPMOVSDW ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtpd_epi32 (__m512d a)  VCVTPD2DQ ymm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvt_roundpd_epi32 (__m512d a, int rounding)  VCVTPD2DQ ymm1, zmm2 {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_32(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtepi64_epi32 (__m512i a)  VPMOVQD ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_256_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtsepi64_epi32 (__m512i a)  VPMOVSQD ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_256_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvttpd_epi32 (__m512d a)  VCVTTPD2DQ ymm1 {k1}{z}, zmm2/m512/m64bcst{sae}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm512_cvtpd_ps (__m512d a)  VCVTPD2PS ymm1,         zmm2/m512  VCVTPD2PS ymm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm512_cvt_roundpd_ps (__m512d a, int rounding)  VCVTPD2PS ymm1, zmm2 {er}"""
        ...

    @staticmethod
    def convert_to_vector_256_u_int_16(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtepi32_epi16 (__m512i a)  VPMOVDW ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_256_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtusepi32_epi16 (__m512i a)  VPMOVUSDW ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtpd_epu32 (__m512d a)  VCVTPD2UDQ ymm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        __m256i _mm512_cvt_roundpd_epu32 (__m512d a, int rounding)
            VCVTPD2UDQ ymm1, zmm2 {er}
        """
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_32(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtepi64_epi32 (__m512i a)  VPMOVQD ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_256_u_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtusepi64_epi32 (__m512i a)  VPMOVUSQD ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_256_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvttpd_epu32 (__m512d a)  VCVTTPD2UDQ ymm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cvtepi32_pd (__m256i a)  VCVTDQ2PD zmm1 {k1}{z}, ymm2/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cvtps_pd (__m256 a)  VCVTPS2PD zmm1 {k1}{z}, ymm2/m256/m32bcst{sae}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtepi8_epi32 (__m128i a)  VPMOVSXBD zmm1 {k1}{z}, xmm2/m128"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtepi16_epi32 (__m128i a)  VPMOVSXWD zmm1 {k1}{z}, ymm2/m256"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtps_epi32 (__m512 a)  VCVTPS2DQ zmm1 {k1}{z}, zmm2/m512/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvt_roundps_epi32 (__m512 a, int rounding)  VCVTPS2DQ zmm1, zmm2 {er}"""
        ...

    @staticmethod
    def convert_to_vector_512_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvttps_epi32 (__m512 a)  VCVTTPS2DQ zmm1 {k1}{z}, zmm2/m512/m32bcst{sae}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtepi8_epi64 (__m128i a)  VPMOVSXBQ zmm1 {k1}{z}, xmm2/m64"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtepi32_epi64 (__m128i a)  VPMOVSXDQ zmm1 {k1}{z}, ymm2/m256"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_single(value: System.Runtime.Intrinsics.Vector512[int], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_cvt_roundepi32_ps (__m512i a, int rounding)  VCVTDQ2PS zmm1, zmm2 {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_single(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_cvtepi32_ps (__m512i a)  VCVTDQ2PS zmm1 {k1}{z}, zmm2/m512/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtepi8_epi32 (__m128i a)  VPMOVSXBD zmm1 {k1}{z}, xmm2/m128"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtepi16_epi32 (__m128i a)  VPMOVSXWD zmm1 {k1}{z}, ymm2/m256"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtps_epu32 (__m512 a)  VCVTPS2UDQ zmm1 {k1}{z}, zmm2/m512/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvt_roundps_epu32 (__m512 a, int rounding)  VCVTPS2UDQ zmm1, zmm2 {er}"""
        ...

    @staticmethod
    def convert_to_vector_512_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvttps_epu32 (__m512 a)  VCVTTPS2UDQ zmm1 {k1}{z}, zmm2/m512/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtepi8_epi64 (__m128i a)  VPMOVSXBQ zmm1 {k1}{z}, xmm2/m64"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtepi32_epi64 (__m128i a)  VPMOVSXDQ zmm1 {k1}{z}, ymm2/m256"""
        ...

    @staticmethod
    @overload
    def divide(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_div_ps (__m512 a, __m512 b)  VDIVPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def divide(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_div_round_ps (__m512 a, __m512 b, int rounding)  VDIVPS zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    def divide_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_div_round_sd (__m128d a, __m128d b, int rounding)  VDIVSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def duplicate_even_indexed(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_moveldup_ps (__m512 a)  VMOVSLDUP zmm1 {k1}{z}, zmm2/m512"""
        ...

    @staticmethod
    def duplicate_odd_indexed(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_movehdup_ps (__m512 a)  VMOVSHDUP zmm1 {k1}{z}, zmm2/m512"""
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm512_extracti128_si512 (__m512i a, const int imm8)  VEXTRACTI32x4 xmm1/m128 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm512_extractf32x4_ps (__m512 a, const int imm8)  VEXTRACTF32x4 xmm1/m128 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    @overload
    def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_extracti256_si512 (__m512i a, const int imm8)  VEXTRACTI64x4 ymm1/m256 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    @overload
    def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm512_extractf256_ps (__m512 a, const int imm8)  VEXTRACTF64x4 ymm1/m256 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    def fixup(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], table: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fixupimm_ps(__m512 a, __m512 b, __m512i tbl, int imm);  VFIXUPIMMPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst{sae}, imm8"""
        ...

    @staticmethod
    def fixup_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], table: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fixupimm_ss(__m128 a, __m128 b, __m128i tbl, int imm);  VFIXUPIMMSS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}, imm8"""
        ...

    @staticmethod
    @overload
    def fused_multiply_add(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fmadd_ps (__m512 a, __m512 b, __m512 c)  VFMADDPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def fused_multiply_add(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fmadd_round_ps (__m512 a, __m512 b, __m512 c, int r)  VFMADDPS zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    @overload
    def fused_multiply_add_negated(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fnmadd_ps (__m512 a, __m512 b, __m512 c)  VFNMADDPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def fused_multiply_add_negated(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fnmadd_round_ps (__m512 a, __m512 b, __m512 c, int r)  VFNMADDPS zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    def fused_multiply_add_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fnmadd_round_ss (__m128 a, __m128 b, __m128 c, int r)  VFNMADDSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def fused_multiply_add_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fmadd_round_ss (__m128 a, __m128 b, __m128 c, int r)  VFMADDSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    @overload
    def fused_multiply_add_subtract(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fmaddsub_ps (__m512 a, __m512 b, __m512 c)  VFMADDSUBPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def fused_multiply_add_subtract(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fmaddsub_ps (__m512 a, __m512 b, __m512 c, int c)  VFMADDSUBPS zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fmsub_ps (__m512 a, __m512 b, __m512 c)  VFMSUBPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fmsub_round_ps (__m512 a, __m512 b, __m512 c, int r)  VFMSUBPS zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract_add(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fmsubadd_ps (__m512 a, __m512 b, __m512 c)  VFMSUBADDPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract_add(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fmsubadd_round_ps (__m512 a, __m512 b, __m512 c)  VFMSUBADDPS zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract_negated(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fnmsub_ps (__m512 a, __m512 b, __m512 c)  VFNMSUBPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract_negated(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_fnmsub_round_ps (__m512 a, __m512 b, __m512 c, int r)  VFNMSUBPS zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    def fused_multiply_subtract_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fnmsub_round_ss (__m128 a, __m128 b, __m128 c, int r)  VFNMSUBSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def fused_multiply_subtract_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fmsub_round_ss (__m128 a, __m128 b, __m128 c, int r)  VFMSUBSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def get_exponent(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_getexp_ps (__m512 a)  VGETEXPPS zmm1 {k1}{z}, zmm2/m512/m32bcst{sae}"""
        ...

    @staticmethod
    @overload
    def get_exponent_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_getexp_ss (__m128 a)  VGETEXPSS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}"""
        ...

    @staticmethod
    @overload
    def get_exponent_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_getexp_ss (__m128 a, __m128 b)  VGETEXPSS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    def get_mantissa(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_getmant_ps (__m512 a)  VGETMANTPS zmm1 {k1}{z}, zmm2/m512/m32bcst{sae}"""
        ...

    @staticmethod
    @overload
    def get_mantissa_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_getmant_ss (__m128 a)  VGETMANTSS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}"""
        ...

    @staticmethod
    @overload
    def get_mantissa_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_getmant_ss (__m128 a, __m128 b)  VGETMANTSS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_inserti128_si512 (__m512i a, __m128i b, const int imm8)  VINSERTI32x4 zmm1 {k1}{z}, zmm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_insertf32x4_ps (__m512 a, __m128 b, int imm8)  VINSERTF32x4 zmm1 {k1}{z}, zmm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    @overload
    def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector256[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_inserti256_si512 (__m512i a, __m256i b, const int imm8)  VINSERTI64x4 zmm1 {k1}{z}, zmm2, xmm3/m256, imm8"""
        ...

    @staticmethod
    @overload
    def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector256[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_insertf256_ps (__m512 a, __m256 b, int imm8)  VINSERTF64x4 zmm1 {k1}{z}, zmm2, xmm3/m256, imm8"""
        ...

    @staticmethod
    def load_aligned_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_load_si512 (__m512i const * mem_addr)  VMOVDQA32 zmm1 {k1}{z}, m512"""
        ...

    @staticmethod
    def load_aligned_vector_512_non_temporal(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_stream_load_si512 (__m512i const* mem_addr)  VMOVNTDQA zmm1, m512"""
        ...

    @staticmethod
    def load_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_loadu_si512 (__m512i const * mem_addr)  VMOVDQU32 zmm1 {k1}{z}, m512"""
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_max_epi32 (__m512i a, __m512i b)  VPMAXSD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_max_ps (__m512 a, __m512 b)  VMAXPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst{sae}"""
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_min_epi32 (__m512i a, __m512i b)  VPMINSD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_min_ps (__m512 a, __m512 b)  VMINPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst{sae}"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_mul_epi32 (__m512i a, __m512i b)  VPMULDQ zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_mul_ps (__m512 a, __m512 b)  VMULPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_mul_round_ps (__m512 a, __m512 b, int rounding)  VMULPS zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_mullo_epi32 (__m512i a, __m512i b)  VPMULLD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    def multiply_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_mul_round_ss (__m128 a, __m128 b, int rounding)  VMULSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def Or(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_or_si512 (__m512i a, __m512i b)  VPORD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    def permute_2x_64(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_permute_pd (__m512d a, int imm8)  VPERMILPD zmm1 {k1}{z}, zmm2/m512/m64bcst, imm8"""
        ...

    @staticmethod
    def permute_4x_32(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_permute_ps (__m512 a, int imm8)  VPERMILPS zmm1 {k1}{z}, zmm2/m512/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def permute_4x_64(value: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_permute4x64_epi64 (__m512i a, const int imm8)  VPERMQ zmm1 {k1}{z}, zmm2/m512/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def permute_4x_64(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_permute4x64_pd (__m512d a, const int imm8)  VPERMPD zmm1 {k1}{z}, zmm2/m512/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def permute_var_16x_32(left: System.Runtime.Intrinsics.Vector512[int], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_permutevar16x32_epi32 (__m512i a, __m512i b)  VPERMD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_16x_32(left: System.Runtime.Intrinsics.Vector512[float], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_permutevar16x32_ps (__m512 a, __m512i b)  VPERMPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_16x_32x_2(lower: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_permutex2var_epi32 (__m512i a, __m512i idx, __m512i b)  VPERMI2D zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst  VPERMT2D zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_16x_32x_2(lower: System.Runtime.Intrinsics.Vector512[float], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_permutex2var_ps (__m512 a, __m512i idx, __m512i b)  VPERMI2PS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst  VPERMT2PS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    def permute_var_2x_64(left: System.Runtime.Intrinsics.Vector512[float], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_permutevar_pd (__m512d a, __m512i b)  VPERMILPD zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst"""
        ...

    @staticmethod
    def permute_var_4x_32(left: System.Runtime.Intrinsics.Vector512[float], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_permutevar_ps (__m512 a, __m512i b)  VPERMILPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_8x_64(value: System.Runtime.Intrinsics.Vector512[int], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_permutevar8x64_epi64 (__m512i a, __m512i b)  VPERMQ zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_8x_64(value: System.Runtime.Intrinsics.Vector512[float], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_permutevar8x64_pd (__m512d a, __m512i b)  VPERMPD zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_8x_64x_2(lower: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_permutex2var_epi64 (__m512i a, __m512i idx, __m512i b)  VPERMI2Q zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst  VPERMT2Q zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_8x_64x_2(lower: System.Runtime.Intrinsics.Vector512[float], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_permutex2var_pd (__m512d a, __m512i idx, __m512i b)  VPERMI2PD zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst  VPERMT2PD zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst"""
        ...

    @staticmethod
    def reciprocal_14(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_rcp14_ps (__m512 a, __m512 b)  VRCP14PS zmm1 {k1}{z}, zmm2/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def reciprocal_14_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_rcp14_ss (__m128 a)  VRCP14SS xmm1 {k1}{z}, xmm2, xmm3/m32"""
        ...

    @staticmethod
    @overload
    def reciprocal_14_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_rcp14_ss (__m128 a, __m128 b)  VRCP14SS xmm1 {k1}{z}, xmm2, xmm3/m32The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    def reciprocal_sqrt_14(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_rsqrt14_ps (__m512 a, __m512 b)  VRSQRT14PS zmm1 {k1}{z}, zmm2/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_rsqrt14_ss (__m128 a)  VRSQRT14SS xmm1 {k1}{z}, xmm2, xmm3/m32"""
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_rsqrt14_ss (__m128 a, __m128 b)  VRSQRT14SS xmm1 {k1}{z}, xmm2, xmm3/m32The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    def rotate_left(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_rol_epi32 (__m512i a, int imm8)  VPROLD zmm1 {k1}{z}, zmm2/m512/m32bcst, imm8"""
        ...

    @staticmethod
    def rotate_left_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_rolv_epi32 (__m512i a, __m512i b)  VPROLDV zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    def rotate_right(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_ror_epi32 (__m512i a, int imm8)  VPRORD zmm1 {k1}{z}, zmm2/m512/m32bcst, imm8"""
        ...

    @staticmethod
    def rotate_right_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_rorv_epi32 (__m512i a, __m512i b)  VPRORDV zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    def round_scale(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_roundscale_ps (__m512 a, int imm)  VRNDSCALEPS zmm1 {k1}{z}, zmm2/m512/m32bcst{sae}, imm8"""
        ...

    @staticmethod
    @overload
    def round_scale_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_roundscale_ss (__m128 a, int imm)  VRNDSCALESS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}, imm8"""
        ...

    @staticmethod
    @overload
    def round_scale_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_roundscale_ss (__m128 a, __m128 b, int imm)  VRNDSCALESS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}, imm8The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def scale(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_scalef_ps (__m512 a, __m512 b)  VSCALEFPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def scale(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_scalef_round_ps (__m512 a, __m512 b, int rounding)  VSCALEFPS zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    @overload
    def scale_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_scalef_ss (__m128 a, __m128 b)  VSCALEFSS xmm1 {k1}{z}, xmm2, xmm3/m32{er}"""
        ...

    @staticmethod
    @overload
    def scale_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_scalef_round_ss (__m128 a, __m128 b)  VSCALEFSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_sll_epi32 (__m512i a, __m128i count)  VPSLLD zmm1 {k1}{z}, zmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_slli_epi32 (__m512i a, int imm8)  VPSLLD zmm1 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_sllv_epi32 (__m512i a, __m512i count)  VPSLLVD ymm1 {k1}{z}, ymm2, ymm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """_mm512_sra_epi32 (__m512i a, __m128i count)  VPSRAD zmm1 {k1}{z}, zmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_srai_epi32 (__m512i a, int imm8)  VPSRAD zmm1 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_srav_epi32 (__m512i a, __m512i count)  VPSRAVD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_srl_epi32 (__m512i a, __m128i count)  VPSRLD zmm1 {k1}{z}, zmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_srli_epi32 (__m512i a, int imm8)  VPSRLD zmm1 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_srlv_epi32 (__m512i a, __m512i count)  VPSRLVD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def shuffle(value: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_shuffle_epi32 (__m512i a, const int imm8)  VPSHUFD zmm1 {k1}{z}, zmm2/m512/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def shuffle(value: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_shuffle_ps (__m512 a, __m512 b, const int imm8)  VSHUFPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def shuffle_4x_128(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_shuffle_f64x2 (__m512d a, __m512d b, const int imm8)  VSHUFF64x2 zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def shuffle_4x_128(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_shuffle_i32x4 (__m512i a, __m512i b, const int imm8)  VSHUFI32x4 zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def sqrt(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_sqrt_ps (__m512 a)  VSQRTPS zmm1 {k1}{z}, zmm2/m512/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def sqrt(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_sqrt_round_ps (__m512 a, int rounding)  VSQRTPS zmm1, zmm2 {er}"""
        ...

    @staticmethod
    def sqrt_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_sqrt_round_ss (__m128 a, __m128 b, int rounding)  VSQRTSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        """void _mm512_storeu_si512 (__m512i * mem_addr, __m512i a)  VMOVDQU32 m512 {k1}{z}, zmm1"""
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[float]) -> None:
        """void _mm512_storeu_ps (float * mem_addr, __m512 a)  VMOVUPS m512 {k1}{z}, zmm1"""
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        """void _mm512_store_si512 (__m512i * mem_addr, __m512i a)  VMOVDQA32 m512 {k1}{z}, zmm1"""
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[float]) -> None:
        """void _mm512_store_ps (float * mem_addr, __m512 a)  VMOVAPS m512 {k1}{z}, zmm1"""
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        """void _mm512_stream_si512 (__m512i * mem_addr, __m512i a)  VMOVNTDQ m512, zmm1"""
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[float]) -> None:
        """void _mm512_stream_ps (float * mem_addr, __m512 a)  VMOVNTPS m512, zmm1"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_sub_epi32 (__m512i a, __m512i b)  VPSUBD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_sub_ps (__m512 a, __m512 b)  VSUBPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_sub_round_ps (__m512 a, __m512 b, int rounding)  VSUBPS zmm1, zmm2, zmm3 {er}"""
        ...

    @staticmethod
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_sub_round_ss (__m128 a, __m128 b, int rounding)  VSUBSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector512[int], b: System.Runtime.Intrinsics.Vector512[int], c: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_ternarylogic_si512 (__m512i a, __m512i b, __m512i c, int imm)  VPTERNLOGD zmm1 {k1}{z}, zmm2, zmm3/m512, imm8The above native signature does not exist. We provide this additional overload for consistency with the other bitwise APIs."""
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_ternarylogic_ps (__m512 a, __m512 b, __m512 c, int imm)  VPTERNLOGD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst, imm8The above native signature does not exist. We provide this additional overload for consistency with the other bitwise APIs."""
        ...

    @staticmethod
    @overload
    def unpack_high(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_unpackhi_epi32 (__m512i a, __m512i b)  VPUNPCKHDQ zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def unpack_high(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_unpackhi_ps (__m512 a, __m512 b)  VUNPCKHPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def unpack_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_unpacklo_epi32 (__m512i a, __m512i b)  VPUNPCKLDQ zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def unpack_low(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_unpacklo_ps (__m512 a, __m512 b)  VUNPCKLPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    def xor(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_xor_si512 (__m512i a, __m512i b)  VPXORD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...


class Avx512BW(System.Runtime.Intrinsics.X86.Avx512F, metaclass=abc.ABCMeta):
    """Provides access to X86 AVX512BW hardware instructions via intrinsics."""

    class VL(System.Runtime.Intrinsics.X86.Avx512F.VL, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX512BW+VL hardware instructions via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cmpgt_epu8 (__m128i a, __m128i b)  VPCMPUB k1 {k2}, xmm2, xmm3/m128, imm8(6)"""
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cmpgt_epu8 (__m256i a, __m256i b)  VPCMPUB k1 {k2}, ymm2, ymm3/m256, imm8(6)"""
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cmpge_epu8 (__m128i a, __m128i b)  VPCMPUB k1 {k2}, xmm2, xmm3/m128, imm8(5)"""
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cmpge_epu8 (__m256i a, __m256i b)  VPCMPUB k1 {k2}, ymm2, ymm3/m256, imm8(5)"""
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cmplt_epu8 (__m128i a, __m128i b)  VPCMPUB k1 {k2}, xmm2, xmm3/m128, imm8(1)"""
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cmplt_epu8 (__m256i a, __m256i b)  VPCMPUB k1 {k2}, ymm2, ymm3/m256, imm8(1)"""
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cmple_epu8 (__m128i a, __m128i b)  VPCMPUB k1 {k2}, xmm2, xmm3/m128, imm8(2)"""
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cmple_epu8 (__m256i a, __m256i b)  VPCMPUB k1 {k2}, ymm2, ymm3/m256, imm8(2)"""
            ...

        @staticmethod
        @overload
        def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cmpne_epu8 (__m128i a, __m128i b)  VPCMPUB k1 {k2}, xmm2, xmm3/m128, imm8(4)"""
            ...

        @staticmethod
        @overload
        def compare_not_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cmpne_epu8 (__m256i a, __m256i b)  VPCMPUB k1 {k2}, ymm2, ymm3/m256, imm8(4)"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtepi16_epi8 (__m128i a)  VPMOVWB xmm1/m64 {k1}{z}, xmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtepi16_epi8 (__m256i a)  VPMOVWB xmm1/m128 {k1}{z}, ymm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtusepi16_epi8 (__m128i a)  VPMOVUWB xmm1/m64 {k1}{z}, xmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtusepi16_epi8 (__m256i a)  VPMOVUWB xmm1/m128 {k1}{z}, ymm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtepi16_epi8 (__m128i a)  VPMOVWB xmm1/m64 {k1}{z}, zmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtepi16_epi8 (__m256i a)  VPMOVWB xmm1/m128 {k1}{z}, zmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtsepi16_epi8 (__m128i a)  VPMOVSWB xmm1/m64 {k1}{z}, zmm2"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm256_cvtsepi16_epi8 (__m256i a)  VPMOVSWB xmm1/m128 {k1}{z}, zmm2"""
            ...

        @staticmethod
        def permute_var_16x_16(left: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_permutevar16x16_epi16 (__m256i a, __m256i b)  VPERMW ymm1 {k1}{z}, ymm2, ymm3/m256"""
            ...

        @staticmethod
        def permute_var_16x_16x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_permutex2var_epi16 (__m256i a, __m256i idx, __m256i b)  VPERMI2W ymm1 {k1}{z}, ymm2, ymm3/m256  VPERMT2W ymm1 {k1}{z}, ymm2, ymm3/m256"""
            ...

        @staticmethod
        def permute_var_8x_16(left: System.Runtime.Intrinsics.Vector128[int], control: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_permutevar8x16_epi16 (__m128i a, __m128i b)  VPERMW xmm1 {k1}{z}, xmm2, xmm3/m128"""
            ...

        @staticmethod
        def permute_var_8x_16x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_permutex2var_epi16 (__m128i a, __m128i idx, __m128i b)  VPERMI2W xmm1 {k1}{z}, xmm2, xmm3/m128  VPERMT2W xmm1 {k1}{z}, xmm2, xmm3/m128"""
            ...

        @staticmethod
        @overload
        def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_sllv_epi16 (__m128i a, __m128i count)  VPSLLVW xmm1 {k1}{z}, xmm2, xmm3/m128"""
            ...

        @staticmethod
        @overload
        def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_sllv_epi16 (__m256i a, __m256i count)  VPSLLVW ymm1 {k1}{z}, ymm2, ymm3/m256"""
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_srav_epi16 (__m128i a, __m128i count)  VPSRAVW xmm1 {k1}{z}, xmm2, xmm3/m128"""
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_srav_epi16 (__m256i a, __m256i count)  VPSRAVW ymm1 {k1}{z}, ymm2, ymm3/m256"""
            ...

        @staticmethod
        @overload
        def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_srlv_epi16 (__m128i a, __m128i count)  VPSRLVW xmm1 {k1}{z}, xmm2, xmm3/m128"""
            ...

        @staticmethod
        @overload
        def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_srlv_epi16 (__m256i a, __m256i count)  VPSRLVW ymm1 {k1}{z}, ymm2, ymm3/m256"""
            ...

        @staticmethod
        @overload
        def sum_absolute_differences_in_block_32(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_dbsad_epu8 (__m128i a, __m128i b, int imm8)  VDBPSADBW xmm1 {k1}{z}, xmm2, xmm3/m128"""
            ...

        @staticmethod
        @overload
        def sum_absolute_differences_in_block_32(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_dbsad_epu8 (__m256i a, __m256i b, int imm8)  VDBPSADBW ymm1 {k1}{z}, ymm2, ymm3/m256"""
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx512F.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX512BW hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def abs(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_abs_epi8 (__m512i a)  VPABSB zmm1 {k1}{z}, zmm2/m512"""
        ...

    @staticmethod
    def add(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_add_epi8 (__m512i a, __m512i b)  VPADDB zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def add_saturate(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_adds_epi8 (__m512i a, __m512i b)  VPADDSB zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def align_right(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_alignr_epi8 (__m512i a, __m512i b, const int count)  VPALIGNR zmm1 {k1}{z}, zmm2, zmm3/m512, imm8"""
        ...

    @staticmethod
    def average(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_avg_epu8 (__m512i a, __m512i b)  VPAVGB zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def blend_variable(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_blendv_epu8 (__m512i a, __m512i b, __m512i mask)  VPBLENDMB zmm1 {k1}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def broadcast_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_broadcastb_epi8 (__m128i a)  VPBROADCASTB zmm1 {k1}{z}, xmm2/m8"""
        ...

    @staticmethod
    def compare_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmpeq_epu8 (__m512i a, __m512i b)  VPCMPEQB k1 {k2}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmpgt_epu8 (__m512i a, __m512i b)  VPCMPUB k1 {k2}, zmm2, zmm3/m512, imm8(6)"""
        ...

    @staticmethod
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmpge_epu8 (__m512i a, __m512i b)  VPCMPUB k1 {k2}, zmm2, zmm3/m512, imm8(5)"""
        ...

    @staticmethod
    def compare_less_than(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmplt_epu8 (__m512i a, __m512i b)  VPCMPUB k1 {k2}, zmm2, zmm3/m512, imm8(1)"""
        ...

    @staticmethod
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmple_epu8 (__m512i a, __m512i b)  VPCMPUB k1 {k2}, zmm2, zmm3/m512, imm8(2)"""
        ...

    @staticmethod
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cmpne_epu8 (__m512i a, __m512i b)  VPCMPUB k1 {k2}, zmm2, zmm3/m512, imm8(4)"""
        ...

    @staticmethod
    def convert_to_vector_256_byte(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtepi16_epi8 (__m512i a)  VPMOVWB ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_256_byte_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtusepi16_epi8 (__m512i a)  VPMOVUWB ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_256_s_byte(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtepi16_epi8 (__m512i a)  VPMOVWB ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_256_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_cvtsepi16_epi8 (__m512i a)  VPMOVSWB ymm1/m256 {k1}{z}, zmm2"""
        ...

    @staticmethod
    def convert_to_vector_512_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtepi8_epi16 (__m128i a)  VPMOVSXBW zmm1 {k1}{z}, ymm2/m256"""
        ...

    @staticmethod
    def convert_to_vector_512_u_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtepi8_epi16 (__m128i a)  VPMOVSXBW zmm1 {k1}{z}, ymm2/m256"""
        ...

    @staticmethod
    def load_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_loadu_epi8 (__m512i const * mem_addr)  VMOVDQU8 zmm1 {k1}{z}, m512"""
        ...

    @staticmethod
    def max(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_max_epi8 (__m512i a, __m512i b)  VPMAXSB zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def min(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_min_epi8 (__m512i a, __m512i b)  VPMINSB zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def multiply_add_adjacent(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_madd_epi16 (__m512i a, __m512i b)  VPMADDWD zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def multiply_high(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_mulhi_epi16 (__m512i a, __m512i b)  VPMULHW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def multiply_high_round_scale(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_mulhrs_epi16 (__m512i a, __m512i b)  VPMULHRSW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_mullo_epi16 (__m512i a, __m512i b)  VPMULLW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def pack_signed_saturate(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_packs_epi16 (__m512i a, __m512i b)  VPACKSSWB zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def pack_unsigned_saturate(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_packus_epi16 (__m512i a, __m512i b)  VPACKUSWB zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def permute_var_32x_16(left: System.Runtime.Intrinsics.Vector512[int], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_permutevar32x16_epi16 (__m512i a, __m512i b)  VPERMW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def permute_var_32x_16x_2(lower: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_permutex2var_epi16 (__m512i a, __m512i idx, __m512i b)  VPERMI2W zmm1 {k1}{z}, zmm2, zmm3/m512  VPERMT2W zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_sll_epi16 (__m512i a, __m128i count)  VPSLLW zmm1 {k1}{z}, zmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_slli_epi16 (__m512i a, int imm8)  VPSLLW zmm1 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    def shift_left_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector512[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_bslli_epi128 (__m512i a, const int imm8)  VPSLLDQ zmm1, zmm2/m512, imm8"""
        ...

    @staticmethod
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_sllv_epi16 (__m512i a, __m512i count)  VPSLLVW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """_mm512_sra_epi16 (__m512i a, __m128i count)  VPSRAW zmm1 {k1}{z}, zmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_srai_epi16 (__m512i a, int imm8)  VPSRAW zmm1 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_srav_epi16 (__m512i a, __m512i count)  VPSRAVW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_srl_epi16 (__m512i a, __m128i count)  VPSRLW zmm1 {k1}{z}, zmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_srli_epi16 (__m512i a, int imm8)  VPSRLW zmm1 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    def shift_right_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector512[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_bsrli_epi128 (__m512i a, const int imm8)  VPSRLDQ zmm1, zmm2/m128, imm8"""
        ...

    @staticmethod
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_srlv_epi16 (__m512i a, __m512i count)  VPSRLVW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def shuffle(value: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_shuffle_epi8 (__m512i a, __m512i b)  VPSHUFB zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def shuffle_high(value: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_shufflehi_epi16 (__m512i a, const int imm8)  VPSHUFHW zmm1 {k1}{z}, zmm2/m512, imm8"""
        ...

    @staticmethod
    def shuffle_low(value: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_shufflelo_epi16 (__m512i a, const int imm8)  VPSHUFLW zmm1 {k1}{z}, zmm2/m512, imm8"""
        ...

    @staticmethod
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        """void _mm512_storeu_epi8 (__m512i * mem_addr, __m512i a)  VMOVDQU8 m512 {k1}{z}, zmm1"""
        ...

    @staticmethod
    def subtract(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_sub_epi8 (__m512i a, __m512i b)  VPSUBB zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_subs_epi8 (__m512i a, __m512i b)  VPSUBSB zmm1 {k1}{z}, zmm2, zmm3/m128"""
        ...

    @staticmethod
    def sum_absolute_differences(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_sad_epu8 (__m512i a, __m512i b)  VPSADBW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def sum_absolute_differences_in_block_32(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_dbsad_epu8 (__m512i a, __m512i b)  VDBPSADBW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def unpack_high(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_unpackhi_epi8 (__m512i a, __m512i b)  VPUNPCKHBW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def unpack_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_unpacklo_epi8 (__m512i a, __m512i b)  VPUNPCKLBW zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...


class Avx512Vbmi(System.Runtime.Intrinsics.X86.Avx512BW, metaclass=abc.ABCMeta):
    """Provides access to X86 AVX512VBMI hardware instructions via intrinsics"""

    class VL(System.Runtime.Intrinsics.X86.Avx512BW.VL, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX512VBMI+VL hardware instructions via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        @overload
        def multi_shift(control: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_multishift_epi64_epi8(__m128i a, __m128i b)  VPMULTISHIFTQB xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
            ...

        @staticmethod
        @overload
        def multi_shift(control: System.Runtime.Intrinsics.Vector256[int], value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_multishift_epi64_epi8(__m256i a, __m256i b)  VPMULTISHIFTQB ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
            ...

        @staticmethod
        def permute_var_16x_8(left: System.Runtime.Intrinsics.Vector128[int], control: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_permutevar64x8_epi8 (__m128i a, __m128i b)  VPERMB xmm1 {k1}{z}, xmm2, xmm3/m128"""
            ...

        @staticmethod
        def permute_var_16x_8x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_permutex2var_epi8 (__m128i a, __m128i idx, __m128i b)  VPERMI2B xmm1 {k1}{z}, xmm2, xmm3/m128  VPERMT2B xmm1 {k1}{z}, xmm2, xmm3/m128"""
            ...

        @staticmethod
        def permute_var_32x_8(left: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_permutevar64x8_epi8 (__m256i a, __m256i b)  VPERMB ymm1 {k1}{z}, ymm2, ymm3/m256"""
            ...

        @staticmethod
        def permute_var_32x_8x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_permutex2var_epi8 (__m256i a, __m256i idx, __m256i b)  VPERMI2B ymm1 {k1}{z}, ymm2, ymm3/m256  VPERMT2B ymm1 {k1}{z}, ymm2, ymm3/m256"""
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx512BW.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX512VBMI hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def multi_shift(control: System.Runtime.Intrinsics.Vector512[int], value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_multishift_epi64_epi8(__m512i a, __m512i b)  VPMULTISHIFTQB zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst"""
        ...

    @staticmethod
    def permute_var_64x_8(left: System.Runtime.Intrinsics.Vector512[int], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_permutevar64x8_epi8 (__m512i a, __m512i b)  VPERMB zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...

    @staticmethod
    def permute_var_64x_8x_2(lower: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_permutex2var_epi8 (__m512i a, __m512i idx, __m512i b)  VPERMI2B zmm1 {k1}{z}, zmm2, zmm3/m512  VPERMT2B zmm1 {k1}{z}, zmm2, zmm3/m512"""
        ...


class Aes(System.Runtime.Intrinsics.X86.Sse2, metaclass=abc.ABCMeta):
    """Provides access to X86 AES hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Sse2.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AES hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def decrypt(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_aesdec_si128 (__m128i a, __m128i RoundKey)   AESDEC xmm1,       xmm2/m128  VAESDEC xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def decrypt_last(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_aesdeclast_si128 (__m128i a, __m128i RoundKey)   AESDECLAST xmm1,       xmm2/m128  VAESDECLAST xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def encrypt(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_aesenc_si128 (__m128i a, __m128i RoundKey)   AESENC xmm1,       xmm2/m128  VAESENC xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def encrypt_last(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_aesenclast_si128 (__m128i a, __m128i RoundKey)   AESENCLAST xmm1,       xmm2/m128  VAESENCLAST xmm1, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def inverse_mix_columns(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_aesimc_si128 (__m128i a)   AESIMC xmm1, xmm2/m128  VAESIMC xmm1, xmm2/m128"""
        ...

    @staticmethod
    def keygen_assist(value: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_aeskeygenassist_si128 (__m128i a, const int imm8)   AESKEYGENASSIST xmm1, xmm2/m128, imm8  VAESKEYGENASSIST xmm1, xmm2/m128, imm8"""
        ...


class Gfni(System.Runtime.Intrinsics.X86.Sse41, metaclass=abc.ABCMeta):
    """Provides access to X86 GFNI hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Sse41.X64, metaclass=abc.ABCMeta):
        """Provides access to the X86 GFNI hardware instructions that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    class V256(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def galois_field_affine_transform(x: System.Runtime.Intrinsics.Vector256[int], a: System.Runtime.Intrinsics.Vector256[int], b: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_gf2p8affine_epi64_epi8 (__m256i x, __m256i A, int b)   GF2P8AFFINEQB ymm1, ymm2/m256, imm8  VGF2P8AFFINEQB ymm1, ymm2, ymm3/m256, imm8  VGF2P8AFFINEQB ymm1{k1}{z}, ymm2, ymm3/m256/m64bcst, imm8"""
            ...

        @staticmethod
        def galois_field_affine_transform_inverse(x: System.Runtime.Intrinsics.Vector256[int], a: System.Runtime.Intrinsics.Vector256[int], b: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_gf2p8affineinv_epi64_epi8 (__m256i x, __m256i A, int b)   GF2P8AFFINEINVQB ymm1, ymm2/m256, imm8  VGF2P8AFFINEINVQB ymm1, ymm2, ymm3/m256, imm8  VGF2P8AFFINEINVQB ymm1{k1}{z}, ymm2, ymm3/m256/m64bcst, imm8"""
            ...

        @staticmethod
        def galois_field_multiply(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_gf2p8mul_epi8 (__m256i a, __m256i b)   GF2P8MULB ymm1, ymm2/m256  VGF2P8MULB ymm1, ymm2, ymm3/m256  VGF2P8MULB ymm1{k1}{z}, ymm2, ymm3/m256"""
            ...

    class V512(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def galois_field_affine_transform(x: System.Runtime.Intrinsics.Vector512[int], a: System.Runtime.Intrinsics.Vector512[int], b: int) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_gf2p8affine_epi64_epi8 (__m512i x, __m512i A, int b)   GF2P8AFFINEQB zmm1, zmm2/m512, imm8  VGF2P8AFFINEQB zmm1, zmm2, zmm3/m512, imm8  VGF2P8AFFINEQB zmm1{k1}{z}, zmm2, zmm3/m512/m64bcst, imm8"""
            ...

        @staticmethod
        def galois_field_affine_transform_inverse(x: System.Runtime.Intrinsics.Vector512[int], a: System.Runtime.Intrinsics.Vector512[int], b: int) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_gf2p8affineinv_epi64_epi8 (__m512i x, __m512i A, int b)   GF2P8AFFINEINVQB zmm1, zmm2/m512, imm8  VGF2P8AFFINEINVQB zmm1, zmm2, zmm3/m512, imm8  VGF2P8AFFINEINVQB zmm1{k1}{z}, zmm2, zmm3/m512/m64bcst, imm8"""
            ...

        @staticmethod
        def galois_field_multiply(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_gf2p8mul_epi8 (__m512i a, __m512i b)   GF2P8MULB zmm1, zmm2/m512  VGF2P8MULB zmm1, zmm2, zmm3/m512  VGF2P8MULB zmm1{k1}{z}, zmm2, zmm3/m512"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def galois_field_affine_transform(x: System.Runtime.Intrinsics.Vector128[int], a: System.Runtime.Intrinsics.Vector128[int], b: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_gf2p8affine_epi64_epi8 (__m128i x, __m128i A, int b)   GF2P8AFFINEQB xmm1, xmm2/m128, imm8  VGF2P8AFFINEQB xmm1, xmm2, xmm3/m128, imm8  VGF2P8AFFINEQB xmm1{k1}{z}, xmm2, xmm3/m128/m64bcst, imm8"""
        ...

    @staticmethod
    def galois_field_affine_transform_inverse(x: System.Runtime.Intrinsics.Vector128[int], a: System.Runtime.Intrinsics.Vector128[int], b: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_gf2p8affineinv_epi64_epi8 (__m128i x, __m128i A, int b)   GF2P8AFFINEINVQB xmm1, xmm2/m128, imm8  VGF2P8AFFINEINVQB xmm1, xmm2, xmm3/m128, imm8  VGF2P8AFFINEINVQB xmm1{k1}{z}, xmm2, xmm3/m128/m64bcst, imm8"""
        ...

    @staticmethod
    def galois_field_multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_gf2p8mul_epi8 (__m128i a, __m128i b)   GF2P8MULB xmm1, xmm2/m128  VGF2P8MULB xmm1, xmm2, xmm3/m128  VGF2P8MULB xmm1{k1}{z}, xmm2, xmm3/m128"""
        ...


class Fma(System.Runtime.Intrinsics.X86.Avx, metaclass=abc.ABCMeta):
    """Provides access to X86 FMA hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Avx.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 FMA hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def multiply_add(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fmadd_ps (__m128 a, __m128 b, __m128 c)  VFMADDPS xmm1,         xmm2, xmm3/m128  VFMADDPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def multiply_add(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_fmadd_ps (__m256 a, __m256 b, __m256 c)  VFMADDPS ymm1,         ymm2, ymm3/m256  VFMADDPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def multiply_add_negated(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fnmadd_ps (__m128 a, __m128 b, __m128 c)  VFNMADDPS xmm1,         xmm2, xmm3/m128  VFNMADDPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def multiply_add_negated(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_fnmadd_ps (__m256 a, __m256 b, __m256 c)  VFNMADDPS ymm1,         ymm2, ymm3/m256  VFNMADDPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def multiply_add_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fnmadd_ss (__m128 a, __m128 b, __m128 c)  VFNMADDSS xmm1,         xmm2, xmm3/m32  VFNMADDSS xmm1 {k1}{z}, xmm2, xmm3/m32{er}"""
        ...

    @staticmethod
    def multiply_add_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fmadd_ss (__m128 a, __m128 b, __m128 c)  VFMADDSS xmm1,         xmm2, xmm3/m32  VFMADDSS xmm1 {k1}{z}, xmm2, xmm3/m32{er}"""
        ...

    @staticmethod
    @overload
    def multiply_add_subtract(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fmaddsub_ps (__m128 a, __m128 b, __m128 c)  VFMADDSUBPS xmm1,         xmm2, xmm3/m128  VFMADDSUBPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def multiply_add_subtract(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_fmaddsub_ps (__m256 a, __m256 b, __m256 c)  VFMADDSUBPS ymm1,         ymm2, ymm3/m256  VFMADDSUBPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def multiply_subtract(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fmsub_ps (__m128 a, __m128 b, __m128 c)  VFMSUBPS xmm1,         xmm2, xmm3/m128  VFMSUBPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def multiply_subtract(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_fmsub_ps (__m256 a, __m256 b, __m256 c)  VFMSUBPS ymm1,         ymm2, ymm3/m256  VFMSUBPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def multiply_subtract_add(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fmsubadd_ps (__m128 a, __m128 b, __m128 c)  VFMSUBADDPS xmm1,         xmm2, xmm3/m128  VFMSUBADDPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def multiply_subtract_add(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_fmsubadd_ps (__m256 a, __m256 b, __m256 c)  VFMSUBADDPS ymm1,         ymm2, ymm3/m256  VFMSUBADDPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def multiply_subtract_negated(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fnmsub_ps (__m128 a, __m128 b, __m128 c)  VFNMSUBPS xmm1,         xmm2, xmm3/m128  VFNMSUBPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def multiply_subtract_negated(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_fnmsub_ps (__m256 a, __m256 b, __m256 c)  VFNMSUBPS ymm1,         ymm2, ymm3/m256  VFNMSUBPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    def multiply_subtract_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fnmsub_ss (__m128 a, __m128 b, __m128 c)  VFNMSUBSS xmm1,         xmm2, xmm3/m32  VFNMSUBSS xmm1 {k1}{z}, xmm2, xmm3/m32{er}"""
        ...

    @staticmethod
    def multiply_subtract_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_fmsub_ss (__m128 a, __m128 b, __m128 c)  VFMSUBSS xmm1,         xmm2, xmm3/m32  VFMSUBSS xmm1 {k1}{z}, xmm2, xmm3/m32{er}"""
        ...


class Popcnt(System.Runtime.Intrinsics.X86.Sse42, metaclass=abc.ABCMeta):
    """Provides access to X86 POPCNT hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Sse42.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 POPCNT hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def pop_count(value: int) -> int:
            """__int64 _mm_popcnt_u64 (unsigned __int64 a)  POPCNT r64, r/m64This intrinsic is only available on 64-bit processes"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def pop_count(value: int) -> int:
        """int _mm_popcnt_u32 (unsigned int a)  POPCNT r32, r/m32"""
        ...


class Avx512CD(System.Runtime.Intrinsics.X86.Avx512F, metaclass=abc.ABCMeta):
    """Provides access to X86 AVX512CD hardware instructions via intrinsics."""

    class VL(System.Runtime.Intrinsics.X86.Avx512F.VL, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX512CD+VL hardware instructions via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        @overload
        def detect_conflicts(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_conflict_epi32 (__m128i a)  VPCONFLICTD xmm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def detect_conflicts(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_conflict_epi32 (__m256i a)  VPCONFLICTD ymm1 {k1}{z}, ymm2/m256/m32bcst"""
            ...

        @staticmethod
        @overload
        def leading_zero_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_lzcnt_epi32 (__m128i a)  VPLZCNTD xmm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def leading_zero_count(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_lzcnt_epi32 (__m256i a)  VPLZCNTD ymm1 {k1}{z}, ymm2/m256/m32bcst"""
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx512F.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX512CD hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def detect_conflicts(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_conflict_epi32 (__m512i a)  VPCONFLICTD zmm1 {k1}{z}, zmm2/m512/m32bcst"""
        ...

    @staticmethod
    def leading_zero_count(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_lzcnt_epi32 (__m512i a)  VPLZCNTD zmm1 {k1}{z}, zmm2/m512/m32bcst"""
        ...


class Bmi2(System.Runtime.Intrinsics.X86.X86Base, metaclass=abc.ABCMeta):
    """Provides access to X86 BMI2 hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.X86Base.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 BMI2 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        @overload
        def multiply_no_flags(left: int, right: int, low: typing.Any) -> int:
            """unsigned __int64 _mulx_u64 (unsigned __int64 a, unsigned __int64 b, unsigned __int64* hi)  MULX r64a, r64b, r/m64The above native signature does not directly correspond to the managed signature.This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def multiply_no_flags(left: int, right: int) -> int:
            """unsigned __int64 _mulx_u64 (unsigned __int64 a, unsigned __int64 b, unsigned __int64* hi)  MULX r64a, r64b, r/m64The above native signature does not directly correspond to the managed signature.This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def parallel_bit_deposit(value: int, mask: int) -> int:
            """unsigned __int64 _pdep_u64 (unsigned __int64 a, unsigned __int64 mask)  PDEP r64a, r64b, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def parallel_bit_extract(value: int, mask: int) -> int:
            """unsigned __int64 _pext_u64 (unsigned __int64 a, unsigned __int64 mask)  PEXT r64a, r64b, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def zero_high_bits(value: int, index: int) -> int:
            """unsigned __int64 _bzhi_u64 (unsigned __int64 a, unsigned int index)  BZHI r64a, r/m64, r64bThis intrinsic is only available on 64-bit processes"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    @overload
    def multiply_no_flags(left: int, right: int, low: typing.Any) -> int:
        """unsigned int _mulx_u32 (unsigned int a, unsigned int b, unsigned int* hi)  MULX r32a, r32b, r/m32The above native signature does not directly correspond to the managed signature."""
        ...

    @staticmethod
    @overload
    def multiply_no_flags(left: int, right: int) -> int:
        """unsigned int _mulx_u32 (unsigned int a, unsigned int b, unsigned int* hi)  MULX r32a, r32b, r/m32The above native signature does not directly correspond to the managed signature."""
        ...

    @staticmethod
    def parallel_bit_deposit(value: int, mask: int) -> int:
        """unsigned int _pdep_u32 (unsigned int a, unsigned int mask)  PDEP r32a, r32b, r/m32"""
        ...

    @staticmethod
    def parallel_bit_extract(value: int, mask: int) -> int:
        """unsigned int _pext_u32 (unsigned int a, unsigned int mask)  PEXT r32a, r32b, r/m32"""
        ...

    @staticmethod
    def zero_high_bits(value: int, index: int) -> int:
        """unsigned int _bzhi_u32 (unsigned int a, unsigned int index)  BZHI r32a, r/m32, r32b"""
        ...


class Avx10v1(System.Runtime.Intrinsics.X86.Avx2, metaclass=abc.ABCMeta):
    """Provides access to X86 AVX10.1 hardware instructions via intrinsics"""

    class X64(System.Runtime.Intrinsics.X86.Avx2.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX10.1 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128d _mm_cvt_roundsi64_sd (__m128d a, __int64 b, int rounding)  VCVTSI2SD xmm1, xmm2, r64 {er}This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128d _mm_cvtsi64_sd (__m128d a, __int64 b)  VCVTUSI2SD xmm1, xmm2, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_cvt_roundi64_ss (__m128 a, __int64 b, int rounding)  VCVTSI2SS xmm1, xmm2, r64 {er}This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_cvtsi64_ss (__m128 a, __int64 b)  VCVTUSI2SS xmm1, xmm2, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def convert_to_int_64(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
            """__int64 _mm_cvt_roundss_i64 (__m128 a, int rounding)  VCVTSS2SI r64, xmm1 {er}This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_to_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            """unsigned __int64 _mm_cvtss_u64 (__m128 a)  VCVTSS2USI r64, xmm1/m32{er}This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def convert_to_u_int_64(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
            """unsigned __int64 _mm_cvt_roundss_u64 (__m128 a, int rounding)  VCVTSS2USI r64, xmm1 {er}This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def convert_to_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            """unsigned __int64 _mm_cvttss_u64 (__m128 a)  VCVTTSS2USI r64, xmm1/m32{er}This intrinsic is only available on 64-bit processes"""
            ...

    class V512(System.Runtime.Intrinsics.X86.Avx512BW, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX10.1/512 hardware instructions via intrinsics."""

        class X64(System.Runtime.Intrinsics.X86.Avx512BW.X64, metaclass=abc.ABCMeta):
            """Provides access to the x86 AVX10.1/512 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

            IS_SUPPORTED: bool
            """Gets a value that indicates whether the APIs in this class are supported."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def And(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512 _mm512_and_ps (__m512 a, __m512 b)  VANDPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
            ...

        @staticmethod
        def and_not(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512 _mm512_andnot_ps (__m512 a, __m512 b)  VANDNPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
            ...

        @staticmethod
        @overload
        def broadcast_pair_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_broadcast_i32x2 (__m128i a)  VBROADCASTI32x2 zmm1 {k1}{z}, xmm2/m64"""
            ...

        @staticmethod
        @overload
        def broadcast_pair_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512 _mm512_broadcast_f32x2 (__m128 a)  VBROADCASTF32x2 zmm1 {k1}{z}, xmm2/m64"""
            ...

        @staticmethod
        def broadcast_vector_128_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_broadcast_i64x2 (__m128i const * mem_addr)  VBROADCASTI64x2 zmm1 {k1}{z}, m128"""
            ...

        @staticmethod
        def broadcast_vector_256_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_broadcast_i32x8 (__m256i const * mem_addr)  VBROADCASTI32x8 zmm1 {k1}{z}, m256"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m512 _mm512_cvtepi64_ps (__m512i a)  VCVTQQ2PS ymm1 {k1}{z}, zmm2/m512/m64bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[int], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm512_cvt_roundepi64_ps (__m512i a, int r)  VCVTQQ2PS ymm1, zmm2 {er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512d _mm512_cvtepi64_pd (__m512i a)  VCVTQQ2PD zmm1 {k1}{z}, zmm2/m512/m64bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector512[int], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512d _mm512_cvt_roundepi64_pd (__m512i a, int r)  VCVTQQ2PD zmm1, zmm2 {er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvtps_epi64 (__m512 a)  VCVTPS2QQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvtpd_epi64 (__m512d a)  VCVTPD2QQ zmm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvt_roundps_epi64 (__m512 a, int r)  VCVTPS2QQ zmm1, ymm2 {er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvt_roundpd_epi64 (__m512d a, int r)  VCVTPD2QQ zmm1, zmm2 {er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvttps_epi64 (__m512 a)  VCVTTPS2QQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvttpd_epi64 (__m512 a)  VCVTTPD2QQ zmm1 {k1}{z}, zmm2/m512/m64bcst{sae}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvtps_epu64 (__m512 a)  VCVTPS2UQQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvtpd_epu64 (__m512d a)  VCVTPD2UQQ zmm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvt_roundps_epu64 (__m512 a, int r)  VCVTPS2UQQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvt_roundpd_epu64 (__m512d a, int r)  VCVTPD2UQQ zmm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvttps_epu64 (__m512 a)  VCVTTPS2UQQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_cvttpd_epu64 (__m512d a)  VCVTTPD2UQQ zmm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
            ...

        @staticmethod
        def detect_conflicts(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_conflict_epi32 (__m512i a)  VPCONFLICTD zmm1 {k1}{z}, zmm2/m512/m32bcst"""
            ...

        @staticmethod
        @overload
        def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm512_extracti64x2_epi64 (__m512i a, const int imm8)  VEXTRACTI64x2 xmm1/m128 {k1}{z}, zmm2, imm8"""
            ...

        @staticmethod
        @overload
        def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128d _mm512_extractf64x2_pd (__m512d a, const int imm8)  VEXTRACTF64x2 xmm1/m128 {k1}{z}, zmm2, imm8"""
            ...

        @staticmethod
        @overload
        def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm512_extracti32x8_epi32 (__m512i a, const int imm8)  VEXTRACTI32x8 ymm1/m256 {k1}{z}, zmm2, imm8"""
            ...

        @staticmethod
        @overload
        def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm512_extractf32x8_ps (__m512 a, const int imm8)  VEXTRACTF32x8 ymm1/m256 {k1}{z}, zmm2, imm8"""
            ...

        @staticmethod
        @overload
        def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_inserti64x2_si512 (__m512i a, __m128i b, const int imm8)  VINSERTI64x2 zmm1 {k1}{z}, zmm2, xmm3/m128, imm8"""
            ...

        @staticmethod
        @overload
        def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512d _mm512_insertf64x2_pd (__m512d a, __m128d b, int imm8)  VINSERTF64x2 zmm1 {k1}{z}, zmm2, xmm3/m128, imm8"""
            ...

        @staticmethod
        @overload
        def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector256[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_inserti32x8_si512 (__m512i a, __m256i b, const int imm8)  VINSERTI32x8 zmm1 {k1}{z}, zmm2, xmm3/m256, imm8"""
            ...

        @staticmethod
        @overload
        def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector256[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512 _mm512_insertf32x8_ps (__m512 a, __m256 b, int imm8)  VINSERTF32x8 zmm1 {k1}{z}, zmm2, xmm3/m256, imm8"""
            ...

        @staticmethod
        def leading_zero_count(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_lzcnt_epi32 (__m512i a)  VPLZCNTD zmm1 {k1}{z}, zmm2/m512/m32bcst"""
            ...

        @staticmethod
        def multiply_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_mullo_epi64 (__m512i a, __m512i b)  VPMULLQ zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst"""
            ...

        @staticmethod
        def multi_shift(control: System.Runtime.Intrinsics.Vector512[int], value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_multishift_epi64_epi8( __m512i a, __m512i b)  VPMULTISHIFTQB zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst"""
            ...

        @staticmethod
        def Or(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512 _mm512_or_ps (__m512 a, __m512 b)  VORPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
            ...

        @staticmethod
        def permute_var_64x_8(left: System.Runtime.Intrinsics.Vector512[int], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_permutevar64x8_epi8 (__m512i a, __m512i b)  VPERMB zmm1 {k1}{z}, zmm2, zmm3/m512"""
            ...

        @staticmethod
        def permute_var_64x_8x_2(lower: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            """__m512i _mm512_permutex2var_epi8 (__m512i a, __m512i idx, __m512i b)  VPERMI2B zmm1 {k1}{z}, zmm2, zmm3/m512  VPERMT2B zmm1 {k1}{z}, zmm2, zmm3/m512"""
            ...

        @staticmethod
        def range(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512 _mm512_range_ps(__m512 a, __m512 b, int imm);  VRANGEPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst{sae}, imm8"""
            ...

        @staticmethod
        def reduce(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512 _mm512_reduce_ps(__m512 a, int imm);  VREDUCEPS zmm1 {k1}{z}, zmm2/m512/m32bcst{sae}, imm8"""
            ...

        @staticmethod
        def xor(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
            """__m512 _mm512_xor_ps (__m512 a, __m512 b)  VXORPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_abs_epi64 (__m128i a)  VPABSQ xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_abs_epi64 (__m128i a)  VPABSQ ymm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    def add_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_add_round_sd (__m128d a, __m128d b, int rounding)  VADDSD xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    @overload
    def align_right_32(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_alignr_epi32 (__m128i a, __m128i b, const int count)  VALIGND xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def align_right_32(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_alignr_epi32 (__m256i a, __m256i b, const int count)  VALIGND ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def align_right_64(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_alignr_epi64 (__m128i a, __m128i b, const int count)  VALIGNQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def align_right_64(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_alignr_epi64 (__m256i a, __m256i b, const int count)  VALIGNQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst, imm8"""
        ...

    @staticmethod
    def broadcast_pair_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_broadcast_i32x2 (__m128i a)  VBROADCASTI32x2 xmm1 {k1}{z}, xmm2/m64"""
        ...

    @staticmethod
    @overload
    def broadcast_pair_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_broadcast_f32x2 (__m128 a)  VBROADCASTF32x2 ymm1 {k1}{z}, xmm2/m64"""
        ...

    @staticmethod
    @overload
    def broadcast_pair_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_broadcast_i32x2 (__m128i a)  VBROADCASTI32x2 ymm1 {k1}{z}, xmm2/m64"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cmpgt_epu8 (__m128i a, __m128i b)  VPCMPUB k1 {k2}, xmm2, xmm3/m128, imm8(6)"""
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cmpgt_epu8 (__m256i a, __m256i b)  VPCMPUB k1 {k2}, ymm2, ymm3/m256, imm8(6)"""
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cmpge_epu8 (__m128i a, __m128i b)  VPCMPUB k1 {k2}, xmm2, xmm3/m128, imm8(5)"""
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cmpge_epu8 (__m256i a, __m256i b)  VPCMPUB k1 {k2}, ymm2, ymm3/m256, imm8(5)"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cmplt_epi32 (__m128i a, __m128i b)  VPCMPD k1 {k2}, xmm2, xmm3/m128/m32bcst, imm8(1)"""
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cmplt_epu8 (__m256i a, __m256i b)  VPCMPUB k1 {k2}, ymm2, ymm3/m256, imm8(1)"""
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cmple_epu8 (__m128i a, __m128i b)  VPCMPUB k1 {k2}, xmm2, xmm3/m128, imm8(2)"""
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cmple_epu8 (__m256i a, __m256i b)  VPCMPUB k1 {k2}, ymm2, ymm3/m256, imm8(2)"""
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cmpne_epu8 (__m128i a, __m128i b)  VPCMPUB k1 {k2}, xmm2, xmm3/m128, imm8(4)"""
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cmpne_epu8 (__m256i a, __m256i b)  VPCMPUB k1 {k2}, ymm2, ymm3/m256, imm8(4)"""
        ...

    @staticmethod
    def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cvtsi32_sd (__m128d a, int b)  VCVTUSI2SD xmm1, xmm2, r/m32"""
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvt_roundi32_ss (__m128 a, int b, int rounding)VCVTSI2SS xmm1, xmm2, r32 {er}"""
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvtsi32_ss (__m128 a, int b)  VCVTUSI2SS xmm1, xmm2, r/m32"""
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvt_roundsd_ss (__m128 a, __m128d b, int rounding)VCVTSD2SS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
        """int _mm_cvt_roundsd_i32 (__m128d a, int rounding)  VCVTSD2SI r32, xmm1 {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
        """unsigned int _mm_cvt_roundsd_u32 (__m128d a, int rounding)  VCVTSD2USI r32, xmm1 {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        """unsigned int _mm_cvtsd_u32 (__m128d a)  VCVTSD2USI r32, xmm1/m64{er}"""
        ...

    @staticmethod
    def convert_to_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        """unsigned int _mm_cvttsd_u32 (__m128d a)  VCVTTSD2USI r32, xmm1/m64{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtepi32_epi8 (__m128i a)  VPMOVDB xmm1/m32 {k1}{z}, xmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtepi32_epi8 (__m256i a)  VPMOVDB xmm1/m64 {k1}{z}, ymm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtusepi32_epi8 (__m128i a)  VPMOVUSDB xmm1/m32 {k1}{z}, xmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtusepi32_epi8 (__m256i a)  VPMOVUSDB xmm1/m64 {k1}{z}, ymm2"""
        ...

    @staticmethod
    def convert_to_vector_128_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_cvtepi64_pd (__m128i a)  VCVTQQ2PD xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtepi32_epi16 (__m128i a)  VPMOVDW xmm1/m64 {k1}{z}, zmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtepi32_epi16 (__m256i a)  VPMOVDW xmm1/m128 {k1}{z}, zmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtsepi32_epi16 (__m128i a)  VPMOVSDW xmm1/m64 {k1}{z}, zmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtsepi32_epi16 (__m256i a)  VPMOVSDW xmm1/m128 {k1}{z}, zmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtepi64_epi32 (__m128i a)  VPMOVQD xmm1/m64 {k1}{z}, xmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtepi64_epi32 (__m256i a)  VPMOVQD xmm1/m128 {k1}{z}, ymm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtsepi64_epi32 (__m128i a)  VPMOVSQD xmm1/m64 {k1}{z}, xmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtsepi64_epi32 (__m256i a)  VPMOVSQD xmm1/m128 {k1}{z}, ymm2"""
        ...

    @staticmethod
    def convert_to_vector_128_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtpd_epi64 (__m128d a)  VCVTPD2QQ xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    def convert_to_vector_128_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvttpd_epi64 (__m128d a)  VCVTTPD2QQ xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtepi32_epi8 (__m128i a)  VPMOVDB xmm1/m32 {k1}{z}, zmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtepi32_epi8 (__m256i a)  VPMOVDB xmm1/m64 {k1}{z}, zmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtsepi32_epi8 (__m128i a)  VPMOVSDB xmm1/m32 {k1}{z}, zmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtsepi32_epi8 (__m256i a)  VPMOVSDB xmm1/m64 {k1}{z}, zmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_cvtepi64_ps (__m128i a)  VCVTQQ2PS xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm256_cvtepi64_ps (__m256i a)  VCVTQQ2PS xmm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtepi32_epi16 (__m128i a)  VPMOVDW xmm1/m64 {k1}{z}, xmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtepi32_epi16 (__m256i a)  VPMOVDW xmm1/m128 {k1}{z}, ymm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtusepi32_epi16 (__m128i a)  VPMOVUSDW xmm1/m64 {k1}{z}, xmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtusepi32_epi16 (__m256i a)  VPMOVUSDW xmm1/m128 {k1}{z}, ymm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtpd_epu32 (__m128d a)  VCVTPD2UDQ xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtepi64_epi32 (__m128i a)  VPMOVQD xmm1/m128 {k1}{z}, xmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtpd_epu32 (__m256d a)  VCVTPD2UDQ xmm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtepi64_epi32 (__m256i a)  VPMOVQD xmm1/m128 {k1}{z}, ymm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtusepi64_epi32 (__m128i a)  VPMOVUSQD xmm1/m128 {k1}{z}, xmm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvtusepi64_epi32 (__m256i a)  VPMOVUSQD xmm1/m128 {k1}{z}, ymm2"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvttpd_epu32 (__m128d a)  VCVTTPD2UDQ xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm256_cvttpd_epu32 (__m256d a)  VCVTTPD2UDQ xmm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    def convert_to_vector_128_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvtpd_epu64 (__m128d a)  VCVTPD2UQQ xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    def convert_to_vector_128_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_cvttpd_epu64 (__m128d a)  VCVTTPD2UQQ xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm512_cvtepu32_pd (__m128i a)  VCVTUDQ2PD ymm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_cvtepi64_pd (__m256i a)  VCVTQQ2PD ymm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvtps_epi64 (__m128 a)  VCVTPS2QQ ymm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvtpd_epi64 (__m256d a)  VCVTPD2QQ ymm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvttps_epi64 (__m128 a)  VCVTTPS2QQ ymm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvttpd_epi64 (__m256d a)  VCVTTPD2QQ ymm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_cvtepu32_ps (__m256i a)  VCVTUDQ2PS ymm1 {k1}{z}, ymm2/m256/m32bcst"""
        ...

    @staticmethod
    def convert_to_vector_256_u_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvtps_epu32 (__m256 a)  VCVTPS2UDQ ymm1 {k1}{z}, ymm2/m256/m32bcst"""
        ...

    @staticmethod
    def convert_to_vector_256_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvttps_epu32 (__m256 a)  VCVTTPS2UDQ ymm1 {k1}{z}, ymm2/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvtps_epu64 (__m128 a)  VCVTPS2UQQ ymm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvtpd_epu64 (__m256d a)  VCVTPD2UQQ ymm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvttps_epu64 (__m128 a)  VCVTTPS2UQQ ymm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_cvttpd_epu64 (__m256d a)  VCVTTPD2UQQ ymm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def detect_conflicts(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_conflict_epi32 (__m128i a)  VPCONFLICTD xmm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def detect_conflicts(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_conflict_epi32 (__m256i a)  VPCONFLICTD ymm1 {k1}{z}, ymm2/m256/m32bcst"""
        ...

    @staticmethod
    def divide_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_div_round_sd (__m128d a, __m128d b, int rounding)  VDIVSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    @overload
    def fixup(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], table: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_fixupimm_pd(__m128d a, __m128d b, __m128i tbl, int imm);  VFIXUPIMMPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def fixup(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], table: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_fixupimm_pd(__m256d a, __m256d b, __m256i tbl, int imm);  VFIXUPIMMPD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst, imm8"""
        ...

    @staticmethod
    def fixup_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], table: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_fixupimm_sd(__m128d a, __m128d b, __m128i tbl, int imm);  VFIXUPIMMSD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}, imm8"""
        ...

    @staticmethod
    def fused_multiply_add_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_fnmadd_round_sd (__m128d a, __m128d b, __m128d c, int r)  VFNMADDSD xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def fused_multiply_add_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_fmadd_round_sd (__m128d a, __m128d b, __m128d c, int r)  VFMADDSD xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def fused_multiply_subtract_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_fnmsub_round_sd (__m128d a, __m128d b, __m128d c, int r)  VFNMSUBSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    def fused_multiply_subtract_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_fmsub_round_sd (__m128d a, __m128d b, __m128d c, int r)  VFMSUBSS xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    @overload
    def get_exponent(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_getexp_pd (__m128d a)  VGETEXPPD xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def get_exponent(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_getexp_pd (__m256d a)  VGETEXPPD ymm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def get_exponent_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_getexp_sd (__m128d a, __m128d b)  VGETEXPSD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def get_exponent_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_getexp_sd (__m128d a)  VGETEXPSD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}"""
        ...

    @staticmethod
    @overload
    def get_mantissa(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_getmant_pd (__m128d a)  VGETMANTPD xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def get_mantissa(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_getmant_pd (__m256d a)  VGETMANTPD ymm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def get_mantissa_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_getmant_sd (__m128d a, __m128d b)  VGETMANTSD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def get_mantissa_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_getmant_sd (__m128d a)  VGETMANTSD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}"""
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_lzcnt_epi32 (__m128i a)  VPLZCNTD xmm1 {k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_lzcnt_epi32 (__m256i a)  VPLZCNTD ymm1 {k1}{z}, ymm2/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_max_epi64 (__m128i a, __m128i b)  VPMAXSQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_max_epi64 (__m256i a, __m256i b)  VPMAXSQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_min_epi64 (__m128i a, __m128i b)  VPMINSQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_min_epi64 (__m256i a, __m256i b)  VPMINSQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def multiply_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_mullo_epi64 (__m128i a, __m128i b)  VPMULLQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def multiply_low(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_mullo_epi64 (__m256i a, __m256i b)  VPMULLQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    def multiply_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_mul_round_sd (__m128d a, __m128d b, int rounding)  VMULSD xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    @overload
    def multi_shift(control: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_multishift_epi64_epi8(__m128i a, __m128i b)  VPMULTISHIFTQB xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def multi_shift(control: System.Runtime.Intrinsics.Vector256[int], value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_multishift_epi64_epi8(__m256i a, __m256i b)  VPMULTISHIFTQB ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    def permute_var_16x_16(left: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permutevar16x16_epi16 (__m256i a, __m256i b)  VPERMW ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def permute_var_16x_16x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permutex2var_epi16 (__m256i a, __m256i idx, __m256i b)  VPERMI2W ymm1 {k1}{z}, ymm2, ymm3/m256  VPERMT2W ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def permute_var_16x_8(left: System.Runtime.Intrinsics.Vector128[int], control: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_permutevar64x8_epi8 (__m128i a, __m128i b)  VPERMB xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def permute_var_16x_8x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_permutex2var_epi8 (__m128i a, __m128i idx, __m128i b)  VPERMI2B xmm1 {k1}{z}, xmm2, xmm3/m128  VPERMT2B xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def permute_var_2x_64x_2(lower: System.Runtime.Intrinsics.Vector128[float], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_permutex2var_pd (__m128d a, __m128i idx, __m128i b)  VPERMI2PD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst  VPERMT2PD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_2x_64x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_permutex2var_epi64 (__m128i a, __m128i idx, __m128i b)  VPERMI2Q xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst  VPERMT2Q xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    def permute_var_32x_8(left: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permutevar64x8_epi8 (__m256i a, __m256i b)  VPERMB ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    def permute_var_32x_8x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permutex2var_epi8 (__m256i a, __m256i idx, __m256i b)  VPERMI2B ymm1 {k1}{z}, ymm2, ymm3/m256  VPERMT2B ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    @overload
    def permute_var_4x_32x_2(lower: System.Runtime.Intrinsics.Vector128[float], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_permutex2var_ps (__m128 a, __m128i idx, __m128i b)  VPERMI2PS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst  VPERMT2PS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_4x_32x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_permutex2var_epi32 (__m128i a, __m128i idx, __m128i b)  VPERMI2D xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst  VPERMT2D xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_4x_64(value: System.Runtime.Intrinsics.Vector256[float], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_permute4x64_pd (__m256d a, __m256i b)  VPERMPD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_4x_64(value: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permute4x64_epi64 (__m256i a, __m256i b)  VPERMQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_4x_64x_2(lower: System.Runtime.Intrinsics.Vector256[float], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_permutex2var_pd (__m256d a, __m256i idx, __m256i b)  VPERMI2PD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst  VPERMT2PD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_4x_64x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permutex2var_epi64 (__m256i a, __m256i idx, __m256i b)  VPERMI2Q ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst  VPERMT2Q ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    def permute_var_8x_16(left: System.Runtime.Intrinsics.Vector128[int], control: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_permutevar8x16_epi16 (__m128i a, __m128i b)  VPERMW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    def permute_var_8x_16x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_permutex2var_epi16 (__m128i a, __m128i idx, __m128i b)  VPERMI2W xmm1 {k1}{z}, xmm2, xmm3/m128  VPERMT2W xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def permute_var_8x_32x_2(lower: System.Runtime.Intrinsics.Vector256[float], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm256_permutex2var_ps (__m256 a, __m256i idx, __m256i b)  VPERMI2PS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst  VPERMT2PS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def permute_var_8x_32x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_permutex2var_epi32 (__m256i a, __m256i idx, __m256i b)  VPERMI2D ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst  VPERMT2D ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def range(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_range_pd(__m128d a, __m128d b, int imm);  VRANGEPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def range(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_range_pd(__m256d a, __m256d b, int imm);  VRANGEPD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst, imm8"""
        ...

    @staticmethod
    def range_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_range_sd(__m128d a, __m128d b, int imm);  VRANGESD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}, imm8"""
        ...

    @staticmethod
    @overload
    def reciprocal_14(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_rcp14_pd (__m128d a, __m128d b)  VRCP14PD xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def reciprocal_14(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_rcp14_pd (__m256d a, __m256d b)  VRCP14PD ymm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def reciprocal_14_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_rcp14_sd (__m128d a, __m128d b)  VRCP14SD xmm1 {k1}{z}, xmm2, xmm3/m64The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def reciprocal_14_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_rcp14_sd (__m128d a)  VRCP14SD xmm1 {k1}{z}, xmm2, xmm3/m64"""
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_rsqrt14_pd (__m128d a, __m128d b)  VRSQRT14PD xmm1 {k1}{z}, xmm2/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_rsqrt14_pd (__m256d a, __m256d b)  VRSQRT14PD ymm1 {k1}{z}, ymm2/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_rsqrt14_sd (__m128d a, __m128d b)  VRSQRT14SD xmm1 {k1}{z}, xmm2, xmm3/m64The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_rsqrt14_sd (__m128d a)  VRSQRT14SD xmm1 {k1}{z}, xmm2, xmm3/m64"""
        ...

    @staticmethod
    @overload
    def reduce(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_reduce_pd(__m128d a, int imm);  VREDUCEPD xmm1 {k1}{z}, xmm2/m128/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def reduce(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_reduce_pd(__m256d a, int imm);  VREDUCEPD ymm1 {k1}{z}, ymm2/m256/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def reduce_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_reduce_sd(__m128d a, __m128d b, int imm);  VREDUCESD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}, imm8The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def reduce_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_reduce_sd(__m128d a, int imm);  VREDUCESD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}, imm8"""
        ...

    @staticmethod
    @overload
    def rotate_left(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_rol_epi32 (__m128i a, int imm8)  VPROLD xmm1 {k1}{z}, xmm2/m128/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def rotate_left(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_rol_epi32 (__m256i a, int imm8)  VPROLD ymm1 {k1}{z}, ymm2/m256/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def rotate_left_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_rolv_epi32 (__m128i a, __m128i b)  VPROLDV xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def rotate_left_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_rolv_epi32 (__m256i a, __m256i b)  VPROLDV ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def rotate_right(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_ror_epi32 (__m128i a, int imm8)  VPRORD xmm1 {k1}{z}, xmm2/m128/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def rotate_right(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_ror_epi32 (__m256i a, int imm8)  VPRORD ymm1 {k1}{z}, ymm2/m256/m32bcst, imm8"""
        ...

    @staticmethod
    @overload
    def rotate_right_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_rorv_epi32 (__m128i a, __m128i b)  VPRORDV xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def rotate_right_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_rorv_epi32 (__m256i a, __m256i b)  VPRORDV ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst"""
        ...

    @staticmethod
    @overload
    def round_scale(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_roundscale_pd (__m128d a, int imm)  VRNDSCALEPD xmm1 {k1}{z}, xmm2/m128/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def round_scale(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_roundscale_pd (__m256d a, int imm)  VRNDSCALEPD ymm1 {k1}{z}, ymm2/m256/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def round_scale_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_roundscale_sd (__m128d a, __m128d b, int imm)  VRNDSCALESD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}, imm8The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    @overload
    def round_scale_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_roundscale_sd (__m128d a, int imm)  VRNDSCALESD xmm1 {k1}{z}, xmm2, xmm3/m64{sae}, imm8"""
        ...

    @staticmethod
    @overload
    def scale(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_scalef_pd (__m128d a, int imm)  VSCALEFPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def scale(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_scalef_pd (__m256d a, int imm)  VSCALEFPD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def scale_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_scalef_round_sd (__m128d a, __m128d b)  VSCALEFSD xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    @overload
    def scale_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_scalef_sd (__m128d a, __m128d b)  VSCALEFSD xmm1 {k1}{z}, xmm2, xmm3/m64{er}"""
        ...

    @staticmethod
    @overload
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_sllv_epi16 (__m128i a, __m128i count)  VPSLLVW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_sllv_epi16 (__m256i a, __m256i count)  VPSLLVW ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__128i _mm_srai_epi64 (__m128i a, int imm8)  VPSRAQ xmm1 {k1}{z}, xmm2, imm8"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_sra_epi64 (__m128i a, __m128i count)  VPSRAQ xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_srai_epi64 (__m256i a, int imm8)  VPSRAQ ymm1 {k1}{z}, ymm2, imm8"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_sra_epi64 (__m256i a, __m128i count)  VPSRAQ ymm1 {k1}{z}, ymm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_srav_epi64 (__m128i a, __m128i count)  VPSRAVQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_srav_epi64 (__m256i a, __m256i count)  VPSRAVQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
        ...

    @staticmethod
    @overload
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_srlv_epi16 (__m128i a, __m128i count)  VPSRLVW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_srlv_epi16 (__m256i a, __m256i count)  VPSRLVW ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    @overload
    def shuffle_2x_128(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_shuffle_f64x2 (__m256d a, __m256d b, const int imm8)  VSHUFF64x2 ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def shuffle_2x_128(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_shuffle_i32x4 (__m256i a, __m256i b, const int imm8)  VSHUFI32x4 ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst, imm8"""
        ...

    @staticmethod
    def sqrt_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_sqrt_round_sd (__m128d a, __m128d b, int rounding)  VSQRTSD xmm1, xmm2 xmm3 {er}"""
        ...

    @staticmethod
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_sub_round_sd (__m128d a, __m128d b, int rounding)  VSUBSD xmm1, xmm2, xmm3 {er}"""
        ...

    @staticmethod
    @overload
    def sum_absolute_differences_in_block_32(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_dbsad_epu8 (__m128i a, __m128i b, int imm8)  VDBPSADBW xmm1 {k1}{z}, xmm2, xmm3/m128"""
        ...

    @staticmethod
    @overload
    def sum_absolute_differences_in_block_32(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_dbsad_epu8 (__m256i a, __m256i b, int imm8)  VDBPSADBW ymm1 {k1}{z}, ymm2, ymm3/m256"""
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector128[int], b: System.Runtime.Intrinsics.Vector128[int], c: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_ternarylogic_si128 (__m128i a, __m128i b, __m128i c, byte imm)  VPTERNLOGD xmm1 {k1}{z}, xmm2, xmm3/m128, imm8The above native signature does not exist. We provide this additional overload for consistency with the other bitwise APIs."""
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm_ternarylogic_pd (__m128d a, __m128d b, __m128d c, int imm)  VPTERNLOGQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst, imm8The above native signature does not exist. We provide this additional overload for consistency with the other bitwise APIs."""
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector256[int], b: System.Runtime.Intrinsics.Vector256[int], c: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_ternarylogic_si256 (__m256i a, __m256i b, __m256i c, byte imm)  VPTERNLOGD ymm1 {k1}{z}, ymm2, ymm3/m256, imm8The above native signature does not exist. We provide this additional overload for consistency with the other bitwise APIs."""
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256d _mm256_ternarylogic_pd (__m256d a, __m256d b, __m256d c, int imm)  VPTERNLOGQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst, imm8The above native signature does not exist. We provide this additional overload for consistency with the other bitwise APIs."""
        ...


class Avx512DQ(System.Runtime.Intrinsics.X86.Avx512F, metaclass=abc.ABCMeta):
    """Provides access to X86 AVX512DQ hardware instructions via intrinsics."""

    class VL(System.Runtime.Intrinsics.X86.Avx512F.VL, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX512DQ+VL hardware instructions via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def broadcast_pair_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_broadcast_i32x2 (__m128i a)  VBROADCASTI32x2 xmm1 {k1}{z}, xmm2/m64"""
            ...

        @staticmethod
        @overload
        def broadcast_pair_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_broadcast_i32x2 (__m128i a)  VBROADCASTI32x2 ymm1 {k1}{z}, xmm2/m64"""
            ...

        @staticmethod
        @overload
        def broadcast_pair_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_broadcast_f32x2 (__m128 a)  VBROADCASTF32x2 ymm1 {k1}{z}, xmm2/m64"""
            ...

        @staticmethod
        def convert_to_vector_128_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128d _mm_cvtepi64_pd (__m128i a)  VCVTQQ2PD xmm1 {k1}{z}, xmm2/m128/m64bcst"""
            ...

        @staticmethod
        def convert_to_vector_128_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtps_epi64 (__m128 a)  VCVTPS2QQ xmm1 {k1}{z}, xmm2/m64/m32bcst"""
            ...

        @staticmethod
        def convert_to_vector_128_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvttps_epi64 (__m128 a)  VCVTTPS2QQ xmm1 {k1}{z}, xmm2/m64/m32bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_cvtepi64_ps (__m128i a)  VCVTQQ2PS xmm1 {k1}{z}, xmm2/m128/m64bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm256_cvtepi64_ps (__m256i a)  VCVTQQ2PS xmm1 {k1}{z}, ymm2/m256/m64bcst"""
            ...

        @staticmethod
        def convert_to_vector_128_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvtps_epu64 (__m128 a)  VCVTPS2UQQ xmm1 {k1}{z}, xmm2/m64/m32bcst"""
            ...

        @staticmethod
        def convert_to_vector_128_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_cvttps_epu64 (__m128 a)  VCVTTPS2UQQ xmm1 {k1}{z}, xmm2/m64/m32bcst"""
            ...

        @staticmethod
        def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256d _mm256_cvtepi64_pd (__m256i a)  VCVTQQ2PD ymm1 {k1}{z}, ymm2/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cvtps_epi64 (__m128 a)  VCVTPS2QQ ymm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cvtpd_epi64 (__m256d a)  VCVTPD2QQ ymm1 {k1}{z}, ymm2/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cvttps_epi64 (__m128 a)  VCVTTPS2QQ ymm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cvttpd_epi64 (__m256d a)  VCVTTPD2QQ ymm1 {k1}{z}, ymm2/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cvtps_epu64 (__m128 a)  VCVTPS2UQQ ymm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_u_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cvtpd_epu64 (__m256d a)  VCVTPD2UQQ ymm1 {k1}{z}, ymm2/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cvttps_epu64 (__m128 a)  VCVTTPS2UQQ ymm1 {k1}{z}, xmm2/m128/m32bcst"""
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_cvttpd_epu64 (__m256d a)  VCVTTPD2UQQ ymm1 {k1}{z}, ymm2/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def multiply_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            """__m128i _mm_mullo_epi64 (__m128i a, __m128i b)  VPMULLQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst"""
            ...

        @staticmethod
        @overload
        def multiply_low(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            """__m256i _mm256_mullo_epi64 (__m256i a, __m256i b)  VPMULLQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst"""
            ...

        @staticmethod
        @overload
        def range(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_range_ps(__m128 a, __m128 b, int imm);  VRANGEPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def range(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_range_ps(__m256 a, __m256 b, int imm);  VRANGEPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def reduce(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            """__m128 _mm_reduce_ps(__m128 a, int imm);  VREDUCEPS xmm1 {k1}{z}, xmm2/m128/m32bcst, imm8"""
            ...

        @staticmethod
        @overload
        def reduce(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            """__m256 _mm256_reduce_ps(__m256 a, int imm);  VREDUCEPS ymm1 {k1}{z}, ymm2/m256/m32bcst, imm8"""
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx512F.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX512DQ hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def And(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_and_ps (__m512 a, __m512 b)  VANDPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    def and_not(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_andnot_ps (__m512 a, __m512 b)  VANDNPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    @overload
    def broadcast_pair_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_broadcast_i32x2 (__m128i a)  VBROADCASTI32x2 zmm1 {k1}{z}, xmm2/m64"""
        ...

    @staticmethod
    @overload
    def broadcast_pair_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_broadcast_f32x2 (__m128 a)  VBROADCASTF32x2 zmm1 {k1}{z}, xmm2/m64"""
        ...

    @staticmethod
    def broadcast_vector_128_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_broadcast_i64x2 (__m128i const * mem_addr)  VBROADCASTI64x2 zmm1 {k1}{z}, m128"""
        ...

    @staticmethod
    def broadcast_vector_256_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_broadcast_i32x8 (__m256i const * mem_addr)  VBROADCASTI32x8 zmm1 {k1}{z}, m256"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m512 _mm512_cvtepi64_ps (__m512i a)  VCVTQQ2PS ymm1 {k1}{z}, zmm2/m512/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[int], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm512_cvt_roundepi64_ps (__m512i a, int r)  VCVTQQ2PS ymm1, zmm2 {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cvtepi64_pd (__m512i a)  VCVTQQ2PD zmm1 {k1}{z}, zmm2/m512/m64bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector512[int], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_cvt_roundepi64_pd (__m512i a, int r)  VCVTQQ2PD zmm1, zmm2 {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtps_epi64 (__m512 a)  VCVTPS2QQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtpd_epi64 (__m512d a)  VCVTPD2QQ zmm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvt_roundps_epi64 (__m512 a, int r)  VCVTPS2QQ zmm1, ymm2 {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvt_roundpd_epi64 (__m512d a, int r)  VCVTPD2QQ zmm1, zmm2 {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvttps_epi64 (__m512 a)  VCVTTPS2QQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvttpd_epi64 (__m512 a)  VCVTTPD2QQ zmm1 {k1}{z}, zmm2/m512/m64bcst{sae}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtps_epu64 (__m512 a)  VCVTPS2UQQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvtpd_epu64 (__m512d a)  VCVTPD2UQQ zmm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvt_roundps_epu64 (__m512 a, int r)  VCVTPS2UQQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvt_roundpd_epu64 (__m512d a, int r)  VCVTPD2UQQ zmm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvttps_epu64 (__m512 a)  VCVTTPS2UQQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}"""
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_cvttpd_epu64 (__m512d a)  VCVTTPD2UQQ zmm1 {k1}{z}, zmm2/m512/m64bcst{er}"""
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm512_extracti64x2_epi64 (__m512i a, const int imm8)  VEXTRACTI64x2 xmm1/m128 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128d _mm512_extractf64x2_pd (__m512d a, const int imm8)  VEXTRACTF64x2 xmm1/m128 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    @overload
    def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm512_extracti32x8_epi32 (__m512i a, const int imm8)  VEXTRACTI32x8 ymm1/m256 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    @overload
    def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """__m256 _mm512_extractf32x8_ps (__m512 a, const int imm8)  VEXTRACTF32x8 ymm1/m256 {k1}{z}, zmm2, imm8"""
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_inserti64x2_si512 (__m512i a, __m128i b, const int imm8)  VINSERTI64x2 zmm1 {k1}{z}, zmm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512d _mm512_insertf64x2_pd (__m512d a, __m128d b, int imm8)  VINSERTF64x2 zmm1 {k1}{z}, zmm2, xmm3/m128, imm8"""
        ...

    @staticmethod
    @overload
    def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector256[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_inserti32x8_si512 (__m512i a, __m256i b, const int imm8)  VINSERTI32x8 zmm1 {k1}{z}, zmm2, xmm3/m256, imm8"""
        ...

    @staticmethod
    @overload
    def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector256[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_insertf32x8_ps (__m512 a, __m256 b, int imm8)  VINSERTF32x8 zmm1 {k1}{z}, zmm2, xmm3/m256, imm8"""
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """__m512i _mm512_mullo_epi64 (__m512i a, __m512i b)  VPMULLQ zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst"""
        ...

    @staticmethod
    def Or(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_or_ps (__m512 a, __m512 b)  VORPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...

    @staticmethod
    def range(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_range_ps(__m512 a, __m512 b, int imm);  VRANGEPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst{sae}, imm8"""
        ...

    @staticmethod
    def range_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_range_ss(__m128 a, __m128 b, int imm);  VRANGESS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}, imm8"""
        ...

    @staticmethod
    def reduce(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_reduce_ps(__m512 a, int imm);  VREDUCEPS zmm1 {k1}{z}, zmm2/m512/m32bcst{sae}, imm8"""
        ...

    @staticmethod
    @overload
    def reduce_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_reduce_ss(__m128 a, int imm);  VREDUCESS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}, imm8"""
        ...

    @staticmethod
    @overload
    def reduce_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """__m128 _mm_reduce_ss(__m128 a, __m128 b, int imm);  VREDUCESS xmm1 {k1}{z}, xmm2, xmm3/m32{sae}, imm8The above native signature does not exist. We provide this additional overload for consistency with the other scalar APIs."""
        ...

    @staticmethod
    def xor(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """__m512 _mm512_xor_ps (__m512 a, __m512 b)  VXORPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst"""
        ...


class Avx10v2(System.Runtime.Intrinsics.X86.Avx10v1, metaclass=abc.ABCMeta):
    """Provides access to X86 AVX10.2 hardware instructions via intrinsics"""

    class X64(System.Runtime.Intrinsics.X86.Avx10v1.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX10.2 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    class V512(System.Runtime.Intrinsics.X86.Avx10v1.V512, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVX10.2/512 hardware instructions via intrinsics."""

        class X64(System.Runtime.Intrinsics.X86.Avx10v1.V512.X64, metaclass=abc.ABCMeta):
            """Provides access to the x86 AVX10.2/512 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

            IS_SUPPORTED: bool
            """Gets a value that indicates whether the APIs in this class are supported."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        @overload
        def convert_to_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """VCVTPS2IUBS zmm1{k1}{z}, zmm2/m512/m32bcst {er}"""
            ...

        @staticmethod
        @overload
        def convert_to_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            """VCVTPS2IUBS zmm1{k1}{z}, zmm2/m512/m32bcst {er}"""
            ...

        @staticmethod
        def convert_to_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """VCVTTPS2IUBS zmm1{k1}{z}, zmm2/m512/m32bcst {sae}"""
            ...

        @staticmethod
        @overload
        def convert_to_s_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """VCVTPS2IBS zmm1{k1}{z}, zmm2/m512/m32bcst {er}"""
            ...

        @staticmethod
        @overload
        def convert_to_s_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            """VCVTPS2IBS zmm1{k1}{z}, zmm2/m512/m32bcst {er}"""
            ...

        @staticmethod
        def convert_to_s_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            """VCVTTPS2IBS zmm1{k1}{z}, zmm2/m512/m32bcst {sae}"""
            ...

        @staticmethod
        def min_max(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
            """VMINMAXPD zmm1{k1}{z}, zmm2, zmm3/m512/m64bcst {sae}, imm8"""
            ...

        @staticmethod
        def multiple_sum_absolute_differences(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: int) -> System.Runtime.Intrinsics.Vector512[int]:
            """VMPSADBW zmm1{k1}{z}, zmm2, zmm3/m512, imm8"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    @overload
    def convert_to_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """VCVTPS2IUBS xmm1{k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """VCVTPS2IUBS ymm1{k1}{z}, ymm2/m256/m32bcst {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """VCVTTPS2IUBS xmm1{k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """VCVTTPS2IUBS ymm1{k1}{z}, ymm2/m256/m32bcst {sae}"""
        ...

    @staticmethod
    @overload
    def convert_to_s_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """VCVTPS2IBS xmm1{k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_s_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """VCVTPS2IBS ymm1{k1}{z}, ymm2/m256/m32bcst {er}"""
        ...

    @staticmethod
    @overload
    def convert_to_s_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """VCVTTPS2IBS xmm1{k1}{z}, xmm2/m128/m32bcst"""
        ...

    @staticmethod
    @overload
    def convert_to_s_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """VCVTTPS2IBS ymm1{k1}{z}, ymm2/m256/m32bcst {sae}"""
        ...

    @staticmethod
    @overload
    def min_max(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """VMINMAXPD xmm1{k1}{z}, xmm2, xmm3/m128/m64bcst, imm8"""
        ...

    @staticmethod
    @overload
    def min_max(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        """VMINMAXPD ymm1{k1}{z}, ymm2, ymm3/m256/m64bcst {sae}, imm8"""
        ...

    @staticmethod
    def min_max_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        """VMINMAXSD xmm1{k1}{z}, xmm2, xmm3/m64 {sae}, imm8"""
        ...

    @staticmethod
    def move_scalar(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """VMOVD xmm1, xmm2/m32"""
        ...

    @staticmethod
    def store_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        """VMOVW xmm1/m16, xmm2"""
        ...


class AvxVnni(System.Runtime.Intrinsics.X86.Avx2, metaclass=abc.ABCMeta):
    """Provides access to the x86 AVXVNNI hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.Avx2.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 AVXVNNI hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    @overload
    def multiply_widening_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_dpbusd_epi32 (__m128i src, __m128i a, __m128i b)VPDPBUSD xmm, xmm, xmm/m128"""
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add(addend: System.Runtime.Intrinsics.Vector256[int], left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_dpbusd_epi32 (__m256i src, __m256i a, __m256i b)VPDPBUSD ymm, ymm, ymm/m256"""
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """__m128i _mm_dpbusds_epi32 (__m128i src, __m128i a, __m128i b)VPDPBUSDS xmm, xmm, xmm/m128"""
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add_saturate(addend: System.Runtime.Intrinsics.Vector256[int], left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """__m256i _mm256_dpbusds_epi32 (__m256i src, __m256i a, __m256i b)VPDPBUSDS ymm, ymm, ymm/m256"""
        ...


class Bmi1(System.Runtime.Intrinsics.X86.X86Base, metaclass=abc.ABCMeta):
    """Provides access to X86 BMI1 hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.X86Base.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 BMI1 hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def and_not(left: int, right: int) -> int:
            """unsigned __int64 _andn_u64 (unsigned __int64 a, unsigned __int64 b)  ANDN r64a, r64b, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def bit_field_extract(value: int, start: int, length: int) -> int:
            """unsigned __int64 _bextr_u64 (unsigned __int64 a, unsigned int start, unsigned int len)  BEXTR r64a, r/m64, r64bThis intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        @overload
        def bit_field_extract(value: int, control: int) -> int:
            """unsigned __int64 _bextr2_u64 (unsigned __int64 a, unsigned __int64 control)  BEXTR r64a, r/m64, r64bThis intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def extract_lowest_set_bit(value: int) -> int:
            """unsigned __int64 _blsi_u64 (unsigned __int64 a)  BLSI r64, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def get_mask_up_to_lowest_set_bit(value: int) -> int:
            """unsigned __int64 _blsmsk_u64 (unsigned __int64 a)  BLSMSK r64, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def reset_lowest_set_bit(value: int) -> int:
            """unsigned __int64 _blsr_u64 (unsigned __int64 a)  BLSR r64, r/m64This intrinsic is only available on 64-bit processes"""
            ...

        @staticmethod
        def trailing_zero_count(value: int) -> int:
            """__int64 _mm_tzcnt_64 (unsigned __int64 a)  TZCNT r64, r/m64This intrinsic is only available on 64-bit processes"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def and_not(left: int, right: int) -> int:
        """unsigned int _andn_u32 (unsigned int a, unsigned int b)  ANDN r32a, r32b, r/m32"""
        ...

    @staticmethod
    @overload
    def bit_field_extract(value: int, start: int, length: int) -> int:
        """unsigned int _bextr_u32 (unsigned int a, unsigned int start, unsigned int len)  BEXTR r32a, r/m32, r32b"""
        ...

    @staticmethod
    @overload
    def bit_field_extract(value: int, control: int) -> int:
        """unsigned int _bextr2_u32 (unsigned int a, unsigned int control)  BEXTR r32a, r/m32, r32b"""
        ...

    @staticmethod
    def extract_lowest_set_bit(value: int) -> int:
        """unsigned int _blsi_u32 (unsigned int a)  BLSI r32, r/m32"""
        ...

    @staticmethod
    def get_mask_up_to_lowest_set_bit(value: int) -> int:
        """unsigned int _blsmsk_u32 (unsigned int a)  BLSMSK r32, r/m32"""
        ...

    @staticmethod
    def reset_lowest_set_bit(value: int) -> int:
        """unsigned int _blsr_u32 (unsigned int a)  BLSR r32, r/m32"""
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        """int _mm_tzcnt_32 (unsigned int a)  TZCNT r32, r/m32"""
        ...


class Lzcnt(System.Runtime.Intrinsics.X86.X86Base, metaclass=abc.ABCMeta):
    """Provides access to X86 LZCNT hardware instructions via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.X86Base.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 LZCNT hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

        @staticmethod
        def leading_zero_count(value: int) -> int:
            """unsigned __int64 _lzcnt_u64 (unsigned __int64 a)  LZCNT r64, r/m64This intrinsic is only available on 64-bit processes"""
            ...

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def leading_zero_count(value: int) -> int:
        """unsigned int _lzcnt_u32 (unsigned int a)  LZCNT r32, r/m32"""
        ...


class X86Serialize(System.Runtime.Intrinsics.X86.X86Base, metaclass=abc.ABCMeta):
    """Provides access to the x86 SERIALIZE hardware instruction via intrinsics."""

    class X64(System.Runtime.Intrinsics.X86.X86Base.X64, metaclass=abc.ABCMeta):
        """Provides access to the x86 SERIALIZE hardware instructions, that are only available to 64-bit processes, via intrinsics."""

        IS_SUPPORTED: bool
        """Gets a value that indicates whether the APIs in this class are supported."""

    IS_SUPPORTED: bool
    """Gets a value that indicates whether the APIs in this class are supported."""

    @staticmethod
    def serialize() -> None:
        """void _serialize (void);"""
        ...


