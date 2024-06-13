

import requests
from requests.auth import HTTPBasicAuth
import json


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


url_add_layer = "http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/datastores/postgis_yk051_kantakaupunki_2021_2025/featuretypes/" 

for layer in layers:
    xml_featuretype = "<featureType><name>" + layer + "</name><nativeName>" + layer + "</nativeName><abstract>Ylläpito: yleiskaavoitus</abstract></featureType>"
    
    headers = {'Content-Type': 'application/xml'}
    response = requests.post(url_add_layer, data=xml_featuretype.encode('utf-8'), headers=headers, auth=HTTPBasicAuth(username, password))
    # response = requests.get("https://api.github.com")
    response_code = response.status_code
    if response_code != 201:
        print(url_add_layer)
        print(layer)
        print(str(response_code))


# Säädetään oikeudet lisätyille tasoille
url_security = "http://geodata.tampere.fi/geoserver/rest/security/acl/layers"
json_data_security = {}

for layer in layers:
    json_data_security['yleiskaavoitus.' + layer + '.r' ] = 'ROLE_YLEISKAAVA_SISAINEN'
# json_data_security = json.dumps(data_security)

# headers = {'Content-Type': 'application/xml'}
response = requests.post(url_security, json=json_data_security, auth=HTTPBasicAuth(username, password))
# response = requests.get("https://api.github.com")
response_code = response.status_code
if response_code != 200:
    print(url_security)
    print(str(response_code))

for idx, layer in enumerate(layers):
    layer_ehdotus = layers_ehdotus[idx]

    url_layer = 'http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/layers/' + layer_ehdotus + '.json'

    response = requests.get(url_layer, auth=HTTPBasicAuth(username, password))
    response_code = response.status_code
    if response_code != 200:
        print(url_layer)
        print(str(response_code))
    else:
        json_layer = response.json()
        default_style = json_layer['layer']['defaultStyle']
        # print(default_style)
        json_layer = {
            'layer': {
                'name': layer,
                "workspace": "yleiskaavoitus",
                'defaultStyle': default_style
            }
        }

        url_layer = 'http://geodata.tampere.fi/geoserver/rest/workspaces/yleiskaavoitus/layers/' + layer + '.json'

        response = requests.put(url_layer, json=json_layer, auth=HTTPBasicAuth(username, password))
        response_code = response.status_code
        if response_code != 200:
            print(url_layer)
            print(str(response_code))
