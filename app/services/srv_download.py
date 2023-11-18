import pycountry


class DownloadService(object):
    __instance = None

    @staticmethod
    def download_entity_dataset(base_url: str, country_name: str, administrative_division_code: str,
                                entity_type: str) -> str:
        country_code = pycountry.countries.get(name=country_name).alpha_3
        entity_filename = f'{country_code.lower()}_{administrative_division_code}_{entity_type}.parquet'
        return base_url + entity_filename
