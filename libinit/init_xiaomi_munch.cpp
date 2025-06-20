/*
 * Copyright (C) 2021 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <libinit_dalvik_heap.h>
#include <libinit_variant.h>

#include "vendor_init.h"

static const variant_info_t munch_in_info = {
    .hwc_value = "INDIA",
    .sku_value = "",
    
    .mod_device = "munchin",
    .name = "munchin",
    .brand = "POCO",
    .device = "munch",
    .marketname = "POCO F4",
    .model = "22021211RI",
    .build_fingerprint = "POCO/munch_in/munch:13/RKQ1.211001.001/V816.0.9.0.ULMMIXM:user/release-keys",

    .nfc = true,
};

static const variant_info_t munch_global_info = {
    .hwc_value = "GLOBAL",
    .sku_value = "",
    
    .mod_device = "munch_global",
    .name = "munch_global",
    .brand = "POCO",
    .device = "munch",
    .marketname = "POCO F4",
    .model = "22021211RG",
    .build_fingerprint = "POCO/munch_global/munch:13/RKQ1.211001.001/V816.0.9.0.ULMMIXM:user/release-keys",

    .nfc = true,
};

static const variant_info_t munch_info = {
    .hwc_value = "",
    .sku_value = "",
    
    .mod_device = "munch",
    .name = "munch",
    .brand = "Redmi",
    .device = "munch",
    .marketname = "Redmi K40S",
    .model = "22021211RC",
    .build_fingerprint = "Redmi/munch/munch:13/RKQ1.211001.001/V816.0.9.0.ULMMIXM:user/release-keys",

    .nfc = true,
};

static const std::vector<variant_info_t> variants = {
    munch_in_info,
    munch_global_info,
    munch_info,
};

void vendor_load_properties() {
    search_variant(variants);
    set_dalvik_heap();
}
