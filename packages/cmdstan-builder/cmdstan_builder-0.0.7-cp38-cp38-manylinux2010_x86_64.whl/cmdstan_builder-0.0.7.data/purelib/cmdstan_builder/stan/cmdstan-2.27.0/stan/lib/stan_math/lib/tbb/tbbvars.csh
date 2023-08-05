#!/bin/csh
setenv TBBROOT "/Users/parthiv.naresh/PycharmProjects/cmdstan-ext/cmdstan_builder/stan/cmdstan-2.27.0/stan/lib/stan_math/lib/tbb_2020.3" #
setenv tbb_bin "/Users/parthiv.naresh/PycharmProjects/cmdstan-ext/cmdstan_builder/stan/cmdstan-2.27.0/stan/lib/stan_math/lib/tbb" #
if (! $?CPATH) then #
    setenv CPATH "${TBBROOT}/include" #
else #
    setenv CPATH "${TBBROOT}/include:$CPATH" #
endif #
if (! $?LIBRARY_PATH) then #
    setenv LIBRARY_PATH "${tbb_bin}" #
else #
    setenv LIBRARY_PATH "${tbb_bin}:$LIBRARY_PATH" #
endif #
if (! $?DYLD_LIBRARY_PATH) then #
    setenv DYLD_LIBRARY_PATH "${tbb_bin}" #
else #
    setenv DYLD_LIBRARY_PATH "${tbb_bin}:$DYLD_LIBRARY_PATH" #
endif #
 #
