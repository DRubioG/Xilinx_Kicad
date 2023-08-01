*******************************************************************************
** © Copyright 2020 Xilinx, Inc. All rights reserved.
** This file contains confidential and proprietary information of Xilinx, Inc. and 
** is protected under U.S. and international copyright and other intellectual property laws.
*******************************************************************************
**   ____  ____ 
**  /   /\/   / 
** /___/  \  /   Vendor: Xilinx 
** \   \   \/    
**  \   \        readme.txt Version: 2.14
**  /   /        Date Last Modified: 11/10/2020
** /___/   /\    Date Created: 12/04/13
** \   \  /  \   Associated Filename: usaall.zip
**  \___\/\___\ 
** 
**  Device: UltraScale Architecture
**  Revision History: 
**	v1.0:	Initial release
**	v1.1:	Added XCKU035 FBVA676, FBVA900, and FFVA1156 packages
**	v1.2:	Removed all packages except FBVA676, FBVA900, and FFVA1156 for all devices
**		Renamed MGTAVTTRCAL and MGTRREF pin names for FBVA676, FBVA900, and FFVA1156 packages
**	v1.3:	Added files for packages:
**				FFVA1517
**				FLVA1517
**				FFVB1517
**				FLVB1517
**				FFVC1517
**				FFVA1760
**				FLVA1760
**				FFVD1924
**				FLVD1924
**				FFVE1924
**				FLVE1924
**				FHGE1924
**				FLVF1924
**				FFVJ1924
**				FLVJ1924
**				FHGJ1924
**				FLVA2377
**				FLGB2377
**				FLGA2892
**	v1.4:	For XCKU100 and XCKU115 in the FLVD1924 package, changed SLR number for bank 70 from 0 to 1
**		Removed FFVC1517 packages
**	v1.5:	Added FFVC1517 packages with updated power pins
**		Removed files for the nonexistent XCVU080FFVJ package
**	v1.6:	Removed all Virtex UltraScale files
**		Removed all A1760 and B1517 files
**	v1.7:	Added B1760, A2104, B2104, C2104, and A2577 files
**	v1.8:	Fixed No-Connect column in KU060/KU075-FFVA1156 to include KU035 and MGTRREF/MGTAVTTRCAL pins
**		Fixed No-Connect column in VU160/VU190-FLGC2104 to include MGTRREF/MGTAVTTRCAL pins
**		Added VU440 packages
**	v1.9:	Removed all packages for KU075 and KU100
**		Added packages for KU115, VU065, VU080, VU095, and VU125
**	v1.10:	Added packages for KU085 and KU095
**		Added the SFVA784 package
**		Fixed the No-Connect column for all devices in FFVB1760/FLVB1760 and FLVF1924 to account for unconnected banks in KU080
**	v1.11:	Temporarily removed SFVA784 files pending a pinout update
**	v1.12:	Added KU025-FFVA1156 package
**		Updated No-Connect column in all FFVA1156 packages
**		Fixed I/O Type for banks 84/94 for KU115-FLVB2104 package
**		Added the SFVA784 package for KU035 and KU040
**		Added the KU095-FFVA1156
**	v2.0:	Added "(Preliminary)" to all packages that are still in the design stage
**		Added files for Kintex/Virtex UltraScale+:
**			xcku11pffva1156
**			xcku11pffvd900
**			xcku11pffve1517
**			xcku13pffve900
**			xcku15pffva1156
**			xcku15pffva1760
**			xcku15pffve1517
**			xcku15pffve1760
**			xcku3pffva676
**			xcku3pffvb676
**			xcku3pffvd900
**			xcku3psfvb784
**			xcku5pffva676
**			xcku5pffvb676
**			xcku5pffvd900
**			xcku5psfvb784
**			xcku9pffve900
**			xcvu11pflga2577
**			xcvu11pflgb2104
**			xcvu11pflgc2104
**			xcvu11pflgf1924
**			xcvu13pfhga2104
**			xcvu13pfhgb2104
**			xcvu13pfhgc2104
**			xcvu13pflga2577
**			xcvu3pffvc1517
**			xcvu5pflva2104
**			xcvu5pflvb2104
**			xcvu5pflvc2104
**			xcvu7pflva2104
**			xcvu7pflvb2104
**			xcvu7pflvc2104
**			xcvu9pflga2104
**			xcvu9pflga2577
**			xcvu9pflgb2104
**			xcvu9pflgc2104
**		Updated No-Connect column in:
**			xcku035fbva676
**			xcku035ffva1156
**			xcku040fbva676
**			xcku040ffva1156
**			xcku060ffva1156
**			xcku095ffva1156
**			xcku115flvb2104
**			xcvu080ffvb2104
**			xcvu095ffvb2104
**			xcvu125flvb2104
**			xcvu125flvc2104
**			xcvu160flgb2104
**			xcvu160flgc2104
**			xcvu190flga2577
**			xcvu190flgb2104
**			xcvu190flgc2104
**		Updated pinout for xcku025ffva1156
**	v2.1:	Removed files for packages:
**			xcku3pffva676
**			xcku3pffvb676
**			xcku3psfvb784
**			xcku5pffva676
**			xcku5pffvd900
**			xcku5psfvb784
**			xcku11pffva1156
**			xcku11pffvd900
**			xcku11pffve1517
**			xcku15pffva1156
**			xcku15pffva1760
**			xcku15pffve1760
**			xcvu11pflga2577
**			xcvu11pflgb2104
**			xcvu11pflgc2104
**			xcvu11pflgf1924
**			xcvu13pfhga2104
**			xcvu13pfhgb2104
**			xcvu13pfhgc2104
**			xcvu13pflga2577
**				Updated files for packages:
**				xcku3pffvb676
**				xcku3pffvd900
**				xcku5pffvb676
**				xcku5pffvd900
**				xcku15pffve1517
**				xcvu7pflvb2104
**				xcvu9pflgb2104
**	v2.2:			Added files for:
**				xcku3pffva676
**				xcku5pffva676
**				xcku15pffve1760
**	v2.3 (10/26/2016):		Replaced all UltraScale+ files with upgraded header version
**				Added xcku15pffva1760
**	v2.4 (12/01/2016):		Added xcvu13pflga2577
**				Added xcvu13pfhgb2104
**				Added xcku15pffva1156
**				Added xcvu11pflgb2104
**	v2.5 (01/26/2017):		Added xcvu11pflgf1924
**				Added xcvu13pfhgc2104
**	v2.6 (05/23/2017):		Added xcku3psfvb784
**				Added xcku5psfvb784
**				Added xcku11pffve1517
**				Added xcku11pffva1156
**				Added xcvu13pfhga2104
**				Added xcvu11pflga2577
**				Added xcvu11pflgc2104
**				Added xcvu13pfigd2104
**				Updated xcvu7pflva2104
**				Updated xcvu7pflvb2104
**				Updated xcvu9pflga2104
**				Updated xcvu9pflgb2104
**				Updated xcvu9pflga2577
**				Updated xcku9pffve900
**				Updated xcku3pffva676
**				Updated xcku3pffvb676
**				Updated xcku3psfvb784
**				Updated xcku3pffvd900
**				Updated xcku5pffva676
**				Updated xcku5pffvb676
**				Updated xcku5psfvb784
**				Updated xcku5pffvd900
**				Updated xcvu3pffvc1517
**				Updated xcvu9pflgc2104
**	v2.7 (09/27/2017):		Added xcku11pffvd900
**				Added xcvu11pfsgd2104
**				Updated xcku13pffve900
**				Updated xcku15pffva1156
**				Updated xcku15pffva1760
**				Updated xcku15pffve1517
**				Updated xcku15pffve1760
**				Updated xcvu11pflga2577
**				Updated xcvu11pflgb2104
**				Updated xcvu11pflgc2104
**				Updated xcvu11pflgf1924
**				Updated xcvu13pfhga2104
**				Updated xcvu13pfhgb2104
**				Updated xcvu13pfhgc2104
**				Updated xcvu13pfigd2104
**				Updated xcvu13pflga2577
**				Updated xcvu5pflva2104
**				Updated xcvu5pflvb2104
**				Updated xcvu5pflvc2104
**				Updated xcvu7pflvc2104
**				Updated xcvu9pfsgd2104
**				Updated xcku11pffve1517
**				Updated xcku11pffva1156
**	v2.8 (12/05/2017):		Updated xcvu11pfsgd2104
**	v2.9 (03/06/2018):		Added xcvu31pfsvh1924
**				Added xcvu33pfsvh2104
**				Added xcvu35pfsvh2104
**				Added xcvu35pfsvh2892
**				Added xcvu37pfsvh2892
**				Added xqku15pffra1156
**				Added xqku15pffre1517
**				Added xqku5pffrb676
**				Added xqku5psfrb784
**				Added xqvu11pflrc2104
**				Added xqvu3pffrc1517
**				Added xqvu7pflra2104
**				Added xqvu7pflrb2104
**	v2.10 (10/29/2018):		Updated:
**					xqku15pffra1156
**					xqku15pffre1517
**	v2.11 (09/13/2019):			Added:
**					xcvu27pfigd2104
**					xcvu27pfsga2577
**					xcvu29pfigd2104
**					xcvu29pfsga2577
**				Updated:
**					xcvu31pfsvh1924
**					xcvu33pfsvh2104
**					xcvu35pfsvh2104
**					xcvu35pfsvh2892
**					xcvu37pfsvh2892
**					xqku5pffrb676
**					xqku5psfrb784
**	v2.12 (02/27/2020):			Added:
**					xcvu47pfsvh2892
**					xcvu45pfsvh2892
**					xcvu45pfsvh2104
**					xcvu19pfsva3824
**					xcvu19pfsvb3824
**	v2.12 (05/05/2020):		Added:
**					xcvu13pfsga2577
**	v2.13 (11/10/2020):		Added:
**					xcku19pffvj1760
**					xcku19pffvb2104
**					xcvu23pvsva1365
**					xcvu23pfsvj1760
**					xcvu57pfsvk2892
*******************************************************************************
**
**  Disclaimer: 
**
**	This disclaimer is not a license and does not grant any rights to the materials 
**             	distributed herewith. Except as otherwise provided in a valid license issued to you 
**	by Xilinx, and to the maximum extent permitted by applicable law: 
**	(1) THESE MATERIALS ARE MADE AVAILABLE "AS IS" AND WITH ALL FAULTS, 
**	AND XILINX HEREBY DISCLAIMS ALL WARRANTIES AND CONDITIONS, EXPRESS, IMPLIED, OR STATUTORY, 
**	INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT, OR 
**	FITNESS FOR ANY PARTICULAR PURPOSE; and (2) Xilinx shall not be liable (whether in contract 
**	or tort, including negligence, or under any other theory of liability) for any loss or damage 
**	of any kind or nature related to, arising under or in connection with these materials, 
**	including for any direct, or any indirect, special, incidental, or consequential loss 
**	or damage (including loss of data, profits, goodwill, or any type of loss or damage suffered 
**	as a result of any action brought by a third party) even if such damage or loss was 
**	reasonably foreseeable or Xilinx had been advised of the possibility of the same.


**  Critical Applications:
**
**	Xilinx products are not designed or intended to be fail-safe, or for use in any application 
**	requiring fail-safe performance, such as life-support or safety devices or systems, 
**	Class III medical devices, nuclear facilities, applications related to the deployment of airbags,
**	or any other applications that could lead to death, personal injury, or severe property or 
**	environmental damage (individually and collectively, "Critical Applications"). Customer assumes 
**	the sole risk and liability of any use of Xilinx products in Critical Applications, subject only 
**	to applicable laws and regulations governing limitations on product liability.

**  THIS COPYRIGHT NOTICE AND DISCLAIMER MUST BE RETAINED AS PART OF THIS FILE AT ALL TIMES.

*******************************************************************************
** IMPORTANT NOTES **

1) These package files contain advance information and are subject to change without notice and are provided solely for information purposes.

2) Please refer to the UltraScale Architecture Package Files section of UG575, UltraScale Architecture Packaging and Pinouts, for detailed information on the contents of the package files.

 
