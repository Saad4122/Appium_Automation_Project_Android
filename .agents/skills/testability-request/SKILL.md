---
name: testability-request
description: Write a clear request to the UBL Digital development team when automation is blocked by missing accessibility ids, security controls, OTP, biometrics, WebView debugging or test data. Use when a script change cannot solve the problem.
---

# Testability request for developers

## Goal
A short, professional request the dev team can act on, that never weakens production
security.

## First classify the problem (state it in the request)
- Genuine app defect
- Automation limitation
- Missing testability support (e.g. no resource-id)
- Expected security behaviour (e.g. FLAG_SECURE, root detection), not a defect
- Environment/config issue

## Common requests
| Problem | Ask for |
|---|---|
| Elements have no resource-id | Stable resource-ids, naming `<screen>_<element>_<type>`, e.g. `payAnyone_confirm_button` |
| Jetpack Compose ids invisible | `testTagsAsResourceId = true` in QA build |
| Screenshots black (FLAG_SECURE) | Screenshot allowed in QA-only build with synthetic data |
| Randomised PIN keypad | Accessibility metadata per key in QA build |
| OTP in UAT | Approved fixed test OTP or test OTP service for UAT only |
| Biometrics | Test-environment biometric simulation |
| WebView can't be inspected | WebView debugging enabled in QA build |
| Device blocked by device checks | Allowlist approved test devices in UAT |
| Data runs out (balance/limits) | Test data reset/seeding for automation accounts |

## Rules
- Changes only for non-production, access-controlled QA/UAT builds.
- Must be reviewed by the security team.
- Never ask to disable a control in production.
- No real credentials, account numbers or customer data in the request.
- Do not put technical test ids into `contentDescription` (it is read by TalkBack). Ask for resource-ids.

## Output template
```
Title: <short, specific>

Problem Description:
Current Behaviour:
Automation Impact: (which journeys/tests are blocked, how many)
Classification: <one from the list above>
Requested Development Enhancement:
Acceptance Criteria:
 - [ ] ...
Security Considerations: (QA build only, production unchanged, reviewed by security)
Validation Approach: (how QA will confirm it works)
```
Save as `docs/testability_requests/<yyyy-mm-dd>-<short-name>.md` if the user agrees.
