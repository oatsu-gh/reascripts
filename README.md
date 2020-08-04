# reascripts
 REAPER の ReaScript であそぶ。

## 環境

- Windows 10 2004
- Python 3.8.5 (64-bit)
- REAPER v6.13/x64

## やりたいこと

- 再生しながらリージョンまたはマーカーを取得して見やすく表示

## 設計

### 使いそうなAPI

- RPR_GetLastMarkerAndCurRegion()
- RPR_ShowConsoleMsg(str)
- RPR_ShowMessageBox(str, 'title')
- RPR_ClearConsole()