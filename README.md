# lucidac-resources

This repository bundles resources for anabrid's [LUCIDAC](https://anabrid.com/lucidac) device, the first-to-market reconfigurable, fully integrated and hackable hybrid digital-analog computer.

As part of anabrid's lineup of products, the LUCIDAC undergoes changes and updates as we further develop our systems. These updates, together with updated documentation are available in this repository.

Furthermore, we welcome any contributions to the initial software stack (see below) and also issue reports for the LUCIDAC device and software.

## On "hackability" - `mainline` vs. `initial` stack

LUCIDAC was released with an initial software stack consisting of
- [Firmware](https://github.com/anabrid/lucidac-firmware) and
- [lucipy](https://github.com/anabrid/lucipy) as user-facing Python client.

Since then, anabrid's range of products have grown and the LUCIDAC has been successively integrated into anabrid's core software stack. 

The the "initial stack" was released under the open MIT license, allowing users to read the code and modify ("hack") the device to their liking. With this stack, the full functionality of the LUCIDAC is accessible. All custom modifications are made at the user's sole risk, and anabrid expressly disclaims all warranties and liability for their operation, consistent with the terms of the MIT license. Support for modifications is provided on a volunteer basis only.

Newer developments and advanced features, referred to as the LUCIDAC Mainline Stack, are distributed solely as binary packages without source code access. These components are licensed under a separate Proprietary End-User License Agreement (EULA), which governs their use. For more information, please contact Anabrid directly.
