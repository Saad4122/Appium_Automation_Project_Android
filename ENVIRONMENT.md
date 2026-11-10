# ENVIRONMENT.md: UBL Digital Android Automation

_Values marked **[CONFIRM]** have not been verified yet. Never guess them; fill them from
command output. No secrets, serial numbers or UDIDs belong in this file._

_Last reviewed against commit `a64d580` (2026-11-11)._

---

## 1. Tool versions

| Component | Version | Source |
|---|---|---|
| Python | [CONFIRM] | `python --version` |
| Appium server | [CONFIRM] | `appium -v` |
| UiAutomator2 driver | [CONFIRM] | `appium driver list --installed` |
| Appium-Python-Client | 5.3.1 | `requirements.txt` |
| Selenium | 4.36.0 | `requirements.txt` |
| pytest | 8.4.2 | `requirements.txt` |
| python-dotenv | not used | `config/settings.py` has its own `.env` reader |
| Report plugin (pytest-html etc.) | none | `requirements.txt` |

All other entries in `requirements.txt` are pinned dependencies of pytest and Selenium.

## 2. Device

| Item | Value |
|---|---|
| Model | Samsung Galaxy A51 (`appium:deviceName`); confirm with `adb shell getprop ro.product.model`: [CONFIRM] |
| Android version | [CONFIRM] (`adb shell getprop ro.build.version.release`) |
| Real device / emulator | Real device (expected): [CONFIRM] |
| Device selection | `appium:udid` is **commented out** in `utils/driver_setup.py`, so Appium uses whichever device is connected. Keep exactly one device connected until a UDID is set. |

## 3. App

| Item | Value |
|---|---|
| Package | `app.com.brd` |
| Launch activity | `app.com.brd.presentation.main.MainActivity` |
| Build / version | [CONFIRM] |
| Test environment (SIT / UAT) | [CONFIRM] |
| UI technology (Views / Compose / Flutter / RN) | [CONFIRM] |
| Supported languages | [CONFIRM] |

## 4. Capabilities (`utils/driver_setup.py` → `ANDROID_CAPS`)

| Capability | Value | Meaning |
|---|---|---|
| `platformName` | Android | — |
| `appium:automationName` | UiAutomator2 | Android driver |
| `appium:deviceName` | Galaxy A51 | Label only; not used to choose the device |
| `appium:udid` | commented out | Set this to pin a specific device |
| `appium:appPackage` | `app.com.brd` | App under test |
| `appium:appActivity` | `…presentation.main.MainActivity` | Screen launched |
| `appium:noReset` | True | Keeps app data (device binding) |
| `appium:newCommandTimeout` | 300 | Abandoned sessions end after 5 minutes |
| `appium:disableWindowAnimation` | True | Fewer animation timing issues |
| `appium:autoGrantPermissions` | False | Permission dialogs stay visible |

Server URL: `http://127.0.0.1:4723` (hard-coded in `driver_setup.py`).

## 5. Setup

```bash
cd ~/Desktop/Appium_Automation_Project_Android        # (unverified path)
python3 -m venv appium_env                            # first time only
source appium_env/bin/activate
pip install -r requirements.txt
cp .env.example .env                                  # fill TEST account only; never commit
appium                                                # separate terminal
adb devices                                           # exactly one device, state "device"
```

## 6. Run commands

| Purpose | Command |
|---|---|
| List tests without running | `python -m pytest --collect-only -q` |
| Smoke test | `python -m pytest testcases/test_00_driver_smoke.py -v` |
| One module | `python -m pytest testcases/payments -v` |
| One epic | `python -m pytest testcases/payments/pay_anyone -v` |
| By marker | `python -m pytest -m smoke -v` |
| Safe payment checks only | `python -m pytest -m "payments and not state_changing" -v` |
| One test | `python -m pytest "testcases/test_00_driver_smoke.py::test_driver_starts_android_session" -v` |

All commands are **(unverified)** until they've been run on this machine.

**Warning:** a full `python -m pytest` currently opens an Appium session for each of the
86 skeleton tests before they skip, and runs two tests that still contain iOS logic. Run
single files or markers until that's fixed (see `TEST_AUTOMATION_STATUS.md`).

## 7. Known environment issues

- [CONFIRM]: none recorded yet.
