# This file is generated by objective.metadata
#
# Last update: Sun Sep  9 13:27:52 2018

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
misc.update({'CMIODeviceRS422Command': objc.createStructType('CMIODeviceRS422Command', sel32or64(b'{CMIODeviceRS422Command=^CL^CLL}', b'{CMIODeviceRS422Command=^CI^CII}'), ['mCommand', 'mCommandLength', 'mResponse', 'mResponseLength', 'mResponseUsed']), 'CMIODeviceAVCCommand': objc.createStructType('CMIODeviceAVCCommand', sel32or64(b'{CMIODeviceAVCCommand=^CL^CLL}', b'{CMIODeviceAVCCommand=^CI^CII}'), ['mCommand', 'mCommandLength', 'mResponse', 'mResponseLength', 'mResponseUsed']), 'CMIODeviceSMPTETimeCallback': objc.createStructType('CMIODeviceSMPTETimeCallback', b'{CMIODeviceSMPTETimeCallback=^?^v}', ['mGetSMPTETimeProc', 'mRefCon']), 'CMIOStreamScheduledOutputNotificationProcAndRefCon': objc.createStructType('CMIOStreamScheduledOutputNotificationProcAndRefCon', b'{CMIOStreamScheduledOutputNotificationProcAndRefCon=^?^?}', ['scheduledOutputNotificationProc', 'scheduledOutputNotificationRefCon']), 'CMIOStreamDeck': objc.createStructType('CMIOStreamDeck', sel32or64(b'{CMIOStreamDeck=LLL}', b'{CMIOStreamDeck=III}'), ['mStatus', 'mState', 'mState2']), 'CMIODeviceStreamConfiguration': objc.createStructType('CMIODeviceStreamConfiguration', sel32or64(b'{CMIODeviceStreamConfiguration=L^L}', b'{CMIODeviceStreamConfiguration=I^I}'), ['mNumberStreams', 'mNumberChannels']), 'CMIOObjectPropertyAddress': objc.createStructType('CMIOObjectPropertyAddress', sel32or64(b'{CMIOObjectPropertyAddress=LLL}', b'{CMIOObjectPropertyAddress=III}'), ['mSelector', 'mScope', 'mElement'])})
constants = '''$kCMIOBlockBufferAttachmentKey_CVPixelBufferReference@^{__CFString=}$kCMIOSampleBufferAttachmentKey_CAAudioTimeStamp@^{__CFString=}$kCMIOSampleBufferAttachmentKey_ClientSequenceID@^{__CFString=}$kCMIOSampleBufferAttachmentKey_ClosedCaptionSampleBuffer@^{__CFString=}$kCMIOSampleBufferAttachmentKey_DiscontinuityFlags@^{__CFString=}$kCMIOSampleBufferAttachmentKey_HDV1_PackData@^{__CFString=}$kCMIOSampleBufferAttachmentKey_HDV2_VAUX@^{__CFString=}$kCMIOSampleBufferAttachmentKey_HostTime@^{__CFString=}$kCMIOSampleBufferAttachmentKey_MouseAndKeyboardModifiers@^{__CFString=}$kCMIOSampleBufferAttachmentKey_MuxedSourcePresentationTimeStamp@^{__CFString=}$kCMIOSampleBufferAttachmentKey_NativeSMPTEFrameCount@^{__CFString=}$kCMIOSampleBufferAttachmentKey_NoDataMarker@^{__CFString=}$kCMIOSampleBufferAttachmentKey_NumberOfVideoFramesInBuffer@^{__CFString=}$kCMIOSampleBufferAttachmentKey_NumberOfVideoFramesInGOP@^{__CFString=}$kCMIOSampleBufferAttachmentKey_PulldownCadenceInfo@^{__CFString=}$kCMIOSampleBufferAttachmentKey_RepeatedBufferContents@^{__CFString=}$kCMIOSampleBufferAttachmentKey_SMPTETime@^{__CFString=}$kCMIOSampleBufferAttachmentKey_SequenceNumber@^{__CFString=}$kCMIOSampleBufferAttachmentKey_SourceAudioFormatDescription@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorFrameRect@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorIsDrawnInFramebuffer@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorIsVisible@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorPositionX@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorPositionY@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorReference@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorScale@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_CursorSeed@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_KeyboardModifiers@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_KeyboardModifiersEvent@^{__CFString=}$kCMIOSampleBufferAttachment_MouseAndKeyboardModifiersKey_MouseButtonState@^{__CFString=}$'''
enums = '''$kCMIOAVCDeviceType_DVCPro100_720p@1685481584$kCMIOAVCDeviceType_DVCPro100_NTSC@1685467502$kCMIOAVCDeviceType_DVCPro100_PAL@1685467504$kCMIOAVCDeviceType_DVCPro50_NTSC@1685468526$kCMIOAVCDeviceType_DVCPro50_PAL@1685468528$kCMIOAVCDeviceType_DVCProHD_1080i50@1685481525$kCMIOAVCDeviceType_DVCProHD_1080i60@1685481526$kCMIOAVCDeviceType_DVCPro_NTSC@1685483630$kCMIOAVCDeviceType_DVCPro_PAL@1685483632$kCMIOAVCDeviceType_DV_NTSC@1685480224$kCMIOAVCDeviceType_DV_PAL@1685480304$kCMIOAVCDeviceType_MPEG2@1836082994$kCMIOAVCDeviceType_Unknown@1970170734$kCMIOBacklightCompensationControlClassID@1651207284$kCMIOBlackLevelControlClassID@1651207286$kCMIOBooleanControlClassID@1953458028$kCMIOBooleanControlPropertyValue@1650685548$kCMIOBrightnessControlClassID@1651665268$kCMIOContrastControlClassID@1668576116$kCMIOControlClassID@1633907820$kCMIOControlPropertyElement@1667591277$kCMIOControlPropertyScope@1668506480$kCMIOControlPropertyVariant@1668702578$kCMIODataDestinationControlClassID@1684370292$kCMIODataSourceControlClassID@1685287523$kCMIODeckShuttlePause@0$kCMIODeckShuttlePlay1x@6$kCMIODeckShuttlePlayFast@7$kCMIODeckShuttlePlayFaster@8$kCMIODeckShuttlePlayFastest@9$kCMIODeckShuttlePlayHighSpeed@10$kCMIODeckShuttlePlayNextFrame@1$kCMIODeckShuttlePlayPreviousFrame@-1$kCMIODeckShuttlePlaySlow1@3$kCMIODeckShuttlePlaySlow2@4$kCMIODeckShuttlePlaySlow3@5$kCMIODeckShuttlePlaySlowest@2$kCMIODeckShuttleReverse1x@-6$kCMIODeckShuttleReverseFast@-7$kCMIODeckShuttleReverseFaster@-8$kCMIODeckShuttleReverseFastest@-9$kCMIODeckShuttleReverseHighSpeed@-10$kCMIODeckShuttleReverseSlow1@-3$kCMIODeckShuttleReverseSlow2@-4$kCMIODeckShuttleReverseSlow3@-5$kCMIODeckShuttleReverseSlowest@-2$kCMIODeckStateFastForward@6$kCMIODeckStateFastRewind@7$kCMIODeckStatePause@2$kCMIODeckStatePlay@1$kCMIODeckStatePlayReverse@5$kCMIODeckStatePlaySlow@3$kCMIODeckStateReverseSlow@4$kCMIODeckStateStop@0$kCMIODeckStatusBusy@1$kCMIODeckStatusLocal@2$kCMIODeckStatusNoDevice@7$kCMIODeckStatusNotThreaded@3$kCMIODeckStatusOpcode@5$kCMIODeckStatusSearchingForDevice@6$kCMIODeckStatusTapeInserted@4$kCMIODeviceAVCSignalMode8mmNTSC@6$kCMIODeviceAVCSignalMode8mmPAL@134$kCMIODeviceAVCSignalModeAudio@32$kCMIODeviceAVCSignalModeDVCPro100_50@240$kCMIODeviceAVCSignalModeDVCPro100_60@112$kCMIODeviceAVCSignalModeDVCPro25_525_60@120$kCMIODeviceAVCSignalModeDVCPro25_625_50@248$kCMIODeviceAVCSignalModeDVCPro50_525_60@116$kCMIODeviceAVCSignalModeDVCPro50_625_50@244$kCMIODeviceAVCSignalModeDVHS@1$kCMIODeviceAVCSignalModeHD1125_60@8$kCMIODeviceAVCSignalModeHD1250_50@136$kCMIODeviceAVCSignalModeHDV1_50@144$kCMIODeviceAVCSignalModeHDV1_60@16$kCMIODeviceAVCSignalModeHDV2_50@154$kCMIODeviceAVCSignalModeHDV2_60@26$kCMIODeviceAVCSignalModeHi8NTSC@14$kCMIODeviceAVCSignalModeHi8PAL@142$kCMIODeviceAVCSignalModeMPEG12Mbps_50@148$kCMIODeviceAVCSignalModeMPEG12Mbps_60@20$kCMIODeviceAVCSignalModeMPEG25Mbps_50@144$kCMIODeviceAVCSignalModeMPEG25Mbps_60@16$kCMIODeviceAVCSignalModeMPEG6Mbps_50@152$kCMIODeviceAVCSignalModeMPEG6Mbps_60@24$kCMIODeviceAVCSignalModeMicroMV12Mbps_50@164$kCMIODeviceAVCSignalModeMicroMV12Mbps_60@36$kCMIODeviceAVCSignalModeMicroMV6Mbps_50@168$kCMIODeviceAVCSignalModeMicroMV6Mbps_60@40$kCMIODeviceAVCSignalModeSD525_60@0$kCMIODeviceAVCSignalModeSD625_50@128$kCMIODeviceAVCSignalModeSDL525_60@4$kCMIODeviceAVCSignalModeSDL625_50@132$kCMIODeviceAVCSignalModeSVHS525_60@13$kCMIODeviceAVCSignalModeSVHS625_50@237$kCMIODeviceAVCSignalModeVHSMESECAM@213$kCMIODeviceAVCSignalModeVHSMPAL@37$kCMIODeviceAVCSignalModeVHSNPAL@181$kCMIODeviceAVCSignalModeVHSNTSC@5$kCMIODeviceAVCSignalModeVHSPAL@165$kCMIODeviceAVCSignalModeVHSSECAM@197$kCMIODeviceClassID@1633969526$kCMIODevicePermissionsError@560492391$kCMIODevicePropertyAVCDeviceSignalMode@1886221165$kCMIODevicePropertyAVCDeviceType@1886216564$kCMIODevicePropertyCanProcessAVCCommand@1886216547$kCMIODevicePropertyCanProcessRS422Command@1916023346$kCMIODevicePropertyCanSwitchFrameRatesWithoutFrameDrops@1718775396$kCMIODevicePropertyClientSyncDiscontinuity@1886217075$kCMIODevicePropertyDeviceCanBeDefaultDevice@1684434036$kCMIODevicePropertyDeviceHasChanged@1684629094$kCMIODevicePropertyDeviceIsAlive@1818850926$kCMIODevicePropertyDeviceIsRunning@1735354734$kCMIODevicePropertyDeviceIsRunningSomewhere@1735356005$kCMIODevicePropertyDeviceMaster@1886219880$kCMIODevicePropertyDeviceUID@1969841184$kCMIODevicePropertyExcludeNonDALAccess@1769500257$kCMIODevicePropertyHogMode@1869180523$kCMIODevicePropertyIIDCCSRData@1668510308$kCMIODevicePropertyIIDCInitialUnitSpace@1769303667$kCMIODevicePropertyLatency@1819569763$kCMIODevicePropertyLinkedAndSyncedCoreAudioDeviceUID@1886155620$kCMIODevicePropertyLinkedCoreAudioDeviceUID@1886156132$kCMIODevicePropertyLocation@1684828003$kCMIODevicePropertyLocationBuiltInDisplay@1$kCMIODevicePropertyLocationExternalDevice@3$kCMIODevicePropertyLocationExternalDisplay@2$kCMIODevicePropertyLocationExternalWirelessDevice@4$kCMIODevicePropertyLocationUnknown@0$kCMIODevicePropertyModelUID@1836411236$kCMIODevicePropertyPlugIn@1886156135$kCMIODevicePropertySMPTETimeCallback@1886221155$kCMIODevicePropertyScopeInput@1768845428$kCMIODevicePropertyScopeOutput@1869968496$kCMIODevicePropertyScopePlayThrough@1886679669$kCMIODevicePropertyStreamConfiguration@1936482681$kCMIODevicePropertyStreams@1937009955$kCMIODevicePropertySuspendedByUser@1935833461$kCMIODevicePropertyTransportType@1953653102$kCMIODevicePropertyVideoDigitizerComponents@1986292071$kCMIODeviceUnknown@0$kCMIODeviceUnsupportedFormatError@560226676$kCMIODirectionControlClassID@1684632165$kCMIOExposureControlClassID@2020635506$kCMIOExposureControlPropertyConvergenceSpeed@1701016432$kCMIOExposureControlPropertyIntegrationTime@1701408372$kCMIOExposureControlPropertyLockThreshold@1701602155$kCMIOExposureControlPropertyMaximumGain@1701667192$kCMIOExposureControlPropertyRegionOfInterest@1701998441$kCMIOExposureControlPropertyStability@1702065273$kCMIOExposureControlPropertyStable@1702065250$kCMIOExposureControlPropertyTarget@1702127476$kCMIOExposureControlPropertyUnlockThreshold@1702194283$kCMIOFeatureControlClassID@1718903668$kCMIOFeatureControlPropertyAbsoluteNative@1717792353$kCMIOFeatureControlPropertyAbsoluteRange@1717789042$kCMIOFeatureControlPropertyAbsoluteUnitName@1717794158$kCMIOFeatureControlPropertyAbsoluteValue@1717789046$kCMIOFeatureControlPropertyAutomaticManual@1717789037$kCMIOFeatureControlPropertyConvertAbsoluteToNative@1717645934$kCMIOFeatureControlPropertyConvertNativeToAbsolute@1718497889$kCMIOFeatureControlPropertyNativeRange@1717792370$kCMIOFeatureControlPropertyNativeValue@1717792374$kCMIOFeatureControlPropertyOnOff@1717792623$kCMIOFeatureControlPropertyTune@1717793902$kCMIOFocusControlClassID@1717794163$kCMIOGainControlClassID@1734437230$kCMIOGammaControlClassID@1735224673$kCMIOHardwareBadDeviceError@560227702$kCMIOHardwareBadObjectError@560947818$kCMIOHardwareBadPropertySizeError@561211770$kCMIOHardwareBadStreamError@561214578$kCMIOHardwareIllegalOperationError@1852797029$kCMIOHardwareNoError@0$kCMIOHardwareNotRunningError@1937010544$kCMIOHardwareNotStoppedError@1920298528$kCMIOHardwarePropertyAllowScreenCaptureDevices@2036691744$kCMIOHardwarePropertyAllowWirelessScreenCaptureDevices@2004050788$kCMIOHardwarePropertyDefaultInputDevice@1682533920$kCMIOHardwarePropertyDefaultOutputDevice@1682929012$kCMIOHardwarePropertyDeviceForUID@1685416292$kCMIOHardwarePropertyDevices@1684370979$kCMIOHardwarePropertyIsInitingOrExiting@1768845172$kCMIOHardwarePropertyPlugInForBundleID@1885954665$kCMIOHardwarePropertyProcessIsMaster@1835103092$kCMIOHardwarePropertySleepingIsAllowed@1936483696$kCMIOHardwarePropertySuspendedBySystem@1935833459$kCMIOHardwarePropertyUnloadingIsAllowed@1970170980$kCMIOHardwarePropertyUserSessionIsActiveOrHeadless@1970496882$kCMIOHardwareSuspendedBySystemError@1684369017$kCMIOHardwareUnknownPropertyError@2003332927$kCMIOHardwareUnspecifiedError@2003329396$kCMIOHardwareUnsupportedOperationError@1970171760$kCMIOHueControlClassID@1752524064$kCMIOInvalidSequenceNumber@18446744073709551615$kCMIOIrisControlClassID@1769105779$kCMIOJackControlClassID@1784767339$kCMIONoiseReductionControlClassID@1932684914$kCMIOObjectClassID@1634689642$kCMIOObjectClassIDWildcard@707406378$kCMIOObjectPropertyClass@1668047219$kCMIOObjectPropertyCreator@1869638759$kCMIOObjectPropertyElementCategoryName@1818452846$kCMIOObjectPropertyElementMaster@0$kCMIOObjectPropertyElementName@1818454126$kCMIOObjectPropertyElementNumberName@1818455662$kCMIOObjectPropertyElementWildcard@4294967295$kCMIOObjectPropertyListenerAdded@1818850145$kCMIOObjectPropertyListenerRemoved@1818850162$kCMIOObjectPropertyManufacturer@1819107691$kCMIOObjectPropertyName@1819173229$kCMIOObjectPropertyOwnedObjects@1870098020$kCMIOObjectPropertyOwner@1937007734$kCMIOObjectPropertyScopeGlobal@1735159650$kCMIOObjectPropertyScopeWildcard@707406378$kCMIOObjectPropertySelectorWildcard@707406378$kCMIOObjectSystemObject@1$kCMIOObjectUnknown@0$kCMIOOpticalFilterClassID@1869637236$kCMIOPanControlClassID@1885433376$kCMIOPanTiltAbsoluteControlClassID@1886675298$kCMIOPanTiltRelativeControlClassID@1886679660$kCMIOPlugInClassID@1634757735$kCMIOPlugInPropertyBundleID@1885956452$kCMIOPowerLineFrequencyControlClassID@1886873201$kCMIOSampleBufferDiscontinuityFlag_BufferOverrun@128$kCMIOSampleBufferDiscontinuityFlag_ClientSyncDiscontinuity@1024$kCMIOSampleBufferDiscontinuityFlag_CodecSettingsChanged@131072$kCMIOSampleBufferDiscontinuityFlag_DataFormatChanged@8192$kCMIOSampleBufferDiscontinuityFlag_DataWasDropped@64$kCMIOSampleBufferDiscontinuityFlag_DataWasFlushed@32$kCMIOSampleBufferDiscontinuityFlag_DiscontinuityInDTS@256$kCMIOSampleBufferDiscontinuityFlag_DurationWasExtended@32768$kCMIOSampleBufferDiscontinuityFlag_MalformedData@16$kCMIOSampleBufferDiscontinuityFlag_NoDataMarker@4096$kCMIOSampleBufferDiscontinuityFlag_PacketError@4$kCMIOSampleBufferDiscontinuityFlag_RelatedToDiscontinuity@512$kCMIOSampleBufferDiscontinuityFlag_SleepWakeCycle@65536$kCMIOSampleBufferDiscontinuityFlag_StreamDiscontinuity@8$kCMIOSampleBufferDiscontinuityFlag_TimecodeDiscontinuity@2$kCMIOSampleBufferDiscontinuityFlag_TimingReferenceJumped@16384$kCMIOSampleBufferDiscontinuityFlag_TrickPlay@2048$kCMIOSampleBufferDiscontinuityFlag_UnknownDiscontinuity@1$kCMIOSampleBufferNoDataEvent_DeviceDidNotSync@2$kCMIOSampleBufferNoDataEvent_DeviceInWrongMode@3$kCMIOSampleBufferNoDataEvent_NoMedia@1$kCMIOSampleBufferNoDataEvent_ProcessingError@4$kCMIOSampleBufferNoDataEvent_SleepWakeCycle@5$kCMIOSampleBufferNoDataEvent_Unknown@0$kCMIOSampleBufferNoDiscontinuities@0$kCMIOSaturationControlClassID@1935766645$kCMIOSelectorControlClassID@1936483188$kCMIOSelectorControlPropertyAvailableItems@1935892841$kCMIOSelectorControlPropertyCurrentItem@1935893353$kCMIOSelectorControlPropertyItemName@1935894894$kCMIOSharpnessControlClassID@1936224880$kCMIOShutterControlClassID@1936225394$kCMIOStreamClassID@1634956402$kCMIOStreamPropertyCanProcessDeckCommand@1885627236$kCMIOStreamPropertyClock@1886217068$kCMIOStreamPropertyDeck@1684366187$kCMIOStreamPropertyDeckCueing@1668638051$kCMIOStreamPropertyDeckDropness@1685221232$kCMIOStreamPropertyDeckFrameNumber@1952673636$kCMIOStreamPropertyDeckLocal@1819239276$kCMIOStreamPropertyDeckThreaded@1953002084$kCMIOStreamPropertyDeviceSyncTimeoutInMSec@1886219826$kCMIOStreamPropertyDirection@1935960434$kCMIOStreamPropertyEndOfData@1886217572$kCMIOStreamPropertyFirstOutputPresentationTimeStamp@1886351476$kCMIOStreamPropertyFormatDescription@1885762592$kCMIOStreamPropertyFormatDescriptions@1885762657$kCMIOStreamPropertyFrameRate@1852207732$kCMIOStreamPropertyFrameRateRanges@1718776423$kCMIOStreamPropertyFrameRates@1852207651$kCMIOStreamPropertyInitialPresentationTimeStampForLinkedAndSyncedAudio@1768975475$kCMIOStreamPropertyLatency@1819569763$kCMIOStreamPropertyMinimumFrameRate@1835430516$kCMIOStreamPropertyNoDataEventCount@1886219827$kCMIOStreamPropertyNoDataTimeoutInMSec@1886219825$kCMIOStreamPropertyOutputBufferQueueSize@1886220145$kCMIOStreamPropertyOutputBufferRepeatCount@1886220146$kCMIOStreamPropertyOutputBufferUnderrunCount@1886220149$kCMIOStreamPropertyOutputBuffersNeededForThrottledPlayback@1835624038$kCMIOStreamPropertyOutputBuffersRequiredForStartup@1886220147$kCMIOStreamPropertyPreferredFormatDescription@1886545508$kCMIOStreamPropertyPreferredFrameRate@1886545522$kCMIOStreamPropertyScheduledOutputNotificationProc@1936682608$kCMIOStreamPropertyStartingChannel@1935894638$kCMIOStreamPropertyStillImage@1937010023$kCMIOStreamPropertyStillImageFormatDescriptions@1937008244$kCMIOStreamPropertyTerminalType@1952805485$kCMIOStreamUnknown@0$kCMIOSystemObjectClassID@1634957683$kCMIOTemperatureControlClassID@1952804208$kCMIOTiltControlClassID@1953066100$kCMIOWhiteBalanceControlClassID@2003329644$kCMIOWhiteBalanceUControlClassID@2003329653$kCMIOWhiteBalanceVControlClassID@2003329654$kCMIOWhiteLevelControlClassID@2003332214$kCMIOZoomControlClassID@2054123373$kCMIOZoomRelativeControlClassID@2054122866$'''
misc.update({})
functions={'CMIOObjectShow': (sel32or64(b'vL', b'vI'),), 'CMIOStreamDeckJog': (sel32or64(b'lLl', b'iIi'),), 'CMIOObjectAddPropertyListenerBlock': (sel32or64(b'lL^{CMIOObjectPropertyAddress=LLL}@@?', b'iI^{CMIOObjectPropertyAddress=III}@@?'), '', {'arguments': {1: {'type_modifier': 'n'}, 3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}, 1: {'type': 'I'}, 2: {'type': '^{CMIOObjectPropertyAddress=III}', 'type_modifier': 'n', 'c_array_length_in_arg': 1}}}}}}), 'CMIOStreamDeckCueTo': (sel32or64(b'lLQZ', b'iIQZ'),), 'CMIOObjectGetPropertyData': (sel32or64(b'lL^{CMIOObjectPropertyAddress=LLL}L^vL^L^v', b'iI^{CMIOObjectPropertyAddress=III}I^vI^I^v'), '', {'arguments': {1: {'type_modifier': 'n'}, 3: {'c_array_length_in_arg': 2, 'type_modifier': 'o'}, 5: {'type_modifier': 'o'}, 6: {'c_array_length_in_arg': (4, 5), 'type_modifier': 'o'}}}), 'CMIOSampleBufferCreateForImageBuffer': (sel32or64(b'l^{__CFAllocator=}^{__CVBuffer=}^{opaqueCMFormatDescription=}^{_CMSampleTimingInfo={_CMTime=qiIq}{_CMTime=qiIq}{_CMTime=qiIq}}QL^^{opaqueCMSampleBuffer=}', b'i^{__CFAllocator=}^{__CVBuffer=}^{opaqueCMFormatDescription=}^{_CMSampleTimingInfo={_CMTime=qiIq}{_CMTime=qiIq}{_CMTime=qiIq}}QI^^{opaqueCMSampleBuffer=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {3: {'type_modifier': 'n'}, 6: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CMIOObjectRemovePropertyListener': (sel32or64(b'lL^{CMIOObjectPropertyAddress=LLL}^?^v', b'iI^{CMIOObjectPropertyAddress=III}^?^v'), '', {'arguments': {1: {'type_modifier': 'n'}, 2: {'callable': {'retval': {'type': b'i'}, 'arguments': {0: {'type': b'I'}, 1: {'type': b'I'}, 2: {'type': b'^{CMIOObjectPropertyAddress=III}'}, 3: {'type': b'^v'}}}}}}), 'CMIOSampleBufferCreateNoDataMarker': (sel32or64(b'l^{__CFAllocator=}L^{opaqueCMFormatDescription=}QL^^{opaqueCMSampleBuffer=}', b'i^{__CFAllocator=}I^{opaqueCMFormatDescription=}QI^^{opaqueCMSampleBuffer=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {5: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CMIOObjectGetPropertyDataSize': (sel32or64(b'lL^{CMIOObjectPropertyAddress=LLL}L^v^L', b'iI^{CMIOObjectPropertyAddress=III}I^v^I'), '', {'arguments': {1: {'type_modifier': 'n'}, 3: {'c_array_length_in_arg': 2, 'type_modifier': 'n'}, 4: {'type_modifier': 'o'}}}), 'CMIOStreamClockPostTimingEvent': (sel32or64(b'l{_CMTime=qiIq}QZ@', b'i{_CMTime=qiIq}QZ@'),), 'CMIODeviceStopStream': (sel32or64(b'lLL', b'iII'),), 'CMIODeviceStartStream': (sel32or64(b'lLL', b'iII'),), 'CMIOSampleBufferCreate': (sel32or64(b'l^{__CFAllocator=}^{OpaqueCMBlockBuffer=}^{opaqueCMFormatDescription=}LL^{_CMSampleTimingInfo={_CMTime=qiIq}{_CMTime=qiIq}{_CMTime=qiIq}}L^LQL^^{opaqueCMSampleBuffer=}', b'i^{__CFAllocator=}^{OpaqueCMBlockBuffer=}^{opaqueCMFormatDescription=}II^{_CMSampleTimingInfo={_CMTime=qiIq}{_CMTime=qiIq}{_CMTime=qiIq}}I^QQI^^{opaqueCMSampleBuffer=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {10: {'already_cfretained': True, 'type_modifier': 'o'}, 5: {'c_array_length_in_arg': 4, 'type_modifier': 'n'}, 7: {'c_array_length_in_arg': 6, 'type_modifier': 'n'}}}), 'CMIOStreamCopyBufferQueue': (sel32or64(b'lL^?^v^^{opaqueCMSimpleQueue=}', b'iI^?^v^^{opaqueCMSimpleQueue=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'I'}, 1: {'type': b'^v'}, 2: {'type': b'^v'}}}}, 3: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CMIOObjectAddPropertyListener': (sel32or64(b'lL^{CMIOObjectPropertyAddress=LLL}^?^v', b'iI^{CMIOObjectPropertyAddress=III}^?^v'), '', {'arguments': {1: {'type_modifier': 'n'}, 2: {'callable': {'retval': {'type': b'i'}, 'arguments': {0: {'type': b'I'}, 1: {'type': b'I'}, 2: {'type': b'^{CMIOObjectPropertyAddress=III}'}, 3: {'type': b'^v'}}}}}}), 'CMIOObjectHasProperty': (sel32or64(b'ZL^{CMIOObjectPropertyAddress=LLL}', b'ZI^{CMIOObjectPropertyAddress=III}'), '', {'arguments': {1: {'type_modifier': 'n'}}}), 'CMIOObjectIsPropertySettable': (sel32or64(b'lL^{CMIOObjectPropertyAddress=LLL}^Z', b'iI^{CMIOObjectPropertyAddress=III}^Z'), '', {'arguments': {1: {'type_modifier': 'n'}, 2: {'type_modifier': 'o'}}}), 'CMIOSampleBufferGetSequenceNumber': (b'Q^{opaqueCMSampleBuffer=}',), 'CMIOStreamClockCreate': (sel32or64(b'l^{__CFAllocator=}^{__CFString=}^v{_CMTime=qiIq}LL^@', b'i^{__CFAllocator=}^{__CFString=}^v{_CMTime=qiIq}II^@'), '', {'retval': {'already_cfretained': True}, 'arguments': {6: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CMIOStreamClockInvalidate': (sel32or64(b'l@', b'i@'),), 'CMIOObjectsPublishedAndDied': (sel32or64(b'l^^{CMIOHardwarePlugInInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}LL^LL^L', b'i^^{CMIOHardwarePlugInInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}II^II^I'),), 'CMIOObjectSetPropertyData': (sel32or64(b'lL^{CMIOObjectPropertyAddress=LLL}L^vL^v', b'iI^{CMIOObjectPropertyAddress=III}I^vI^v'),), 'CMIOSampleBufferGetDiscontinuityFlags': (sel32or64(b'L^{opaqueCMSampleBuffer=}', b'I^{opaqueCMSampleBuffer=}'),), 'CMIOStreamDeckPlay': (sel32or64(b'lL', b'iI'),), 'CMIOSampleBufferSetDiscontinuityFlags': (sel32or64(b'v^{__CFAllocator=}^{opaqueCMSampleBuffer=}L', b'v^{__CFAllocator=}^{opaqueCMSampleBuffer=}I'),), 'CMIOStreamDeckStop': (sel32or64(b'lL', b'iI'),), 'CMIOObjectPropertiesChanged': (sel32or64(b'l^^{CMIOHardwarePlugInInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}LL^{CMIOObjectPropertyAddress=LLL}', b'i^^{CMIOHardwarePlugInInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}II^{CMIOObjectPropertyAddress=III}'),), 'CMIOSampleBufferSetSequenceNumber': (b'v^{__CFAllocator=}^{opaqueCMSampleBuffer=}Q',), 'CMIOSampleBufferCopySampleAttachments': (sel32or64(b'l^{opaqueCMSampleBuffer=}^{opaqueCMSampleBuffer=}', b'i^{opaqueCMSampleBuffer=}^{opaqueCMSampleBuffer=}'), '', {'retval': {'already_cfretained': True}}), 'CMIOObjectCreate': (sel32or64(b'l^^{CMIOHardwarePlugInInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}LL^L', b'i^^{CMIOHardwarePlugInInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}II^I'), '', {'retval': {'already_cfretained': True}}), 'CMIOStreamClockConvertHostTimeToDeviceTime': (b'{_CMTime=qiIq}Q@',), 'CMIOObjectRemovePropertyListenerBlock': (sel32or64(b'lL^{CMIOObjectPropertyAddress=LLL}@@?', b'iI^{CMIOObjectPropertyAddress=III}@@?'), '', {'arguments': {1: {'type_modifier': 'n'}, 3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}, 1: {'type': 'I'}, 2: {'type': '^{CMIOObjectPropertyAddress=III}', 'type_modifier': 'n', 'c_array_length_in_arg': 1}}}}}}), 'CMIOSampleBufferCopyNonRequiredAttachments': (sel32or64(b'l^{opaqueCMSampleBuffer=}^{opaqueCMSampleBuffer=}I', b'i^{opaqueCMSampleBuffer=}^{opaqueCMSampleBuffer=}I'), '', {'retval': {'already_cfretained': True}})}
aliases = {'kCMIOStreamUnknown': 'kCMIOObjectUnknown', 'kCMIODeviceUnknown': 'kCMIOObjectUnknown'}
expressions = {}

# END OF FILE
