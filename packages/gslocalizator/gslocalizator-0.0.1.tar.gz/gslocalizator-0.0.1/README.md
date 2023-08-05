
### Quick Start
```py
#!/usr/bin/env python
from gslocalizator.string_file import SaveFormat
from gslocalizator import GoogleSheetLocalizator as GSLr
from cfg import *


def main():
    with GSLr(GSL_CREDS_FILE, GSL_SPREADSHEET_ID) as gslr:
        gslr.tran(
            from_sheet_range='main!A1:E',
            with_key_column='iOS（IM）Key',
            from_value_column_to_file={
                'zh-Hans': '.datas/ios/strings_main/zh-Hans.lproj/Localizable.strings',
                'zh-Hant': '.datas/ios/strings_main/zh-Hant.lproj/Localizable.strings',
                'en': '.datas/ios/strings_main/en.lproj/Localizable.strings',
                'ja': '.datas/ios/strings_main/ja.lproj/Localizable.strings',
            },
            exclude_headers=['//']
        ).request(
        ).save(format=SaveFormat.iOS)


if __name__ == '__main__':
    main()
```