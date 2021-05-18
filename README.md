A simple script to measure powmod timings

=== Python 2.7 ===
```
python powmodtest.py
================================================================================
Iterations: 1200
Func Name:                     Native Func:                  Time:
================================================================================
_pow2mod_bitshift              None                           1.065336
_pow2mod_f                     pow                            0.682585
_pow2mod_f                     powmod                         1.073672
================================================================================
Iterations: 100
Func Name:                     Native Func:                  Time:
================================================================================
pow                            None                           0.273095
powmod                         None                           0.562275
_powmod_bs                     None                           1.513844
--------------------------------------------------------------------------------
_powmod_catch2                 pow                            0.415599
_powmod_catch2                 powmod                         0.771345
_powmod_catch22                None                           0.712725
_powmod_catch2                 _powmod_bs                     1.649839
--------------------------------------------------------------------------------
_powmod_catchEven              pow                            0.695169
_powmod_catchEven              powmod                         1.203543
_powmod_catchEven              _powmod_bs                     2.020275
--------------------------------------------------------------------------------
_pow                           pow                            5.693182
_pow                           powmod                         6.001722
_pow                           _powmod_bs                     6.634488
```

=== Python 3.9 ===
```
python3 powmodtest.py
================================================================================
Iterations: 1200
Func Name:                     Native Func:                  Time:
================================================================================
_pow2mod_bitshift              None                           0.880005
_pow2mod_f                     pow                            1.938313
_pow2mod_f                     powmod                         1.154819
================================================================================
Iterations: 100
Func Name:                     Native Func:                  Time:
================================================================================
pow                            None                           0.991846
powmod                         None                           0.585883
_powmod_bs                     None                           1.533876
--------------------------------------------------------------------------------
_powmod_catch2                 pow                            1.220823
_powmod_catch2                 powmod                         0.795703
_powmod_catch22                None                           0.706532
_powmod_catch2                 _powmod_bs                     1.755621
--------------------------------------------------------------------------------
_powmod_catchEven              pow                            1.508047
_powmod_catchEven              powmod                         1.414726
_powmod_catchEven              _powmod_bs                     2.115719
--------------------------------------------------------------------------------
_pow                           pow                            8.119277
_pow                           powmod                         8.132482
_pow                           _powmod_bs                     9.281946
```
