0.5.2 (2021-08-26)
==================

- Updated ENGINEERING value to F213 in optical_element. [#29]

- Workaround for setuptools_scm issues with recent versions of pip. [#31]

0.5.1 (2021-08-24)
==================

- Added tests for mask maker utility. [#25]

- Added Dark Current model maker and tests. [#26]

- Added Readnoise maker utility and tests. [#23]

- Added Gain maker utility and tests. [#24]

0.5.0 (2021-08-07)
==================

0.4.0 (2021-08-06)
==================

- Added support for ScienceRawModel. Removed basic from ref_common in testing/utils. [#20]

- Added support for dq_init step in cal_step. [#18]

0.3.0 (2021-07-23)
==================

- Added code for DQ support. Added ramp and mask helper functions. Removed refout and zeroframe. [#17]

0.2.0 (2021-06-28)
==================

- Added support for ramp, ramp_fit_output, wfi_img_photom models. [#15]

- Set rad requirement to 0.2.0 and update factories and tests.  Add ``DarkRefModel``,
  ``GainRefModel``, and ``MaskRefModel``. [#11]
