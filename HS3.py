from s3_filename import s3_filename

class add_hs3_path:
    def __init__(self, rasters, base_path):
        self.rasters = rasters
        self.path = base_path
        self.files = []
        self.get_file_names()
        self.add_cogs()

    def get_file_names(self):
        S3 = s3_filename(self.path, 'ghrc-cog', 'HS3/')
        self.files = S3.get_filenames_hs3()

    def add_cogs(self):
        for file in self.files:
            len1 = 11
            len3 = 11
            total = len(file)
            len2 = total - len1 - len3
            date = f"{file[2:6]}{file[6:8]}{file[8:10]}"
            filepath = f'{self.path}/{file}'
            self.rasters[('HS3',f'{file[2:6]}{file[6:8]}{file[8:10]}', f'{file[11:11+len2]}')] = f'{filepath}'

# self.rasters[('VHRSC','2013_03_01','LIS')] = f'{self.path}/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_1.0_co.tif'
# self.rasters[('VHRSC','2013_07_01','LIS')] = f'{self.path}/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_2.0_co.tif'
# self.rasters[('VHRSC','2013_10_01','LIS')] = f'{self.path}/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_3.0_co.tif'
# self.rasters[('VHRSC','2013_12_01','LIS')] = f'{self.path}/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_4.0_co.tif'