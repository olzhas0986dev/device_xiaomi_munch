#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/init/init.batterysecret.rc': blob_fixup()
        .regex_replace('.*seclabel u:r:batterysecret:s0\n', ''),
    'vendor/etc/libnfc-nci.conf': blob_fixup()
        .add_line_if_missing('LEGACY_MIFARE_READER=1'),
    'vendor/lib/hw/audio.primary.munch.so': blob_fixup()
        .binary_regex_replace(
            b'/vendor/lib/liba2dpoffload.so',
            b'liba2dpoffload_munch.so\x00\x00\x00\x00\x00\x00',
        ),
    'vendor/lib64/camera/components/com.mi.node.watermark.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
    'vendor/lib64/hw/camera.qcom.so': blob_fixup()
        .binary_regex_replace(
            b'\x73\x74\x5F\x6C\x69\x63\x65\x6E\x73\x65\x2E\x6C\x69\x63',
            b'\x63\x61\x6D\x65\x72\x61\x5F\x63\x6E\x66\x2E\x74\x78\x74',
        ),
    (
        'vendor/lib64/libMIAIHDRhvx_interface.so',
        'vendor/lib64/libarcsoft_hdrplus_hvx_stub.so',
    ): blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open'),
    (
        'vendor/lib64/libarcsoft_super_night_raw.so',
    ) : blob_fixup()
        .clear_symbol_version('rpcmem_alloc')
        .clear_symbol_version('rpcmem_free')
        .clear_symbol_version('rpcmem_to_fd'),
    'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so': blob_fixup()
        .binary_regex_replace(b'\x9A\x0A\x00\x94', b'\x1F\x20\x03\xD5'),
}  # fmt: skip

namespace_imports = [
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/qcom-caf/sm8250',
    'hardware/xiaomi',
    'vendor/qcom/opensource/display',
    'vendor/xiaomi/sm8250-common',
]

module = ExtractUtilsModule(
    'munch',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'sm8250-common', module.vendor)
    utils.run()
