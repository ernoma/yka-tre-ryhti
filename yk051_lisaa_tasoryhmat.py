import requests
from requests.auth import HTTPBasicAuth
import pprint

layer_groups_ehdotus = [
    'yk051_k1_yhdyskuntarakenne_ehdotus',
    'yk051_k2_viherymparisto_ja_vapaa_ajan_palvelut_ehdotus',
    'yk051_k3_kulttuuriperinto_ehdotus',
    'yk051_k4_kestava_vesitalous_ymparistoterveys_ja_yhdyskuntatekninen_huolto_ehdotus',
    'yk051_k5_osa_alueiden_kehittamisperiaatteet_ehdotus',
    'yk051_kumoutuvat_yk047_ehdotus_layergroup',
    'yk051_kumoutuvat_yk048_ehdotus_layergroup',
    'yk051_kumoutuvat_yk049_ehdotus_layergroup',
    'yk051_ehdotus_yhdistelma_k4_kestava_vesitalous_ymparistoterveys_ja_yhdyskuntatekninen_huolto',
    'yk051_ehdotus_yhdistelma_k3_kulttuuriperinto',
    'yk051_ehdotus_yhdistelma_k2_viherymparisto_ja_vapaa_ajan_palvelut',
    'yk051_ehdotus_yhdistelma_k1_yhdyskuntarakenne',
    'yk051_ehdotus_yhdistelma_keskusta_k1_maankaytto',
    'yk051_ehdotus_yhdistelma_keskusta_k2_liikenne'
]

layer_groups = [
    { 'name': 'yk051_t_ehdotus_k1_yhdyskuntarakenne_layergroup' ,
     'title': 'Kartta 1 – Yhdyskuntarakenne - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_k2_viherymparisto_ja_vapaa_ajan_palvelut_layergroup' ,
     'title': 'Kartta 2 – Viherympäristö ja vapaa-ajan palvelut - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_k3_kulttuuriperinto_layergroup' ,
     'title': 'Kartta 3 – Kulttuuriperintö - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_k4_kestava_vesitalous_ymparistoterveys_ja_yhdyskuntatekninen_huolto_layergroup' ,
     'title': 'Kartta 4 – Kestävä vesitalous, ympäristöterveys ja yhdyskuntatekninen huolto - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_k5_osa_alueiden_kehittamisperiaatteet_layergroup' ,
     'title': 'Kartta 5 – Osa-alueiden kehittämisperiaatteet - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_kumoutuvat_yk047_layergroup' ,
     'title': 'Kumottavien merkintöjen kartta Kantakaupungin yleiskaavan 2040 merkinnöille - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_kumoutuvat_yk048_layergroup' ,
     'title': 'Kumottavien merkintöjen kartta Keskustan strategisen osayleiskaavan merkinnöille - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_kumoutuvat_yk049_layergroup' ,
     'title': 'Kumottavien merkintöjen kartta Kantakaupungin vaiheyleiskaavan - valtuustokausi 2017-2021 merkinnöille - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_yhdistelma_k4_kestava_vesitalous_ymparistoterveys_ja_yhdyskuntatekninen_huolto_layergroup' ,
     'title': 'Kartta 4 – Kestävä vesitalous, ympäristöterveys ja yhdyskuntatekninen huolto - Kaavayhdistelmä - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_yhdistelma_k3_kulttuuriperinto_layergroup' ,
     'title': 'Kartta 3 – Kulttuuriperintö - Kaavayhdistelmä - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_yhdistelma_k2_viherymparisto_ja_vapaa_ajan_palvelut_layergroup' ,
     'title': 'Kartta 2 – Viherympäristö ja vapaa-ajan palvelut - Kaavayhdistelmä - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_yhdistelma_k1_yhdyskuntarakenne_layergroup' ,
     'title': 'Kartta 1 – Yhdyskuntarakenne - Kaavayhdistelmä - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_yhdistelma_keskusta_k1_maankaytto_layergroup' ,
     'title': 'Keskusta - Kartta 1 - Maankäyttö yhdistelmä - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     },
    { 'name': 'yk051_t_ehdotus_yhdistelma_keskusta_k2_liikenne_layergroup' ,
     'title': 'Keskusta - Kartta 2 - Liikenne yhdistelmä - Tarkistettu ehdotus - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025'
     }
]


layers_ehdotus = [
    "yk051_ehdotus_k1_apugeometria_point_view",
    "yk051_ehdotus_k2_apugeometria_point_view",
    "yk051_ehdotus_k3_apugeometria_point_view",
    "yk051_ehdotus_k3_apugeometria_line_view",
    "yk051_ehdotus_k4_apugeometria_point_view",
    "yk051_ehdotus_k4_apugeometria_viiva_view",
    "yk051_ehdotus_k5_apugeometria_point_view",
    "yk051_ehdotus_k5_keskusta_apugeometria_point_view",
    "yk051_ehdotus_k5_keskusta_apugeometria_viiva_view",

    "yk051_ehdotus_k5_keskusta_aluev_polygon_view",
    "yk051_ehdotus_k5_keskusta_tayd_aluek_polygon_view",
    "yk051_ehdotus_k5_keskusta_viivak_line_view",
    "yk051_ehdotus_k5_keskusta_viivak_jk_yht_tarve_line_view",
    "yk051_ehdotus_k5_keskusta_pistek_point_view",
    
    "yk051_ehdotus_k5_osa_alue_rajaukset_polygon_view",
    "yk051_ehdotus_k5_keskusta_maankaytto_kaavan_ulkorajaus_view",
    "yk051_ehdotus_k5_keskusta_liikenne_kaavan_ulkorajaus_view",
    
    "yk051_ehdotus_k1_aluevaraukset_polygon_view",
    "yk051_ehdotus_k1_taydentavat_aluekohteet_polygon_view",
    "yk051_ehdotus_k1_viivakohteet_line_view",
    "yk051_ehdotus_k1_pistekohteet_point_view",
    "yk051_ehdotus_k2_aluevaraukset_polygon_view",
    "yk051_ehdotus_k2_taydentavat_aluekohteet_polygon_view",
    "yk051_ehdotus_k2_viivakohteet_line_view",
    "yk051_ehdotus_k2_pistekohteet_point_view",
    "yk051_ehdotus_k3_aluevaraukset_polygon_view",
    "yk051_ehdotus_k3_taydentavat_aluekohteet_polygon_view",
    "yk051_ehdotus_k3_viivakohteet_line_view",
    "yk051_ehdotus_k3_pistekohteet_point_view",
    "yk051_ehdotus_k4_taydentavat_aluekohteet_polygon_view",
    "yk051_ehdotus_k4_viivakohteet_line_view",
    "yk051_ehdotus_k4_pistekohteet_point_view",
    "yk051_ehdotus_k5_aluevaraukset_polygon_view",
    "yk051_ehdotus_k5_taydentavat_aluekohteet_polygon_view",
    "yk051_ehdotus_k5_viivakohteet_line_view",
    "yk051_ehdotus_k5_pistekohteet_point_view",

    "yk051_ehdotus_kaavan_ulkorajaus_view",
    "yk051_ehdotus_k1_kaavan_ulkorajaus_view",
    "yk051_ehdotus_k2_kaavan_ulkorajaus_view",
    "yk051_ehdotus_k3_kaavan_ulkorajaus_view",
    "yk051_ehdotus_k4_kaavan_ulkorajaus_view",
    "yk051_ehdotus_k5_kaavan_ulkorajaus_view",

    "yk051_ehdotus_kumout_apugeometria_point_view",
    "yk051_ehdotus_kumout_apugeometria_line_view",
    "yk051_ehdotus_kumout_yk047_k4_apugeometria_line_view",
    "yk051_ehdotus_kumout_yk048_apugeometria_point_view",

    "yk051_ehdotus_kumout_yk047_kaavaobjekti_alue_view",
    "yk051_ehdotus_kumout_yk047_kaavaobjekti_alue_tayd_view",
    "yk051_ehdotus_kumout_yk047_kaavaobjekti_viiva_view",
    "yk051_ehdotus_kumout_yk047_kaavaobjekti_piste_view",
    "yk051_ehdotus_kumout_yk048_kaavaobjekti_alue_view",
    "yk051_ehdotus_kumout_yk048_kaavaobjekti_alue_tayd_view",
    "yk051_ehdotus_kumout_yk048_kaavaobjekti_viiva_view",
    "yk051_ehdotus_kumout_yk048_kaavaobjekti_piste_view",
    "yk051_ehdotus_kumout_yk049_kaavaobjekti_alue_view",
    "yk051_ehdotus_kumout_yk049_kaavaobjekti_alue_tayd_view",
    "yk051_ehdotus_kumout_yk049_kaavaobjekti_viiva_view",
    "yk051_ehdotus_kumout_yk049_kaavaobjekti_piste_view",

    "yk051_ehdotus_kumout_yk047_kaavan_ulkorajaus_view",
    "yk051_ehdotus_kumout_yk048_kaavan_ulkorajaus_view",
    "yk051_ehdotus_kumout_yk049_kaavan_ulkorajaus_view",

    "yk051_ehdotus_yk2040_k1_voimaan_jaavat_apugeometria_piste_point",
    "yk051_ehdotus_yk2040_k1_voimaan_jaavat_kalue_polygon_view",
    "yk051_ehdotus_yk2040_k2_voimaan_jaavat_kalue_polygon_view",
    "yk051_ehdotus_yk2040_k3_voimaan_jaavat_kalue_polygon_view",
    "yk051_ehdotus_yk2040_k4_voimaan_jaavat_kalue_polygon_view",
    "yk051_ehdotus_yk2040_k1_voimaan_jaavat_kalue_taydentava_polygon",
    "yk051_ehdotus_yk2040_k2_voimaan_jaavat_kalue_taydentava_polygon",
    "yk051_ehdotus_yk2040_k3_voimaan_jaavat_kalue_taydentava_polygon",
    "yk051_ehdotus_yk2040_k4_voimaan_jaavat_kalue_taydentava_polygon",
    "yk051_ehdotus_yk2040_k1_voimaan_jaavat_kviiva_line_view",
    "yk051_ehdotus_yk2040_k2_voimaan_jaavat_kviiva_line_view",
    "yk051_ehdotus_yk2040_k3_voimaan_jaavat_kviiva_line_view",
    "yk051_ehdotus_yk2040_k4_voimaan_jaavat_kviiva_line_view",
    "yk051_ehdotus_yk2040_k1_voimaan_jaavat_kpiste_point_view",
    "yk051_ehdotus_yk2040_k2_voimaan_jaavat_kpiste_point_view",
    "yk051_ehdotus_yk2040_k3_voimaan_jaavat_kpiste_point_view",
    "yk051_ehdotus_yk2040_k4_voimaan_jaavat_kpiste_point_view",
    "yk051_ehdotus_yk2040_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_ehdotus_yk2040_k1_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_ehdotus_yk2040_k2_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_ehdotus_yk2040_k3_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_ehdotus_yk2040_k4_voimaan_jaavat_kaavan_ulkorajaus_view",

    "yk051_ehdotus_yk048_k2_voimaan_jaavat_apugeometria_point_view",
    "yk051_ehdotus_yk048_k1_voimaan_jaavat_kalue_polygon_view",
    # "yk051_ehdotus_yk048_k2_voimaan_jaavat_kalue_polygon_view",
    "yk051_ehdotus_yk048_k1_voimaan_jaavat_kalue_taydentava_polygon_",
    "yk051_ehdotus_yk048_k2_voimaan_jaavat_kalue_taydentava_polygon_",
    # "yk051_ehdotus_yk048_k1_voimaan_jaavat_kviiva_line_view",
    "yk051_ehdotus_yk048_k2_voimaan_jaavat_kviiva_line_view",
    "yk051_ehdotus_yk048_k1_voimaan_jaavat_kpiste_point_view",
    "yk051_ehdotus_yk048_k2_voimaan_jaavat_kpiste_point_view",
    "yk051_ehdotus_yk048_k1_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_ehdotus_yk048_k2_voimaan_jaavat_kaavan_ulkorajaus_view",

    "yk051_ehdotus_yk049_k1_voimaan_jaavat_apugeometria_piste_point_",
    "yk051_ehdotus_yk049_k4_voimaan_jaavat_apugeometria_piste_point_",
    "yk051_ehdotus_yk049_k1_voimaan_jaavat_kalue_polygon_view",
    "yk051_ehdotus_yk049_k2_voimaan_jaavat_kalue_polygon_view",
    "yk051_ehdotus_yk049_k3_voimaan_jaavat_kalue_polygon_view",
    "yk051_ehdotus_yk049_k4_voimaan_jaavat_kalue_polygon_view",
    "yk051_ehdotus_yk049_k1_voimaan_jaavat_kalue_taydentava_polygon_",
    "yk051_ehdotus_yk049_k2_voimaan_jaavat_kalue_taydentava_polygon_",
    "yk051_ehdotus_yk049_k3_voimaan_jaavat_kalue_taydentava_polygon_",
    "yk051_ehdotus_yk049_k4_voimaan_jaavat_kalue_taydentava_polygon_",
    "yk051_ehdotus_yk049_k1_voimaan_jaavat_kviiva_line_view",
    "yk051_ehdotus_yk049_k2_voimaan_jaavat_kviiva_line_view",
    "yk051_ehdotus_yk049_k3_voimaan_jaavat_kviiva_line_view",
    "yk051_ehdotus_yk049_k4_voimaan_jaavat_kviiva_line_view",
    "yk051_ehdotus_yk049_k1_voimaan_jaavat_kpiste_point_view",
    "yk051_ehdotus_yk049_k2_voimaan_jaavat_kpiste_point_view",
    "yk051_ehdotus_yk049_k3_voimaan_jaavat_kpiste_point_view",
    "yk051_ehdotus_yk049_k4_voimaan_jaavat_kpiste_point_view",
    "yk051_ehdotus_yk049_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_ehdotus_yk049_k1_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_ehdotus_yk049_k2_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_ehdotus_yk049_k3_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_ehdotus_yk049_k4_voimaan_jaavat_kaavan_ulkorajaus_view",

    "yk051_ehdotus_k5_keskusta_liikenne_tayd_aluek_polygon_view",
    "yk051_ehdotus_k5_keskusta_liikenne_viivak_line_view",
    "yk051_ehdotus_k5_keskusta_liikenne_pistek_point_view",

    "yk051_ehdotus_k5_keskusta_maankaytto_tayd_aluek_polygon_view",
    "yk051_ehdotus_k5_keskusta_maankaytto_viivak_line_view",
    "yk051_ehdotus_k5_keskusta_maankaytto_pistek_point_view",

    "yk051_ehdotus_k5_keskusta_liikenne_apugeometria_point_view",
    "yk051_ehdotus_k5_keskusta_liikenne_apugeometria_viiva_view",

    "yk051_ehdotus_k5_keskusta_maankaytto_apugeometria_point_view",
    "yk051_ehdotus_k5_keskusta_maankaytto_apugeometria_viiva_view"
]


layers = [
    "yk051_t_ehdotus_k1_apugeometria_point_view",
    "yk051_t_ehdotus_k2_apugeometria_point_view",
    "yk051_t_ehdotus_k3_apugeometria_point_view",
    "yk051_t_ehdotus_k3_apugeometria_line_view",
    "yk051_t_ehdotus_k4_apugeometria_point_view",
    "yk051_t_ehdotus_k4_apugeometria_viiva_view",
    "yk051_t_ehdotus_k5_apugeometria_point_view",
    "yk051_t_ehdotus_k5_keskusta_apugeometria_point_view",
    "yk051_t_ehdotus_k5_keskusta_apugeometria_viiva_view",

    "yk051_t_ehdotus_k5_keskusta_aluev_polygon_view",
    "yk051_t_ehdotus_k5_keskusta_tayd_aluek_polygon_view",
    "yk051_t_ehdotus_k5_keskusta_viivak_line_view",
    "yk051_t_ehdotus_k5_keskusta_viivak_jk_yht_tarve_line_view",
    "yk051_t_ehdotus_k5_keskusta_pistek_point_view",
    
    "yk051_t_ehdotus_k5_osa_alue_rajaukset_polygon_view",
    "yk051_t_ehdotus_k5_keskusta_maankaytto_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_k5_keskusta_liikenne_kaavan_ulkorajaus_view",
    
    "yk051_t_ehdotus_k1_aluevaraukset_polygon_view",
    "yk051_t_ehdotus_k1_taydentavat_aluekohteet_polygon_view",
    "yk051_t_ehdotus_k1_viivakohteet_line_view",
    "yk051_t_ehdotus_k1_pistekohteet_point_view",
    "yk051_t_ehdotus_k2_aluevaraukset_polygon_view",
    "yk051_t_ehdotus_k2_taydentavat_aluekohteet_polygon_view",
    "yk051_t_ehdotus_k2_viivakohteet_line_view",
    "yk051_t_ehdotus_k2_pistekohteet_point_view",
    "yk051_t_ehdotus_k3_aluevaraukset_polygon_view",
    "yk051_t_ehdotus_k3_taydentavat_aluekohteet_polygon_view",
    "yk051_t_ehdotus_k3_viivakohteet_line_view",
    "yk051_t_ehdotus_k3_pistekohteet_point_view",
    "yk051_t_ehdotus_k4_taydentavat_aluekohteet_polygon_view",
    "yk051_t_ehdotus_k4_viivakohteet_line_view",
    "yk051_t_ehdotus_k4_pistekohteet_point_view",
    "yk051_t_ehdotus_k5_aluevaraukset_polygon_view",
    "yk051_t_ehdotus_k5_taydentavat_aluekohteet_polygon_view",
    "yk051_t_ehdotus_k5_viivakohteet_line_view",
    "yk051_t_ehdotus_k5_pistekohteet_point_view",

    "yk051_t_ehdotus_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_k1_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_k2_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_k3_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_k4_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_k5_kaavan_ulkorajaus_view",

    "yk051_t_ehdotus_kumout_apugeometria_point_view",
    "yk051_t_ehdotus_kumout_apugeometria_line_view",
    "yk051_t_ehdotus_kumout_yk047_k4_apugeometria_line_view",
    "yk051_t_ehdotus_kumout_yk048_apugeometria_point_view",

    "yk051_t_ehdotus_kumout_yk047_kaavaobjekti_alue_view",
    "yk051_t_ehdotus_kumout_yk047_kaavaobjekti_alue_tayd_view",
    "yk051_t_ehdotus_kumout_yk047_kaavaobjekti_viiva_view",
    "yk051_t_ehdotus_kumout_yk047_kaavaobjekti_piste_view",
    "yk051_t_ehdotus_kumout_yk048_kaavaobjekti_alue_view",
    "yk051_t_ehdotus_kumout_yk048_kaavaobjekti_alue_tayd_view",
    "yk051_t_ehdotus_kumout_yk048_kaavaobjekti_viiva_view",
    "yk051_t_ehdotus_kumout_yk048_kaavaobjekti_piste_view",
    "yk051_t_ehdotus_kumout_yk049_kaavaobjekti_alue_view",
    "yk051_t_ehdotus_kumout_yk049_kaavaobjekti_alue_tayd_view",
    "yk051_t_ehdotus_kumout_yk049_kaavaobjekti_viiva_view",
    "yk051_t_ehdotus_kumout_yk049_kaavaobjekti_piste_view",

    "yk051_t_ehdotus_kumout_yk047_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_kumout_yk048_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_kumout_yk049_kaavan_ulkorajaus_view",

    "yk051_t_ehdotus_yk2040_k1_voimaan_jaavat_apugeometria_piste_poi",
    "yk051_t_ehdotus_yk2040_k1_voimaan_jaavat_kalue_polygon_view",
    "yk051_t_ehdotus_yk2040_k2_voimaan_jaavat_kalue_polygon_view",
    "yk051_t_ehdotus_yk2040_k3_voimaan_jaavat_kalue_polygon_view",
    "yk051_t_ehdotus_yk2040_k4_voimaan_jaavat_kalue_polygon_view",
    "yk051_t_ehdotus_yk2040_k1_voimaan_jaavat_kalue_taydentava_polyg",
    "yk051_t_ehdotus_yk2040_k2_voimaan_jaavat_kalue_taydentava_polyg",
    "yk051_t_ehdotus_yk2040_k3_voimaan_jaavat_kalue_taydentava_polyg",
    "yk051_t_ehdotus_yk2040_k4_voimaan_jaavat_kalue_taydentava_polyg",
    "yk051_t_ehdotus_yk2040_k1_voimaan_jaavat_kviiva_line_view",
    "yk051_t_ehdotus_yk2040_k2_voimaan_jaavat_kviiva_line_view",
    "yk051_t_ehdotus_yk2040_k3_voimaan_jaavat_kviiva_line_view",
    "yk051_t_ehdotus_yk2040_k4_voimaan_jaavat_kviiva_line_view",
    "yk051_t_ehdotus_yk2040_k1_voimaan_jaavat_kpiste_point_view",
    "yk051_t_ehdotus_yk2040_k2_voimaan_jaavat_kpiste_point_view",
    "yk051_t_ehdotus_yk2040_k3_voimaan_jaavat_kpiste_point_view",
    "yk051_t_ehdotus_yk2040_k4_voimaan_jaavat_kpiste_point_view",
    "yk051_t_ehdotus_yk2040_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_yk2040_k1_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_yk2040_k2_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_yk2040_k3_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_yk2040_k4_voimaan_jaavat_kaavan_ulkorajaus_view",

    "yk051_t_ehdotus_yk048_k2_voimaan_jaavat_apugeometria_point_view",
    "yk051_t_ehdotus_yk048_k1_voimaan_jaavat_kalue_polygon_view",
    # "yk051_t_ehdotus_yk048_k2_voimaan_jaavat_kalue_polygon_view",
    "yk051_t_ehdotus_yk048_k1_voimaan_jaavat_kalue_taydentava_polygo",
    "yk051_t_ehdotus_yk048_k2_voimaan_jaavat_kalue_taydentava_polygo",
    # "yk051_t_ehdotus_yk048_k1_voimaan_jaavat_kviiva_line_view",
    "yk051_t_ehdotus_yk048_k2_voimaan_jaavat_kviiva_line_view",
    "yk051_t_ehdotus_yk048_k1_voimaan_jaavat_kpiste_point_view",
    "yk051_t_ehdotus_yk048_k2_voimaan_jaavat_kpiste_point_view",
    "yk051_t_ehdotus_yk048_k1_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_yk048_k2_voimaan_jaavat_kaavan_ulkorajaus_view",

    "yk051_t_ehdotus_yk049_k1_voimaan_jaavat_apugeometria_piste_poin",
    "yk051_t_ehdotus_yk049_k4_voimaan_jaavat_apugeometria_piste_poin",
    "yk051_t_ehdotus_yk049_k1_voimaan_jaavat_kalue_polygon_view",
    "yk051_t_ehdotus_yk049_k2_voimaan_jaavat_kalue_polygon_view",
    "yk051_t_ehdotus_yk049_k3_voimaan_jaavat_kalue_polygon_view",
    "yk051_t_ehdotus_yk049_k4_voimaan_jaavat_kalue_polygon_view",
    "yk051_t_ehdotus_yk049_k1_voimaan_jaavat_kalue_taydentava_polygo",
    "yk051_t_ehdotus_yk049_k2_voimaan_jaavat_kalue_taydentava_polygo",
    "yk051_t_ehdotus_yk049_k3_voimaan_jaavat_kalue_taydentava_polygo",
    "yk051_t_ehdotus_yk049_k4_voimaan_jaavat_kalue_taydentava_polygo",
    "yk051_t_ehdotus_yk049_k1_voimaan_jaavat_kviiva_line_view",
    "yk051_t_ehdotus_yk049_k2_voimaan_jaavat_kviiva_line_view",
    "yk051_t_ehdotus_yk049_k3_voimaan_jaavat_kviiva_line_view",
    "yk051_t_ehdotus_yk049_k4_voimaan_jaavat_kviiva_line_view",
    "yk051_t_ehdotus_yk049_k1_voimaan_jaavat_kpiste_point_view",
    "yk051_t_ehdotus_yk049_k2_voimaan_jaavat_kpiste_point_view",
    "yk051_t_ehdotus_yk049_k3_voimaan_jaavat_kpiste_point_view",
    "yk051_t_ehdotus_yk049_k4_voimaan_jaavat_kpiste_point_view",
    "yk051_t_ehdotus_yk049_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_yk049_k1_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_yk049_k2_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_yk049_k3_voimaan_jaavat_kaavan_ulkorajaus_view",
    "yk051_t_ehdotus_yk049_k4_voimaan_jaavat_kaavan_ulkorajaus_view",

    "yk051_t_ehdotus_k5_keskusta_liikenne_tayd_aluek_polygon_view",
    "yk051_t_ehdotus_k5_keskusta_liikenne_viivak_line_view",
    "yk051_t_ehdotus_k5_keskusta_liikenne_pistek_point_view",

    "yk051_t_ehdotus_k5_keskusta_maankaytto_tayd_aluek_polygon_view",
    "yk051_t_ehdotus_k5_keskusta_maankaytto_viivak_line_view",
    "yk051_t_ehdotus_k5_keskusta_maankaytto_pistek_point_view",

    "yk051_t_ehdotus_k5_keskusta_liikenne_apugeometria_point_view",
    "yk051_t_ehdotus_k5_keskusta_liikenne_apugeometria_viiva_view",

    "yk051_t_ehdotus_k5_keskusta_maankaytto_apugeometria_point_view",
    "yk051_t_ehdotus_k5_keskusta_maankaytto_apugeometria_viiva_view"
]


username = ''
password = ''


for idx, layer_group in enumerate(layer_groups):
    url = "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/layergroups/" + layer_groups_ehdotus[idx] + ".json"

    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    response_code = response.status_code
    if response_code != 200:
        print(url)
        print(str(response_code))
    else:
        json_lg = response.json()
        json_lg['layerGroup']['name'] = layer_group['name']
        json_lg['layerGroup']['title'] = layer_group['title']
        json_lg['layerGroup']['abstractTxt'] = "Kantakaupungin vaiheyleiskaavan - valtuustokausi 2021-2025 (yk051) tarkistetun ehdotuksen kartta.\r\n\r\nYlläpito: yleiskaavoitus"

        for idx2, published in enumerate(json_lg['layerGroup']['publishables']['published']):
            old_name = published["name"]
            for idx3, layer_ehdotus in enumerate(layers_ehdotus):
                if ("yleiskaavoitus:" + layer_ehdotus) == old_name:
                    new_name = "yleiskaavoitus:" + layers[idx3]
                    json_lg['layerGroup']['publishables']['published'][idx2]["name"] = new_name
                    old_href = json_lg['layerGroup']['publishables']['published'][idx2]["href"]
                    old_href_parts = old_href.split('/')
                    new_href = ''
                    for old_href_part in old_href_parts[:-1]:
                        new_href = new_href + '/' + old_href_part
                    new_href = new_href + '/' + layers[idx3] + ".json"
                    json_lg['layerGroup']['publishables']['published'][idx2]["href"] = new_href
                    break
        
        if 'dateCreated' in json_lg['layerGroup']:
            json_lg['layerGroup'].pop('dateCreated')
        # pprint.pp(json_lg)
        # break

        url = "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/layergroups"
        response = requests.post(url, json=json_lg, auth=HTTPBasicAuth(username, password))
        # response = requests.get("https://api.github.com")
        response_code = response.status_code
        if response_code != 201:
            print(layer_group)
            print(str(response_code))
            pprint.pp(json_lg)

    # break


# Säädetään oikeudet lisätyille tasoille
url_security = "http://geodata.tampere.fi/geoserver/rest/security/acl/layers"
json_data_security = {}

for layer_group in layer_groups:
    json_data_security['yleiskaavoitus.' + layer_group['name'] + '.r' ] = 'ROLE_YLEISKAAVA_SISAINEN'
# json_data_security = json.dumps(data_security)

# headers = {'Content-Type': 'application/xml'}
response = requests.post(url_security, json=json_data_security, auth=HTTPBasicAuth(username, password))
# response = requests.get("https://api.github.com")
response_code = response.status_code
if response_code != 200:
    print(url_security)
    print(str(response_code))

# json_layergroup = {
# {
#     "layerGroup": {
#         "name": "yk051_k1_yhdyskuntarakenne_ehdotus",
#         "mode": "NAMED",
#         "title": "Kartta 1 - Tarkistettu ehdotus – Yhdyskuntarakenne - Kantakaupungin vaiheyleiskaava – valtuustokausi 2021-2025",
#         "abstractTxt": "Kantakaupungin vaiheyleiskaavan - valtuustokausi 2021-2025 (yk051) ehdotuksen kartta.\r\n\r\nYlläpito: yleiskaavoitus",
#         "workspace": {
#             "name": "yleiskaavoitus"
#         },
#         "publishables": {
#             "published": [
#                 {
#                     "@type": "layer",
#                     "name": "yleiskaavoitus:yk051_ehdotus_kaavan_ulkorajaus_view",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/layers/yk051_ehdotus_kaavan_ulkorajaus_view.json"
#                 },
#                 {
#                     "@type": "layer",
#                     "name": "yleiskaavoitus:yk051_ehdotus_k1_kaavan_ulkorajaus_view",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/layers/yk051_ehdotus_k1_kaavan_ulkorajaus_view.json"
#                 },
#                 {
#                     "@type": "layer",
#                     "name": "yleiskaavoitus:yk051_ehdotus_k1_aluevaraukset_polygon_view",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/layers/yk051_ehdotus_k1_aluevaraukset_polygon_view.json"
#                 },
#                 {
#                     "@type": "layer",
#                     "name": "yleiskaavoitus:yk051_ehdotus_k1_taydentavat_aluekohteet_polygon_view",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/layers/yk051_ehdotus_k1_taydentavat_aluekohteet_polygon_view.json"
#                 },
#                 {
#                     "@type": "layer",
#                     "name": "yleiskaavoitus:yk051_ehdotus_k1_viivakohteet_line_view",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/layers/yk051_ehdotus_k1_viivakohteet_line_view.json"
#                 },
#                 {
#                     "@type": "layer",
#                     "name": "yleiskaavoitus:yk051_ehdotus_k1_pistekohteet_point_view",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/layers/yk051_ehdotus_k1_pistekohteet_point_view.json"
#                 }
#             ]
#         },
#         "styles": {
#             "style": [
#                 {
#                     "name": "yleiskaavoitus:yk051_kaavan_ulkorajaus_30m",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/styles/yk051_kaavan_ulkorajaus_30m.json"
#                 },
#                 {
#                     "name": "yleiskaavoitus:yk051_kaavan_ulkorajaus",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/styles/yk051_kaavan_ulkorajaus.json"
#                 },
#                 {
#                     "name": "yleiskaavoitus:yk051_k1_aluevaraukset_polygon_luonnos_view",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/styles/yk051_k1_aluevaraukset_polygon_luonnos_view.json"
#                 },
#                 {
#                     "name": "yleiskaavoitus:yk051_k1_taydentavat_aluekohteet_polygon_luonnos_view",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/styles/yk051_k1_taydentavat_aluekohteet_polygon_luonnos_view.json"
#                 },
#                 {
#                     "name": "yleiskaavoitus:yk051_k1_viivakohteet_line_luonnos_view",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/styles/yk051_k1_viivakohteet_line_luonnos_view.json"
#                 },
#                 {
#                     "name": "yleiskaavoitus:yk051_k1_pistekohteet_point_luonnos_view",
#                     "href": "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/styles/yk051_k1_pistekohteet_point_luonnos_view.json"
#                 }
#             ]
#         },
#         "bounds": {
#             "minx": 2.4471982380158763E7,
#             "maxx": 2.4528017619841237E7,
#             "miny": 6638475.265834785,
#             "maxy": 7639659.41418248,
#             "crs": {
#                 "@class": "projected",
#                 "$": "EPSG:3878"
#             }
#         },
#         "dateCreated": "2023-09-19 10:56:03.546 UTC"
#     }
# }

