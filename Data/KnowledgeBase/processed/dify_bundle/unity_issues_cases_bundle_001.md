# unity_issues_cases

This file is a Dify upload bundle generated from local JSONL sources.


---

<!-- source=github_issue; title=VRChat (438100); url=https://github.com/ValveSoftware/Proton/issues/1199 -->

# VRChat (438100)

- Source: github_issue
- URL: https://github.com/ValveSoftware/Proton/issues/1199

[System Information Original](https://gist.github.com/Goofybud16/3bdc6ed7d3ffe49b5b2c9ff039f5f8c4)
[System Information - Updated Jan 27, 2019](https://gist.github.com/Goofybud16/3ae46844a6dff5597ab12d083c53c5a1)
Problem:
Was able to load into the hub successfully after going through tutorial, but most other player models did not render correctly, if at all.
Upon restarting the game, it crashes upon loading into the hub.
Mouse keeps pulling towards the bottom right.
Game locked up on exit with a black screen.
All other behavior appeared to be correct.


---

<!-- source=github_issue; title=Champion "Discriminated Unions"; url=https://github.com/dotnet/csharplang/issues/113 -->

# Champion "Discriminated Unions"

- Source: github_issue
- URL: https://github.com/dotnet/csharplang/issues/113

- [ ] Proposal added
- [ ] Discussed in LDM
- [ ] Decision in LDM
- [ ] Finalized (done, rejected, inactive)
- [ ] Spec'ed
See
- https://github.com/dotnet/roslyn/issues/188
- https://github.com/dotnet/csharplang/issues/75
- https://github.com/dotnet/csharplang/blob/master/meetings/2017/LDM-2017-01-10.md
- https://github.com/dotnet/csharplang/issues/485
### Design meetings
https://github.com/dotnet/csharplang/blob/main/meetings/2022/LDM-2022-08-31.md#discriminated-unions
https://github.com/dotnet/csharplang/blob/main/meetings/2022/LDM-2022-09-26.md#discriminated-unions
https://github.com/dotnet/csharplang/blob/main/meetings/2024/LDM-2024-07-24.md#discriminated-unions


---

<!-- source=github_issue; title=Champion: Simplified parameter null validation code; url=https://github.com/dotnet/csharplang/issues/2145 -->

# Champion: Simplified parameter null validation code

- Source: github_issue
- URL: https://github.com/dotnet/csharplang/issues/2145

- [x] Proposal added
- [x] Discussed in LDM
- [x] Decision in LDM
- [x] Finalized (rejected)
- [x] Spec'ed
Specification: https://github.com/dotnet/csharplang/blob/main/proposals/param-nullchecking.md
In short though this allows for standard `null` validation on parameters to be simplified using a small annotation on parameters:
``` csharp
// Before
void Insert(string s) {
if (s is null)
throw new ArgumentNullException(nameof(s));
...
}
// After
void Insert(string s!!) {
...
}
```
LDM history:
- https://github.com/dotnet/csharplang/blob/master/meetings/2019/LDM-2019-01-14.md
- https://github.com/dotnet/csharplang/blob/master/meetings/2019/LDM-2019-07-10.md#param
- https://github.com/dotnet/csharplang/blob/main/meetings/2022/LDM-2022-04-06.md#parameter-null-checking
- https://github.com/dotnet/csharplang/blob/main/meetings/2022/LDM-2022-04-13.md#parameter-null-checking


---

<!-- source=github_issue; title=Game crash (on Linux) TM:PE V11 STABLE; url=https://github.com/CitiesSkylinesMods/TMPE/issues/817 -->

# Game crash (on Linux) TM:PE V11 STABLE

- Source: github_issue
- URL: https://github.com/CitiesSkylinesMods/TMPE/issues/817

> # Temporary solution
> * Use latest [development build](https://ci.appveyor.com/api/projects/krzychu124/tmpe/artifacts/TMPE.zip?branch=master) or [**TEST**](https://steamcommunity.com/sharedfiles/filedetails/?id=2489276785) workshop version
>
### Describe the problem
I run Cities:Skylines on LInux (Manjaro),
Hardware if it matters: AMD FX 8370, Nvidia GeForce 750 Ti (Diver 440.64)
When I start a saved city everything is fine until I un-pause it, then it will either freeze or crash. When I unsubscribe to this mod the city will load and run.
### Steps to reproduce
1. Load saved city.
2. un-pause game
3.
### Log files
https://ufile.io/9vld1vi2
### Savegame?
https://ufile.io/fyy8h170
### Screenshots?
None
### Notes or questions?


---

<!-- source=github_issue; title=WinUI 3.0 roadmap - we need your input!; url=https://github.com/microsoft/microsoft-ui-xaml/issues/717 -->

# WinUI 3.0 roadmap - we need your input!

- Source: github_issue
- URL: https://github.com/microsoft/microsoft-ui-xaml/issues/717

# WinUI 3.0
At the Microsoft Build conference in May 2019 we shared our plans for WinUI 3.0, which will greatly expand the scope of WinUI to include the full native Windows UI platform. This means that the full Xaml framework would be developed on GitHub and ship out of band as [NuGet](https://docs.microsoft.com/nuget/what-is-nuget) packages.
The WinUI roadmap is now up to date with the latest plans for WinUI 3.0:
**https://github.com/microsoft/microsoft-ui-xaml/blob/master/docs/roadmap.md**
You can also watch the Build 2019 conference session *[State of the Union: The Windows Presentation Platform](https://mybuild.techcommunity.microsoft.com/sessions/77008)* for more details.
We'd love to hear what you think, and have some specific questions below.
## How will this affect building Windows apps and components?
WinUI 3.0 will provide many benefits compared to the UWP Xaml framework, WPF, WinForms and MFC.
So, we want to make sure it's easy for everyone to use WinUI 3.0 in new and existing apps. There are a few ways we can approach this, and we'd love to hear your feedback on what areas we should focus on.
Our current thinking is:
### Creating a new app
We plan to create new Visual Studio 2019 project templates for common languages (e.g. C# using .NET Core, standard C++17 using [C++/WinRT](https://docs.microsoft.com/windows/uwp/cpp-and-winrt-apis/)) and app model + packaging (UWP + AppX, Win32 + [MSIX](https://docs.microsoft.com/windows/msix/)).
> **What templates would interest you most?**
The developer experience would be similar to current UWP apps.
### Adding WinUI 3.0 to existing Win32 apps
WinUI 3.0 will include [Xaml Islands](https://docs.microsoft.com/windows/uwp/xaml-platform/xaml-host-controls), which let you use WinUI Xaml in your existing WPF, Windows Forms, and C++ Win32 applications.
The current version of Xaml Islands is only supported on Windows 10 May 2019 Update (1903), but the WinUI version should be backward-compatible to Creators Update (15063).
> **Were you aware of Xaml Islands for modernizing desktop apps?
Does this expanded backward-compatibility on Windows 10 make Xaml Islands more useful to you?**
### Updating your existing UWP Xaml app to WinUI 3.0
You'll have to update your app's target version to WinUI 3.0 to take advantage of it, similar to retargeting to a newer UWP SDK today.
We want to maximize compatibility between UWP Xaml and WinUI 3.0, but there will be some things to be aware of when updating.
1\. **Namespace update**
The root namespace for Xaml, composition, and input APIs in WinUI will be different than the Windows UWP SDK root namespace:
| Old namespace | New namespace (tentative) |
| - | - |
| `Windows.UI.Xaml` | `Microsoft.UI.Xaml` |
| `Windows.UI.Composition` | `Microsoft.UI.Composition` |
| `Windows.UI.Input` | `Microsoft.UI.Input` |
We're exploring options for helping you automatically update namespaces when retargeting your UWP app to WinUI 3, at least for .NET apps.
> **Would it help if Visual Studio or another tool automatically updated namespaces for you?**
2\. **Mixing UWP and WinUI Xaml components**
The fastest path to releasing WinUI 3.0 would be to not support mixing:
* UWP [Windows.UI.Xaml.UIElement](https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.UIElement) and [Windows.UI.Composition.Visual](https://docs.microsoft.com/windows/uwp/composition/composition-visual-tree) elements
with:
* WinUI 3.0 `Microsoft.UI.Xaml.UIElement` and `Microsoft.UI.Composition.Visual` elements
in the same app.
However, one of our biggest concerns is the compatibility issues and work that could create for existing UWP apps and component libraries, particularly if you're authoring or consuming UWP Xaml control libraries.
For example, existing versions of the [Windows Community Toolkit](https://docs.microsoft.com/windows/communitytoolkit) wouldn't be usable in WinUI 3.0 apps, so both the Toolkit and any apps using it would need to update before using WinUI 3.0.
We hope that all UWP Xaml control libraries can be updated to WinUI 3.0, but we know that even in the best case it would take time for everyone to update.
> **How important to you is full compatibility between existing UWP Xaml components and WinUI 3.0 apps?**
> **Do you create or use UWP Xaml control libraries or WinRT components that you couldn't easily recompile and update alongside app code?**
> **What would be your preferred solution for using UWP Xaml components with WinUI 3?**
## General questions
1. What do you think about the overall 3.0 plan outlined above and in the [roadmap](https://github.com/microsoft/microsoft-ui-xaml/blob/master/docs/roadmap.md)? Would it enable you to use WinUI for your new and existing Windows apps?
2. What kind of apps would you be most excited to use WinUI 3.0 for? Creating a new Win32 app and packaging it with [MSIX](https://docs.microsoft.com/windows/msix/)? Adding new views to a WPF app? Modernizing a C++ MFC app with Fluent UI?


---

<!-- source=github_issue; title=Mod translations; url=https://github.com/Sgt-Imalas/Sgt_Imalas-Oni-Mods/issues/86 -->

# Mod translations

- Source: github_issue
- URL: https://github.com/Sgt-Imalas/Sgt_Imalas-Oni-Mods/issues/86

### What mod is that translation for?
Cluster Generation Manager
### Additional Comments
Is it possible to make these settings translatable? In a clean game these settings are in Russian, but when installing this mod they become in English.
![123](https://github.com/Sgt-Imalas/Sgt_Imalas-Oni-Mods/assets/50534207/75a79742-a1cd-4d42-b526-443c43624e5e)
### translation file
Finished the translation, now I'm checking how the text looks in the game, as soon as I finish I'll provide it to you.


---

<!-- source=github_issue; title=SUPPORT page for CriticalComponentsAbsent Fatal Error; url=https://github.com/KSP-ModularManagement/KSPe/issues/17 -->

# SUPPORT page for CriticalComponentsAbsent Fatal Error

- Source: github_issue
- URL: https://github.com/KSP-ModularManagement/KSPe/issues/17

Currently, we have two main reasons for this error to appear:
## Very old KSPe artefacts left forgotten in your disk
![Screen Shot 2023-03-13 at 10 06 17](https://user-images.githubusercontent.com/64334/224710655-cac6eec4-a161-433f-9a03-b34f53e6402e.png)
**Remove** all KSPe files as explained on [INSTALL.md](https://github.com/net-lisias-ksp/KSPe/blob/mestre/INSTALL.md) and reinstall.
## Something else
![Screen Shot 2021-09-24 at 21 34 34](https://user-images.githubusercontent.com/64334/134751883-ab565b47-fa96-46c0-bdfc-e08d60e8de95.png)
Something else is happening in your rig. Yell for help here (mention me by using @Lisias , it will make me notice your post faster)
You **should** post your `KSP.log` on your comment (you can drag and drop it into the text-box) so I can see what's happening. Please reproduce the problem then quit KSP (to prevent truncating the thing) before posting the `KSP.log`.


---

<!-- source=github_issue; title=Tracking issue for illumos and Solaris x86-64 port work; url=https://github.com/dotnet/runtime/issues/34944 -->

# Tracking issue for illumos and Solaris x86-64 port work

- Source: github_issue
- URL: https://github.com/dotnet/runtime/issues/34944

Cut from https://github.com/dotnet/runtime/issues/4173.
Given below is a high-level list of work items for Solaris x86-64 port:
- [x] Native configurations (#34756)
- [x] CoreCLR native components (#35173)
- <del>awaiting next release of libunwind https://github.com/libunwind/libunwind/releases/tag/v1.5-rc1 or higher with changes from https://github.com/libunwind/libunwind/pull/171, for Solaris support.</del>
- upstream PR was merged, libunwind is updated to 1.5 by @sdmaclea in #36027.
- [ ] PAL tests
- one test is failing is due to #35362.
- another one is related to raising thread priority, after lowering it from the same value as a non-root user. this either requires implementation using [`priocntl(2)`](https://illumos.org/man/2/priocntl) directly for SunOS targets, or wait for https://www.illumos.org/issues/4963.
- [x] Libraries native components (#34867)
- on SmartOS x86_64 with gcc 7x:
```sh
# from runtime repo root
./src/libraries/Native/build-native.sh -gcc
```
- [x] Mono native components (#37560)
- Full mono (https://github.com/mono/mono) is already available on Solaris, requires some configurations for netcore mono in this repository.
- [x] Installer native components (#34263)
- on SmartOS x86_64 with gcc 7x:
```sh
# from runtime repo root
src/installer/corehost/build.sh -commithash $(git rev-parse HEAD) -gcc \
-apphostver 5.0.0-dev -hostver 5.0.0-dev -fxrver 5.0.0-dev -policyver 5.0.0-dev
```
- [ ] MSBuild configurations
- [x] CoreCLR managed components (#36266)
- [ ] Libraries managed components
- Most of the partial classes can be shared with Linux (e.g. by moving it under Unix names) and modifying msbuild configurations.
- [ ] Installer managed components
- [x] CoreCLR tests (#37824)
- [ ] Libraries tests
- [ ] Mono tests
- [ ] Installer tests
- [ ] Packaging configurations
- [x] RID (#37016)
- [x] Cross compilation on Linux (dotnet/arcade#5584, dotnet/dotnet-buildtools-prereqs-docker#324, #37753)
- as done for other operating systems, e.g. FreeBSD: https://github.com/dotnet/arcade/blob/3443768/eng/common/cross/build-rootfs.sh#L243.
- script gets mirrored at https://github.com/dotnet/runtime/blob/master/eng/common/cross/build-rootfs.sh.
- [x] SDK (dotnet/sdk#12198)
- [ ] CI hook
- similar to https://github.com/dotnet/dotnet-buildtools-prereqs-docker/pull/277 and https://github.com/dotnet/runtime/pull/34521
- external (GitHub Actions) CI has set up using the official illumos docker image: https://github.com/am11/runtime/blob/feature/sunos/ci/.github/workflows/main.yml
- example run: https://github.com/am11/runtime/actions/runs/145127885
- on tag push, it creates a GitHub release and upload artifacts (files under `Shipping` directory), e..g. https://github.com/am11/runtime/releases/tag/5.0.0-dev.1


---

<!-- source=github_issue; title=General Support Issue; url=https://github.com/KSP-ModularManagement/ModuleManager/issues/2 -->

# General Support Issue

- Source: github_issue
- URL: https://github.com/KSP-ModularManagement/ModuleManager/issues/2

So you got a message like this one, clicked on the Ok button and reached here?
![Screen Shot 2023-09-11 at 22 50 25](https://github.com/net-lisias-ksp/ModuleManager/assets/64334/f53629e4-8f6b-4e30-bd6a-88dc788efad9)
Well, there's something very wrong on your KSP installation, usually a missing dependency or a borked CKAN update.
Please send me your KSP.log below and I will inspect it for the problem, and then I will be able to provide you with a solution. You can ping me on [Forum](https://forum.kerbalspaceprogram.com/profile/187168-lisias/) too, so I will probably be notified faster about this.


---

<!-- source=github_issue; title=Crash Test for TweakScale - the Ground Breaking tests; url=https://github.com/TweakScale/TweakScale/issues/42 -->

# Crash Test for TweakScale - the Ground Breaking tests

- Source: github_issue
- URL: https://github.com/TweakScale/TweakScale/issues/42

## Intro
This is the Issue where reports and logs for the Crash Test to check the current status quo for the not too far TweakScale 2.5, as well to test concept for new DLCs.
## Objective
The TweakScale code appears to be stable (but bugs **are** happening now and then). ~~What's bugging me is how Add'Ons will behave once TweakScale start to use the :FOR thingy.~~ *[not anymore, I dropped out the `:FOR` thingy. Perhaps on TS3…]*
Some are already using :AFTER or :BEFORE, these ones I expect to be fine . ~~But the MM LEGACY ones I expect to cause breakage. I want to identify them and see what can be done to prevent the havoc, as well to work on push requests to fix them.~~
## Instructions
The tests will be simple:
1. shove a bunch on new and old Add'Ons
1. BACKUP YOUR SAVE GAMES AND CRAFTS. EVERY SINGLE TIME.
1. start KSP
1. play a little
1. quit KSP
* Important to guarantee KSP.log integrity if you use [Hyperspace](https://forum.kerbalspaceprogram.com/index.php?/topic/172841-14-16-hyperspace-load-ksp-faster-on-hdd-or-not/&tab=comments#comment-3331451).
* And you really should be using Hyperspace!
1. and then zip the KSP.LOG and the Module Manager caches
* (all of them, don't bother picking only the changed ones).
* Post them here, if you can. It will make things way better for me.
1. shove some more Add'Ons, delete some, restart.
* To the extent of your patience﻿. :)
This is a somewhat long term task - you don't have to do all at once. Au contraire, it's better to post many entries, as many as you have the guts to withhold :), with your testing sessions - the aim is to try to simulate what we will face on the wild, with lots of people installing lots of different (some of them old) AddOns.
The Target for these release are both KSP 1.3.1, KSP 1.4.3, KSP 1.7.3 and KSP 1.12.5 - but really, any version will do. TweakScale and patches are essentially the same for all KSP versions ~~at this moment~~ *[ and it will be kept this way]*.
Even by not answering you right now, **I WILL CHECK EVERY SINGLE ENTRY** sooner or later (I'm building automated tools to help me on the task). In order to give feedback, I will use the reactions as markers:
![Screen Shot 2019-05-08 at 12 41 00](https://user-images.githubusercontent.com/64334/57389456-9f19ac80-7190-11e9-8aa3-121f368d40bc.png)
* Eyes: I saw your post, and I scheduled it to analysis
* Rocket: I'm currently analysing it, or scheduled it to be so in the next timewindow.
* Hooray: Analysis concluded, no (new) issues found!
* "+1" : Analysis concluded, new issues found and you helped to prevent it happening on the wild! :)
Analysis will not be made chronologically, but everyone will.
## WARNING
The binaries can be compiled in DEBUG mode, so it may spit an awfully amount of logging. This can affect the game performance sometimes.
Be advise: this can break your KSP, ruin your Windows, kill your pet, offend your mom and poison your kids. :D
## Related issues
These tests can also help me to diagnose/fix/check the following issues (issues are cumulative, the newest versions also need to be tested for the same old issues!)
* 2.5.0.63
* TweakScale/TweakScale#339
* TweakScale/TweakScale#336
* TweakScale/TweakScale#325
* TweakScale/TweakScale#323
* TweakScale/TweakScale#312
* TweakScale/TweakScale#307
* TweakScale/TweakScale#283
* 2.5.0.62
* TweakScale/TweakScale#319
* TweakScale/TweakScale#307
* 2.5.0.61
* TweakScale/TweakScale#309
* 2.5.0.60
* TweakScale/TweakScale#308
* TweakScale/TweakScale#307
* Backports https://github.com/net-lisias-ksp/AviationLights/issues/4
* 2.5.0.59
* Maintenance release. No issues closed.
* 2.5.0.58
* Catching up with mainstream
* TweakScale/TweakScale#268
* TweakScale/TweakScale#261
* TweakScale/TweakScale#252
* TweakScale/TweakScale#246
* TweakScale/TweakScale#238
* Works specific 2.5 issues:
* TweakScale/TweakScale#290
* TweakScale/TweakScale#289
* TweakScale/TweakScale#287
* TweakScale/TweakScale#286
* #285
* TweakScale/TweakScale#280
* TweakScale/TweakScale#279
* TweakScale/TweakScale#276
* TweakScale/TweakScale#195
* 2.5.0.57
* Maintenance release. No issues closed.
* 2.5.0.56
* ***withdrawn***
* 2.5.0.55
* Maintenance release. No issues closed.
* 2.5.0.54
* ***withdrawn***
* 2.5.0.53
* ***withdrawn***
* 2.5.0.52
* ***withdrawn***
* 2.5.0.50
* ***withdrawn***
* 2.5.0.49
* TweakScale/TweakScale#187 (rework)
* TweakScale/TweakScale#184 (rework)
* TweakScale/TweakScale#46
* 2.5.0.48
* TweakScale/TweakScale#260
* TweakScale/TweakScale#258
* TweakScale/TweakScale#34
* TweakScale/TweakScale#31
* 2.5.0.47
* New features. No issue closed.
* 2.5.0.46
* TweakScale/TweakScale#256
* TweakScale/TweakScale#255
* 2.5.0.45
* TweakScale/TweakScale#254
* 2.5.0.44
* TweakScale/TweakScale#249
* 2.5.0.43
* TweakScale/TweakScale#244
* 2.5.0.42
* TweakScale/TweakScale#237
* TweakScale/TweakScale#236
* TweakScale/TweakScale#218
* 2.5.0.40
* TweakScale/TweakScale#219
* TweakScale/TweakScale#86
* 2.5.0.39
* TweakScale/TweakScale#211
* TweakScale/TweakScale#209
* TweakScale/TweakScale#197
* TweakScale/TweakScale#167
* TweakScale/TweakScale#139
* 2.5.0.38
* TweakScale/TweakScale#208
* TweakScale/TweakScale#207
* TweakScale/TweakScale#175
* TweakScale/TweakScale#163
* TweakScale/TweakScale#131
* TweakScale/TweakScale#36
* 2.5.0.37
* No issues solved. Maintenance release.
* 2.5.0.36
* No issues solved. Maintenance release.
* 2.5.0.35
* TweakScale/TweakScale#201
* 2.5.0.34
* TweakScale/TweakScale#198
* TweakScale/TweakScale#165
* TweakScale/TweakScale#186
* TweakScale/TweakScale#184
* TweakScale/TweakScale#182
* TweakScale/TweakScale#181
* TweakScale/TweakScale#128
* TweakScale/TweakScale#120
* TweakScale/TweakScale#50
* 2.5.0.32
* TweakScale/TweakScale#85
* 2.5.0.31
* TweakScale/TweakScale#170
* 2.5.0.30
* No issues solved. New features release for testing!!! #HURRAY!!!
* 2.5.0.24 to 2.5.0.29
* No issues solved. Maintenance release.
* 2.5.0.23
* TweakScale/TweakScale#142
* TweakScale/TweakScale#87 (partial)
* 2.5.0.22
* No issues solved. Maintenance release.
* 2.5.0.21
* TweakScale/TweakScale#138
* TweakScale/TweakScale#13 - **HURRAY!**
* 2.5.0.20
* TweakScale/TweakScale#137
* TweakScale/TweakScale#136
* 2.5.0.18
* No issues solved. Maintenance release.
* 2.5.0.17
* No issues solved. Maintenance release.
* 2.5.0.16
* TweakScale/TweakScale#125
* 2.5.0.15
* TweakScale/TweakScale#119
* TweakScale/TweakScale#124
* 2.5.0.14
* TweakScale/TweakScale#114
* TweakScale/TweakScale#115
* 2.5.0.13
* [TweakScaleCompanion_FS#1](https://github.com/net-lisias-ksp/TweakScaleCompantion_FS/issues/1)
* [TweakScaleCompanion_FS#2](https://github.com/net-lisias-ksp/TweakScaleCompantion_FS/issues/2)
* 2.5.0.12
* TweakScale/TweakScale#110
* 2.5.0.11
* TweakScale/TweakScale#95
* TweakScale/TweakScale#106
* 2.5.0.10
* TweakScale/TweakScale#7
* TweakScale/TweakScale#35
* TweakScale/TweakScale#73
* TweakScale/TweakScale#95
* TweakScale/TweakScale#101
* 2.5.0.9
* TweakScale/TweakScale#98
* 2.5.0.8
* TweakScale/TweakScale#46
* TweakScale/TweakScale#73
* TweakScale/TweakScale#74
* 2.5.0.7
* TweakScale/TweakScale#21
* TweakScale/TweakScale#26
* TweakScale/TweakScale#69
* TweakScale/TweakScale#76
* 2.5.0.6
* TweakScale/TweakScale#30
* TweakScale/TweakScale#71
* 2.5.0.5
* Hot Fix patches support
* 2.5.0.4
* TweakScale/TweakScale#65
* 2.5.0.3
* TweakScale/TweakScale#47
* TweakScale/TweakScale#48
* TweakScale/Companion_Gambiarras#6
* TweakScale/TweakScale#50
* TweakScale/TweakScale#58
* 2.5.0.2
* TweakScale/TweakScale#51
* TweakScale/TweakScale#54
* TweakScale/Companion_Gambiarras#5
* TweakScale/TweakScale#57
* 2.5.0.1
* TweakScale/TweakScale#7
* TweakScale/TweakScale#41
* TweakScale/TweakScale#42
* 2.5.0.0
* TweakScale/TweakScale#10
* TweakScale/TweakScale#11
* TweakScale/TweakScale#21
* TweakScale/TweakScale#31
* TweakScale/TweakScale#34
* TweakScale/TweakScale#35
There's a lot of thingies to do yet.
## Binaries
[TweakScale-2.5.0.63-BETA.zip](https://github.com/net-lisias-ksp/TweakScale/releases/tag/PRERELEASE%2F2.5.0.63) (Compiled as Release, as the logging is impairing KSP performance).
[KSPe](https://github.com/net-lisias-ksp/KSPe) is a hard dependency. Always install the [latest release](https://github.com/net-lisias-ksp/KSPe/releases). Please updated it to the absolute latest (even if in PRE-Release). `KSPe.Light.TweakScale` is provided to keep compatibility with the [TweakScale Companions](https://forum.kerbalspaceprogram.com/index.php?/topic/192216-*/).
Please note that you will **need** the latest [KSP Recall ](https://forum.kerbalspaceprogram.com/index.php?/topic/192048-ksp-recall-0030-2020-0518/)in order to use it on KSP 1.4 to KSP 1.12.x.
Thanks in advance for the help


---

<!-- source=github_issue; title=Discussion: `try` expression without `catch` for inline use; url=https://github.com/dotnet/csharplang/issues/220 -->

# Discussion: `try` expression without `catch` for inline use

- Source: github_issue
- URL: https://github.com/dotnet/csharplang/issues/220

## Proposal: `try` expression without `catch` for inline use
### Intent
Sometimes it is not necessary to catch an exception, because you can either check side conditions or proceed though the expression is failed. In these cases it would be nice to skip the exception checking.
### Example
In current code there would be something like
```C#
try {
var textStream = new StreamReader("C:\nonexistingfile.txt");
ProcessFile(textStream);
}
catch { }
GoOnWithOtherThings();
```
or even wrap it additionally with
```C#
var fileName = @"C:\notexisting.txt";
if (File.Exists(fileName)) {
// try block from above
}
GoOnWithOtherThings();
```
This could be abbrevated and streamlined drastically with
```C#
var textStream = try new StreamReader("C:\nonexistingfile.txt");
if (textStream != null) ProcessFile(textStream);
GoOnWithOtherThings();
```
The catching isn't necessary here, because a null-check (that should be done in `ProcessFile()` anyway) already cares about the failure. A complete `try { } catch { }` is just unnecessary boilerplate.
I guess that there are plenty of other useful scenarios where this would come in handy.
### Other languages
PHP uses the `@` operator before an expression to suppress errors and warnings
```PHP
$fp = @fsockopen("www.example.com", 80, $errno, $errstr, 30);
if (!$fp) {
echo "$errstr ($errno)<br />\n";
```
In PHP `@` is used quite often to shorten things.
Now, open for discussion... 😄


---

<!-- source=github_issue; title=Symbolの中でゲームづくりしている人 集まろう; url=https://github.com/ymuichiro/symbol_japan_forum/issues/5 -->

# Symbolの中でゲームづくりしている人 集まろう

- Source: github_issue
- URL: https://github.com/ymuichiro/symbol_japan_forum/issues/5

## 提起
Symbolの中でゲーム作りしている人、情報交換しませんか？
課題、面白い取り組み、なんでも、まずは書いてみましょう！
Related comments:
ふぁーさん　本当にありがとうございます。
今、僕はUNITYで超初心者用の本を読みながらsample gameを作っています。まだまだ駆け出しなので情報交換の場を作ってくださって大変心強く思います。そして、自分もやってみたいなー、初心者だから無理かなー？て思ってる人たちと一緒に進んでいけたらなと思います。仲間がいれば、僕も頑張って続けることができると思います。
ここは参加したい場所なのでとりあえず記念カキコ
Unity用Symbolアセット置いときます！
https://github.com/0x070696E65/Symnity


---

<!-- source=github_issue; title=AOT-stubs for Bolt Community Addons in Addressables on Android; url=https://github.com/RealityStop/Bolt.Addons.Community/issues/67 -->

# AOT-stubs for Bolt Community Addons in Addressables on Android

- Source: github_issue
- URL: https://github.com/RealityStop/Bolt.Addons.Community/issues/67

Hello! We are heavily relying on using [addressables](https://docs.unity3d.com/Manual/com.unity.addressables.html) in our project. To support logic in our addressable asset packs, we've started looking into Visual Scripting, and it seems this is not supported out of the box on AOT-platforms such as Android, since all logic has to be pre-compiled in the base project. We've been able to have some success by following the steps described in [this thread](https://forum.unity.com/threads/1269071/) to generate AOT-stubs, however we are still having some issues with the community addons package.
The error is as follows:
`ExecutionEngineException: Attempting to call method 'Unity.VisualScripting.Community.OnUnityEvent::OneParamHandler<System.Single>' for which no ahead of time (AOT) code was generated.`
As per the above linked thread, we've modified the AotPreBuilder script to include the needed namespaces in order to generate AOT-stubs for the needed APIs. I've tried to include the following namespaces:
- Unity.VisualScripting
- Unity.VisualScripting.Community
- Bolt.Addons.Community
- Bolt.Addons.Community.Runtime
We're still getting the above exception in Android builds, although it seems to work on standalone Windows builds.
We've also tried with and without engine code stripping enabled.
We have also tried to include a reference to the `Bolt.Addons.Community.Runtime` asmdef, and made a dummy script with a direct reference to a `OnUnityEvent` node, to no avail.
`OnUnityEvent` is the node we have mainly used in our testing to simplify our graphs (although we'd like to use more of the addon nodes). Does this node specifically, or the rest of the package, have other dependencies we need to include in the AotPreBuilder script? Are there other steps we can take in trying to figure this out? Any and all insight or tips on this matter is greatly appreciated. Thanks!


---

<!-- source=github_issue; title=User- and developer-friendly way of distributing tasks using UtilPack.NuGet.MSBuild task factory; url=https://github.com/stazz/UtilPack/issues/7 -->

# User- and developer-friendly way of distributing tasks using UtilPack.NuGet.MSBuild task factory

- Source: github_issue
- URL: https://github.com/stazz/UtilPack/issues/7

Currently, there is no standardized way of distribute tasks relying on UtilPack.NuGet.MSBuild task factory.
So far, UtilPack.NuGet.MSBuild task factory has been used by very small group of people (me and couple others), and the way of using UtilPack.NuGet.MSBuild task factory has been to manually add `PackageReference` to UtilPack.NuGet.MSBuild (directly to `.csproj` or to proxy `.build`/`.targets` file, if one would like to eliminate `Pack` task to automatically create dependency to UtilPack.NuGet.MSBuild package), and then, also manually, add the `UsingTask` directives.
However, this is obviously not a very long-term solution, since one can not assume that every user of the task has required knowledge and time to manually edit project files.
Ideally, to achieve best end-user experience, it would be enough to simply add NuGet reference to package containing the custom task.
The rest is, for the consumer point of view, technical implementation details - as long as no extra "polluting" references are added to the build artifacts.
Therefore, there are two requirements:
- __One NuGet package reference to the custom task package should be enough__, and
- __that reference should not add any new references to consumer project__.
The @dazinator pointed out in #6 that situation fulfilling both of these requirements would be achieved by having two NuGet packages: one to be added by consumer project, and other that would be restored and executed by UtilPack.NuGet.MSBuild task factory.
However, while easy for consumer, this adds quite a lot of overhead and plumbing code for developers of the tasks.
There is another way, which is not entirely free of overhad and plumbing code, but requires only one NuGet package.
Consider the following structure of example NuGet package, let's call it MyExamplePackage:
- `build` folder, with
- `MyExamplePackage.targets` file,
- `functionality` folder, with
- `Functionality.targets` file
- `lib` folder, with
- `netstandard1.3` folder, with
- `MyExamplePackage.dll` assembly, containing our custom task
The contents of `build/MyExamplePackage.targets` file would be:
```xml
<Project xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
<!-- Hook into build process of consumer package. The exact logic for this varies depending on what kind of functionality this package provides, but let's use this as an example. -->
<PropertyGroup>
<BuildDependsOn>
MyExamplePackageBuild;
$(BuildDependsOn);
</BuildDependsOn>
</PropertyGroup>
<!-- Properties containing paths to functionality files and directories. -->
<PropertyGroup>
<MyExamplePackage_FunctionalityDir>$(MSBuildThisFileDirectory)/functionality</MyExamplePackage_FunctionalityDir>
<MyExamplePackage_FunctionalityFile>$(MyExamplePackage_FunctionalityDir)/Functionality.targets</MyExamplePackage_FunctionalityFile>
<MyExamplePackage_FunctionalityObjFolder>$(MyExamplePackage_FunctionalityDir)/obj</MyExamplePackage_FunctionalityObjFolder>
</PropertyGroup>
<!-- This target gets called when consumer project is built. -->
<Target Name="MyExamplePackageBuild">
<!-- Restore infrastructure stuff, if not done already. -->
<CallTarget
Condition="!Exists('$(MyExamplePackage_FunctionalityObjFolder)')"
Targets="MyExamplePackageBuild_RestoreInfrastructure"
/>
<!-- Now do actual stuff. -->
<CallTarget
Targets="MyExamplePackageBuild_CallFunctionality"
/>
</Target>
<!-- This target gets called by MyExamplePackageBuild, if necessary -->
<Target Name="MyExamplePackageBuild_RestoreInfrastructure">
<!-- We are going to call MSBuild via Exec (because doing this directly via MSBuild task does not (yet?) work properly) -->
<PropertyGroup Condition=" '$(MSBuildExecCMD)' == '' ">
<MSBuildExecCMD Condition=" '$(MSBuildRuntimeType)' == 'Core' ">dotnet msbuild</MSBuildExecCMD>
<MSBuildExecCMD Condition=" '$(MSBuildRuntimeType)' != 'Core' ">"$(MSBuildBinPath)\MSBuild.exe"</MSBuildExecCMD>
</PropertyGroup>
<!-- Restore Functionality.targets file -->
<Exec
Command="$(MSBuildExecCMD) /t:Restore &quot;$(MyExamplePackage_FunctionalityFile)&quot;"
/>
</Target>
<!-- This target gets called by MyExamplePackageBuild, always. -->
<Target Name="MyExamplePackageBuild_CallFunctionality">
<!-- The functionality/Functionality.targets file is now restored, so we can call MSBuild directly on it. -->
<MSBuild
Projects="$(MyExamplePackage_FunctionalityFile)"
Targets="PerformFunctionality"
UnloadProjectsOnCompletion="true"
/>
</Target>
</Project>
```
The contents of `build/functionality/Functionality.targets` file could be something like this:
```xml
<Project Sdk="Microsoft.NET.Sdk">
<PropertyGroup>
<!-- This is required, otherwise MSBuild will end up in error. -->
<TargetFramework>netstandard1.0</TargetFramework>
</PropertyGroup>
<!-- A reference to UtilPack.NuGet.MSBuild task factory. -->
<ItemGroup>
<PackageReference Include="UtilPack.NuGet.MSBuild" Version="1.1.3" />
</ItemGroup>
<!-- UsingTask directive. -->
<UsingTask
Condition=" '$(UtilPackNuGetMSBuildAssemblyPath)' != '' "
TaskFactory="UtilPack.NuGet.MSBuild.NuGetTaskRunnerFactory"
AssemblyFile="$(UtilPackNuGetMSBuildAssemblyPath)"
TaskName="MyExamplePackage.Tasks.MyExamplePackageTask"
>
<Task>
<NuGetTaskInfo>
<PackageID>MyExamplePackage</PackageID>
<PackageVersion>1.0.0</PackageVersion>
</NuGetTaskInfo>
</Task>
</UsingTask>
<Target Name="PerformFunctionality">
<!-- This target will get called by build/MyExamplePackage.targets file. -->
<!-- Execute our custom task. -->
<MyExamplePackage.Tasks.MyExamplePackageTask
Prefix="Hello"
/>
</Target>
</Project>
```
The build flow would be something like this:
1. The `build/MyExamplePackage.targets` file would hook itself into build process, and cause execution of `MyExamplePackageBuild` target.
2. On initial build, the `MyExamplePackageBuild` target detects the non-existance of `build/functionality/obj` folder, causing `build/functionality/Functionality.targets` file to be restored.
- Restoring that file causes creation of `build/functionality/obj` folder, holding all required info related to e.g. UtilPack.NuGet.MSBuild task factory (as it was referenced in `build/functionality/Functionality.targets` file via `PackageReference`).
3. On next builds, the restore would be skipped, as everything should be ready anyway.
4. Then, the `PerformFunctionality` target in `build/functionality/Functionality.targets` file would get executed. This target causes UtilPack.NuGet.MSBuild to execute `MyExamplePackage.Tasks.MyExamplePackageTask` task in `MyExamplePackage` (this package).
5. The UtilPack.NuGet.MSBuild will load the `lib/netstandard1.3/MyExamplePackage.dll` file, search for `MyExamplePackage.Tasks.MyExamplePackageTask` type there, and execute it as MSBuild task.
As a result, both requirements mentioned above would be satisfied: consumer needs to just add reference to custom task NuGet package, and as a result, no extra references are added to consumer project.
I'll add some kind of template project, for testing and demonstrating purposes, once I get it done.


---

<!-- source=github_issue; title=Port Modding API to Hollow Knight 1.5.12459; url=https://github.com/jhearom/api/issues/1 -->

# Port Modding API to Hollow Knight 1.5.12459

- Source: github_issue
- URL: https://github.com/jhearom/api/issues/1

Tracking port work for the Hollow Knight Modding API fork against PC patch 1.5.12459.
Context:
- Current `master` branch last worked against Hollow Knight 1.5.78.11833.
- New analysis target data is available locally at `/codex/hollow_knight_analysis/hk_1512459`.
- Initial work is focused on understanding current API behavior, enabling useful logging, and gathering startup failure data before deeper game-source analysis.
Proposed milestones:
- Confirm current build/install path and logging surfaces.
- Produce a logging-enabled test install against 1.5.12459.
- Capture first startup/load failures on the new patch.
- Triage breakages by bootstrap, hooks, menu/UI, save/loading, and preload pipeline.
- Port and validate enough functionality for baseline mod loading.


---

<!-- source=github_issue; title=Implement sliding window scale logic.; url=https://github.com/RevenantX/LiteNetLib/issues/110 -->

# Implement sliding window scale logic.

- Source: github_issue
- URL: https://github.com/RevenantX/LiteNetLib/issues/110

I have been testing LiteNetLib, Lidgren-gen3 and Lidgren-old (the one from Google Code) and Lidgren-old is beating the competitors by far... On my test I have 750 clients connected to a single server instance, receiving ~15 reliable msgs/s and ~100 unreliable msgs/s and Lidgren-old can handle all this data perfectly! Using the same "game code" but using Lidgren-gen3 or LiteNetLib the test "fails" between 100 and 120 clients... Maybe I am missing something with LiteNetLib API, so I can achieve better performance... Do you have any idea where I am doing wrong with your Lib? If you need I can share the code :)
* My test is using my area of interest management layer, so it can efficiently send to clients only data important to them. Only using this technique I was able to achieve 750 clients on a single server :) Every client is also sending ~15 unreliable msgs/s (movement messages)
Thanks and keep the awesome work!


---

<!-- source=github_issue; title=[Tropical Biome]Checklist; url=https://github.com/kaptain-kavern/CK_AnimalPlant_Pack/issues/2 -->

# [Tropical Biome]Checklist

- Source: github_issue
- URL: https://github.com/kaptain-kavern/CK_AnimalPlant_Pack/issues/2

- [ ] **[Change animal density repartition](https://github.com/kaptain-kavern/AnimalPack/issues/1) :**
**_Common**_: Anteater, Capybara, Chinchilla, Sloth, Tapir, Capuchin Monkey, Spider Monkey, Squirrel Monkey,
**_Uncommon**_: Gorilla, Jaguar, Orangutan, Panda Bear, Tiger, Macaw, Toucan, Parrot, Python, Peacock, Elephant
**_Rare**_: Cobra, Komodo Dragon, Panther, Iguana, Ocelot
**_Very Rare**_: Cassowary, White Tiger
**_Wild Animals to remove from Biome :**_
_Alpaca - Boomalope - Emu - Rat - Tortoise - Turkey - Wild Boar - Monkey_
- [ ] **[Change plant density repartition](https://github.com/kaptain-kavern/AnimalPack/issues/6) :**
**_Common**_: Fern (3 variations), Palm (3 variations), Teak Tree, Cecropia Tree
**_Uncommon**_: Bromeliad, Mahogany Tree, Strangler Fig
**_Rare**_: Corpse Flower, Bamboo
**_Wild Plants Removed from Biome :**_
_Bush - Raspberry - Tall Grass - Dandelion_
- [x] ~~**[Change Weather](https://github.com/kaptain-kavern/AnimalPack/issues/7) :**
Mostly Clear -> Mostly Rainy
Temperature/ Heat Index: from 20 - 30 to 20 - 39 (to account for humidity)~~
- [x] ~~**Animal Density decreased from 7.2 to 6.0**
_But it was originally 8 and not 7.2_~~
- [x] ~~**Pack Animals Removed from Biome :**
_Muffalo_~~
- [x] ~~**Pack Animals Added to Biome :**
_Elephant_
This one is bit trickier because of reference to PackAnimal in Defs for _/Core/Defs/FactionDefs/Factions_Misc.xml_ (see https://github.com/kaptain-kavern/AnimalPack/issues/3)~~
- [x] ~~**Plant Density increased from 1.0 to 3.0**~~
- [x] ~~**[Factions Added](https://github.com/kaptain-kavern/AnimalPack/issues/5) :**
Wilders
Jungle Traders~~


---

<!-- source=github_issue; title=Add JSILabel text class; url=https://github.com/Mihara/RasterPropMonitor/issues/486 -->

# Add JSILabel text class

- Source: github_issue
- URL: https://github.com/Mihara/RasterPropMonitor/issues/486

Once the callback system from Issue #343 is implemented, add a three-value color system to JSIVariableLabel:
```
variableName = (defined variable)
positiveColor = R,G,B,A
negativeColor = R,G,B,A
zeroColor = R,G,B,A
```
This addresses the use of variables simply to color text on those labels, which results in a lot of variable queries and string re-processing. Changing it to use the callback system to select colors will make it more responsive, and it will eliminate all of the round trips and string parsing overhead.


---

<!-- source=github_issue; title=[Ver 1.0.1] Some Issues/Feedback/Question; url=https://github.com/MehimoNemo/LethalCompanyShrinkRay/issues/66 -->

# [Ver 1.0.1] Some Issues/Feedback/Question

- Source: github_issue
- URL: https://github.com/MehimoNemo/LethalCompanyShrinkRay/issues/66

thread
Related comments:
keep up the good work! really enjoy ur creation
Will take a look at the issues in detail next Monday. Thanks for reporting.
Enlarging beyond normal size is a planned feature, which will come once the current version is more stable. It's planned somewhere after 0.4.0.
1. Current solution for enlarging is temporary and will change in the near future, likely through UI with mode selection
2. Good suggestion, but a little bit lower in priority currently. Will keep that in mind in my way towards 0.4.0
3. Good solution for single player, will keep it in mind
4. Weird, I always test in Lan mode. Do you have a logoutput from it?
5. The only one I don't fully agree with, as the gun is overall still a regular item


---

<!-- source=github_issue; title=Linux Version; url=https://github.com/StunlockStudios/vrising-dedicated-server-instructions/issues/1 -->

# Linux Version

- Source: github_issue
- URL: https://github.com/StunlockStudios/vrising-dedicated-server-instructions/issues/1

I know it's in the plans, where it's better to get notified when a Linux version will be available?
Even just an issue here (even this one) to which anyone can just subscribe would be fantastic, Thanks!


---

<!-- source=github_issue; title=1.2 Update; url=https://github.com/KSP-RO/RealismOverhaul/issues/1436 -->

# 1.2 Update

- Source: github_issue
- URL: https://github.com/KSP-RO/RealismOverhaul/issues/1436

- [x] RSS (req Kopernicus)
- [x] FAR https://github.com/ferram4/Ferram-Aerospace-Research/tree/KSP_update (tested, not yet live)
- [x] RF https://github.com/NathanKell/ModularFuelSystem/releases
- [x] TACLS https://github.com/KSP-RO/TacLifeSupport/releases
- [x] RealHeat needs recompile? (https://github.com/KSP-RO/RealHeat/pull/2)
- [x] AJE https://github.com/KSP-RO/AJE/tree/KSP_1.2 (not released, possibly close)
- [x] CLS https://github.com/codepoetpbowden/ConnectedLivingSpace/releases (I haven't tested)
- [x] CBK
- [x] DRE https://github.com/Starwaster/DeadlyReentry/releases (I haven't tested)
- [x] KJR https://github.com/ferram4/Kerbal-Joint-Reinforcement/releases/tag/v3.3.1
- [x] Persistent Rotation http://spacedock.info/mod/447/PersistentRotation
- [x] PF https://github.com/e-dog/ProceduralFairings/releases
- [x] PP https://github.com/Swamp-Ig/ProceduralParts/releases (worked fine w/o RF in KSP 1.2.2)
- [x] RealChute https://github.com/StupidChris/RealChute/releases/tag/v1.4.1.2
- [x] RT https://github.com/RemoteTechnologiesGroup/RemoteTech/releases/tag/1.8.3
- [x] TestFlight https://github.com/KSP-RO/TestFlight/releases/tag/1.8.0.0


---

<!-- source=github_issue; title=Unity 2018.2 Application.isWebPlayer error in ParseInitializeBehaviour...; url=https://github.com/parse-community/Parse-SDK-dotNET/issues/294 -->

# Unity 2018.2 Application.isWebPlayer error in ParseInitializeBehaviour...

- Source: github_issue
- URL: https://github.com/parse-community/Parse-SDK-dotNET/issues/294

Unity 2018.2 has removed the **UnityEngine.Application.isWebPlayer** property which is causing a runtime error. This is the full error:
```
MissingMethodException: Method not found: 'UnityEngine.Application.get_isWebPlayer'.
Parse.ParseClient.Initialize (Configuration configuration)
Parse.ParseClient.Initialize (System.String applicationId, System.String dotnetKey, System.String serverURL)
Parse.ParseInitializeBehaviour.Initialize ()
Parse.ParseInitializeBehaviour.Awake ()
```


---

<!-- source=github_issue; title=Problem with Spawning at runtime and with NetworkedTransform; url=https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/46 -->

# Problem with Spawning at runtime and with NetworkedTransform

- Source: github_issue
- URL: https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/46

Hi,
I try to implement a jenga tower. So, I have introduced a JengaBlock prefab. I have added the Networked Object, the Tracked Object, the Networked Transform, and the Rigidbody component. I have also included this prefab in the Networked Prefabs of my Network Manager. Then I have created an empty object and named it Spawn Networked Objects. With the Spawn Networked Objects selected I added a new script and named it SpawnNetworkedObjects.cs. For convenience I'm attaching you the script so you can reproduce the buggy behavior I get.
```csharp
using MLAPI;
using MLAPI.Data;
using MLAPI.MonoBehaviours.Core;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class SpawnNetworkedObjects : NetworkedBehaviour
{
public GameObject JengaBlock;
private GameObject[] JengaBlocks;
const int height = 8;
// This is equivalent to overriding OnStartServer()
private void Start()
{
JengaBlocks = new GameObject[height * 3];
NetworkingManager.singleton.OnServerStarted = makeJengaBlocks;
}
void makeJengaBlocks()
{
float xDistPercentage = 0.5f;
float yDistPercentage = 0.4f;
int i = 0;
for (int y = 0; y < height; y++)
{
for (int x = -1; x <= 1; x++)
{
if ((y & 1) == 0)
{
JengaBlocks[i] = Instantiate(JengaBlock, new Vector3(x * xDistPercentage, y * yDistPercentage, 0.0f), Quaternion.identity);
JengaBlocks[i].GetComponent<NetworkedObject>().Spawn();
}
else
{
JengaBlocks[i] = Instantiate(JengaBlock, new Vector3(0.0f, y * yDistPercentage, x * xDistPercentage), Quaternion.Euler(0.0f, 90.0f, 0.0f));
JengaBlocks[i].GetComponent<NetworkedObject>().Spawn();
}
i++;
}
}
}
}
```
There are two problems here:
1) although the Jenga tower is properly constructed on the Host, this is not the case for the Client.
2) When I interact with the Jenga blocks in one of the Clients, the blocks seem to not be synchronized between the Client and the Host.
How can I fix these issues? Is it something I'm doing so wrong here?
Thanks!


---

<!-- source=github_issue; title=Codist 5.13 Beta; url=https://github.com/wmjordan/Codist/issues/169 -->

# Codist 5.13 Beta

- Source: github_issue
- URL: https://github.com/wmjordan/Codist/issues/169

## Notice
My mother is seriously sick.
I am busy looking for Traditional Chinese Medicine (TCM) therapy which may bring the best treatment to her, after that the doctors in the hospital said that they told me the situation was not good.
## Update on 10-22
My mother's situation got better then worsen. I felt sad about that.
I have to learn TCM harder and could not yet afford too much time on Codist and in the following months.
The new beta released had addressed the memory leak issue of Codist and #177.
## Support for VS 2022
The support for VS 2022 appears to be done after the release of VS 2022 Preview 7.
## Download
[Codist 6897](https://github.com/wmjordan/Codist/files/7452922/Codist.zip)
[Codist 6874](https://github.com/wmjordan/Codist/files/7377359/Codist.zip)
[Codist 6754](https://github.com/wmjordan/Codist/files/7235066/Codist.zip)
[Codist 6730](https://github.com/wmjordan/Codist/files/7175664/Codist.zip)
[Codist 6713](https://github.com/wmjordan/Codist/files/6948342/Codist.zip)
[Codist 6707](https://github.com/wmjordan/Codist/files/6930366/Codist.zip)
[Codist 6688](https://github.com/wmjordan/Codist/files/6920251/Codist.zip)
[Codist 6686](https://github.com/wmjordan/Codist/files/6910448/Codist.zip)
[Codist 6672](https://github.com/wmjordan/Codist/files/6904392/Codist.zip)
[Codist 6657](https://github.com/wmjordan/Codist/files/6897296/Codist.zip)
[Codist 6651](https://github.com/wmjordan/Codist/files/6889454/Codist.zip)
[Codist 6646](https://github.com/wmjordan/Codist/files/6883128/Codist.zip)
[Codist 6623](https://github.com/wmjordan/Codist/files/6878280/Codist.zip)
## General
* [X] Support VS 2022 (b6623, b6651, b6657, b6672, b6686, b6688, b6730, b6897)
* [x] #171 (b6646)
* [x] #173 (b6754, b6874)
## Syntax Highlight
* [x] Fixed memory leak and CPU usage issue (b6707, b6713)
## Navigation Bar
* [x] #177 (b6874)
* [x] Drop-down menus on the right side of the bar were incompletely visible (b6874)


---

<!-- source=github_issue; title=General Support Issue; url=https://github.com/TweakScale/TweakScale/issues/92 -->

# General Support Issue

- Source: github_issue
- URL: https://github.com/TweakScale/TweakScale/issues/92

This issue is for general support for people that have a github account and prefer to handle things here.
(way more practical than using dropbox!).
Please use this issue for initial contact. We may open a new issue for handling your issue if needed, but most cases are simple enough to be handled on a couple posts, so this is the best place to start up!


---

<!-- source=github_issue; title=Issue getting VideoAdsSample to display ads when built as Windows Store App; url=https://github.com/microsoft/unityplugins/issues/21 -->

# Issue getting VideoAdsSample to display ads when built as Windows Store App

- Source: github_issue
- URL: https://github.com/microsoft/unityplugins/issues/21

Issue:
I am not able to see Video Ads when I deploy the Unity VideoAdsSample project as a Windows Store App. Below are the steps I am taking and the results.
1. Ran the PowerShell script successfully.
2. Opened the Unity Video Ad Sample project unityplugins-master\Samples\Advertising\VideoAdsSample
3. Imported unityplugins-master\UnityPackages\Microsoft.UnityPlugins.Advertising
4. I attempted to build the project as Window Store app and received the attached error
<img width="1188" alt="unitybuilderror" src="https://cloud.githubusercontent.com/assets/4729905/10899232/b7ccda4c-81a0-11e5-8ace-c5d2e516f94d.PNG">
5. I was able to resolve the issue by changing the platforms for plugins from "Any Platform" to "Editor" on Assets/Plugins/Microsoft.UnityPlugins.Advertising
<img width="582" alt="advertisingdllplugin_editor" src="https://cloud.githubusercontent.com/assets/4729905/10899240/cdbed83c-81a0-11e5-9309-7d4f409a91ee.PNG">
6. I was then able to build for the Window Store
7. I added Microsoft.UnityPlugins.Utils.Initialize((action) => AppCallbacks.Instance.InvokeOnAppThread(new AppCallbackItem(() => action()), false)) after Window.Current.Activate() within App.xaml.cs
8. I rebuilt the solution for Release x86 and received the following error message. I have attached a screenshot and the output for Build and Debug.
<img width="901" alt="windows10applicationerror" src="https://cloud.githubusercontent.com/assets/4729905/10899262/0f850bce-81a1-11e5-8bdd-675410fb63eb.PNG">
***************\* BEGIN Output_Build.txt *****************
1>------ Build started: Project: VideoAdsSample, Configuration: Release x86 ------
1> UnityInstallationDir "C:\Program Files\Unity\Editor".
1> UnityWSAPlayerDir "C:\Program Files\Unity\Editor\Data\PlaybackEngines\metrosupport".
1> UnityProjectDir "C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample".
1> Copying unprocessed assemblies...
1> Running AssemblyConverter...
1> AssemblyConverter done.
1> VideoAdsSample -> C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\VideoAdsSample.exe
1>C:\Program Files (x86)\MSBuild\Microsoft\VisualStudio\v14.0\AppxPackage\Microsoft.AppXPackage.Targets(1778,5): warning APPX1707: No implementation file was provided for the .winmd file 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\Microsoft.Advertising.winmd'. To generate registration information in the app manifest, specify the 'Implementation' metadata on the .winmd reference item in the project file.
2>------ Deploy started: Project: VideoAdsSample, Configuration: Release x86 ------
2>Updating the layout...
2>Copying files: Total 4 mb to layout...
2>Checking whether required frameworks are installed...
2>Registering the application to run from layout...
2>Deployment complete (913ms). Full package name: "VideoAdsSample_1.0.0.0_x86__pzq3xp76mxafg"
========== Build: 1 succeeded, 0 failed, 0 up-to-date, 0 skipped ==========
========== Deploy: 1 succeeded, 0 failed, 0 skipped ==========
***************\* END Output_Build.txt *****************
***************\* BEGIN Output_Debug.txt *****************
'VideoAdsSample.exe' (CoreCLR: DefaultDomain): Loaded 'C:\Program Files\WindowsApps\Microsoft.NET.CoreRuntime.1.0_1.0.23302.0_x86__8wekyb3d8bbwe\mscorlib.ni.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\entrypoint\VideoAdsSample.exe'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
Symbols for the module 'VideoAdsSample.exe' were not loaded.
1. Use a debug build configuration or disable the debug option 'Enable Just My Code'.
2. Check the 'Symbols' settings under debugging options.'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Runtime.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\WinMetadata\Windows.winmd'. Module was built without symbols.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Runtime.InteropServices.WindowsRuntime.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\UnityPlayer.winmd'. Module was built without symbols.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Runtime.WindowsRuntime.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Runtime.WindowsRuntime.UI.Xaml.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\Microsoft.UnityPlugins.Common.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Collections.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\WinRTBridge.winmd'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\BridgeInterface.winmd'. Module was built without symbols.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Private.Uri.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Threading.Tasks.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\UnityEngine.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\Assembly-CSharp-firstpass.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\Assembly-CSharp.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\UnityEngine.Networking.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\UnityEngine.UI.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.IO.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Net.Primitives.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Private.Networking.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Reflection.Primitives.dll'. Module was built without symbols.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Reflection.dll'. Module was built without symbols.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Text.Encoding.dll'. Module was built without symbols.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Runtime.InteropServices.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Threading.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Runtime.Extensions.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Diagnostics.Debug.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
Module information:
Built with Compiler Ver '190023026'
Built from '5.2/release' branch
Version is '5.2.2f1 (3757309da7e7)'
Release build
Application type 'XAML'
Used 'UWP'
PlayerConnection initialized from C:/Users/scott.havird/Downloads/unityplugins-master_1.0/unityplugins-master/Samples/Advertising/VideoAdsSample/out_2015.11.02_pm/VideoAdsSample/bin/x86/Release/AppX/Data (debug = 0)
PlayerConnection initialized network socket : 0.0.0.0 55179
Multi-casting "[IP] 10.0.1.6 [Port] 55179 [Flags] 2 [Guid] 1889589057 [EditorId] 4294967295 [Version] 1048832 [Id] MetroPlayerX86(DESKTOP-F93AH1S) [Debug] 0" to [225.0.0.222:54997]...
GfxDevice: creating device client; threaded=1
Disabling Low Latency presentation API.
Direct3D:
```
Version: Direct3D 11.0 [level 11.0]
Renderer: NVIDIA GeForce GT 750M (ID=0xfe9)
Vendor: NVIDIA
VRAM: 1990 MB
```
Initialize engine version: 5.2.2f1 (3757309da7e7)
Disabling independent input source.
Logical Screen DPI is 144.00.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\UnityEngineProxy.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\Microsoft.UnityPlugins.Advertising.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Linq.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Text.RegularExpressions.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled.
'VideoAdsSample.exe' (CoreCLR: CoreCLR_UWP_Domain): Loaded 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\bin\x86\Release\AppX\System.Globalization.dll'. Module was built without symbols.
Start-ad initiation
(Filename: C:/buildslave/unity/build/artifacts/generated/Metro/runtime/UnityEngineDebugBindings.gen.cpp Line: 70)
Exception: Object reference not set to an instance of an object.
Type: System.NullReferenceException
Module: Assembly-CSharp
InnerException: <No Data>
AdditionalInfo:<No Data>
at mainSceneManager.Start()
at mainSceneManager.$Invoke7(Int64 instance, Int64\* args)
at UnityEngine.Internal.$MethodUtility.InvokeMethod(Int64 instance, Int64\* args, IntPtr method)
(Filename: Line: 0)
NullReferenceException: Object reference not set to an instance of an object.
at mainSceneManager.Start()
at mainSceneManager.$Invoke7(Int64 instance, Int64\* args)
at UnityEngine.Internal.$MethodUtility.InvokeMethod(Int64 instance, Int64\* args, IntPtr method)
(Filename: <Unknown> Line: 0)
NullReferenceException: Object reference not set to an instance of an object.
at mainSceneManager.RequestAd()
at UnityEngine.Events.InvokableCall.Invoke(Object[] args)
at UnityEngine.Events.InvokableCallList.Invoke(Object[] parameters)
at UnityEngine.UI.Button.Press()
at UnityEngine.UI.Button.OnPointerClick(PointerEventData eventData)
at UnityEngine.EventSystems.ExecuteEvents.Execute(IPointerClickHandler handler, BaseEventData eventData)
at UnityEngine.EventSystems.ExecuteEvents.Execute[T](GameObject target, BaseEventData eventData, EventFunction`1 functor)
(Filename: <Unknown> Line: 0)
NullReferenceException: Object reference not set to an instance of an object.
at mainSceneManager.ShowAd()
at UnityEngine.Events.InvokableCall.Invoke(Object[] args)
at UnityEngine.Events.InvokableCallList.Invoke(Object[] parameters)
at UnityEngine.UI.Button.Press()
at UnityEngine.UI.Button.OnPointerClick(PointerEventData eventData)
at UnityEngine.EventSystems.ExecuteEvents.Execute(IPointerClickHandler handler, BaseEventData eventData)
at UnityEngine.EventSystems.ExecuteEvents.Execute[T](GameObject target, BaseEventData eventData, EventFunction`1 functor)
(Filename: <Unknown> Line: 0)
Trimming D3D resources.
The program '[14168] VideoAdsSample.exe: Program Trace' has exited with code 0 (0x0).
The program '[14168] VideoAdsSample.exe' has exited with code 1 (0x1).
***************\* END Output_Debug.txt *****************
The output for the build shows some interesting information, line 9 from Output_Build.txt"C:\Program Files (x86)\MSBuild\Microsoft\VisualStudio\v14.0\AppxPackage\Microsoft.AppXPackage.Targets(1778,5): warning APPX1707: No implementation file was provided for the .winmd file 'C:\Users\scott.havird\Downloads\unityplugins-master_1.0\unityplugins-master\Samples\Advertising\VideoAdsSample\out_2015.11.02_pm\VideoAdsSample\Microsoft.Advertising.winmd'. To generate registration information in the app manifest, specify the 'Implementation' metadata on the .winmd reference item in the project file." Could this be why I am recieving the null reference exception?
Setup:
unityplugins version 1.0
Visual Studio Enterpirse 2015 Version 14.0.23107.0 D14REL
.NET Framework Version 4.6.00079
Thanks,
Scott


---

<!-- source=github_issue; title=Change Camera Views Using Python Apis; url=https://github.com/lgsvl/simulator/issues/1246 -->

# Change Camera Views Using Python Apis

- Source: github_issue
- URL: https://github.com/lgsvl/simulator/issues/1246

Hi
Currently, there are 3 camera views 'Follow', 'Cinematic' and 'Free' available in LGSVL simulator. How to perform the following activities while running simulator from Python Api's:
1) Switch between camera views,
2) Control zoom in/out of a particular camera angle,
3) Offset position of camera to either left or right direction to get better view of scenario.


---

<!-- source=github_issue; title=Game slows down/freezes after playing a while; url=https://github.com/TeamPorcupine/ProjectPorcupine/issues/796 -->

# Game slows down/freezes after playing a while

- Source: github_issue
- URL: https://github.com/TeamPorcupine/ProjectPorcupine/issues/796

Playing the game whether in the Unity editor or as a standalone program after placing a few furniture the garbage collection (we think) goes nuts and freezes the game, pretty good sign in Unity that GC is taking place.
The length of freezes seems to be tied to the number and complexity of the furniture placed, for example 40 stockpiles creates small but very frequent freezes while a smelter and a miner creates longer less frequent freezes that leads to the game freezes for more than 2 minutes.
Some users see a increased memory usage,I didn't. I think that is just when running in Unity editor. Many saw an increased cpu usage during the freezes mine jumped from 10% to 22% during the freeze events.
We discussed this in the discord chat and one theory is that has to do with the number of foreach loops since a foreach triggers GC.
Developers involved where @Mizipzor , @NogginBops and @longtomjr


---

<!-- source=github_issue; title=allow references to structs to be stored in fields of ref structs; url=https://github.com/dotnet/csharplang/issues/1147 -->

# allow references to structs to be stored in fields of ref structs

- Source: github_issue
- URL: https://github.com/dotnet/csharplang/issues/1147

Unity is a game engine that uses C# extensively.
We're in need of a way to have a struct that contains one or more pointers to other structs that we want to be able to read/write from/to. We do this with unsafe code today:
```C#
struct Color { float r,g,b; }
unsafe struct Group
{
Color* _color;
ref Color color => ref *_color;
}
```
But we would love to do this without unsafe code, and would like to suggest a feature where it's allowed to store references to structs in fields of ref structs, that can guarantee that these pointers don't escape onto the heap:
```C#
struct Color { float r,g,b; }
ref struct Group
{
ref Color color;
}
```
**EDIT** link to spec for this feature https://github.com/dotnet/csharplang/blob/main/proposals/low-level-struct-improvements.md


---

<!-- source=github_issue; title=MacGameNSWindow throwing exception at startup; url=https://github.com/MonoGame/MonoGame/issues/4451 -->

# MacGameNSWindow throwing exception at startup

- Source: github_issue
- URL: https://github.com/MonoGame/MonoGame/issues/4451

I've just updated to the latest git version of MonoGame at the time I'm writing this.
I created a new MonoGame (MonoMac) project and run it and it throws the following error:
```
Unhandled Exception:
System.NullReferenceException: Object reference not set to an instance of an object
at ObjCRuntime.Class.Register (System.Type type) [0x00001] in <filename unknown>:0
at ObjCRuntime.Class.GetHandle (System.Type type) [0x00001] in <filename unknown>:0
at Foundation.NSObject.AllocIfNeeded () [0x0001e] in <filename unknown>:0
at Foundation.NSObject..ctor (Foundation.NSObjectFlag x) [0x00007] in <filename unknown>:0
at AppKit.NSResponder..ctor (Foundation.NSObjectFlag t) [0x00000] in <filename unknown>:0
at AppKit.NSWindow..ctor (CGRect contentRect, NSWindowStyle aStyle, NSBackingStore bufferingType, Boolean deferCreation) [0x00000] in <filename unknown>:0
at Microsoft.Xna.Framework.MacGameNSWindow..ctor (CGRect rect, NSWindowStyle style, NSBackingStore backing, Boolean defer) [0x00000] in /Users/tanis/Documents/MonoGame/MonoGame.Framework/MacOS/MacGameNSWindow.cs:64
at Microsoft.Xna.Framework.MacGamePlatform.InitializeMainWindow () [0x0002f] in /Users/tanis/Documents/MonoGame/MonoGame.Framework/MacOS/MacGamePlatform.cs:133
at Microsoft.Xna.Framework.MacGamePlatform..ctor (Microsoft.Xna.Framework.Game game) [0x00038] in /Users/tanis/Documents/MonoGame/MonoGame.Framework/MacOS/MacGamePlatform.cs:117
at Microsoft.Xna.Framework.GamePlatform.PlatformCreate (Microsoft.Xna.Framework.Game game) [0x00002] in /Users/tanis/Documents/MonoGame/MonoGame.Framework/GamePlatform.Desktop.cs:18
at Microsoft.Xna.Framework.Game..ctor () [0x0020d] in /Users/tanis/Documents/MonoGame/MonoGame.Framework/Game.cs:68
at StencilBuffer.MacOS.Game1..ctor () [0x00000] in /Users/tanis/Documents/MonoGame/Test/Interactive/MacOS/StencilBuffer.MacOS/Game1.cs:19
at StencilBuffer.MacOS.AppDelegate.FinishedLaunching (MonoMac.Foundation.NSObject notification) [0x00028] in /Users/tanis/Documents/MonoGame/Test/Interactive/MacOS/StencilBuffer.MacOS/Main.cs:39
at (wrapper dynamic-method) System.Object:[StencilBuffer.MacOS.AppDelegate:Void FinishedLaunching(MonoMac.Foundation.NSObject)] (MonoMac.Foundation.NSObject,MonoMac.ObjCRuntime.Selector,MonoMac.Foundation.NSObject)
at (wrapper native-to-managed) System.Object:[StencilBuffer.MacOS.AppDelegate:Void FinishedLaunching(MonoMac.Foundation.NSObject)] (MonoMac.Foundation.NSObject,MonoMac.ObjCRuntime.Selector,MonoMac.Foundation.NSObject)
at (wrapper managed-to-native) MonoMac.AppKit.NSApplication:NSApplicationMain (int,string[])
at MonoMac.AppKit.NSApplication.Main (System.String[] args) [0x0003d] in <filename unknown>:0
at StencilBuffer.MacOS.Program.Main (System.String[] args) [0x0001d] in /Users/tanis/Documents/MonoGame/Test/Interactive/MacOS/StencilBuffer.MacOS/Main.cs:22
[ERROR] FATAL UNHANDLED EXCEPTION: System.NullReferenceException: Object reference not set to an instance of an object
at ObjCRuntime.Class.Register (System.Type type) [0x00001] in <filename unknown>:0
at ObjCRuntime.Class.GetHandle (System.Type type) [0x00001] in <filename unknown>:0
at Foundation.NSObject.AllocIfNeeded () [0x0001e] in <filename unknown>:0
at Foundation.NSObject..ctor (Foundation.NSObjectFlag x) [0x00007] in <filename unknown>:0
at AppKit.NSResponder..ctor (Foundation.NSObjectFlag t) [0x00000] in <filename unknown>:0
at AppKit.NSWindow..ctor (CGRect contentRect, NSWindowStyle aStyle, NSBackingStore bufferingType, Boolean deferCreation) [0x00000] in <filename unknown>:0
at Microsoft.Xna.Framework.MacGameNSWindow..ctor (CGRect rect, NSWindowStyle style, NSBackingStore backing, Boolean defer) [0x00000] in /Users/tanis/Documents/MonoGame/MonoGame.Framework/MacOS/MacGameNSWindow.cs:64
at Microsoft.Xna.Framework.MacGamePlatform.InitializeMainWindow () [0x0002f] in /Users/tanis/Documents/MonoGame/MonoGame.Framework/MacOS/MacGamePlatform.cs:133
at Microsoft.Xna.Framework.MacGamePlatform..ctor (Microsoft.Xna.Framework.Game game) [0x00038] in /Users/tanis/Documents/MonoGame/MonoGame.Framework/MacOS/MacGamePlatform.cs:117
at Microsoft.Xna.Framework.GamePlatform.PlatformCreate (Microsoft.Xna.Framework.Game game) [0x00002] in /Users/tanis/Documents/MonoGame/MonoGame.Framework/GamePlatform.Desktop.cs:18
at Microsoft.Xna.Framework.Game..ctor () [0x0020d] in /Users/tanis/Documents/MonoGame/MonoGame.Framework/Game.cs:68
at StencilBuffer.MacOS.Game1..ctor () [0x00000] in /Users/tanis/Documents/MonoGame/Test/Interactive/MacOS/StencilBuffer.MacOS/Game1.cs:19
at StencilBuffer.MacOS.AppDelegate.FinishedLaunching (MonoMac.Foundation.NSObject notification) [0x00028] in /Users/tanis/Documents/MonoGame/Test/Interactive/MacOS/StencilBuffer.MacOS/Main.cs:39
at (wrapper dynamic-method) System.Object:[StencilBuffer.MacOS.AppDelegate:Void FinishedLaunching(MonoMac.Foundation.NSObject)] (MonoMac.Foundation.NSObject,MonoMac.ObjCRuntime.Selector,MonoMac.Foundation.NSObject)
at (wrapper native-to-managed) System.Object:[StencilBuffer.MacOS.AppDelegate:Void FinishedLaunching(MonoMac.Foundation.NSObject)] (MonoMac.Foundation.NSObject,MonoMac.ObjCRuntime.Selector,MonoMac.Foundation.NSObject)
at (wrapper managed-to-native) MonoMac.AppKit.NSApplication:NSApplicationMain (int,string[])
at MonoMac.AppKit.NSApplication.Main (System.String[] args) [0x0003d] in <filename unknown>:0
at StencilBuffer.MacOS.Program.Main (System.String[] args) [0x0001d] in /Users/tanis/Documents/MonoGame/Test/Interactive/MacOS/StencilBuffer.MacOS/Main.cs:22
```
Is there anything obvious that I could be missing?
Thanks!


---

<!-- source=github_issue; title=Google Play Games Services plugin v10; url=https://github.com/playgameservices/play-games-plugin-for-unity/issues/2687 -->

# Google Play Games Services plugin v10

- Source: github_issue
- URL: https://github.com/playgameservices/play-games-plugin-for-unity/issues/2687

Google Play Game Services is pleased to announce that Google Play Games Services plugin v10 is now available.
The new plugin now directly uses the main PGS Java SDK. As a result, the new plugin is significantly smaller and by using Proguard you may be able to decrease it even further. Directly accessing the Java SDK also makes it easier to debug issues.
Please help us to continue to improve the Plugin by reporting bugs in this version of the plugin. In a few weeks, we will merge this version into the Master branch with reported bugs addressed.
### Using the new plugin
If you are already using the Google Play Games Services Plugin in your project, you can update to the new one by deleting the GooglePlayGames directory from your project and importing the new package that can be found [here](https://github.com/playgameservices/play-games-plugin-for-unity/tree/android-java-client/current-build).
If you are not yet using Google Play Games Services Plugin, then follow the instructions in the Readme file but use the new package which can be found [here](https://github.com/playgameservices/play-games-plugin-for-unity/tree/android-java-client/current-build) instead of the one in current-build.


---

<!-- source=github_issue; title=[Todo list] Future-proofing MonoGame; url=https://github.com/MonoGame/MonoGame/issues/6879 -->

# [Todo list] Future-proofing MonoGame

- Source: github_issue
- URL: https://github.com/MonoGame/MonoGame/issues/6879

Hey there!
Many efforts have been started to future-proof MonoGame and make it a modern .Net framework but it seems that there is no comprehensive centralized point where to understand how things should move forward and their current state.
Hence, I'm trying to maintain this issue to keep track of the different tasks. Please feel free to point me to any untracked tasks or progress.
I guess that we will agree on the following main objective: **making MonoGame fully .Net Standard 2.0 compliant in its entirety** (all targets, all of its tools, and its build/test/package process), while maintaining a backward compatibility where it's relevant.
This would mean: being able to consume MonoGame as a ```dotnet``` (Core) framework, and as a full .Net framework.
So here comes the long list. @cra0zy @Jjagg @tomspilman please let me know if this list makes sense to you and if there's anything more to say about the current state of the repository.
**Moving to .Net Standard 2.0 (and .Net Core compatibility):**
- [x] Removing Protobuild & switching to SDK-style project format #6207 #6768 #4975 #6604
- [x] MonoGame.Framework
- [x] Windows DirectX
- [x] Windows UWP
- [x] DesktopGL
- [x] Android
- [x] iOS
- [x] Archive MonoGame.Framework.Net to a dedicated repo (#6900) -> https://github.com/MonoGame/MonoGame.Framework.Net
- [x] MonoGame.Framework.Content.Pipeline
- [x] Windows
- [x] macOS
- [x] Linux
- [x] Tools/2MGFX
- [x] Windows/macOS/Linux
- [x] Tools/MGCB
- [x] Windows/macOS/Linux
- [x] Tools/Pipeline
- [x] Windows/macOS/Linux
- [x] Remove Protobuild and any file/folder related to it
- [x] Making all tools Dotnet Tools and packaging them as nugets (and make the templates to use them)
- [x] MGCB #6905 #6930
- [x] 2MGFX #6930
- [x] Pipeline #6922
- [x] Making Core templates (that uses global tools) and publishing them as nuget for ```dotnet new -i``` #6930
- [x] Windows DirectX
- [x] ~Windows UWP~ (not .net core compatible)
- [x] DesktopGL
- [x] ~Android~ (not .net core compatible)
- [x] ~iOS~ (not .net core compatible)
- [x] ~Making all targets ```dotnet build/publish``` compatible~ #5339 -> WindowsDX and DesktopGL support `dotnet build`; others require full MSBuild so they can't be built with portable MSBuild that dotnet CLI uses.
**Getting Team City continuous integration to work again:**
- [x] Tests (content pipeline tests should be moved to dedicated test projects)
- [x] Windows DirectX #6957
- [x] DesktopGL #6957
- [x] Building and publishing all targets as nugets #6773
**Keeping a compatibility toward full framework users:**
- [x] Defining which backward compatibility target(s) make sense beside ```netstandard2.0``` (net4? net45? net451?) => ```net452``` that is
- [x] ~Making traditional non-Core templates (that would be packaged as a VS extension along with the tools they would rely on?) for full framework users~ (not relevant anymore)
- [x] ~Allowing to install non-Core tools & templates to MSBuild when building from source (e.g. auto-deploy target at build time) for full framework users~ (not relevant anymore)
- [x] Packaging project templates into a Visual Studio Extension so that templates can be distributed without the need of an installer
**Documentation:**
- [x] Update the Getting Started documentation for setting up projects for all targets
- [x] Update the Publishing & Packaging documentation for distributing apps on all targets
- [x] Document how to build MonoGame from source code and debug it
**Maintenance:**
- [x] Removing the installer #6842
- [x] Dropping irrelevant targets
- [x] macOS (should be integrated into DesktopGL after VideoPlayer has been implemented there -> #6860)
- [x] Linux/WindowsGL (is equivalent to DesktopGL and should be renamed/removed) -> naming is because of Protobuild, the SDK-style project is named DesktopGL.
- [x] Windows Phone? (already dropped)
- [x] ~Web (not maintained)~
- [x] ~tvOS (not maintained)~
- [x] Remove obsolete IDE extensions
- [x] Remove obsolete nuget nuspec
- [x] Remove obsolete zip templates and build F# templates
- [x] Make the Cake script to output all nuget artifacts to the same folder (e.g. ```./ouput``` or ```./build``` once protobuild is gone)
**Bonus stage for console targets (which unfortunately can't be discussed publicly):**
- [x] ~Keeping VS2015 and net45 non-SDK style projects while being compatible with the parent repository structure~ (deprecated)
- [x] Refactoring MGCB and Pipeline to find console targets
- [x] Enforce C# 5.0 language version


---

<!-- source=github_issue; title=Auth cause ClassNotFoundException on GameHelper.; url=https://github.com/playgameservices/play-games-plugin-for-unity/issues/81 -->

# Auth cause ClassNotFoundException on GameHelper.

- Source: github_issue
- URL: https://github.com/playgameservices/play-games-plugin-for-unity/issues/81

I have follow document to install and configure but can't seem to make it work,
even on Minimal project. I'm using Unity 4.3.3f1 and latest version of Google Play Game plugin with Android 4.0.4.
Here is the logcat
03-27 16:32:29.257: I/Unity(13570): [Play Games Plugin DLL] Creating platform-specific Play Games client.
03-27 16:32:29.387: I/Unity(13570): [Play Games Plugin DLL] Making sure PlayGamesHelperObject is ready.
03-27 16:32:29.417: I/Unity(13570): [Play Games Plugin DLL] Initializing Android Client.
03-27 16:32:29.417: I/Unity(13570): [Play Games Plugin DLL] Creating GameHelperManager to manage GameHelper.
03-27 16:32:29.427: I/Unity(13570): [Play Games Plugin DLL] Setting up GameHelperManager.
03-27 16:32:29.427: I/Unity(13570): [Play Games Plugin DLL] GHM creating GameHelper.
03-27 16:32:29.447: I/Unity(13570): [Play Games Plugin DLL] PlayGamesHelperObject created.
03-27 16:32:29.447: I/Unity(13570): [Play Games Plugin DLL] AUTH: starting auth process, silent=False
03-27 16:32:29.457: I/Unity(13570): [Play Games Plugin DLL] GHM calling GameHelper constructor with flags=7
03-27 16:32:29.647: I/Unity(13570): AndroidJavaException: java.lang.ClassNotFoundException: com.google.example.games.basegameutils.GameHelper
03-27 16:32:29.647: I/Unity(13570): at UnityEngine.AndroidJNISafe.CheckException () [0x00000] in <filename unknown>:0
03-27 16:32:29.647: I/Unity(13570): at UnityEngine.AndroidJNISafe.CallStaticObjectMethod (IntPtr clazz, IntPtr methodID, UnityEngine.jvalue[] args) [0x00000] in <filename unknown>:0
03-27 16:32:29.647: I/Unity(13570): at UnityEngine.AndroidJavaObject._CallStatic[AndroidJavaObject](System.String methodName, System.Object[] args) [0x00000] in <filename unknown>:0
03-27 16:32:29.647: I/Unity(13570): at UnityEngine.AndroidJavaObject.CallStatic[AndroidJavaObject](System.String methodName, System.Object[] args) [0x00000] in <filename unknown>:0
03-27 16:32:29.647: I/Unity(13570): at UnityEngine.AndroidJavaObject.FindClass (System.String name) [0x00000] in <filename unknown>:0
03-27 16:32:29.647: I/Unity(13570): at UnityEngine.AndroidJavaObject._AndroidJavaObject (System.String className, System.Object[] args) [0x00000] in <filename unknown>:0
03-27 16:32:29.647: I/Unity(13570): at UnityEngine.AndroidJavaObject..ctor (System.String className, System.Object[] args) [0x00000] in <filename unknown>:0
03-27 16:32:29.647: I/Unity(13570): at GooglePlayGames.A
03-27 16:32:29.657: I/Unity(13570): NullReferenceException: Object reference not set to an instance of an object
03-27 16:32:29.657: I/Unity(13570): at GooglePlayGames.Android.AndroidClient+<Authenticate>c__AnonStorey17.<>m__1 () [0x00000] in <filename unknown>:0
03-27 16:32:29.657: I/Unity(13570): at UnityEngine.AndroidJavaRunnableProxy.run () [0x00000] in <filename unknown>:0
03-27 16:32:29.657: I/Unity(13570): at System.Reflection.MonoMethod.Invoke (System.Object obj, BindingFlags invokeAttr, System.Reflection.Binder binder, System.Object[] parameters, System.Globalization.CultureInfo culture) [0x00000] in <filename unknown>:0
03-27 16:32:29.657: I/Unity(13570): Rethrow as TargetInvocationException: UnityEngine.AndroidJavaRunnableProxy.run()
03-27 16:32:29.657: I/Unity(13570): at UnityEngine.AndroidJavaProxy.Invoke (System.String methodName, System.Object[] args) [0x00000] in <filename unknown>:0
03-27 16:32:29.657: I/Unity(13570): at UnityEngine.AndroidJavaProxy.Invoke (System.String methodName, UnityEngine.AndroidJavaObject[] javaArgs) [0x00000] in <filename unknown>:0
03-27 16:32:29.657: I/Unity(13570): at UnityEngine._AndroidJNIHelper.InvokeJavaProxyMethod (UnityEngine.AndroidJavaProxy proxy, IntPtr jmethodName, IntPtr jargs) [0x00000] in <filename unknown>:0


---

<!-- source=github_issue; title=Not an Issue, but I thought This may be of Interest; url=https://github.com/SamDel/ChromeCast-Desktop-Audio-Streamer/issues/19 -->

# Not an Issue, but I thought This may be of Interest

- Source: github_issue
- URL: https://github.com/SamDel/ChromeCast-Desktop-Audio-Streamer/issues/19

I have noted some 'interesting' observations, and am sharing them here in case they may offer some ideas for the User Interface. See attached PDF...
[ChromecastDesktopAudioStreamer-MyNotes.pdf](https://github.com/SamDel/ChromeCast-Desktop-Audio-Streamer/files/2741153/ChromecastDesktopAudioStreamer-MyNotes.pdf)


---

<!-- source=github_issue; title=Spawning A Player and a Non-Player Object; url=https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/40 -->

# Spawning A Player and a Non-Player Object

- Source: github_issue
- URL: https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/40

Hi,
I try to implement the following simple game. Two clients (the host and the remote-client) move a Cube object that is on the Server.
I have introduced the NetworkedObject, the NetworkedTransform and the TrackedObject components. onto the Cube's prefab. I have selected the "Server Only" box in its NetworkedObject component. In my Network Manager object I have set the size to 1 in order to have two spawnable Prefabs, the Cube and the Player. When I start the standalone application and I select Host, only the Player appears, not the Cube. Then, I run the application from unity's editor as a Client and the second player appears. The two scenes seem to be well synced but the Cube is missing.
I have two questions:
1) How do I spawn an object? I want the players to start from different initial position because some weird stuff happen when they collide in the very beginning.
2) How am I supposed to instantiate the Cube properly and make it appear in the game? In the Multiplayer Networking Unity-tutorial (where the HLAPI was used instead), the non-player objects were instantiated within the overridden function OnStartServer(). What is the equivalent function in MLAPI? If there is not one, where should I instantiate my Cube? Furthermore they were using NetworkServer.spawn(non-player-object). What's the equivalent of this in MLAPI?
Thanks!


---

<!-- source=github_issue; title=Game Crashed at Sign In; url=https://github.com/playgameservices/play-games-plugin-for-unity/issues/1724 -->

# Game Crashed at Sign In

- Source: github_issue
- URL: https://github.com/playgameservices/play-games-plugin-for-unity/issues/1724

At Sign Up time my app get crashed using this plugin.
Here are error log that I was getting.
![screen shot 2017-05-03 at 11 32 39 pm](https://cloud.githubusercontent.com/assets/3082151/25674647/4541a976-3059-11e7-87aa-e16aa3dbdd58.png)
Here are Plugins/Android folder structure:
![screen shot 2017-05-03 at 11 34 45 pm](https://cloud.githubusercontent.com/assets/3082151/25674685/6e9dd600-3059-11e7-99c3-d569271031d5.png)
Please reply me for this, what I require to do for solving this error.


---

<!-- source=github_issue; title=Can't Start OmniSharp; url=https://github.com/dotBunny/VSCode/issues/2 -->

# Can't Start OmniSharp

- Source: github_issue
- URL: https://github.com/dotBunny/VSCode/issues/2

Looks like OmniSharp can't start, so many features aren't working? My log:
```
[INFO] Starting OmniSharp at '/Users/mathe015/Repositories/MatchThreeMoji/MatchThreeMoji-csharp.sln'...
[INFO] Started OmniSharp from '/Applications/Visual Studio Code.app/Contents/Resources/app/plugins/vs.language.csharp.o/bin/omnisharp' with process id 77938...
Can't find custom attr constructor image: /Applications/Visual Studio Code.app/Contents/Resources/app/plugins/vs.language.csharp.o/bin/approot/packages/Microsoft.AspNet.Cryptography.Internal/1.0.0-beta4/lib/dnx451/Microsoft.AspNet.Cryptography.Internal.dll mtoken: 0x0a000004
* Assertion at class.c:5695, condition `!mono_loader_get_last_error ()' not met
Stacktrace:
at <unknown> <0xffffffff>
at Microsoft.Framework.DependencyInjection.DataProtectionServices/<GetDefaultServices>d__0.MoveNext () <0x0021b>
at Microsoft.Framework.DependencyInjection.ServiceCollectionExtensions.TryAdd (Microsoft.Framework.DependencyInjection.IServiceCollection,System.Collections.Generic.IEnumerable`1<Microsoft.Framework.DependencyInjection.ServiceDescriptor>) <0x00064>
at Microsoft.Framework.DependencyInjection.DataProtectionServiceCollectionExtensions.AddDataProtection (Microsoft.Framework.DependencyInjection.IServiceCollection) <0x0002b>
at Microsoft.Framework.DependencyInjection.MvcServiceCollectionExtensions.ConfigureDefaultServices (Microsoft.Framework.DependencyInjection.IServiceCollection) <0x0001b>
at Microsoft.Framework.DependencyInjection.MvcServiceCollectionExtensions.AddMvc (Microsoft.Framework.DependencyInjection.IServiceCollection) <0x00013>
at OmniSharp.Startup.ConfigureServices (Microsoft.Framework.DependencyInjection.IServiceCollection) <0x0003f>
at (wrapper runtime-invoke) <Module>.runtime_invoke_void__this___object (object,intptr,intptr,intptr) <0xffffffff>
at <unknown> <0xffffffff>
at (wrapper managed-to-native) System.Reflection.MonoMethod.InternalInvoke (System.Reflection.MonoMethod,object,object[],System.Exception&) <0xffffffff>
* Assertion at class.c:5695, condition `!mono_loader_get_last_error ()' not met
```


---

<!-- source=github_issue; title=Failure of the main functions of the server after the last update.; url=https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/4760 -->

# Failure of the main functions of the server after the last update.

- Source: github_issue
- URL: https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/4760

Since the last update, the following errors keep showing up on my console when players leave my server. After a while, players get a failure to log in error. My console freezes and I can't shut down the server. At the same time, the Rocket.log file is almost 6GB of data. Not only the plugins are failing, but the game's own code is also failing and the following error is displayed on the console.
![1](https://github.com/user-attachments/assets/c4e90ac5-75cc-4ca4-afe2-95fd7560bbc1)
![2](https://github.com/user-attachments/assets/147fac15-610d-4fa0-bc3f-272769dd7fdc)


---

<!-- source=github_issue; title=(NO LONGER ACTIVE); url=https://github.com/SchuhBaum/SimplifiedMoveset/issues/12 -->

# (NO LONGER ACTIVE)

- Source: github_issue
- URL: https://github.com/SchuhBaum/SimplifiedMoveset/issues/12

Hi so i have a non steam version (That i cannot update) and this mod in particular breaks the game for me
my enabled mod list is usually this V (I prefer to copy paste due to list size)
warp
Fisobs
Swallow_Everything
Lineage_Visualizer
Faster_Gates
Giant_Coalescipedes
Guardian
Hud_Fix
InfiniteSpears
inventory
Load_Time_Fix
Bull_Squidcada
Custom_Regions_Support__CRS
Multiplayer_Menu_Label_Fix
Oops_My_Bad
OSHA_Compliant_Shelters_Fixed
Continue_After_Ascending
AntiRock
Carnivore_Reborn
Electric_Lizard
Chill_Reds
Clear_Water
Come_With_Me
Dress_My_Slugcat
DangleFruit_Fix
Dev_Console
Directionality_Fix
Dont_drag_me_into_this
Overseer_Ignorer_Scav_Edition
Metal_Pipe_On_Scav_Death
Stick_Together_CoOp
Yeek_Fix_Discontinued
Unlocked_Saint
Unshackled_Coop
Shiny_Shield_Mask
Pullup_Fix
Pebbles_Body_Disposal_Fix
Rain_World_SCDS
Tube_Worm_Fix
Spear_Snail
Pokéballs
Merge_Fix
Scroll_Wheel_Fix
Strong_Delivery
No_More_Tinnitus
Visible_ID
Testing_Arenas
Voidsea_Fix
Warm_Scugs
More_Stable_Remix_Menu
No_Crash_Karma_Loss
v121_OP_Artificer
v102_OP_Saint
ULTRAKILL_Style_Region_Titles
Today_We_Feast
The_M4rblelous_Entity_Pack
Improved_Input_Config
Bad_Pixel_Remover
Stronger_Slug
Sweet_Dreams
Placed_Objects_Manager_POM
Player_Friends
OSHA_Compliant_Gates
More_Grabs
More_Dlls
Lights_Out
Let_Me_Set_My_Needles_Down
ID_Finder
Five_Pebbles_Pong
Centipede_Shields
Firmly_Grasp_It
Explosion_Immunity
Audio_Fix
Craft_For_All
Community_Challenges
Controllable_Deer
More_Ammo
LEGACY_v1907b_Scissor_Vulture_Priority_Fix
Let_Them_Yap
Modlist_Hotload
Emeralds_Tweaks__Features
Rot_ApplyPalette_Fix
Rocketficer
Remove_Artificer_Stun
Reaper_Lizard
Remix_Auto_Restarter
PupBase
Push_To_Meow
Greyscreen
Omnithrow
No_Mod_Update_Confirm
No_Arena_Grab_Death
BeastMaster
Less_Deadly_Rain
Kill_Feed
Health_Bars
Killable_Garbage_Worms
No_Yeek_Friendly_Fire
Expedite
Flappy_Pebbles
Charged_Flare_Bombs
Mouse_Drag
Display_Arenas
Bubbleweed_Fix
Artificer_Scar_Fix
Artificer_Dont_Swallow
Ascended_Saint
Apex_Up_Your_Spawns
Rotund World usually too


---

<!-- source=github_issue; title=Error building package; url=https://github.com/hanseuljun/kinect-to-hololens/issues/1 -->

# Error building package

- Source: github_issue
- URL: https://github.com/hanseuljun/kinect-to-hololens/issues/1

Hi, I'm trying to setup this repo and am returned the following error at this step, .\vcpkg.exe install asio:x86-windows asio:x64-windows ffmpeg:x86-windows ffmpeg:x64-windows imgui:x86-windows imgui:x64-windows libvpx:x86-windows libvpx:x64-windows ms-gsl:x86-windows ms-gsl:x64-windows opencv:x86-windows opencv:x64-windows:
Error: Building package ffmpeg:x86-windows failed with: BUILD_FAILED
Please ensure you're using the latest portfiles with `.\vcpkg update`, then
submit an issue at https://github.com/Microsoft/vcpkg/issues including:
Package: ffmpeg:x86-windows
Vcpkg version: 2019.09.12-nohash
Additionally, attach any relevant sections from the log files above.
Any idea how to resolve this?


---

<!-- source=github_issue; title=OmniSharp stops working after Mono is installed.; url=https://github.com/dotnet/vscode-csharp/issues/1998 -->

# OmniSharp stops working after Mono is installed.

- Source: github_issue
- URL: https://github.com/dotnet/vscode-csharp/issues/1998

## Environment data
```
.NET Command Line Tools (2.1.3)
Product Information:
Version: 2.1.3
Commit SHA-1 hash: a0ca411ca5
Runtime Environment:
OS Name: gentoo
OS Version:
OS Platform: Linux
RID: linux-x64
Base Path: /opt/dotnet_core/sdk/2.1.3/
Microsoft .NET Core Shared Framework Host
Version : 2.0.4
Build : 7f262f453d8c8479b9af91d34c013b3aa05bc1ff
```
VS Code version: 1.20.0-1516947444
C# Extension version: 1.13.1
## Steps to reproduce
Install the .NET Core SDK without Mono and a fresh install of VSCode. Open up a C# project and verify that extension functionality works.
Install Mono alongside the dotnet tool. Try opening the same project in VSCode.
Install MSBuild for Mono since the OmniSharp warning suggests to do so. Try opening the same project in VSCode.
## Expected behavior
Intellisense, CodeLens, etc. works in all three scenarios. After installing MSBuild, the warning that it is not installed goes away.
## Actual behavior
Intellisense, CodeLens, etc. only work in the case where .NET Core is installed without Mono or Mono MSBuild. The warning that MSBuild is not installed remains after it is installed alongside Mono.
```
Starting OmniSharp server at 2/2/2018, 12:25:16 AM
Target: /home/jaccarmac/src/src/jaccarmac.com/junkcode/free-monad-vs-typeclass
OmniSharp server started wth Mono
Path: /home/jaccarmac/.vscode-insiders/extensions/ms-vscode.csharp-1.13.1/.omnisharp/omnisharp/OmniSharp.exe
PID: 20413
﻿[info]: OmniSharp.Stdio.Host
Starting OmniSharp on gentoo 0.0 (x64)
[warn]: OmniSharp.MSBuild.Discovery.Providers.MonoInstanceProvider
It looks like you have Mono 5.2.0 or greater installed but MSBuild could not be found.
Try installing MSBuild into Mono (e.g. 'sudo apt-get install msbuild') to enable better MSBuild support.
[info]: OmniSharp.MSBuild.Discovery.MSBuildLocator
Located 1 MSBuild instance(s)
1: StandAlone 15.0 - "/home/jaccarmac/.vscode-insiders/extensions/ms-vscode.csharp-1.13.1/.omnisharp/omnisharp/msbuild/15.0/Bin"
[info]: OmniSharp.MSBuild.Discovery.MSBuildLocator
MSBUILD_EXE_PATH environment variable set to '/home/jaccarmac/.vscode-insiders/extensions/ms-vscode.csharp-1.13.1/.omnisharp/omnisharp/msbuild/15.0/Bin/MSBuild.dll'
[info]: OmniSharp.MSBuild.Discovery.MSBuildLocator
Registered MSBuild instance: StandAlone 15.0 - "/home/jaccarmac/.vscode-insiders/extensions/ms-vscode.csharp-1.13.1/.omnisharp/omnisharp/msbuild/15.0/Bin"
MSBuildExtensionsPath = /usr/lib/mono/xbuild
CscToolPath = /home/jaccarmac/.vscode-insiders/extensions/ms-vscode.csharp-1.13.1/.omnisharp/omnisharp/msbuild/15.0/Bin/Roslyn
CscToolExe = csc.exe
MSBuildToolsPath = /home/jaccarmac/.vscode-insiders/extensions/ms-vscode.csharp-1.13.1/.omnisharp/omnisharp/msbuild/15.0/Bin
TargetFrameworkRootPath = /usr/lib/mono/xbuild-frameworks
[info]: OmniSharp.Cake.CakeProjectSystem
Detecting Cake files in '/home/jaccarmac/src/src/jaccarmac.com/junkcode/free-monad-vs-typeclass'.
[info]: OmniSharp.Cake.CakeProjectSystem
Could not find any Cake files
[info]: OmniSharp.DotNet.DotNetProjectSystem
Initializing in /home/jaccarmac/src/src/jaccarmac.com/junkcode/free-monad-vs-typeclass
[info]: OmniSharp.DotNet.DotNetProjectSystem
Auto package restore: False
[info]: OmniSharp.DotNet.DotNetProjectSystem
Update workspace context
[info]: OmniSharp.DotNet.DotNetProjectSystem
Resolving projects references
[info]: OmniSharp.MSBuild.MSBuildProjectSystem
No solution files found in '/home/jaccarmac/src/src/jaccarmac.com/junkcode/free-monad-vs-typeclass'
[info]: OmniSharp.MSBuild.MSBuildProjectSystem
Loading project: /home/jaccarmac/src/src/jaccarmac.com/junkcode/free-monad-vs-typeclass/free-monad-vs-typeclass.csproj
[warn]: OmniSharp.MSBuild.MSBuildProjectSystem
Failed to load project file '/home/jaccarmac/src/src/jaccarmac.com/junkcode/free-monad-vs-typeclass/free-monad-vs-typeclass.csproj'.
/home/jaccarmac/src/src/jaccarmac.com/junkcode/free-monad-vs-typeclass/free-monad-vs-typeclass.csproj(1,1)
Microsoft.Build.Exceptions.InvalidProjectFileException: The imported project "/usr/lib/mono/xbuild/15.0/Microsoft.Common.props" was not found. Confirm that the path in the <Import> declaration is correct, and that the file exists on disk. /opt/dotnet_core/sdk/2.1.3/Sdks/Microsoft.NET.Sdk/Sdk/Sdk.props
at Microsoft.Build.Shared.ProjectErrorUtilities.ThrowInvalidProject (System.String errorSubCategoryResourceName, Microsoft.Build.Shared.IElementLocation elementLocation, System.String resourceName, System.Object[] args) [0x00042] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Shared.ProjectErrorUtilities.VerifyThrowInvalidProject[T1] (System.Boolean condition, System.String errorSubCategoryResourceName, Microsoft.Build.Shared.IElementLocation elementLocation, System.String resourceName, T1 arg0) [0x00003] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Shared.ProjectErrorUtilities.ThrowInvalidProject[T1] (Microsoft.Build.Shared.IElementLocation elementLocation, System.String resourceName, T1 arg0) [0x00000] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Evaluator`4[P,I,M,D].ExpandAndLoadImportsFromUnescapedImportExpression (System.String directoryOfImportingFile, Microsoft.Build.Construction.ProjectImportElement importElement, System.String unescapedExpression, System.Boolean throwOnFileNotExistsError, System.Collections.Generic.List`1[Microsoft.Build.Construction.ProjectRootElement]& imports) [0x00517] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Evaluator`4[P,I,M,D].ExpandAndLoadImportsFromUnescapedImportExpressionConditioned (System.String directoryOfImportingFile, Microsoft.Build.Construction.ProjectImportElement importElement, System.Collections.Generic.List`1[Microsoft.Build.Construction.ProjectRootElement]& projects, System.Boolean throwOnFileNotExistsError) [0x001a6] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Evaluator`4[P,I,M,D].ExpandAndLoadImports (System.String directoryOfImportingFile, Microsoft.Build.Construction.ProjectImportElement importElement) [0x00024] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Evaluator`4[P,I,M,D].EvaluateImportElement (System.String directoryOfImportingFile, Microsoft.Build.Construction.ProjectImportElement importElement) [0x00000] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Evaluator`4[P,I,M,D].PerformDepthFirstPass (Microsoft.Build.Construction.ProjectRootElement currentProjectOrImport) [0x001dd] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Evaluator`4[P,I,M,D].EvaluateImportElement (System.String directoryOfImportingFile, Microsoft.Build.Construction.ProjectImportElement importElement) [0x0002d] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Evaluator`4[P,I,M,D].PerformDepthFirstPass (Microsoft.Build.Construction.ProjectRootElement currentProjectOrImport) [0x000c8] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Evaluator`4[P,I,M,D].Evaluate (Microsoft.Build.BackEnd.Logging.ILoggingService loggingService, Microsoft.Build.Framework.BuildEventContext buildEventContext) [0x000df] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Evaluator`4[P,I,M,D].Evaluate (Microsoft.Build.Evaluation.IEvaluatorData`4[P,I,M,D] data, Microsoft.Build.Construction.ProjectRootElement root, Microsoft.Build.Evaluation.ProjectLoadSettings loadSettings, System.Int32 maxNodeCount, Microsoft.Build.Collections.PropertyDictionary`1[T] environmentProperties, Microsoft.Build.BackEnd.Logging.ILoggingService loggingService, Microsoft.Build.Evaluation.IItemFactory`2[S,T] itemFactory, Microsoft.Build.Evaluation.IToolsetProvider toolsetProvider, Microsoft.Build.Evaluation.ProjectRootElementCache projectRootElementCache, Microsoft.Build.Framework.BuildEventContext buildEventContext, Microsoft.Build.Execution.ProjectInstance projectInstanceIfAnyForDebuggerOnly, Microsoft.Build.BackEnd.SdkResolution sdkResolution) [0x00016] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Project.Reevaluate (Microsoft.Build.BackEnd.Logging.ILoggingService loggingServiceForEvaluation, Microsoft.Build.Evaluation.ProjectLoadSettings loadSettings) [0x0004c] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Project.ReevaluateIfNecessary (Microsoft.Build.BackEnd.Logging.ILoggingService loggingServiceForEvaluation, Microsoft.Build.Evaluation.ProjectLoadSettings loadSettings) [0x00034] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Project.ReevaluateIfNecessary (Microsoft.Build.BackEnd.Logging.ILoggingService loggingServiceForEvaluation) [0x00000] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Project.ReevaluateIfNecessary () [0x00007] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Project.Initialize (System.Collections.Generic.IDictionary`2[TKey,TValue] globalProperties, System.String toolsVersion, System.String subToolsetVersion, Microsoft.Build.Evaluation.ProjectLoadSettings loadSettings) [0x000e9] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Project..ctor (System.String projectFile, System.Collections.Generic.IDictionary`2[TKey,TValue] globalProperties, System.String toolsVersion, System.String subToolsetVersion, Microsoft.Build.Evaluation.ProjectCollection projectCollection, Microsoft.Build.Evaluation.ProjectLoadSettings loadSettings) [0x0009c] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Project..ctor (System.String projectFile, System.Collections.Generic.IDictionary`2[TKey,TValue] globalProperties, System.String toolsVersion, Microsoft.Build.Evaluation.ProjectCollection projectCollection, Microsoft.Build.Evaluation.ProjectLoadSettings loadSettings) [0x00000] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.Project..ctor (System.String projectFile, System.Collections.Generic.IDictionary`2[TKey,TValue] globalProperties, System.String toolsVersion, Microsoft.Build.Evaluation.ProjectCollection projectCollection) [0x00000] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.ProjectCollection.LoadProject (System.String fileName, System.Collections.Generic.IDictionary`2[TKey,TValue] globalProperties, System.String toolsVersion) [0x000f5] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at Microsoft.Build.Evaluation.ProjectCollection.LoadProject (System.String fileName, System.String toolsVersion) [0x00000] in <9ba305957e954df9b0ed46d97ba8f5be>:0
at OmniSharp.MSBuild.ProjectFile.ProjectFileInfo.LoadProject (System.String filePath, System.String solutionDirectory, Microsoft.Extensions.Logging.ILogger logger, OmniSharp.MSBuild.Discovery.MSBuildInstance msbuildInstance, OmniSharp.MSBuild.SdksPathResolver sdksPathResolver, OmniSharp.Options.MSBuildOptions options, System.Collections.Generic.ICollection`1[T] diagnostics, System.Collections.Immutable.ImmutableArray`1[System.String]& targetFrameworks) [0x00054] in <e904597b17e840d49e5c532b51773be0>:0
at OmniSharp.MSBuild.ProjectFile.ProjectFileInfo.Create (System.String filePath, System.String solutionDirectory, Microsoft.Extensions.Logging.ILogger logger, OmniSharp.MSBuild.Discovery.MSBuildInstance msbuildInstance, OmniSharp.MSBuild.SdksPathResolver sdksPathResolver, OmniSharp.Options.MSBuildOptions options, System.Collections.Generic.ICollection`1[T] diagnostics) [0x0000a] in <e904597b17e840d49e5c532b51773be0>:0
at OmniSharp.MSBuild.MSBuildProjectSystem.LoadProject (System.String projectFilePath) [0x00038] in <e904597b17e840d49e5c532b51773be0>:0
[info]: OmniSharp.Script.ScriptProjectSystem
Detecting CSX files in '/home/jaccarmac/src/src/jaccarmac.com/junkcode/free-monad-vs-typeclass'.
[info]: OmniSharp.Script.ScriptProjectSystem
Could not find any CSX files
[info]: OmniSharp.Stdio.Host
Invoking Workspace Options Provider: OmniSharp.Roslyn.CSharp.Services.CSharpWorkspaceOptionsProvider
[info]: OmniSharp.Stdio.Host
Configuration finished.
[info]: OmniSharp.Stdio.Host
Omnisharp server running using Stdio at location '/home/jaccarmac/src/src/jaccarmac.com/junkcode/free-monad-vs-typeclass' on host 18205.
```


---

<!-- source=github_issue; title=Request to add property to MoM Door Token that prevents it from coming back; url=https://github.com/NPBruce/valkyrie/issues/482 -->

# Request to add property to MoM Door Token that prevents it from coming back

- Source: github_issue
- URL: https://github.com/NPBruce/valkyrie/issues/482

Firstly, I want to make clear Valkyrie is an excellent well built application and (except for one issue) does everything I could wish for and I am very impressed with it.
I do have one issue. I am working on a MoM scenario where there are multiple alternative pathways to the same room. This means that the investigators can enter the same room through more than one possible doorway.
The issue is when the door tokens are made visible for the room it is possible that the door has already been entered (and so has already been removed). To avoid putting back a door that has already been removed, I've added a flag to the door which is raised when the door is removed. Then I check if the flag has been raised before placing the door.
What would be cleaner would be to do this in the code. It would, also, be generally useful.
Alternatively, please can someone suggest an easy way of preventing a door from coming back for rooms that can be entered through multiple doorways.


---

<!-- source=github_issue; title=PSA: NetTransport Rewrite; url=https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/1971 -->

# PSA: NetTransport Rewrite

- Source: github_issue
- URL: https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/1971

If you develop server plugins and watch this repository, then this will almost definitely impact your plugins.
In general, the update should be backwards compatible. Nothing should have been removed, however several properties and methods have been marked obsolete.
You can opt-in to the NetTransport beta on Steam to try it out. There are several verbose logging options enabled to help you debug.
The dependency on `SteamNetworking` has been abstracted into "Net Transport Layers". The current default implementation uses `SteamNetworking`, but there is also an experimental Berkeley sockets TCP implementation that can be activated with the `-NetTransport=SystemSockets` command-line option. In the future the system sockets will be used for LAN servers, and when reliability is moved into a separate layer a UDP sockets implementation will be added.
You can also try out an implementation of the new Steam networking with the `-NetTransport=SteamNetworkingSockets` command-line option.
Key changes and their impact:
- Connections are identified by an opaque `ITransportConnection` type. Players in the queue or online are still identified by SteamID however. Methods for sending to SteamIDs have been kept for backwards compatibility, but depend on the SteamID having an active connection.
- RPC channel is now a byte in the RPC header rather than per-message. This will impact anyone manually parsing send/receive RPC messages. If you are doing this then please comment and we will find a better workaround.
- Prior to the Connect message the connection SteamID is unknown. This will only impact plugins messing with the initial Workshop query message or initial Connect message.
- Channels are still of int type (32 bits), but are replicated as bytes (8 bits). They were only ever used to associate RPCs with a per-player component, and there are always less than 255 players on the server, so channel numbers are now recycled. In a future rewrite the channel numbers will be entirely replaced by a net addressable component id.
- Anyone using `SteamGameServerNetworking` to get the connection details should instead use `ITransportConnection.TryGetIPv4Address` and `ITransportConnection.TryGetPort`. Make sure to handle the false case because a future implementation of the "Steam Datagram Relay" will hide the remote address.
Please comment if you have any questions or concerns.


---

<!-- source=github_issue; title=Nullable Reference Types annotations. Fixed by team through multiple PRs.; url=https://github.com/nunit/nunit/issues/3376 -->

# Nullable Reference Types annotations. Fixed by team through multiple PRs.

- Source: github_issue
- URL: https://github.com/nunit/nunit/issues/3376

tl;dr Now that C# 8 is out, people will be using the Nullable Reference Types language feature. We should consider putting the compiler annotations on our library. That would require moving the codebase to C# 8. To reap the benefits in our own codebase, we could also use https://github.com/tunnelvisionlabs/ReferenceAssemblyAnnotator.
### What it is
People who put `<Nullable>enable</Nullable>` in their projects or `#nullable enable` in their source files are then allowed to use the syntax `ReferenceType?` where nulls are permitted. In typical software, nulls end up being actually intended in only a small percentage of the usages of reference types.
The compiler then produces warnings (we have /warnaserror) when a thing that might be null is treated as though it can't be null, like when dotting off which could cause an NRE or when passing to a method which could cause an ArgumentNullException, or when setting a field or property which only causes a problem at a later point in time.
This goes a long way toward solving the billion-dollar problem of nullability blindness in the type system.
https://docs.microsoft.com/en-us/dotnet/csharp/nullable-references
https://devblogs.microsoft.com/dotnet/nullable-reference-types-in-csharp/
https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/nullable-reference-types
Things like `string.IsNullOrEmpty` are annotated with new compiler attributes such as `[NotNullWhen(false)]` on its parameter so that the compiler can recognize that it's a null check. These attributes can be defined by anyone as internal so that they don't conflict with other assemblies. .NET Core 3.0 is the first version of the BCL that adds these attributes as public classes. Referencing https://github.com/tunnelvisionlabs/ReferenceAssemblyAnnotator would define these internally for us without having to maintain the internal attribute definitions ourselves.
### Reasons to do it
- It would be nice to annotate our library so that people who use NUnit are warned if they forget to check things like `TestContext.CurrentContext` for null or if they pass things that could be null to our APIs. It's being up-front about the types that each API accepts in the same way that declaring a parameter `IFoo foo` instead of `object foo` is being more up-front and helpful.
- This would aid the mission of maintaining high-quality internal code written by many different people. We've had our share of null reference exceptions that nothing had forced us to notice at compile time.
- It's not a breaking change.
### Reasons not to do it
- It requires `<LangVersion>8<LangVersion>`. While Visual Studio wouldn't be required in order to compile the codebase, 2019 Update 3 would become the minimum version if you *were* using Visual Studio. You could also compile using the .NET Core 3.0 SDK using the command line or using VS Code and other IDEs.
- It's likely to require us to think about things we never had to reconcile before. Once we start shining around this black light, so to speak, we might not like some of the things we see. (Or is this good, as NUnit 4 begins to take shape?)
- It would touch a decent percentage of our files.
### Proposal
I think we should do it in v3 (because this is my function in life, apparently?) and it's work I enjoy and would prioritize. However, I see these downsides and I'm not going to be overly disappointed if we don't want to do it in v3.
I feel more strongly that we should do this by v4. Otherwise, as one of the most-frequently used libraries, I think we'll end up standing out in an unappealing way as time goes on. I could easily be wrong. But if we do this by v4, the easiest way might be to start now in v3 since it can all be done incrementally.


---

<!-- source=github_issue; title=iOS authentication is failing in latest version; url=https://github.com/elringus/unity-google-drive/issues/18 -->

# iOS authentication is failing in latest version

- Source: github_issue
- URL: https://github.com/elringus/unity-google-drive/issues/18

This was working fine, but coming back to retest now (after all the new features), the iOS authentication is failing now.
Failed to execute authorization procedure. Check application settings and credentials.
We tried changing to 4.6 scripting - but that breaks the entire app on iOS and downloads stop working on Android :(
Please advise how best to debug and fix this?
Joe


---

<!-- source=github_issue; title=Mono.Debugger hangs Visual Studio 2017 for ~3min on the "Starting Android application" step; url=https://github.com/dotnet/android/issues/1664 -->

# Mono.Debugger hangs Visual Studio 2017 for ~3min on the "Starting Android application" step

- Source: github_issue
- URL: https://github.com/dotnet/android/issues/1664

### Steps to Reproduce
1. Build a Xamarin.Android project
2. Run a Xamarin.Android project
<!--
If you have a repro project, you may drag & drop the .zip/etc. onto the issue editor to attach it.
-->
### Expected Behavior
The app should be deployed to the device and run.
### Actual Behavior
VS hangs for ~3 min, the a message pops up, saying _Mono Debugging for Visual Studio 4.10.5 likely caused 194 seconds of unresponsiveness. _ Only after, does the app get deployed.
### Version Information
Microsoft Visual Studio Professional 2017
Version 15.7.1
VisualStudio.15.Release/15.7.1+27703.2000
Microsoft .NET Framework
Version 4.7.02556
<details>
Installed Version: Professional
Application Insights Tools for Visual Studio Package 8.12.10405.1
Application Insights Tools for Visual Studio
ASP.NET and Web Tools 2017 15.0.40501.0
ASP.NET and Web Tools 2017
ASP.NET Core Razor Language Services 15.7.31476
Provides languages services for ASP.NET Core Razor.
Azure App Service Tools v3.0.0 15.0.40424.0
Azure App Service Tools v3.0.0
C# Tools 2.8.0-beta6-62830-08. Commit Hash: e595ee276d14e14bfb3eb323fb57f2aa668bddea
C# components used in the IDE. Depending on your project type and settings, a different version of the compiler may be used.
Common Azure Tools 1.10
Provides common services for use by Azure Mobile Services and Microsoft Azure Tools.
JavaScript Language Service 2.0
JavaScript Language Service
Merq 1.1.17-rc (cba4571)
Command Bus, Event Stream and Async Manager for Visual Studio extensions.
Microsoft Continuous Delivery Tools for Visual Studio 0.3
Simplifying the configuration of continuous build integration and continuous build delivery from within the Visual Studio IDE.
Microsoft JVM Debugger 1.0
Provides support for connecting the Visual Studio debugger to JDWP compatible Java Virtual Machines
Microsoft MI-Based Debugger 1.0
Provides support for connecting Visual Studio to MI compatible debuggers
Microsoft Visual Studio Tools for Containers 1.1
Develop, run, validate your ASP.NET Core applications in the target environment. F5 your application directly into a container with debugging, or CTRL + F5 to edit & refresh your app without having to rebuild the container.
Mono Debugging for Visual Studio 4.10.5-pre (ab58725)
Support for debugging Mono processes with Visual Studio.
Multilingual App Toolkit 4.0
Multilingual App Toolkit helps you localize your Windows Store app by providing file management, pseudo and machine translation, translation editor, and build integration. http://aka.ms/matinstall
NuGet Package Manager 4.6.0
NuGet Package Manager in Visual Studio. For more information about NuGet, visit http://docs.nuget.org/.
ProjectServicesPackage Extension 1.0
ProjectServicesPackage Visual Studio Extension Detailed Info
ResourcePackage Extension 1.0
ResourcePackage Visual Studio Extension Detailed Info
SQL Server Data Tools 15.1.61804.210
Microsoft SQL Server Data Tools
TypeScript Tools 15.7.20419.2003
TypeScript Tools for Microsoft Visual Studio
Visual Basic Tools 2.8.0-beta6-62830-08. Commit Hash: e595ee276d14e14bfb3eb323fb57f2aa668bddea
Visual Basic components used in the IDE. Depending on your project type and settings, a different version of the compiler may be used.
Visual F# Tools 10.1 for F# 4.1 15.7.0.0. Commit Hash: 16ecf5a30ad868d183c58e4a71a71c23d4ed3ba9.
Microsoft Visual F# Tools 10.1 for F# 4.1
Visual Studio Code Debug Adapter Host Package 1.0
Interop layer for hosting Visual Studio Code debug adapters in Visual Studio
Visual Studio Tools for Unity 3.7.0.1
Visual Studio Tools for Unity
VisualStudio.Mac 1.0
Mac Extension for Visual Studio
VSColorOutput 2.5.1
Color output for build and debug windows - http://mike-ward.net/vscoloroutput
WiX Toolset Visual Studio Extension 0.9.21.62588
WiX Toolset Visual Studio Extension version 0.9.21.62588
Copyright (c) .NET Foundation and contributors. All rights reserved.
Xamaridea.VisualStudioPlugin 1.0
VS + Xamarin + IDEA = Love
Xamarin 4.10.0.442 (396b18cef)
Visual Studio extension to enable development for Xamarin.iOS and Xamarin.Android.
Xamarin Designer 4.12.264 (fc37cd02e)
Visual Studio extension to enable Xamarin Designer tools in Visual Studio.
Xamarin.Android SDK 8.3.0.19 (HEAD/342b2ce96)
Xamarin.Android Reference Assemblies and MSBuild support.
Xamarin.iOS and Xamarin.Mac SDK 11.10.1.177 (7e782c1)
Xamarin.iOS and Xamarin.Mac Reference Assemblies and MSBuild support.
</details>
### Log File
<details>
```
Xamarin.VisualStudio.TastyPackage|Information|0|Hooked up SDB tracing adapter
Xamarin.VisualStudio.TastyPackage|Information|0|Initialization finished
Xamarin|Information|0|Xamarin - 4.10.0.442-d15-7+396b18cef
Xamarin.VisualStudio.TastyPackage|Information|0|Hooked up SDB tracing adapter
Xamarin.VisualStudio.TastyPackage|Information|0|Initialization finished
Xamarin.VisualStudio.Android.XamarinAndroidPackage|Warning|0|Initializing Xamarin.VisualStudio.Android.XamarinAndroidPackage
Xamarin.Inspector|Information|0|Inspector extension loaded
Xamarin.Inspector|Error|0|[Inspector] Error preparing project for inspection
System.NullReferenceException: Object reference not set to an instance of an object.
at Xamarin.VisualStudio.Inspector.VSInspectorSession.Create(Project proj, IServiceProvider serviceProvider) in E:\A\_work\6\s\src\Features\VisualStudio.Inspector\Vsix\VSInspectorSession.cs:line 54
at Xamarin.VisualStudio.Inspector.XamarinInspectorPackage.RefreshInspectorSession() in E:\A\_work\6\s\src\Features\VisualStudio.Inspector\Vsix\XamarinInspectorPackage.cs:line 166
Xamarin.Inspector|Error|0|[Inspector] Error preparing project for inspection
System.NullReferenceException: Object reference not set to an instance of an object.
at Xamarin.VisualStudio.Inspector.VSInspectorSession.Create(Project proj, IServiceProvider serviceProvider) in E:\A\_work\6\s\src\Features\VisualStudio.Inspector\Vsix\VSInspectorSession.cs:line 54
at Xamarin.VisualStudio.Inspector.XamarinInspectorPackage.RefreshInspectorSession() in E:\A\_work\6\s\src\Features\VisualStudio.Inspector\Vsix\XamarinInspectorPackage.cs:line 166
Xamarin.VisualStudio.Android.ContinuousPlayerDeviceProvider|Information|0|Live player started
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android SDK Platform-Tools r27.0.1 in directory 'C:\Program Files (x86)\Android\android-sdk\platform-tools'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 27.0.1 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android SDK Tools 25.2.5 r25.2.5 in directory 'C:\Program Files (x86)\Android\android-sdk\tools'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 26.1.1 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android SDK Tools r26.1.1 in directory 'C:\Program Files (x86)\Android\android-sdk\tools'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 26.1.1 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android SDK Build-Tools 27.0.3 r27.0.3 in directory 'C:\Program Files (x86)\Android\android-sdk\build-tools/27.0.3'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 27.0.3 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27.0.2 r27.0.2 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27.0.1 r27.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27 r27.0.0 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26.0.3 r26.0.3 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26.0.2 r26.0.2 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26.0.1 r26.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android SDK Build-Tools 26 r26.0.0 in directory 'C:\Program Files (x86)\Android\android-sdk\build-tools/26.0.0'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 26.0.0 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25.0.3 r25.0.3 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25.0.2 r25.0.2 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25.0.1 r25.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25 r25.0.0 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android Emulator r27.1.10 in directory 'C:\Program Files (x86)\Android\android-sdk\emulator'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 27.1.12 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component NDK r16.1.4479499 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component NDK r14.1.3816874 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 3.0 r3.0.4213617 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.3 r2.3.3614996 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.2 r2.2.3271982 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.1 r2.1.2852477 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.0 r2.0.2558144 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component SDK Patch Applier v4 r1 in directory 'C:\Program Files (x86)\Android\android-sdk\patcher/v4'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 1 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android SDK Platform 27 r1 [Platform: API 27] in directory 'C:\Program Files (x86)\Android\android-sdk\platforms/android-27'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 1 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android SDK Platform 26 r2 [Platform: API 26] in directory 'C:\Program Files (x86)\Android\android-sdk\platforms/android-26'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 2 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android SDK Platform 25 r3 [Platform: API 25] in directory 'C:\Program Files (x86)\Android\android-sdk\platforms/android-25'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 3 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android SDK Platform 24 r2 [Platform: API 24] in directory 'C:\Program Files (x86)\Android\android-sdk\platforms/android-24'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 2 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android SDK Platform 23 r3 [Platform: API 23] in directory 'C:\Program Files (x86)\Android\android-sdk\platforms/android-23'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 3 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 22 r2 [Platform: API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 21 r2 [Platform: API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 20 r2 [Platform: API 20] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 19 r4 [Platform: API 19] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 18 r3 [Platform: API 18] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 17 r3 [Platform: API 17] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 16 r5 [Platform: API 16] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 15 r5 [Platform: API 15] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 14 r4 [Platform: API 14] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 13 r1 [Platform: API 13] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 12 r3 [Platform: API 12] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 11 r2 [Platform: API 11] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 10 r2 [Platform: API 10] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 9 r2 [Platform: API 9] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 8 r3 [Platform: API 8] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 7 r3 [Platform: API 7] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 6 r1 [Platform: API 6] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 5 r1 [Platform: API 5] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 4 r3 [Platform: API 4] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 10] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r2 [System Image: ARMV7a API 14] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 15] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 16] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r5 [System Image: ARMV7a API 17] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 18] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r5 [System Image: ARMV7a API 19] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r2 [System Image: ARMV7a API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r6 [System Image: ARMV7a API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r7 [System Image: ARMV7a API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM 64 v8a System Image r7 [System Image: ARM64V8a API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r4 [System Image: X86 API 10] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r4 [System Image: X86 API 15] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r5 [System Image: X86 API 16] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r3 [System Image: X86 API 17] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r3 [System Image: X86 API 18] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r6 [System Image: X86 API 19] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r5 [System Image: X86 API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r6 [System Image: X86 API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r10 [System Image: X86 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r8 [System Image: X86 API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r5 [System Image: X86_64 API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r6 [System Image: X86_64 API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Intel x86 Atom_64 System Image r10 [System Image: X86_64 API 23] in directory 'C:\Program Files (x86)\Android\android-sdk\system-images/android-23/default/x86_64'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 10 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r8 [System Image: X86_64 API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear ARM EABI v7a System Image r6 [System Image: ARMV7a API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear Intel x86 Atom System Image r6 [System Image: X86 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear ARM EABI v7a System Image r3 [System Image: ARMV7a API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear Intel x86 Atom System Image r3 [System Image: X86 API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear Intel x86 Atom System Image r4 [System Image: X86 API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component China version of Android Wear ARM EABI v7a System Image r4 [System Image: ARMV7a API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component China version of Android Wear Intel x86 Atom System Image r4 [System Image: X86 API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component China version of Android Wear Intel x86 Atom System Image r4 [System Image: X86 API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r3 [System Image: X86 API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV ARM EABI v7a System Image r3 [System Image: ARMV7a API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r3 [System Image: X86 API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV ARM EABI v7a System Image r1 [System Image: ARMV7a API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r14 [System Image: X86 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV ARM EABI v7a System Image r12 [System Image: ARMV7a API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r15 [System Image: X86 API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r9 [System Image: X86 API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r7 [System Image: X86 API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r2 [System Image: X86 API 27] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 10 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 10 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 15 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 15 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 16 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 17 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 17 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 18 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 18 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r33 [System Image: X86 API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r33 [System Image: ARMV7a API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r25 [System Image: X86 API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r25 [System Image: X86_64 API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r25 [System Image: ARMV7a API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r19 [System Image: X86 API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r19 [System Image: ARMV7a API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r19 [System Image: X86_64 API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Google APIs Intel x86 Atom System Image r26 [System Image: X86 API 23 (Google Inc.)] in directory 'C:\Program Files (x86)\Android\android-sdk\system-images/android-23/google_apis/x86'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 26 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r26 [System Image: X86_64 API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r26 [System Image: ARMV7a API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r20 [System Image: X86 API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r20 [System Image: X86_64 API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r20 [System Image: ARMV7a API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM 64 v8a System Image r20 [System Image: ARM64V8a API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Google APIs Intel x86 Atom System Image r11 [System Image: X86 API 25 (Google Inc.)] in directory 'C:\Program Files (x86)\Android\android-sdk\system-images/android-25/google_apis/x86'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 11 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r11 [System Image: X86_64 API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r11 [System Image: ARMV7a API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM 64 v8a System Image r11 [System Image: ARM64V8a API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Google APIs Intel x86 Atom System Image r8 [System Image: X86 API 26 (Google Inc.)] in directory 'C:\Program Files (x86)\Android\android-sdk\system-images/android-26/google_apis/x86'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 8 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r8 [System Image: X86_64 API 26 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r4 [System Image: X86 API 27 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Intel x86 Atom System Image r19 [System Image: X86 API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Google Play Intel x86 Atom System Image r9 [System Image: X86 API 25 (Google Inc.)] in directory 'C:\Program Files (x86)\Android\android-sdk\system-images/android-25/google_apis_playstore/x86'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 9 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Google Play Intel x86 Atom System Image r7 [System Image: X86 API 26 (Google Inc.)] in directory 'C:\Program Files (x86)\Android\android-sdk\system-images/android-26/google_apis_playstore/x86'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 7 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Google Play Intel x86 Atom System Image r3 [System Image: X86 API 27 (Google Inc.)] in directory 'C:\Program Files (x86)\Android\android-sdk\system-images/android-27/google_apis_playstore/x86'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 3 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r3 [Addon: API 3 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 4 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 5 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 6 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 7 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 8 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 9 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 10 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 11 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 12 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 13 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 14 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r3 [Addon: API 15 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r4 [Addon: API 16 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r4 [Addon: API 17 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r4 [Addon: API 18 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r20 [Addon: API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google TV Addon r2 [Addon: API 12 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google TV Addon r1 [Addon: API 13 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Glass Development Kit Preview r11 [Addon: API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Android Support Repository r47.0.0 [Extra: (Android)] in directory 'C:\Program Files (x86)\Android\android-sdk\extras/android/m2repository'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 47.0.0 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Repository r58 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Licensing Library r1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play APK Expansion library r1 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play services for Froyo r12 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Google Play services r46 [Extra: (Google Inc.)] in directory 'C:\Program Files (x86)\Android\android-sdk\extras/google/google_play_services'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 48 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Google USB Driver r11 [Extra: (Google Inc.)] in directory 'C:\Program Files (x86)\Android\android-sdk\extras/google/usb_driver'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 11 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google AdMob Ads SDK r11 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Analytics App Tracking SDK r3 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Web Driver r2 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Cloud Messaging for Android Library r3 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Auto API Simulators r1 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Auto Desktop Head Unit emulator r1.1 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Instant Apps Development SDK r1.1.0 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component GPU Debugging tools r1.0.3 [Extra: (Android)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component GPU Debugging tools r3.1.0 [Extra: (Android)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Detecting component Intel x86 Emulator Accelerator (HAXM installer) r6.2.1 [Extra: (Intel Corporation)] in directory 'C:\Program Files (x86)\Android\android-sdk\extras/intel/Hardware_Accelerated_Execution_Manager'
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0| Found revision 6.2.1 on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform-Tools r27.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Tools 25.2.5 r25.2.5 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Tools r26.1.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27.0.3 r27.0.3 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27.0.2 r27.0.2 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27.0.1 r27.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27 r27.0.0 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26.0.3 r26.0.3 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26.0.2 r26.0.2 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26.0.1 r26.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26 r26.0.0 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25.0.3 r25.0.3 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25.0.2 r25.0.2 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25.0.1 r25.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25 r25.0.0 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Emulator r27.1.10 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component NDK r16.1.4479499 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component NDK r14.1.3816874 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 3.0 r3.0.4213617 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.3 r2.3.3614996 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.2 r2.2.3271982 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.1 r2.1.2852477 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.0 r2.0.2558144 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component SDK Patch Applier v4 r1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 27 r1 [Platform: API 27] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 26 r2 [Platform: API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 25 r3 [Platform: API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 24 r2 [Platform: API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 23 r3 [Platform: API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 22 r2 [Platform: API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 21 r2 [Platform: API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 20 r2 [Platform: API 20] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 19 r4 [Platform: API 19] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 18 r3 [Platform: API 18] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 17 r3 [Platform: API 17] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 16 r5 [Platform: API 16] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 15 r5 [Platform: API 15] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 14 r4 [Platform: API 14] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 13 r1 [Platform: API 13] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 12 r3 [Platform: API 12] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 11 r2 [Platform: API 11] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 10 r2 [Platform: API 10] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 9 r2 [Platform: API 9] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 8 r3 [Platform: API 8] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 7 r3 [Platform: API 7] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 6 r1 [Platform: API 6] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 5 r1 [Platform: API 5] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 4 r3 [Platform: API 4] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 10] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r2 [System Image: ARMV7a API 14] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 15] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 16] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r5 [System Image: ARMV7a API 17] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 18] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r5 [System Image: ARMV7a API 19] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r2 [System Image: ARMV7a API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r6 [System Image: ARMV7a API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r7 [System Image: ARMV7a API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM 64 v8a System Image r7 [System Image: ARM64V8a API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r4 [System Image: X86 API 10] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r4 [System Image: X86 API 15] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r5 [System Image: X86 API 16] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r3 [System Image: X86 API 17] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r3 [System Image: X86 API 18] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r6 [System Image: X86 API 19] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r5 [System Image: X86 API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r6 [System Image: X86 API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r10 [System Image: X86 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r8 [System Image: X86 API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r5 [System Image: X86_64 API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r6 [System Image: X86_64 API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r10 [System Image: X86_64 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r8 [System Image: X86_64 API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear ARM EABI v7a System Image r6 [System Image: ARMV7a API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear Intel x86 Atom System Image r6 [System Image: X86 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear ARM EABI v7a System Image r3 [System Image: ARMV7a API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear Intel x86 Atom System Image r3 [System Image: X86 API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear Intel x86 Atom System Image r4 [System Image: X86 API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component China version of Android Wear ARM EABI v7a System Image r4 [System Image: ARMV7a API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component China version of Android Wear Intel x86 Atom System Image r4 [System Image: X86 API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component China version of Android Wear Intel x86 Atom System Image r4 [System Image: X86 API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r3 [System Image: X86 API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV ARM EABI v7a System Image r3 [System Image: ARMV7a API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r3 [System Image: X86 API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV ARM EABI v7a System Image r1 [System Image: ARMV7a API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r14 [System Image: X86 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV ARM EABI v7a System Image r12 [System Image: ARMV7a API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r15 [System Image: X86 API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r9 [System Image: X86 API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r7 [System Image: X86 API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r2 [System Image: X86 API 27] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 10 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 10 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 15 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 15 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 16 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 17 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 17 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 18 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 18 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r33 [System Image: X86 API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r33 [System Image: ARMV7a API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r25 [System Image: X86 API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r25 [System Image: X86_64 API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r25 [System Image: ARMV7a API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r19 [System Image: X86 API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r19 [System Image: ARMV7a API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r19 [System Image: X86_64 API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r26 [System Image: X86 API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r26 [System Image: X86_64 API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r26 [System Image: ARMV7a API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r20 [System Image: X86 API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r20 [System Image: X86_64 API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r20 [System Image: ARMV7a API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM 64 v8a System Image r20 [System Image: ARM64V8a API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r11 [System Image: X86 API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r11 [System Image: X86_64 API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r11 [System Image: ARMV7a API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM 64 v8a System Image r11 [System Image: ARM64V8a API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r8 [System Image: X86 API 26 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r8 [System Image: X86_64 API 26 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r4 [System Image: X86 API 27 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Intel x86 Atom System Image r19 [System Image: X86 API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Intel x86 Atom System Image r9 [System Image: X86 API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Intel x86 Atom System Image r7 [System Image: X86 API 26 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Intel x86 Atom System Image r3 [System Image: X86 API 27 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r3 [Addon: API 3 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 4 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 5 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 6 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 7 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 8 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 9 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 10 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 11 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 12 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 13 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 14 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r3 [Addon: API 15 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r4 [Addon: API 16 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r4 [Addon: API 17 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r4 [Addon: API 18 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r20 [Addon: API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google TV Addon r2 [Addon: API 12 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google TV Addon r1 [Addon: API 13 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Glass Development Kit Preview r11 [Addon: API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Support Repository r47.0.0 [Extra: (Android)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Repository r58 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Licensing Library r1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play APK Expansion library r1 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play services for Froyo r12 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play services r46 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google USB Driver r11 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google AdMob Ads SDK r11 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Analytics App Tracking SDK r3 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Web Driver r2 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Cloud Messaging for Android Library r3 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Auto API Simulators r1 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Auto Desktop Head Unit emulator r1.1 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Instant Apps Development SDK r1.1.0 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component GPU Debugging tools r1.0.3 [Extra: (Android)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component GPU Debugging tools r3.1.0 [Extra: (Android)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Emulator Accelerator (HAXM installer) r6.2.1 [Extra: (Intel Corporation)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform-Tools r27.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Tools 25.2.5 r25.2.5 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Tools r26.1.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27.0.3 r27.0.3 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27.0.2 r27.0.2 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27.0.1 r27.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 27 r27.0.0 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26.0.3 r26.0.3 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26.0.2 r26.0.2 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26.0.1 r26.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 26 r26.0.0 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25.0.3 r25.0.3 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25.0.2 r25.0.2 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25.0.1 r25.0.1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Build-Tools 25 r25.0.0 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Emulator r27.1.10 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component NDK r16.1.4479499 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component NDK r14.1.3816874 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 3.0 r3.0.4213617 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.3 r2.3.3614996 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.2 r2.2.3271982 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.1 r2.1.2852477 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component LLDB 2.0 r2.0.2558144 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component SDK Patch Applier v4 r1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 27 r1 [Platform: API 27] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 26 r2 [Platform: API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 25 r3 [Platform: API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 24 r2 [Platform: API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 23 r3 [Platform: API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 22 r2 [Platform: API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 21 r2 [Platform: API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 20 r2 [Platform: API 20] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 19 r4 [Platform: API 19] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 18 r3 [Platform: API 18] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 17 r3 [Platform: API 17] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 16 r5 [Platform: API 16] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 15 r5 [Platform: API 15] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 14 r4 [Platform: API 14] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 13 r1 [Platform: API 13] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 12 r3 [Platform: API 12] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 11 r2 [Platform: API 11] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 10 r2 [Platform: API 10] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 9 r2 [Platform: API 9] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 8 r3 [Platform: API 8] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 7 r3 [Platform: API 7] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 6 r1 [Platform: API 6] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 5 r1 [Platform: API 5] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android SDK Platform 4 r3 [Platform: API 4] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 10] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r2 [System Image: ARMV7a API 14] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 15] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 16] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r5 [System Image: ARMV7a API 17] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 18] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r5 [System Image: ARMV7a API 19] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r4 [System Image: ARMV7a API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r2 [System Image: ARMV7a API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r6 [System Image: ARMV7a API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM EABI v7a System Image r7 [System Image: ARMV7a API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component ARM 64 v8a System Image r7 [System Image: ARM64V8a API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r4 [System Image: X86 API 10] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r4 [System Image: X86 API 15] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r5 [System Image: X86 API 16] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r3 [System Image: X86 API 17] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r3 [System Image: X86 API 18] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r6 [System Image: X86 API 19] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r5 [System Image: X86 API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r6 [System Image: X86 API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r10 [System Image: X86 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom System Image r8 [System Image: X86 API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r5 [System Image: X86_64 API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r6 [System Image: X86_64 API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r10 [System Image: X86_64 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Atom_64 System Image r8 [System Image: X86_64 API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear ARM EABI v7a System Image r6 [System Image: ARMV7a API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear Intel x86 Atom System Image r6 [System Image: X86 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear ARM EABI v7a System Image r3 [System Image: ARMV7a API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear Intel x86 Atom System Image r3 [System Image: X86 API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Wear Intel x86 Atom System Image r4 [System Image: X86 API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component China version of Android Wear ARM EABI v7a System Image r4 [System Image: ARMV7a API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component China version of Android Wear Intel x86 Atom System Image r4 [System Image: X86 API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component China version of Android Wear Intel x86 Atom System Image r4 [System Image: X86 API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r3 [System Image: X86 API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV ARM EABI v7a System Image r3 [System Image: ARMV7a API 21] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r3 [System Image: X86 API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV ARM EABI v7a System Image r1 [System Image: ARMV7a API 22] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r14 [System Image: X86 API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV ARM EABI v7a System Image r12 [System Image: ARMV7a API 23] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r15 [System Image: X86 API 24] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r9 [System Image: X86 API 25] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r7 [System Image: X86 API 26] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android TV Intel x86 Atom System Image r2 [System Image: X86 API 27] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 10 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 10 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 15 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 15 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 16 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 17 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 17 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r5 [System Image: ARMV7a API 18 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r5 [System Image: X86 API 18 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r33 [System Image: X86 API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r33 [System Image: ARMV7a API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r25 [System Image: X86 API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r25 [System Image: X86_64 API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r25 [System Image: ARMV7a API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r19 [System Image: X86 API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r19 [System Image: ARMV7a API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r19 [System Image: X86_64 API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r26 [System Image: X86 API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r26 [System Image: X86_64 API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r26 [System Image: ARMV7a API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r20 [System Image: X86 API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r20 [System Image: X86_64 API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r20 [System Image: ARMV7a API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM 64 v8a System Image r20 [System Image: ARM64V8a API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r11 [System Image: X86 API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r11 [System Image: X86_64 API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM EABI v7a System Image r11 [System Image: ARMV7a API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs ARM 64 v8a System Image r11 [System Image: ARM64V8a API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r8 [System Image: X86 API 26 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom_64 System Image r8 [System Image: X86_64 API 26 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs Intel x86 Atom System Image r4 [System Image: X86 API 27 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Intel x86 Atom System Image r19 [System Image: X86 API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Intel x86 Atom System Image r9 [System Image: X86 API 25 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Intel x86 Atom System Image r7 [System Image: X86 API 26 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Intel x86 Atom System Image r3 [System Image: X86 API 27 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r3 [Addon: API 3 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 4 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 5 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 6 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 7 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 8 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 9 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 10 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 11 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 12 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 13 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r2 [Addon: API 14 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r3 [Addon: API 15 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r4 [Addon: API 16 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r4 [Addon: API 17 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r4 [Addon: API 18 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r20 [Addon: API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 24 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 23 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 21 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google APIs r1 [Addon: API 22 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google TV Addon r2 [Addon: API 12 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google TV Addon r1 [Addon: API 13 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Glass Development Kit Preview r11 [Addon: API 19 (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Support Repository r47.0.0 [Extra: (Android)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Repository r58 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play Licensing Library r1 not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play APK Expansion library r1 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play services for Froyo r12 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Play services r46 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google USB Driver r11 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google AdMob Ads SDK r11 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Analytics App Tracking SDK r3 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Web Driver r2 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Google Cloud Messaging for Android Library r3 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Auto API Simulators r1 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Android Auto Desktop Head Unit emulator r1.1 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Instant Apps Development SDK r1.1.0 [Extra: (Google Inc.)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component GPU Debugging tools r1.0.3 [Extra: (Android)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component GPU Debugging tools r3.1.0 [Extra: (Android)] not present on the system
Xamarin.VisualStudio.Progress.ProgressReportService|Information|0|Component Intel x86 Emulator Accelerator (HAXM installer) r6.2.1 [Extra: (Intel Corporation)] not present on the system
```
</details>
<!--
Switch to the "Preview" tab to ensure your issue renders correctly.
Please add an appropriate "Area:" label in the Labels section.
-->


---

<!-- source=github_issue; title=Quest 2 No-Longer Detected via Virtual Desktop; url=https://github.com/Neos-Metaverse/NeosPublic/issues/1520 -->

# Quest 2 No-Longer Detected via Virtual Desktop

- Source: github_issue
- URL: https://github.com/Neos-Metaverse/NeosPublic/issues/1520

Historically you could run Neos via SteamVR or directly via the Oculus runtime, the latter being more performant and generally cleaner. Something has apparently changed recently wherein the latter no-longer works. Neos still works via SteamVR but this was always a big buggy and had a performance penalty so is generally discouraged.
Trying to launch Neos in "Oculus" mode simply starts up in desktop/screen mode now. The logs seem to imply no detection of a headset at all.
Starting other games via the Oculus runtime still work as expected, this seems to be Neos specific hence why it seems something has changed in Neos (Virtual Desktop also deny any changes that could result in this recent difference in behaviour).


---

<!-- source=github_issue; title=[Critical Issue] if install this mod, the client-side cannot use teleport button; url=https://github.com/Charlese2/HostFixes/issues/10 -->

# [Critical Issue] if install this mod, the client-side cannot use teleport button

- Source: github_issue
- URL: https://github.com/Charlese2/HostFixes/issues/10

same as topic, u can test this issue in LAN mode, even launch 2 game process in same device
Related comments:
@Charlese2 i have to mention u, this issue already 2 months, since v1.0.4
[Error : HarmonyX] Error while running static void HostFixes.Patches+HostInitialization::Postfix(Terminal __instance). Error: System.NullReferenceException: Object reference not set to an instance of an object
at HostFixes.Patches+HostInitialization.Postfix (Terminal __instance) [0x0000b] in <a544a9418668440ab2a7c30f10d141f8>:0
at (wrapper dynamic-method) Terminal.DMD<Terminal::Awake>(Terminal)
[Error : Unity Log] NullReferenceException: Object reference not set to an instance of an object
Stack trace:
HostFixes.Plugin+HostFixesServerRecieveRpcs.PressTeleportButtonServerRpc (ShipTeleporter instance, Unity.Netcode.ServerRpcParams serverRpcParams) (at <a544a9418668440ab2a7c30f10d141f8>:0)
(wrapper dynamic-method) ShipTeleporter.DMD<ShipTeleporter::__rpc_handler_389447712>(Unity.Netcode.NetworkBehaviour,Unity.Netcode.FastBufferReader,Unity.Netcode.__RpcParams)
Unity.Netcode.RpcMessageHelpers.Handle (Unity.Netcode.NetworkContext& context, Unity.Netcode.RpcMetadata& metadata, Unity.Netcode.FastBufferReader& payload, Unity.Netcode.__RpcParams& rpcParams) (at <895801699cfc4b4ab52267f31e2a4998>:0)
Rethrow as Exception: Unhandled RPC exception!
UnityEngine.Debug:LogException(Exception)
Unity.Netcode.RpcMessageHelpers:Handle(NetworkContext&, RpcMetadata&, FastBufferReader&, __RpcParams&)
Unity.Netcode.ServerRpcMessage:Handle(NetworkContext&)
Unity.Netcode.NetworkMessageManager:ReceiveMessage(FastBufferReader, NetworkContext&, NetworkMessageManager)
Unity.Netcode.NetworkMessageManager:HandleMessage(NetworkMessageHeader&, FastBufferReader, UInt64, Single, Int32)
Unity.Netcode.NetworkMessageManager:ProcessIncomingMessageQueue()
Unity.Netcode.NetworkManager:NetworkUpdate(NetworkUpdateStage)
Unity.Netcode.NetworkUpdateLoop:RunNetworkUpdateStage(NetworkUpdateStage)
Unity.Netcode.<>c:<CreateLoopSystem>b__0_0()


---

<!-- source=github_issue; title=MacOS arm64 (Apple Silicon) Support - Valheim; url=https://github.com/BepInEx/BepInEx/issues/899 -->

# MacOS arm64 (Apple Silicon) Support - Valheim

- Source: github_issue
- URL: https://github.com/BepInEx/BepInEx/issues/899

### Describe your problem
Valheim just released on MacOS today. [Source](https://www.reddit.com/r/valheim/comments/1dch2nf/valheim_is_now_on_mac/)
On Apple Silicon (arm64) hardware, the game launches an arm64 binary. It is still built with Mono as evidenced by the usual Mono directories in the app bundle.
It appears that the Mac builds of BepInEx are all for Intel x64 platform.
### Proposed solution
Please provide builds of BepInEx for MacOS arm64, or create a Universal Binary. If you create a UB, then all the .dylib files for BepInEx will internally have both an Intel x64 build and an Apple arm64 build in the same file.
A Universal Binary will be easier for users, as they just have to download "the Mac version" and not worry about which architecture their game is running. Some Unity games only ship Intel x64 binaries, but others run natively on arm64 on Apple Silicon.
This game is getting significant exposure at [WWDC 2024](https://developer.apple.com/wwdc24/) and may appear in the Keynote. Mods with BepInEx are very popular, therefore you can expect to see many, many requests for this until it is implemented.
### Alternatives
_No response_


---

<!-- source=github_issue; title=Winter Expand World Overspawn Bug; url=https://github.com/shudnal/Seasons/issues/7 -->

# Winter Expand World Overspawn Bug

- Source: github_issue
- URL: https://github.com/shudnal/Seasons/issues/7

Hi, I just wanted to see if you were already aware of this conflict between Expand World and Seasons.
To replicate the issue:
1. Set day duration in main config file to 15 seconds
2. Start game with both EW and Seasons installed
3. Fly over to a mountain
4. Wait until season changes to winter
5. About midway through winter, NRE's start to pop up in console, and many creatures and pickable items start duplicating where they stand, causing lag
![image](https://github.com/shudnal/Seasons/assets/27255329/5bd6d3c1-d49f-458b-a2d3-379aba4efcbd)
If this is not fixable within Seasons, please let me know.
Thank you,


---

<!-- source=github_issue; title=New update seems to have caused issues on Linux 2021.1.9f1 editor. Crashes and closes editor right away.; url=https://github.com/neon-age/Smart-Inspector/issues/8 -->

# New update seems to have caused issues on Linux 2021.1.9f1 editor. Crashes and closes editor right away.

- Source: github_issue
- URL: https://github.com/neon-age/Smart-Inspector/issues/8

Hey there,
I created a test project a few weeks ago, whenever this was first released, it was using 2021.1.7f1 at the time and I pulled the new changes into the project and went to start it up, but as soon as the editor first loads after the initial Unity splash/loading image, the editor simply closes, or gives a bug report window. I removed the asset from my assets folder and started Unity again to be sure and it loaded just fine. I put the Smart-Inspector folder back in the project and as it was importing/compiling it just locked up. I forced the project closed, tried to open again, and once again it crashed. The below is an excerpt from the tail end of the logs, though, it doesn't seem too helpful, unfortunately.
---- Edit, I added another bit from a log that looks like it has some more info that is relevant to the patcher, not sure if it is related, but it came up just before it locked up again.
<details>
<summary>Tail end of logs</summary>
```sh
Unloading 308 unused Assets to reduce memory usage. Loaded Objects now: 4304.
Total: 4.445728 ms (FindLiveObjects: 0.162896 ms CreateObjectMapping: 0.088576 ms MarkObjects: 3.713755 ms DeleteObjects: 0.479810 ms)
ProgressiveSceneManager::Cancel()
[MODES] ModeService[none].Initialize
[MODES] ModeService[none].LoadModes
[MODES] Loading mode Default (0) for mode-current-id-Test_Project
[LAYOUT] About to load Library/CurrentLayout-default.dwlt, keepMainWindow=False
Unhandled description string [
Unhandled description string ]
Unhandled description string \
[MODES] ModeService[default].InitializeCurrentMode
[MODES] ModeService[default].RaiseModeChanged(default, default)
[MODES] ModeService[default].UpdateModeMenus
Unhandled description string [
Unhandled description string ]
Unhandled description string \
IsTimeToCheckForNewEditor: Update time 1624411204 current 1624408549
[Project] Loading completed in 11.095 seconds
Project init time: 0.273 seconds
Template init time: 0.000 seconds
Package Manager init time: 0.000 seconds
Asset Database init time: 0.000 seconds
Global illumination init time: 0.000 seconds
Assemblies load time: 0.000 seconds
Unity extensions init time: 0.000 seconds
Asset Database refresh time: 0.000 seconds
Scene opening time: 2.838 seconds
Unhandled description string [
Unhandled description string ]
Unhandled description string \
Unhandled description string [
Unhandled description string ]
Unhandled description string \
Caught fatal signal - signo:11 code:128 errno:0 addr:(nil)
Obtained 12 stack frames.
#0 0x007f630425cbb0 in funlockfile
#1 0x007f63040d27d9 in psiginfo
#2 0x007f6304185d3b in __printf_chk
#3 0x007f61241c7e56 in mono_breakpoint_clean_code
#4 0x00000041977308 in (Unknown)
#5 0x00000040f43dac in System.InvalidCastException:.ctor ()
#6 0x007f61240d5be5 in mono_print_method_from_ip
#7 0x007f61242459fc in mono_perfcounter_foreach
#8 0x007f61242491c1 in mono_object_unbox
#9 0x007f6124202c2b in mono_exception_from_token
#10 0x007f61241c73ac in mono_breakpoint_clean_code
#11 0x00000041978fa3 in (Unknown)
Launching bug reporter
QObject: Cannot create children for a parent that is in a different thread.
(Parent is QObject(0x1ebc4c0), parent's thread is QThread(0x1557630), current thread is Thread(0x18016d0)
```
</details>
<details>
<summary>Additional Logs</summary>
```sh
41359000-41369000 rwxp 00000000 00:00 0
41bd2000-41be2000 rwxp 00000000 00:00 0
55e3bdf17000-55e3bfce0000 r--p 00000000 103:05 6704642 /home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity
55e3bfce0000-55e3c316a000 r-xp 01dc9000 103:05 6704642 /home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity
55e3c316a000-55e3c3270000 r--p 05253000 103:05 6704642 /home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity
55e3c3270000-55e3c32bc000 rw-p 05359000 103:05 6704642 /home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity
55e3c32bc000-55e3c3560000 rw-p 00000000 00:00 0
55e3c4c5f000-55e3cec26000 rw-p 00000000 00:00 0 [heap]
7f167487f000-7f167ac49000 r--p 00000000 103:05 6704584 /home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity_s.debug
7f1680000000-7f1680108000 rw-p 00000000 00:00 0
7f1680108000-7f1684000000 ---p 00000000 00:00 0
7f16875ff000-7f1687600000 ---p 00000000 00:00 0
7f1687600000-7f1687e00000 rw-p 00000000 00:00 0
7f1688000000-7f1688021000 rw-p 00000000 00:00 0
7f1688021000-7f168c000000 ---p 00000000 00:00 0
7f168c000000-7f168c02a000 rw-p 00000000 00:00 0
7f168c02a000-7f1690000000 ---p 00000000 00:00 0
7f1690000000-7f1690021000 rw-p 00000000 00:00 0
# ------ A while lot more of the above - cut because it was hundreds/ possibly thousands of lines
# -----------------------------------------------------------------------------------------------
Native stacktrace:
/home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Data/MonoBleedingEdge/MonoEmbedRuntime/libmonobdwgc-2.0.so(+0xd809c) [0x7f175415309c]
/home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Data/MonoBleedingEdge/MonoEmbedRuntime/libmonobdwgc-2.0.so(+0x5be3f) [0x7f17540d6e3f]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x14bb0) [0x7f195db52bb0]
/lib/x86_64-linux-gnu/libpthread.so.0(pthread_mutex_lock+0x4) [0x7f195db49824]
/lib/x86_64-linux-gnu/libnvidia-glcore.so.465.31(+0xda98a9) [0x7f1822e518a9]
/lib/x86_64-linux-gnu/libGLX_nvidia.so.0(+0x7a267) [0x7f184452b267]
/lib/x86_64-linux-gnu/libc.so.6(+0x91f30) [0x7f195d9e5f30]
/lib/x86_64-linux-gnu/libc.so.6(__libc_fork+0x24) [0x7f195da32924]
/home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity(+0x384061d) [0x55e3c175761d]
/home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity(+0x383f335) [0x55e3c1756335]
/home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity(+0x2ac1794) [0x55e3c09d8794]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x14bb0) [0x7f195db52bb0]
/home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity(+0x24af9d8) [0x55e3c03c69d8]
/home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity(+0x2deb6c4) [0x55e3c0d026c4]
/home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity(+0x2deb5c1) [0x55e3c0d025c1]
/home/mosthated/Unity/Hub/Editor/2021.1.9f1/Editor/Unity(+0x4965b94) [0x55e3c287cb94]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x9590) [0x7f195db47590]
/lib/x86_64-linux-gnu/libc.so.6(clone+0x43) [0x7f195da6d223]
Debug info from gdb:
mono_gdb_render_native_backtraces not supported on this platform, unable to find gdb or lldb
Obtained 9 stack frames.
#0 0x0055e3c08b7773 in profiling::Profiler::InitializeUserThread(char const*, char const*)
#1 0x0055e3c0a017a3 in profiling::gc_finalizer_start(void*)
#2 0x007f1754257482 in mono_profiler_set_iomap_report_callback
#3 0x007f175428f9a4 in mono_callspec_cleanup
#4 0x007f1754260cea in mono_threads_set_shutting_down
#5 0x007f17542c2d1b in GC_inner_start_routine
#6 0x007f17542b7851 in GC_call_with_stack_base
#7 0x007f195db47590 in start_thread
#8 0x007f195da6d223 in clone
Launching bug reporter
```
</details>
Thanks,
-MH ------------------------------------


---

<!-- source=github_issue; title=Host not accept issue when after the first game; url=https://github.com/TIRTAGT/LCDirectLAN/issues/2 -->

# Host not accept issue when after the first game

- Source: github_issue
- URL: https://github.com/TIRTAGT/LCDirectLAN/issues/2

![image](https://github.com/TIRTAGT/LCDirectLAN/assets/96377775/083a3ba4-9c97-4602-8626-c81fe68e9ca2)
@TIRTAGT so this issue happen, i try to figure it out why, after the first game (no matter play the hole game or not), quit to main menu and create the game again, this happen
using 127.0.0.1 and port 7777, no ipv6 listening (old released version)
my Dark Hour Modpack code: 018dc3cd-5a10-cdc9-8616-0d9a3b1e4b26
Do not run 2 game programs in the same device, u might will encounter savefile corrupt


---

<!-- source=github_issue; title=Persistent Error: "Ads still not loaded"; url=https://github.com/EvilMindDevs/hms-unity-plugin/issues/163 -->

# Persistent Error: "Ads still not loaded"

- Source: github_issue
- URL: https://github.com/EvilMindDevs/hms-unity-plugin/issues/163

**Description**
I have been trying to get the ads to work in both my code and the demo but they always say ads not loaded
**Expected behavior**
To show banner , interstitial and reward ads as needed
**Current Behavior**
Always says: "ads still not loaded yet"
**Specifications**
Unity: v2018.2.8.8f1
HMS plugin: v2.0.9 - Unity 2018
**Screenshots for additional context**
![image](https://user-images.githubusercontent.com/40564798/129593218-1ada9a2b-66bd-4e00-8ccf-85ccee24714d.png)
![image](https://user-images.githubusercontent.com/40564798/129593284-9d7f5c4f-8271-4a13-a601-3f27ad0b98a7.png)
Please help


---

<!-- source=github_issue; title=trigger object with a note in Unity; url=https://github.com/melanchall/drywetmidi/issues/85 -->

# trigger object with a note in Unity

- Source: github_issue
- URL: https://github.com/melanchall/drywetmidi/issues/85

Hi.
How would you trigger a gameObject with a specific note of a midi file inside Unity?
I'm a total noob in coding so excuse me for the question but I really don't know where to begin.
Related comments:
Hi,
Please clarify your task. What does that mean:
> How would you trigger a gameObject with a specific note of a midi file
?
You want to play MIDI file and make some action on a note?
"You want to play MIDI file and make some action on a note?"
Yes that's it.
I want that Unity to know everytime a specific note is played.
But I don't know what is better to do that:
1/ Analyse the midi file before Unity start
or
2/ Analyse the midi file in real time while it is played and trigger the actions
(This midi file will be created before in my DAW for that specific purpose, I will just create a note in my midi editor everytime I want the same action to be triggered)
Your task has easy solution. Please read [Playback](https://melanchall.github.io/drywetmidi/articles/playback/Overview.html) article and take a look at [NotesPlaybackStarted](https://melanchall.github.io/drywetmidi/api/Melanchall.DryWetMidi.Devices.Playback.html#Melanchall_DryWetMidi_Devices_Playback_NotesPlaybackStarted) and [NotesPlaybackFinished](https://melanchall.github.io/drywetmidi/api/Melanchall.DryWetMidi.Devices.Playback.html#Melanchall_DryWetMidi_Devices_Playback_NotesPlaybackFinished) events.
Small example:
```csharp
var midiFile = MidiFile.Read("The great song.mid");
var outputDevice = OutputDevice.GetByName("Device name");
var playback = midiFile.GetPlayback(outputDevice);
playback.NotesPlaybackStarted += OnNotesPlaybackStarted;
```
and sample `OnNotesPlaybackStarted`:
```csharp
private static void OnNotesPlaybackStarted(object sender, NotesEventArgs e)
{
foreach (var note in e.Notes)
{
Console.WriteLine("Note is " + note);
}
}
```
There are issues related with Unity that may help you:
* #3
* #79
* #84


---

<!-- source=github_issue; title=3D Keyboard; url=https://github.com/microsoft/MixedRealityToolkit-Unity/issues/546 -->

# 3D Keyboard

- Source: github_issue
- URL: https://github.com/microsoft/MixedRealityToolkit-Unity/issues/546

Something that’s come up in several conversations with developers is the challenges with virtual keyboard support in 3D. Looking in the forums, this is a [common](https://forums.hololens.com/discussion/comment/13363) [problem](https://forums.hololens.com/discussion/comment/12365) [there](https://forums.hololens.com/discussion/2222/how-to-make-the-keyboard-appear-in-unity-hololens-app) [too](https://forums.hololens.com/discussion/comment/6703).
The suggested workaround is covered in the article [Keyboard input in Unity](https://developer.microsoft.com/en-us/windows/holographic/keyboard_input_in_unity), but that guidance requires that the user leave the 3D application and requires that the app be built for Xaml instead of D3D.
This is driving many developers to create their own Unity keyboard or purchase one from the Asset Store. I propose that a solid, basic, skinnable keyboard should be included in the Holo Toolkit.


---

<!-- source=github_issue; title=Dissonance issues with players disconnecting and reconnecting; url=https://github.com/Placeholder-Software/Dissonance/issues/55 -->

# Dissonance issues with players disconnecting and reconnecting

- Source: github_issue
- URL: https://github.com/Placeholder-Software/Dissonance/issues/55

## Context
Hi, I have recently implemented Dissonance into my Unity project using UNet High Level API. My project currently supports players being able to join and disconnect from a host server as they please and this has started causing issues with Dissonance. Upon first connection, Dissonance works perfectly and all players have no issues hearing and communicating with each other. It's when a player leaves and reconnects that I'm starting to see some issues.
## Expected Behavior
When a player leaves and reconnects I would like for dissonance to resume working as it did when they first connected. This also begins to cause issues with other players ability to hear each other so I feel like there is something going wrong on the server.
## Actual Behavior
The reconnecting player can no longer broadcast to other players or receive audio even though the 'Voice Broadcast Trigger' and 'Voice Receipt Trigger' are enabled. I have noticed that upon connecting to the server again that the client still see's their previous player ID as a peer under the Dissonance Comms Component on the DissonanceSetup GameObject. I feel this is contributing to the issue as these peer entries continue to stack as the client continues to disconnect and reconnect. Another note is that as this only happens on the client, it is not on the server, making me think that this issue may be the result of de-synchronisation between the server and client ?
## Steps to Reproduce
This problem can be reproduced within the Dissonance demo scene
1. Build the demo scene and run multiple instances on the same computer or separate computers.
2. Connect all players through localhost or over a local IP.
3. Ensure all players can correctly communicate with each other, this step may be difficult off one PC as multiple instances all working off the same microphone will cause intense feedback.
4. Disconnect one player and reconnect them, this should display the behaviour outlined in the 'Actual Behaviour' section of this post. The problem has definitely been replicated if there is an extra peer entry on all clients, to check this one client should be ran through Unity.
## Your Environment
- **Dissonance version used**: v3.0.2
- **Unity version**: 5.6.2f1 (Personal and Pro)
- **Editor Operating System and version**: Microsoft Windows 7 Professional N 6.1.7601
- **Build Settings**: This problem occurs on both Windows and Android
- **Link to your project**: Cannot provide source code or project at this time
##Final Notes
This is quite a pressing issue as this project is on a deadline, any help would be much appreciated.
Thanks for your time,
Jack


---

<!-- source=github_issue; title=SocketCluster for Unity3D; url=https://github.com/sacOO7/SocketclusterClientDotNet/issues/4 -->

# SocketCluster for Unity3D

- Source: github_issue
- URL: https://github.com/sacOO7/SocketclusterClientDotNet/issues/4

Hi.
How can i use this in Unity3D. I just copy **Newtonsoft.Json** dll and **WebSocket4Net** dll and all **c#** scripts to the project . Whether this will be enough ?
Maybe you can provide some integration tips for **Unity** .
Thanks.


---

<!-- source=github_issue; title=[feature] Magic Leap Support; url=https://github.com/Placeholder-Software/Dissonance/issues/125 -->

# [feature] Magic Leap Support

- Source: github_issue
- URL: https://github.com/Placeholder-Software/Dissonance/issues/125

Hoping to get support for Dissonance to work on the Magic Leap.
Currently, the Magic Leap can join a Unet server, and seems to connect to dissonance - the dissonanceComms script gets a unique 'Local Player ID' that is consistent across all other connected instances of unity connected to the server.
However, the Magic Leap does not appear as a 'peer' on any other instance of unity and cannot send or receive voice.
I don't seem to be getting any errors and the same setup is working on other android devices.


---

<!-- source=github_issue; title=Beat Saber (620980); url=https://github.com/ValveSoftware/Proton/issues/6638 -->

# Beat Saber (620980)

- Source: github_issue
- URL: https://github.com/ValveSoftware/Proton/issues/6638

# Compatibility Report
- Name of the game with compatibility issues: Beat Saber (unity_alpha branch)
- Steam AppID of the game: 620980
## System Information
- GPU: <!-- e.g. RX 580 or GTX 970 --> PowerColor RX 6600 XT
- Driver/LLVM version: <!-- e.g. Mesa 18.2/7.0.0 or nvidia 396.54 --> Mesa 22.3.6-1
- Kernel version: <!-- e.g. 4.17 --> 6.1.18-200
- Link to full system information report as [Gist](https://gist.github.com/Meister1593/c6d9e92595173acb7e4a41a5b78aca1a/):
- Proton version: Proton experimental, Proton 7.0-6 (same issue)
- Arch distrobox container under Fedora Silverblue 37
## I confirm:
- [x] that I haven't found an existing compatibility report for this game.
- [x] that I have checked whether there are updates for my system available.
[steam-620980.log](https://github.com/ValveSoftware/Proton/files/11051578/steam-620980.log)
<!-- Please add `PROTON_LOG=1 %command%` to the game's launch options and
attach the generated $HOME/steam-$APPID.log to this issue report as a file.
(Proton logs compress well if needed.)-->
## Symptoms <!-- What's the problem? -->
Can't launch it on newest version that uses OpenXR instead of OpenVR. It shows logo for a split second and closes.
Bonelab on latest beta (openxr powered game) under proton works fine.
## Reproduction
Always.
1. Change beat saber beta to unity_alpha
2. Run SteamVR (be it alvr, or native headset)
3. Run Beat Saber
4. Crash
## Additional notes
In logs there is mentions of missing extension like `XR_KHR_D3D12_enable`, which is [not implemented](https://github.com/ValveSoftware/Proton/blob/proton_7.0/wineopenxr/openxr.c#L703-L709) by Proton at the moment, which is probably the reason it can't start.
Tried to run with `-force-vulkan` but it crashes with InitialiseGraphicsEngine error (probably wasn't built with vulkan support)


---

<!-- source=github_issue; title=Crashlytics not sending any crash reports, getting "failed to retrieve settings" error on logcat.; url=https://github.com/firebase/quickstart-unity/issues/798 -->

# Crashlytics not sending any crash reports, getting "failed to retrieve settings" error on logcat.

- Source: github_issue
- URL: https://github.com/firebase/quickstart-unity/issues/798

<!-- DO NOT DELETE
validate_template=true
template_path=.github/ISSUE_TEMPLATE/issue.md
-->
### [REQUIRED] Please fill in the following fields:
* Unity editor version: 2019.3.15f1
* Firebase Unity SDK version: firebase_unity_sdk_6.15.2
* Source you installed the SDK: .unitypackage
* Problematic Firebase Component: Crashlytics
* Other Firebase Components in use: Analytics
* Additional SDKs you are using: Unity IAP, Gamesparks, Ironsource, Facebook, Appsflyer, GameAnalytics
* Platform you are using the Unity editor on: Windows
* Platform you are targeting: Android
* Scripting Runtime: IL2CPP
### [REQUIRED] Please describe the issue here:
I am getting some data on analytics, but I cannot get crashlytics to report anything. Im stuck on this...
![image](https://user-images.githubusercontent.com/2582934/94442542-011aed80-019c-11eb-884e-be07075f395c.png)
#### Steps to reproduce:
Add the firebase analytics and crashlytics sdks.
Add the google-services.json GoogleService-Info.plist files somewhere in assets folder
Add this code to initialise the firebase
`// Use this for initialization
void Start ()
{
// Initialize Firebase
Firebase.FirebaseApp.CheckAndFixDependenciesAsync().ContinueWith(task => {
var dependencyStatus = task.Result;
if (dependencyStatus == Firebase.DependencyStatus.Available)
{
// Create and hold a reference to your FirebaseApp,
// where app is a Firebase.FirebaseApp property of your application class.
// Crashlytics will use the DefaultInstance, as well;
// this ensures that Crashlytics is initialized.
Firebase.FirebaseApp app = Firebase.FirebaseApp.DefaultInstance;
// Set a flag here for indicating that your project is ready to use Firebase.
VisualDebugger.SetText("crashlytics initialised");
}
else
{
UnityEngine.Debug.LogError(System.String.Format(
"Could not resolve all Firebase dependencies: {0}",dependencyStatus));
VisualDebugger.SetText("crashlytics NOT initialised: " + dependencyStatus);
// Firebase Unity SDK is not safe to use here.
}
});
Invoke("IsCrashEnabled", 5f);
}
void IsCrashEnabled()
{
VisualDebugger.AddLine("IsCrashlyticsCollectionEnabled: "+Firebase.Crashlytics.Crashlytics.IsCrashlyticsCollectionEnabled);
}`
When I run the app, firebase is initialised successfully. Also Firebase.Crashlytics.Crashlytics.IsCrashlyticsCollectionEnabled returns true.
I crash the app in a number of different ways, then open it again without reinstalling. But no crash reports are sent.
When I watch logcat when starting the app I see this error from firebase each time the app is opened
![image](https://user-images.githubusercontent.com/2582934/94443976-bb5f2480-019d-11eb-9fcd-765ba6763538.png)
#### Relevant Code:


---

<!-- source=github_issue; title=NullReferenceException at GoogleSignIn_Result; url=https://github.com/Thaina/google-signin-unity/issues/46 -->

# NullReferenceException at GoogleSignIn_Result

- Source: github_issue
- URL: https://github.com/Thaina/google-signin-unity/issues/46

I'm testing this feature on Android device.
I wrote this simple code from the sample, and the native login dialog displayed successfully.
But when I select a account to sign in, I got a null reference exception.
What did I do wrong?
Environment
Unity 6000.0.54f1, 6000.1.14f1
Android 13
```
void Start()
{
m_Configuration = new GoogleSignInConfiguration
{
WebClientId = m_strWebClientId,
RequestIdToken = true
};
}
public void OnGoogleSignIn()
{
GoogleSignIn.Configuration = m_Configuration;
GoogleSignIn.Configuration.UseGameSignIn = false;
GoogleSignIn.DefaultInstance.SignIn().ContinueWith(OnAuthenticationFinished, TaskScheduler.FromCurrentSynchronizationContext());
}
internal void OnAuthenticationFinished(Task<GoogleSignInUser> task)
{
// breakpoint not triggered
}
```
Error stack from Logcat:
NullReferenceException: Object reference not set to an instance of an object.
at Google.Impl.GoogleSignInImpl.GoogleSignIn_Result (System.Runtime.InteropServices.HandleRef self) [0x00005] in .\Library\PackageCache\com.google.signin@ce996c127c02\GoogleSignIn\Impl\GoogleSignInImpl.cs:187
at Google.Impl.NativeFuture.get_Result () [0x00009] in .\Library\PackageCache\com.google.signin@ce996c127c02\GoogleSignIn\Impl\NativeFuture.cs:38
at Google.Future`1[T].get_Result () [0x00007] in .\Library\PackageCache\com.google.signin@ce996c127c02\GoogleSignIn\Future.cs:65
at Google.Future`1+<WaitForResult>d__8[T].MoveNext () [0x000c0] in .\Library\PackageCache\com.google.signin@ce996c127c02\GoogleSignIn\Future.cs:79
at UnityEngine.SetupCoroutine.InvokeMoveNext (System.Collections.IEnumerator enumerator, System.IntPtr returnValueAddress) [0x00027] in \home\bokken\build\output\unity\unity\Runtime\Export\Scripting\Coroutines.cs:17


---

<!-- source=github_issue; title=Playback produces unexpected results in Unity; url=https://github.com/melanchall/drywetmidi/issues/31 -->

# Playback produces unexpected results in Unity

- Source: github_issue
- URL: https://github.com/melanchall/drywetmidi/issues/31

I've integrated DWM into my Unity project (2019.1.0f2) for MIDI file playback and parsing. I've called `playback.Start()` and the MIDI file will not play. I have tried several MIDI files and nothing will play.
```csharp
// Use the first available OutputDevice (Microsoft GS Wavetable Synth)
var outputDevice = OutputDevice.GetAll().ToArray()[0];
// The MIDI file is copied to this location earlier
var playback = MidiFile.Read(Application.dataPath + @"/Scripts/in.mid").GetPlayback(outputDevice);
```
Later, in a coroutine (so the MIDI file starts playing at a specific time):
```csharp
playback.Start();
```
Playback doesn't want to start, even on the main thread.
Also, `playback.Play()` works, but it freezes the thread which I don't want, and it also drops a *lot* of notes, even on really simple MIDI files.
No exceptions are thrown.
What am I missing? And is there some fix to the dropped notes?


---

<!-- source=github_issue; title=Suggestions/Wishes; url=https://github.com/zAlweNy26/AlweStats/issues/9 -->

# Suggestions/Wishes

- Source: github_issue
- URL: https://github.com/zAlweNy26/AlweStats/issues/9

I use some aedenthorn mods
Clock, Real Clock, Map Coordinates Display (and Compass)
to show infos on screen which i would replace with AlweStats
i'm interested in
- Real Time Clock:
- in upper left corner
- with format string
- with seconds if possible
- with date
- Map Coordinates
- over minimap
- with format strings
- default as "Player (x, y, z)\nFocus (x, y, z)"
- if map open as "Cursor (x, y, z)"
- if build camera used as "Camera (x, y, z)\nFocus x, y, z)"
And please add config option so i can make the background of each box
half transparent and dark. (checkbox or as color setting)


---

<!-- source=github_issue; title=Unity SDK - S3 PostObject Amazon.Runtime.Internal.HttpErrorResponseException when using S3CannedACL.PublicRead; url=https://github.com/aws/aws-sdk-net/issues/332 -->

# Unity SDK - S3 PostObject Amazon.Runtime.Internal.HttpErrorResponseException when using S3CannedACL.PublicRead

- Source: github_issue
- URL: https://github.com/aws/aws-sdk-net/issues/332

AWS SDK version: aws-sdk-unity_3.1.57.0
Platform: Unity v5.3.4f1 (Mac OS Unity Editor and iOS 8.0 onwards)
When posting a file to a S3 bucket using the S3CannedACL.PublicRead, an Amazon.Runtime.Internal.HttpErrorResponseException is returned.
Using the same code but with S3CannedACL.Private, the file is successfully uploaded.
The request is formed as follows:
```
var request = new PostObjectRequest()
{
Bucket = S3BucketName,
Key = fileName,
InputStream = stream,
CannedACL = S3CannedACL.PublicRead
};
```
Is S3CannedACL.PublicRead not a valid option? Or does the bucket need to be configured differently?


---

<!-- source=github_issue; title=IndexOutOfRangeException: Array index is out of range.; url=https://github.com/Demigiant/dotween/issues/16 -->

# IndexOutOfRangeException: Array index is out of range.

- Source: github_issue
- URL: https://github.com/Demigiant/dotween/issues/16

DoTween version v1.0.665
This errors started to happen when a big amount of tweens launch at the same time on different objects (100-300 tween). Maybe there is situations when 2-3 similar tweens start on the same object and same parameter.
IndexOutOfRangeException: Array index is out of range.
DG.Tweening.Core.TweenManager.RemoveActiveTween (DG.Tweening.Tween t) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__DOTween/_DOTween.Assembly/DOTween/Core/TweenManager.cs:786)
DG.Tweening.Core.TweenManager.Update (UpdateType updateType, Single deltaTime, Single independentTime) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__DOTween/_DOTween.Assembly/DOTween/Core/TweenManager.cs:400)
DG.Tweening.Core.DOTweenComponent.Update () (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__DOTween/_DOTween.Assembly/DOTween/Core/DOTweenComponent.cs:50)
And the second one, similar:
IndexOutOfRangeException: Array index is out of range.
(wrapper stelemref) object:stelemref (object,intptr,object)
DG.Tweening.Core.TweenManager.AddActiveTween (DG.Tweening.Tween t) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__DOTween/_DOTween.Assembly/DOTween/Core/TweenManager.cs:731)
DG.Tweening.Core.TweenManager.GetTweener[Color,Color,ColorOptions]() (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__DOTween/_DOTween.Assembly/DOTween/Core/TweenManager.cs:97)
DG.Tweening.DOTween.ApplyTo[Color,Color,ColorOptions](DG.Tweening.Core.DOGetter`1 getter, DG.Tweening.Core.DOSetter`1 setter, Color endValue, Single duration, DG.Tweening.Plugins.Core.ABSTweenPlugin`3 plugin) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__DOTween/_DOTween.Assembly/DOTween/DOTween.cs:879)
DG.Tweening.DOTween.ToAlpha (DG.Tweening.Core.DOGetter`1 getter, DG.Tweening.Core.DOSetter`1 setter, Single endValue, Single duration) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__DOTween/_DOTween.Assembly/DOTween/DOTween.cs:404)
DG.Tweening.ShortcutExtensions.DOFade (UnityEngine.UI.Image target, Single endValue, Single duration) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__DOTween/_DOTween.Assembly/DOTween46/ShortcutExtensions.cs:70)
CCellArrowMap.setState (ECellArrowState st) (at Assets/Scripts/Objects/CCellArrowMap.cs:32)
CCellArrowMap.Start () (at Assets/Scripts/Objects/CCellArrowMap.cs:63)


---

<!-- source=github_issue; title=Signal Handling; url=https://github.com/FEX-Emu/FEX/issues/1682 -->

# Signal Handling

- Source: github_issue
- URL: https://github.com/FEX-Emu/FEX/issues/1682

Splitting from #1558 & #1677, as well as discussions with @neobrain and @Sonicadvance1.
## The issues
(a) Signals can interrupt the JIT compiler or syscall, other FEX-related code, 3rd party libraries, or thunked libraries, which are not guaranteed to be signal re-entrant safe. Any code that touches non-stack memory, or uses mutexes is possibly not signal safe. We currently block signals around some code, either using `ScopedSignalMaskWith*` guards or manually (eg, the dispatcher disabling signal handling around calls to CompileCode)
(b) Signals can interrupt the translated code in the middle of operations that would normally be atomic wrt signals. This may or may not be a problem, depending on how we have implemented x86. A good example is REP* operations. This can be an issue even without LSE elimination, as the recovered guest state might be "teared".
(c) Similar to above, signals can interrupt the translated code in places where we can't recover the guest architectural place, due to optimisations.
(d) Similar to above, synchronous signals might be generated which need to recover a full context and cannot be deffered.
Group 1: From x86 instructions
- SIGSEGV (memops, permissions / unmapped memory)
- SIGBUS (meops, mapping past end of file)
- SIGFPE (all floating point exceptions? Integer overflow too?)
Group 2: Handled from the x86 frontend
- SIGILL (not handled instruction)
- SIGTRAP (breakpoint, `int3` or `int 0x3`
- SIGEMT (not generated)
Group 3: Generated from system calls
- SIGSYS (Bad system call, SVr4; seccomp)
- SIGABRT (raise / __pthread_kill / kill others?)
(e) Signal latency. Whenever we disable the signal mask, like we do around `::CompileCode`, or with the signal + mutex lock guards, signal delivery gets delayed. This is mostly a concern for long-standing/non constant time signal blocking, like around `::CompileCode` (can take up to 10+ miliseconds with complex blocks). There is an argument to be made that we should compile blocks faster, though that will never 100% solve the issue. Also, signal handlers can be delayed while code for them is getting compiled, particularly during their first run.
(f) With deferred signals the opposite problem also appears, that we consume the signal too fast. I'm not sure if this results to an extra signal being possibly queued while a signal is deferred. Also, the signal might appear 'dequeued' to the sender, while it is still 'pending' in FEX, which might lead to some guest instructions running (a bit of 'execution overshoot'), a condition that can be detected, but extremely unlikely to matter to the guest.
(g) While signal delivery is not guaranteed to happen at any speed, lovely features like signal queue merging, which can lead to losing information about the delivered signals, can uncover bugs / assumptions done in the guest code.
## Current status
Our current "signal safety strategy" for (a) is to sprinkle signal disabling code around regions that deadlock. This is very inconsistent throughput the codebase, and there are several bugs waiting to be hit. In general, this is a compromise between "likely to lockup" and "performant code".
For (b) and (c) we currently only partially recover the guest architectural state, store it alongside the host architectural state, and hope the guest code doesn't care too much about the contents of the guest state, and that it will not modify it. We depend on returning to the interrupted host code using the stored host architectural state, in order to resume execution in the middle of any teared instructions, and eventually exit from some point with a valid guest state. This poses another limitation, that the interrupted block cannot be discarded from the code cache, so the code cache cannot be cleared. This might also have further implications around SMC and code invalidations.
## Proposed solutions
For (a) I'd like us to have clear guidelines on how to handle this, as well as a mode that might be slower but offers guaranteed stability. This needs some thought, but is not too hard.
For (b) and (c) the only viable solution I can think of is a combination of deferring the signal delivery until we have a fully recoverable guest state, and storing metadata that can help us exit from the middle of a block. (c) Can be avoided by limiting store elimination from LSE and disabling DSE. We can have a tradeoff between "defer delay" vs "runtime performance".
For (d.1), we'll need special state flushing semantics and/or recovery metadata and/or exit blocks in instructions that may cause them. This requires extra caution around SRA.
For (d.2), the frontend can take care of everything.
For (d.3), we can likely merge it with the syscall handling case of (a)
For (e) we can implement some form of 'aborts' for long running cases with blocked signals, ie early exits during `::CompileCode` or even possible `conditional aborts` ie temporarily pausing the execution but only aborting if re-executed before getting resumed.
For (f), we can modify the behavior syscalls where signal queueing status can be detected, and make them take actual signal delivery by FEX to the guest into account. This cannot be perfect during guest/host process interop.
For (g), we can implement 'user mode queueing', possibly on top of (g), to get closer to native guest behaviour.
(e) + (f) + (g) are edge case behaviors that is unlikely to matter in practice, and can mostly get triggered by compilation stutter completely altering the expected timing of the guest application.
## Related Tickets
#518, #650, #1228, #1666
## Other information
Unity depends on at least graceful handling of asynchronous SIGPWR, SIGXCPU (GC, loose context requirements) and SIGSEGV w/ null pointers (NullReferenceException generation, strict context requirements).


---

<!-- source=github_issue; title=Amazon Polly for Unity; url=https://github.com/aws/aws-sdk-net/issues/627 -->

# Amazon Polly for Unity

- Source: github_issue
- URL: https://github.com/aws/aws-sdk-net/issues/627

How do i use Amazon Polly in Unity?
Related comments:
Amazon Polly is currently not supported on the [AWS Mobile SDK for Unity](http://docs.aws.amazon.com/mobile/sdkforunity/developerguide/).
How do i use the .NET version in Unity? because Unity is in .Net so it should work well on it.
**EDIT**: Why we can't use .NET version in Unity?
If you are asking if the SDK DLLs for .NET 3.5 or 4.5 can be used for Unity, you cannot, because Unity targets Mono which is equivalent to .NET Framework 2.0. Also, the APIs exposed in SDK that targets 3.5 are quite different from the async APIs available in the Unity SDK.


---

<!-- source=github_issue; title=Allow Controller to directly interact with Unity UI elements; url=https://github.com/ExtendRealityLtd/VRTK/issues/639 -->

# Allow Controller to directly interact with Unity UI elements

- Source: github_issue
- URL: https://github.com/ExtendRealityLtd/VRTK/issues/639

Allow users to touch, press, and interact with GUI elements (such as buttons) via controller meshes... as an alternative to laser pointer.
Background info:
As discussed on Slack, the emerging trend seems to be that if elements are within arms length, the user ought to be able to poke at and otherwise interact with them using their finger/hand (or similar custom controller mesh), rather than a twitchy laser pointer. (I've seen laser pointer cause confusion in my own usability testing.) Also, it was mentioned how hover events perhaps ought to be triggered when the controller is within a couple of centimeters, and @thestonefox suggested that a spherecast or capsulecast be used around the controller.


---

<!-- source=github_issue; title=Make a MacOS version; url=https://github.com/nesrak1/UABEA/issues/446 -->

# Make a MacOS version

- Source: github_issue
- URL: https://github.com/nesrak1/UABEA/issues/446

idk just make one im begging for it 🙏
Related comments:
I don't have a mac and have no way to test/compile the binaries. You are welcome to help with it if you want (I could even give you the steps). The code is mostly cross platform, so besides compilation there shouldn't be any code to change really.
would love to help with it 😁 give me the steps and ill totally help you!!
Development is going over at https://github.com/nesrak1/UABEANext right now where the code is a lot easier to get up and running. If you have the [dotnet 8 sdk (download link is for arm mac)](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/sdk-8.0.411-macos-arm64-installer), you can just download the source code, unpack the zip, and run `dotnet run` in a terminal. Mostly everything should work out of the box except for editing textures.
To get texture encoding support working on mac, you'll need to compile [the texture encoder itself](https://github.com/nesrak1/AssetsTools.NET/tree/dev/TextureEncoder) as well as [cuttlefish](https://github.com/nesrak1/Cuttlefish), the library that actually does the encoding. I will write some more details instructions as well as update the cmake project to support mac paths sometime tomorrow.


---

<!-- source=github_issue; title=Hololens 1 connecting on Rosbridge but not communicating both on topics and actions; url=https://github.com/siemens/ros-sharp/issues/278 -->

# Hololens 1 connecting on Rosbridge but not communicating both on topics and actions

- Source: github_issue
- URL: https://github.com/siemens/ros-sharp/issues/278

![3](https://user-images.githubusercontent.com/19976265/72168048-0d280a80-33d5-11ea-9ed3-6ad961213ce8.PNG)
![ros_connector](https://user-images.githubusercontent.com/19976265/72168049-0d280a80-33d5-11ea-9922-bfa9f94c310d.PNG)
![2](https://user-images.githubusercontent.com/19976265/72168050-0dc0a100-33d5-11ea-92dd-ccb7b9032d64.PNG)
* [x] I am at the right place and my issue is directly related to ROS#. General technical questions I would post e.g. at [ROS Answers](https://answers.ros.org/) or [Stack Overflow](https://stackoverflow.com). For library-specific questions I would look for help in the corresponding library forums.
* [x] I have thoroughly read [the Contributing Guideline](Contributing.md) and writing this issue is the right thing to do in my case.
---
## I found a bug! ##
* [x] I am using the latest ROS# version available here on the master branch.
* [x] I am adding all required information, code and data files, screenshots and log files so that you can reproduce the problem.


---

<!-- source=github_issue; title=Help with Directions API; url=https://github.com/mapbox/mapbox-unity-sdk/issues/531 -->

# Help with Directions API

- Source: github_issue
- URL: https://github.com/mapbox/mapbox-unity-sdk/issues/531

Hi, I am trying to find a demo/sample where I can use mapbox unity sdk and use directions api. I want exactly what is described in the following link but for unity. Any help in this regards will be great.
https://www.mapbox.com/help/getting-started-directions-api/


---

<!-- source=github_issue; title=[BUG] VPM cannot find supported editor for 2022.3.6f1 on Linux; url=https://github.com/vrchat-community/creator-companion/issues/408 -->

# [BUG] VPM cannot find supported editor for 2022.3.6f1 on Linux

- Source: github_issue
- URL: https://github.com/vrchat-community/creator-companion/issues/408

### Describe the bug
**NOTE** This is a new behavior as of `0.1.21` and persists in `0.1.22`.
When executing VPM it does not use the editor as configured in the `settings.json` file. Instead, when executed it throws this error:
```console
[14:27:43 INF] Found No Supported Editors
[14:27:43 INF] Unity is not installed.
[14:27:43 ERR] No Unity Editor found, you need to set this before you can make new projects.
```
Additionally, during execution it modifies the `settings.json` file and removes the value set to the `pathToUnityExe` key.
### To Reproduce
1. Install VPM
```console
$ dotnet tool install --global vrchat.vpm.cli
Tool 'vrchat.vpm.cli' was installed with the latest stable version (version '0.1.22').
```
2. Configure `~/.local/share/VRChatCreatorCompanion/settings.json`
```json
1 {
2 "pathToUnityExe": "/home/ellie/Unity/Hub/Editor/2022.3.6f1/Editor/Unity",
3 "pathToUnityHub": "/opt/unityhub/unityhub",
```
3. Execute `vpm new`.
```console
$ vpm new Zoe.1 Avatar -p $PWD
[14:27:43 INF] Found No Supported Editors
[14:27:43 INF] Unity is not installed.
[14:27:43 ERR] No Unity Editor found, you need to set this before you can make new projects.
```
### Expected behavior
```console
$ vpm new Zoe.1 Avatar -p $PWD
[14:36:31 INF] VPM Doesn't know how to look at Linux executables for version yet, so just returning true for PathIsValidUnityVersion(/home/ellie/Unity/Hub/Editor/2022.3.6f1/Editor/Unity)
[14:36:31 INF] VPM Doesn't know how to look at Linux executables for version yet, so just returning true for PathIsValidUnityVersion(/home/ellie/Unity/Hub/Editor/2022.3.6f1/Editor/Unity)
[14:36:31 INF] Unity is installed.
[14:36:31 INF] Let's create a project named Zoe.1 from the template /home/ellie/.local/share/VRChatCreatorCompanion/VRCTemplates/Avatar at the path /media/ellie/Ashley/3D/Projects/Unity/Zoe.1
[14:36:31 INF] Looking for Legacy Packages to Upgrade by Scanning Folders within com.vrchat.avatars
[14:36:31 INF] Looking for Legacy Packages to Upgrade by Scanning Folders within com.vrchat.avatars
[14:36:31 INF] Looking for Legacy Packages to Upgrade by Scanning Folders within com.vrchat.base
[14:36:31 INF] Resolved package com.vrchat.avatars ^3.5.x
[14:36:31 INF] Resolved all VPM Packages in /media/ellie/Ashley/3D/Projects/Unity/Zoe.1
[14:36:32 INF] Looking for Legacy Packages to Upgrade by Scanning Folders within com.vrchat.core.vpm-resolver
[14:36:32 INF] Looking for Legacy Packages to Upgrade by Scanning Folders within com.vrchat.core.vpm-resolver
[14:36:32 INF] Successfully resolved packages for new Project.
[14:36:32 INF] Project created!
```
(This output is tweaked from the `0.1.20` output to say `^3.5.x` instead of `^3.4.x`)
### Screenshots
**Before execution**
![before](https://github.com/vrchat-community/creator-companion/assets/1297911/7982bae7-75c3-4d28-afd6-08580be3a59f)
**After execution**
![after](https://github.com/vrchat-community/creator-companion/assets/1297911/60397cf1-bfcd-4467-8df2-19add4337742)
### Related Product
VPM CLI
### Product Version
0.1.21, 0.1.22
### OS
macOS / Linux
### Additional context
The workaround I have for now is:
1. stick with version `0.1.20`
2. create a project with `vpm`
3. delete the `./Packages/com.vrchat.*` directories from the project folder (as the older vpm installs outdated packages by default for some reason?)
4. `cd` into the project root directory
5. run `vpm resolve project` to install the correct versions of the packages
6. manually add the new project to Unity Hub
7. open the project in the 2022.3.6f1 version of Unity, hitting "Continue" when it warns about opening the project in a different version of Unity than it was created for.


---

<!-- source=github_issue; title=[BUG]: [11:37:51.904] [1] [ERROR] null Exception while loading mod RonivansLegacy_ChemicalProcessing at C:/Users/hhhge/Documents/Klei/OxygenNotIncluded/mods/Steam/3557584850.; url=https://github.com/Sgt-Imalas/Sgt_Imalas-Oni-Mods/issues/289 -->

# [BUG]: [11:37:51.904] [1] [ERROR] null Exception while loading mod RonivansLegacy_ChemicalProcessing at C:/Users/hhhge/Documents/Klei/OxygenNotIncluded/mods/Steam/3557584850.

- Source: github_issue
- URL: https://github.com/Sgt-Imalas/Sgt_Imalas-Oni-Mods/issues/289

### Which Mod?
RonivansLegacy_ChemicalProcessing
### Description of the bug/crash
The game keeps crashing
### Steps To Reproduce
open oni
### Player.log
[Player.log](https://github.com/user-attachments/files/26708760/Player.log)


---

<!-- source=github_issue; title=HoloLens and MapBox issue; url=https://github.com/mapbox/mapbox-unity-sdk/issues/734 -->

# HoloLens and MapBox issue

- Source: github_issue
- URL: https://github.com/mapbox/mapbox-unity-sdk/issues/734

* Unity version: 2018.1.0.f2
* Scripting Runtime Version: .Net 4.x Equivalent.
* Scripting Backend: IL2CPP.
* Api Compatibility Level: .NET 4.x
* Mapbox SDK version: 1.4.1
* The platform you're building to: UWP.
* Target Device: HoloLens.
* Build Type: D3D.
* A description of what you're trying to do:
Render the prefab "CitySimulatorMap" inside the Mixed Reality experience with HoloLens Device/Simulator.
* Steps to recreate the bug if appropriate:
- Create a new project and include HoloToolkit and Examples from [here.](https://github.com/Microsoft/MixedRealityToolkit-Unity/releases)
- Follow steps [here ](https://www.mapbox.com/mapbox-unity-sdk/docs/hololens-development.html)to configure the app for HoloLens.
- Import Mapbox 1.4.1. Exclude GoogleARCore, MapboxAR, UnityARInterface and UnityARKitPlugin.
- Setup Mapbox.
- Add a new scene.
- Apply all 3 options in Mixed Reality Toolkit > Configure.
- Drag the prefab CitySimulatorMap.prefab from Assets/Mapbox/Prefabs to the scene
At this point, everything will work in the Editor.
Trying to compile with above settings will give errors of duplicated/ambiguous use of Description Attribute.
* Applying what was described in #485 by @BergWerkGIS will allow me to compile the project for VS
- Add SQLite to the references
- Build and deploy to Simulator and Device
* Issue:
Map is not rendered.
Here is the [Console Output](https://pastebin.com/Yyme7cxg) from Compilation to Deploy and Debug the App.


---

<!-- source=github_issue; title=win10 build error; url=https://github.com/homuler/MediaPipeUnityPlugin/issues/358 -->

# win10 build error

- Source: github_issue
- URL: https://github.com/homuler/MediaPipeUnityPlugin/issues/358

**System information**
- OS Platform and Distribution (e.g., Linux Ubuntu 20.04, WSL2): windows 10
- Target (e.g. desktop cpu, android arm64):
- Bazel version: 6.0.0
- Python version: 3.9.0
- GCC/G++ version: 9.2.0
- Unity version:
- Android NDK version (if building for Android):
- Xcode version (if building for iOS):
**Describe the problem**
Build error
**Steps to reproduce the issue**
python build.py build --desktop cpu --opencv=cmake -v
**Full logs**
INFO (build.py): Building protobuf sources...
DEBUG (build.py): Running `bazel --output_user_root C:/_bzl build -c opt --action_env PYTHON_BIN_PATH="C://Users//asuka//AppData//Local//Programs//Python//Python39//python.py" --action_env ProgramData --action_env PROCESSOR_ARCHITECTURE --action_env PROCESSOR_IDENTIFIER --action_env PROCESSOR_LEVEL --action_env PROCESSOR_REVISION //mediapipe_api:mediapipe_proto_srcs`
DEBUG: C:/_bzl/d6cplb6i/external/org_tensorflow/third_party/repo.bzl:108:14:
Warning: skipping import of repository 'com_google_absl' because it already exists.
DEBUG: C:/_bzl/d6cplb6i/external/org_tensorflow/third_party/repo.bzl:108:14:
Warning: skipping import of repository 'com_google_protobuf' because it already exists.
DEBUG: C:/_bzl/d6cplb6i/external/org_tensorflow/third_party/repo.bzl:108:14:
Warning: skipping import of repository 'com_google_googletest' because it already exists.
DEBUG: C:/_bzl/d6cplb6i/external/org_tensorflow/third_party/repo.bzl:108:14:
Warning: skipping import of repository 'com_github_gflags_gflags' because it already exists.
DEBUG: C:/_bzl/d6cplb6i/external/org_tensorflow/third_party/repo.bzl:108:14:
Warning: skipping import of repository 'rules_python' because it already exists.
DEBUG: C:/_bzl/d6cplb6i/external/org_tensorflow/third_party/repo.bzl:108:14:
Warning: skipping import of repository 'build_bazel_rules_apple' because it already exists.
DEBUG: C:/_bzl/d6cplb6i/external/org_tensorflow/third_party/repo.bzl:108:14:
Warning: skipping import of repository 'build_bazel_rules_swift' because it already exists.
DEBUG: C:/_bzl/d6cplb6i/external/org_tensorflow/third_party/repo.bzl:108:14:
Warning: skipping import of repository 'build_bazel_apple_support' because it already exists.
DEBUG: C:/_bzl/d6cplb6i/external/org_tensorflow/third_party/repo.bzl:108:14:
Warning: skipping import of repository 'bazel_skylib' because it already exists.
DEBUG: C:/_bzl/d6cplb6i/external/org_tensorflow/third_party/repo.bzl:108:14:
Warning: skipping import of repository 'pybind11' because it already exists.
DEBUG: C:/_bzl/d6cplb6i/external/tf_runtime/third_party/cuda/dependencies.bzl:51:10: The following command will download NVIDIA proprietary software. By using the software you agree to comply with the terms of the license agreement that accompanies the software. If you do not agree to the terms of the license agreement, do not use the software.
INFO: Repository rules_python instantiated at:
C:/users/asuka/desktop/intern/mediapipeunityplugin/WORKSPACE:41:23: in <toplevel>
C:/_bzl/d6cplb6i/external/rules_pkg/deps.bzl:33:10: in rules_pkg_dependencies
C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe
Repository rule git_repository defined at:
C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git.bzl:199:33: in <toplevel>
ERROR: An error occurred during the fetch of repository 'rules_python':
Traceback (most recent call last):
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git.bzl", line 181, column 30, in _git_repository_implementation
update = _clone_or_update(ctx)
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git.bzl", line 36, column 20, in _clone_or_update
git_ = git_repo(ctx, directory)
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git_worker.bzl", line 91, column 12, in git_repo
_update(ctx, git_repo)
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git_worker.bzl", line 101, column 9, in _update
init(ctx, git_repo)
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git_worker.bzl", line 118, column 15, in init
_error(ctx.name, cl, st.stderr)
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git_worker.bzl", line 190, column 9, in _error
fail("error running '%s' while working with @%s:\n%s" % (command_text, name, stderr))
Error in fail: error running 'git init C:/_bzl/d6cplb6i/external/rules_python' while working with @rules_python:
java.io.IOException: ERROR: src/main/native/windows/process.cc(202): CreateProcessW("git" init C:/_bzl/d6cplb6i/external/rules_python): ??????????????????
(error: 2)
ERROR: C:/users/asuka/desktop/intern/mediapipeunityplugin/WORKSPACE:41:23: fetching git_repository rule //external:rules_python: Traceback (most recent call last):
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git.bzl", line 181, column 30, in _git_repository_implementation
update = _clone_or_update(ctx)
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git.bzl", line 36, column 20, in _clone_or_update
git_ = git_repo(ctx, directory)
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git_worker.bzl", line 91, column 12, in git_repo
_update(ctx, git_repo)
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git_worker.bzl", line 101, column 9, in _update
init(ctx, git_repo)
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git_worker.bzl", line 118, column 15, in init
_error(ctx.name, cl, st.stderr)
File "C:/_bzl/d6cplb6i/external/bazel_tools/tools/build_defs/repo/git_worker.bzl", line 190, column 9, in _error
fail("error running '%s' while working with @%s:\n%s" % (command_text, name, stderr))
Error in fail: error running 'git init C:/_bzl/d6cplb6i/external/rules_python' while working with @rules_python:
java.io.IOException: ERROR: src/main/native/windows/process.cc(202): CreateProcessW("git" init C:/_bzl/d6cplb6i/external/rules_python): ??????????????????
(error: 2)
ERROR: C:/users/asuka/desktop/intern/mediapipeunityplugin/mediapipe_api/BUILD:175:8: //mediapipe_api:mediapipe_proto_srcs depends on @rules_pkg//:build_zip in repository @rules_pkg which failed to fetch. no such package '@rules_python//python': error running 'git init C:/_bzl/d6cplb6i/external/rules_python' while working with @rules_python:
java.io.IOException: ERROR: src/main/native/windows/process.cc(202): CreateProcessW("git" init C:/_bzl/d6cplb6i/external/rules_python): ??????????????????
(error: 2)
ERROR: Analysis of target '//mediapipe_api:mediapipe_proto_srcs' failed; build aborted: Analysis failed
INFO: Elapsed time: 0.644s
INFO: 0 processes.
FAILED: Build did NOT complete successfully (0 packages loaded, 0 targets configured)
currently loading: @rules_pkg//
Traceback (most recent call last):
File "C:\Users\asuka\Desktop\Intern\MediaPipeUnityPlugin\build.py", line 444, in <module>
Argument().command().run()
File "C:\Users\asuka\Desktop\Intern\MediaPipeUnityPlugin\build.py", line 112, in run
self._run_command(self._build_proto_srcs_commands())
File "C:\Users\asuka\Desktop\Intern\MediaPipeUnityPlugin\build.py", line 52, in _run_command
return subprocess.run(' '.join(command_list), check=True, shell=shell)
File "C:\Users\asuka\AppData\Local\Programs\Python\Python39\lib\subprocess.py", line 524, in run
raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command 'bazel --output_user_root C:/_bzl build -c opt --action_env PYTHON_BIN_PATH="C://Users//asuka//AppData//Local//Programs//Python//Python39//python.py" --action_env ProgramData --action_env PROCESSOR_ARCHITECTURE --action_env PROCESSOR_IDENTIFIER --action_env PROCESSOR_LEVEL --action_env PROCESSOR_REVISION //mediapipe_api:mediapipe_proto_srcs' returned non-zero exit status 1.
**Additional context**
can anyone help me ?


---

<!-- source=github_issue; title=Plugin Loads but "Empty"; url=https://github.com/sinai-dev/UnityExplorer/issues/7 -->

# Plugin Loads but "Empty"

- Source: github_issue
- URL: https://github.com/sinai-dev/UnityExplorer/issues/7

Hello.
I downloaded the release version (also tried to compile myself to see if anything is different) and plugin loaded.
But, I only get a "black" screen: https://i.imgur.com/ziAoOIt.png
While on the CppExplorer Wiki there are tons of options. Whatever I click, nothing happens and nothing shows up.
My game is Unity 2019.4.2 with latest MelonLoader.
There are no errors during Melon\Game startup and CppExplorer shows, but only what you see in that picture.
Can this be solved in any way?
Thanks.


---

<!-- source=github_issue; title=Solution containing F# and C# projects break some C# tooling, even if projects are not referencing each other; url=https://github.com/dotnet/roslyn/issues/28474 -->

# Solution containing F# and C# projects break some C# tooling, even if projects are not referencing each other

- Source: github_issue
- URL: https://github.com/dotnet/roslyn/issues/28474

**Version Used**: 15.6, 15.7.4, 15.8 preview 4
**Steps to Reproduce**:
1. Create new solution
2. Create a C# project and a F# project
3. Try to perform a rename operation in C# and watch it not work
**Expected Behavior**:
Rename should properly rename when pressing Enter.
**Actual Behavior**:
Nothing happens when pressing Enter on rename.
--
This isn't specific to rename, there are other issues when trying to do F12 navigation.
This is directly related to this: https://github.com/Microsoft/visualfsharp/issues/4796#issuecomment-404344061
Quoting from the issue here:
> After investigation in the case of using rename for a type in C#, Roslyn will iterate over all projects to try to find that type. When it hits a F# project, it will throw because it is trying to get a ISyntaxFactsService from our language service which we don't have and never will. https://github.com/dotnet/roslyn/blob/master/src/Workspaces/Core/Portable/FindSymbols/FindReferences/DependentTypeFinder_ProjectIndex.cs#L55
> When that throws, it will cancel C#'s rename task and nothing works.
> I don't think this is a regression, or at least a very recent one. Most of the code paths to get to this point haven't changed from 11 months to 2 years.
> This also occurs even if the C# project isn't referenced or is referencing a F# project.


---

<!-- source=github_issue; title=Failed to spawn Network Object when Client Joins; url=https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/3897 -->

# Failed to spawn Network Object when Client Joins

- Source: github_issue
- URL: https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/3897

### Description
A clear and concise description of what the bug is.
### Reproduce Steps
1. Hosted using the Build.
2. Joined as a client using the editor.
### Actual Outcome
Second character spawns, but controls don't work.
### Expected Outcome
Spawns a working character.
### Screenshots
<img width="1498" height="214" alt="Image" src="https://github.com/user-attachments/assets/e230479c-81df-495d-9a51-5355334f1f1d" />
[Netcode] Failed to create object locally. [globalObjectIdHash=3783451317]. NetworkPrefab could not be found. Is the prefab registered with NetworkManager?
UnityEngine.Debug:LogError (object)
Unity.Netcode.NetworkLog:LogError (string) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Logging/NetworkLog.cs:34)
Unity.Netcode.NetworkSpawnManager:GetNetworkObjectToSpawn (uint,ulong,System.Nullable`1<UnityEngine.Vector3>,System.Nullable`1<UnityEngine.Quaternion>,bool,byte[]) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Spawning/NetworkSpawnManager.cs:863)
Unity.Netcode.NetworkSpawnManager:CreateLocalNetworkObject (Unity.Netcode.NetworkObject/SerializedObject,byte[]) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Spawning/NetworkSpawnManager.cs:915)
Unity.Netcode.NetworkObject:Deserialize (Unity.Netcode.NetworkObject/SerializedObject&,Unity.Netcode.FastBufferReader,Unity.Netcode.NetworkManager,bool) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkObject.cs:3265)
Unity.Netcode.SceneEventData:SynchronizeSceneNetworkObjects (Unity.Netcode.NetworkManager) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/SceneEventData.cs:1132)
Unity.Netcode.NetworkSceneManager:HandleClientSceneEvent (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2329)
Unity.Netcode.NetworkSceneManager:ClientLoadedSynchronization (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2224)
Unity.Netcode.NetworkSceneManager:OnClientBeginSync (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2155)
Unity.Netcode.NetworkSceneManager:HandleClientSceneEvent (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2311)
Unity.Netcode.NetworkSceneManager:HandleSceneEvent (ulong,Unity.Netcode.FastBufferReader) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2656)
Unity.Netcode.SceneEventMessage:Handle (Unity.Netcode.NetworkContext&) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/Messages/SceneEventMessage.cs:29)
Unity.Netcode.NetworkMessageManager:ReceiveMessage<Unity.Netcode.SceneEventMessage> (Unity.Netcode.FastBufferReader,Unity.Netcode.NetworkContext&,Unity.Netcode.NetworkMessageManager) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:568)
Unity.Netcode.NetworkMessageManager:HandleMessage (Unity.Netcode.NetworkMessageHeader&,Unity.Netcode.FastBufferReader,ulong,single,int) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:422)
Unity.Netcode.NetworkMessageManager:ProcessIncomingMessageQueue () (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:448)
Unity.Netcode.NetworkManager:NetworkUpdate (Unity.Netcode.NetworkUpdateStage) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkManager.cs:349)
Unity.Netcode.NetworkUpdateLoop:RunNetworkUpdateStage (Unity.Netcode.NetworkUpdateStage) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkUpdateLoop.cs:191)
Unity.Netcode.NetworkUpdateLoop/NetworkEarlyUpdate/<>c:<CreateLoopSystem>b__0_0 () (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkUpdateLoop.cs:214)
[Netcode] Failed to spawn NetworkObject for Hash 3783451317.
UnityEngine.Debug:LogError (object)
Unity.Netcode.NetworkLog:LogError (string) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Logging/NetworkLog.cs:34)
Unity.Netcode.NetworkObject:Deserialize (Unity.Netcode.NetworkObject/SerializedObject&,Unity.Netcode.FastBufferReader,Unity.Netcode.NetworkManager,bool) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkObject.cs:3273)
Unity.Netcode.SceneEventData:SynchronizeSceneNetworkObjects (Unity.Netcode.NetworkManager) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/SceneEventData.cs:1132)
Unity.Netcode.NetworkSceneManager:HandleClientSceneEvent (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2329)
Unity.Netcode.NetworkSceneManager:ClientLoadedSynchronization (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2224)
Unity.Netcode.NetworkSceneManager:OnClientBeginSync (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2155)
Unity.Netcode.NetworkSceneManager:HandleClientSceneEvent (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2311)
Unity.Netcode.NetworkSceneManager:HandleSceneEvent (ulong,Unity.Netcode.FastBufferReader) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2656)
Unity.Netcode.SceneEventMessage:Handle (Unity.Netcode.NetworkContext&) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/Messages/SceneEventMessage.cs:29)
Unity.Netcode.NetworkMessageManager:ReceiveMessage<Unity.Netcode.SceneEventMessage> (Unity.Netcode.FastBufferReader,Unity.Netcode.NetworkContext&,Unity.Netcode.NetworkMessageManager) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:568)
Unity.Netcode.NetworkMessageManager:HandleMessage (Unity.Netcode.NetworkMessageHeader&,Unity.Netcode.FastBufferReader,ulong,single,int) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:422)
Unity.Netcode.NetworkMessageManager:ProcessIncomingMessageQueue () (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:448)
Unity.Netcode.NetworkManager:NetworkUpdate (Unity.Netcode.NetworkUpdateStage) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkManager.cs:349)
Unity.Netcode.NetworkUpdateLoop:RunNetworkUpdateStage (Unity.Netcode.NetworkUpdateStage) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkUpdateLoop.cs:191)
Unity.Netcode.NetworkUpdateLoop/NetworkEarlyUpdate/<>c:<CreateLoopSystem>b__0_0 () (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkUpdateLoop.cs:214)
[Netcode] Failed to create object locally. [globalObjectIdHash=161353281]. NetworkPrefab could not be found. Is the prefab registered with NetworkManager?
UnityEngine.Debug:LogError (object)
Unity.Netcode.NetworkLog:LogError (string) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Logging/NetworkLog.cs:34)
Unity.Netcode.NetworkSpawnManager:GetNetworkObjectToSpawn (uint,ulong,System.Nullable`1<UnityEngine.Vector3>,System.Nullable`1<UnityEngine.Quaternion>,bool,byte[]) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Spawning/NetworkSpawnManager.cs:863)
Unity.Netcode.NetworkSpawnManager:CreateLocalNetworkObject (Unity.Netcode.NetworkObject/SerializedObject,byte[]) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Spawning/NetworkSpawnManager.cs:915)
Unity.Netcode.NetworkObject:Deserialize (Unity.Netcode.NetworkObject/SerializedObject&,Unity.Netcode.FastBufferReader,Unity.Netcode.NetworkManager,bool) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkObject.cs:3265)
Unity.Netcode.SceneEventData:SynchronizeSceneNetworkObjects (Unity.Netcode.NetworkManager) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/SceneEventData.cs:1132)
Unity.Netcode.NetworkSceneManager:HandleClientSceneEvent (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2329)
Unity.Netcode.NetworkSceneManager:ClientLoadedSynchronization (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2224)
Unity.Netcode.NetworkSceneManager:OnClientBeginSync (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2155)
Unity.Netcode.NetworkSceneManager:HandleClientSceneEvent (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2311)
Unity.Netcode.NetworkSceneManager:HandleSceneEvent (ulong,Unity.Netcode.FastBufferReader) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2656)
Unity.Netcode.SceneEventMessage:Handle (Unity.Netcode.NetworkContext&) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/Messages/SceneEventMessage.cs:29)
Unity.Netcode.NetworkMessageManager:ReceiveMessage<Unity.Netcode.SceneEventMessage> (Unity.Netcode.FastBufferReader,Unity.Netcode.NetworkContext&,Unity.Netcode.NetworkMessageManager) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:568)
Unity.Netcode.NetworkMessageManager:HandleMessage (Unity.Netcode.NetworkMessageHeader&,Unity.Netcode.FastBufferReader,ulong,single,int) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:422)
Unity.Netcode.NetworkMessageManager:ProcessIncomingMessageQueue () (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:448)
Unity.Netcode.NetworkManager:NetworkUpdate (Unity.Netcode.NetworkUpdateStage) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkManager.cs:349)
Unity.Netcode.NetworkUpdateLoop:RunNetworkUpdateStage (Unity.Netcode.NetworkUpdateStage) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkUpdateLoop.cs:191)
Unity.Netcode.NetworkUpdateLoop/NetworkEarlyUpdate/<>c:<CreateLoopSystem>b__0_0 () (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkUpdateLoop.cs:214)
[Netcode] Failed to spawn NetworkObject for Hash 161353281.
UnityEngine.Debug:LogError (object)
Unity.Netcode.NetworkLog:LogError (string) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Logging/NetworkLog.cs:34)
Unity.Netcode.NetworkObject:Deserialize (Unity.Netcode.NetworkObject/SerializedObject&,Unity.Netcode.FastBufferReader,Unity.Netcode.NetworkManager,bool) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkObject.cs:3273)
Unity.Netcode.SceneEventData:SynchronizeSceneNetworkObjects (Unity.Netcode.NetworkManager) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/SceneEventData.cs:1132)
Unity.Netcode.NetworkSceneManager:HandleClientSceneEvent (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2329)
Unity.Netcode.NetworkSceneManager:ClientLoadedSynchronization (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2224)
Unity.Netcode.NetworkSceneManager:OnClientBeginSync (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2155)
Unity.Netcode.NetworkSceneManager:HandleClientSceneEvent (uint) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2311)
Unity.Netcode.NetworkSceneManager:HandleSceneEvent (ulong,Unity.Netcode.FastBufferReader) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2656)
Unity.Netcode.SceneEventMessage:Handle (Unity.Netcode.NetworkContext&) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/Messages/SceneEventMessage.cs:29)
Unity.Netcode.NetworkMessageManager:ReceiveMessage<Unity.Netcode.SceneEventMessage> (Unity.Netcode.FastBufferReader,Unity.Netcode.NetworkContext&,Unity.Netcode.NetworkMessageManager) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:568)
Unity.Netcode.NetworkMessageManager:HandleMessage (Unity.Netcode.NetworkMessageHeader&,Unity.Netcode.FastBufferReader,ulong,single,int) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:422)
Unity.Netcode.NetworkMessageManager:ProcessIncomingMessageQueue () (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:448)
Unity.Netcode.NetworkManager:NetworkUpdate (Unity.Netcode.NetworkUpdateStage) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkManager.cs:349)
Unity.Netcode.NetworkUpdateLoop:RunNetworkUpdateStage (Unity.Netcode.NetworkUpdateStage) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkUpdateLoop.cs:191)
Unity.Netcode.NetworkUpdateLoop/NetworkEarlyUpdate/<>c:<CreateLoopSystem>b__0_0 () (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkUpdateLoop.cs:214)
NullReferenceException: Object reference not set to an instance of an object
Unity.Netcode.NetworkBehaviour.__endSendRpc (Unity.Netcode.FastBufferWriter& bufferWriter, System.UInt32 rpcMethodId, Unity.Netcode.RpcParams rpcParams, Unity.Netcode.RpcAttribute+RpcAttributeParams attributeParams, Unity.Netcode.SendTo defaultTarget, Unity.Netcode.RpcDelivery rpcDelivery) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkBehaviour.cs:354)
SceneControl.AddPlayer_ServerRpc (Unity.Netcode.NetworkBehaviourReference playRef) (at Assets/Scripts/GameState/SceneControl.cs:23)
PlayerController.OnEnable () (at Assets/Scripts/Player/PlayerController.cs:34)
UnityEngine.Behaviour:set_enabled(Boolean)
Enabler:Enable(Int32) (at Assets/Scripts/Player/Enabler.cs:22)
Enabler:OnNetworkSpawn() (at Assets/Scripts/Player/Enabler.cs:12)
Unity.Netcode.NetworkBehaviour:NetworkSpawn() (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkBehaviour.cs:814)
Unity.Netcode.NetworkObject:InvokeBehaviourNetworkSpawn() (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkObject.cs:2553)
Unity.Netcode.NetworkSpawnManager:SpawnNetworkObjectLocallyCommon(NetworkObject, UInt64, Boolean, Boolean, UInt64, Boolean) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Spawning/NetworkSpawnManager.cs:1208)
Unity.Netcode.NetworkSpawnManager:NonAuthorityLocalSpawn(NetworkObject, SerializedObject&, Boolean) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Spawning/NetworkSpawnManager.cs:1129)
Unity.Netcode.NetworkObject:Deserialize(SerializedObject&, FastBufferReader, NetworkManager, Boolean) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkObject.cs:3335)
Unity.Netcode.SceneEventData:SynchronizeSceneNetworkObjects(NetworkManager) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/SceneEventData.cs:1132)
Unity.Netcode.NetworkSceneManager:HandleClientSceneEvent(UInt32) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2329)
Unity.Netcode.NetworkSceneManager:ClientLoadedSynchronization(UInt32) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2224)
Unity.Netcode.NetworkSceneManager:OnClientBeginSync(UInt32) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2155)
Unity.Netcode.NetworkSceneManager:HandleClientSceneEvent(UInt32) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2311)
Unity.Netcode.NetworkSceneManager:HandleSceneEvent(UInt64, FastBufferReader) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/SceneManagement/NetworkSceneManager.cs:2656)
Unity.Netcode.SceneEventMessage:Handle(NetworkContext&) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/Messages/SceneEventMessage.cs:29)
Unity.Netcode.NetworkMessageManager:ReceiveMessage(FastBufferReader, NetworkContext&, NetworkMessageManager) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:568)
Unity.Netcode.NetworkMessageManager:HandleMessage(NetworkMessageHeader&, FastBufferReader, UInt64, Single, Int32) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:422)
Unity.Netcode.NetworkMessageManager:ProcessIncomingMessageQueue() (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Messaging/NetworkMessageManager.cs:448)
Unity.Netcode.NetworkManager:NetworkUpdate(NetworkUpdateStage) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkManager.cs:349)
Unity.Netcode.NetworkUpdateLoop:RunNetworkUpdateStage(NetworkUpdateStage) (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkUpdateLoop.cs:191)
Unity.Netcode.<>c:<CreateLoopSystem>b__0_0() (at ./Library/PackageCache/com.unity.netcode.gameobjects@c690afa8ab6e/Runtime/Core/NetworkUpdateLoop.cs:214)
### Environment
OS: [Windows]
Unity Version: [e.g. 6000.2.3f1]
Netcode Version: [2.10.0 ]
Netcode Commit: [e.g. https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/commit/ba418fa5b600ad9eb61fab0575f12fbecc2c6520]
Netcode Topology: [Default Unity Transport, ]
### Additional Context
<img width="1489" height="232" alt="Image" src="https://github.com/user-attachments/assets/7a495419-1bec-4365-a0d2-d2f14b54c993" />
<img width="1492" height="222" alt="Image" src="https://github.com/user-attachments/assets/ae22c1ea-460a-4a9b-b402-78d3074b16ab" />


---

<!-- source=github_issue; title=Create a new Resource (resx) file an error occurs; url=https://github.com/dotnet/project-system/issues/1409 -->

# Create a new Resource (resx) file an error occurs

- Source: github_issue
- URL: https://github.com/dotnet/project-system/issues/1409

This bug is created from customer feedback https://developercommunity.visualstudio.com/content/problem/15297/when-creating-new-resource-resx-file-error-occurs.html
When I create a new Resource file, I get following error: "Custom tool ResXFileCodeGenerator failed to produce an output for input file ... but did not log a specific error.". Project is ASP.NET Core on .NET Framework


---

<!-- source=github_issue; title=ARSessionOrigin has no member Raycast; url=https://github.com/TheUnityWorkbench/tuw-arfoundation-demo/issues/1 -->

# ARSessionOrigin has no member Raycast

- Source: github_issue
- URL: https://github.com/TheUnityWorkbench/tuw-arfoundation-demo/issues/1

I followed your tutorial on YouTube. Using unity 2018.3 everything works like a charm. Trying on 2019.2 I get the error that ARSessionOrigin does not contain a definition for Raycast.
So far I couldn't find a reference to raycasting in the documentation.
Any hint?


---

<!-- source=github_issue; title=What should I do when the openbve.exe file is missing?; url=https://github.com/leezer3/OpenBVE/issues/524 -->

# What should I do when the openbve.exe file is missing?

- Source: github_issue
- URL: https://github.com/leezer3/OpenBVE/issues/524

### Description
Please describe the issue you are experiencing.
### Reproduction
If the issue occurs in multiple routes/ trains, please provide one or two samples.
In order to reproduce the issue and debug it, it's helpful to have the following:
## Route
Please provide a link to where the route may be downloaded.
## Train
Please provide a link to the train may be downloaded.
## Logs
Logs may be accessed through the 'Report Problem' button on the bottom left of the screen.
Please provide a log, and a crash-log if the game actually crashes.
### Related information
* Operating system
* Method of control (Keyboard, joystick, RailDriver)
This is what it looks like when you build it.
Severity Code Description Project File Line Non-Display Status
Warning Unable to find referenced component 'System.Drawing'. Route.CsvRw
Error CS0246 'CSScriptLibrary' format or namespace name not found. Check if there is a using directive or assembly reference. OpenBveApi E:\OpenBVE-master\OpenBVE-master\source\OpenBveApi\ObjectTypes\AnimatedObject.cs 3 Active
Error CS0246 'SharpCompress' format or namespace name not found. Check if there is a using directive or assembly reference. OpenBveApi E:\OpenBVE-master\OpenBVE-master\source\OpenBveApi\Packages\Packages.cs 9 Active
Error CS0246 'SharpCompress' format or namespace name not found. Check if there is a using directive or assembly reference. OpenBveApi E:\OpenBVE-master\OpenBVE-master\source\OpenBveApi\Packages\Packages.cs 10 Active
Error CS0246 'SharpCompress' format or namespace name not found. Check if there is a using directive or assembly reference. OpenBveApi E:\OpenBVE-master\OpenBVE-master\source\OpenBveApi\Packages\Packages.cs 11 Active
Error CS0246 'SharpCompress' format or namespace name not found. Check if there is a using directive or assembly reference. OpenBveApi E:\OpenBVE-master\OpenBVE-master\source\OpenBveApi\Packages\Packages.cs 12 Active
Error CS0246 'ValueTuple<,>' format or namespace name not found. Check if there is a using directive or assembly reference. OpenBveApi E:\OpenBVE-master\OpenBVE-master\source\OpenBveApi\System\Hosts.cs 465 Active
Error CS0246 'Ude' format or namespace name not found. Check if there is a using directive or assembly reference. OpenBveApi E:\OpenBVE-master\OpenBVE-master\source\OpenBveApi\System\TextEncoding.cs 2 Active
Error "GetReferenceNearestTargetFrameworkTask" operation not found. Check out the following: 1) Verify that the job name in the project file is the same as the job class name. 2.) Ensure that the task class is "public" and implements the Microsoft.Build.Framework.ITask interface. 3) * in the project file or in the directory "C:\Program Files (x86)\Microsoft Visual Studio\2017\Commonity\MSBuild\15.0\Bin".Use <UsingTask> in the tasks file to verify that the job is declared correctly. AssimpParser
Error "GetReferenceNearestTargetFrameworkTask" operation not found. Check out the following: 1) Verify that the job name in the project file is the same as the job class name. 2.) Ensure that the task class is "public" and implements the Microsoft.Build.Framework.ITask interface. 3) * in the project file or in the directory "C:\Program Files (x86)\Microsoft Visual Studio\2017\Commonity\MSBuild\15.0\Bin".Use <UsingTask> in the tasks file to verify that the job is declared correctly. LibRender2
Error "GetReferenceNearestTargetFrameworkTask" operation not found. Check out the following: 1) Verify that the job name in the project file is the same as the job class name. 2.) Ensure that the task class is "public" and implements the Microsoft.Build.Framework.ITask interface. 3) * in the project file or in the directory "C:\Program Files (x86)\Microsoft Visual Studio\2017\Commonity\MSBuild\15.0\Bin".Use <UsingTask> in the tasks file to verify that the job is declared correctly. SoundManager
Error "GetReferenceNearestTargetFrameworkTask" operation not found. Check out the following: 1) Verify that the job name in the project file is the same as the job class name. 2.) Ensure that the task class is "public" and implements the Microsoft.Build.Framework.ITask interface. 3) * in the project file or in the directory "C:\Program Files (x86)\Microsoft Visual Studio\2017\Commonity\MSBuild\15.0\Bin".Use <UsingTask> in the tasks file to verify that the job is declared correctly. Object.Animated
Error "GetReferenceNearestTargetFrameworkTask" operation not found. Check out the following: 1) Verify that the job name in the project file is the same as the job class name. 2.) Ensure that the task class is "public" and implements the Microsoft.Build.Framework.ITask interface. 3) * in the project file or in the directory "C:\Program Files (x86)\Microsoft Visual Studio\2017\Commonity\MSBuild\15.0\Bin".Use <UsingTask> in the tasks file to verify that the job is declared correctly. Object.CsvB3d
Error "GetReferenceNearestTargetFrameworkTask" operation not found. Check out the following: 1) Verify that the job name in the project file is the same as the job class name. 2.) Ensure that the task class is "public" and implements the Microsoft.Build.Framework.ITask interface. 3) * in the project file or in the directory "C:\Program Files (x86)\Microsoft Visual Studio\2017\Commonity\MSBuild\15.0\Bin".Use <UsingTask> in the tasks file to verify that the job is declared correctly. Object.DirectX
Error "GetReferenceNearestTargetFrameworkTask" operation not found. Check out the following: 1) Verify that the job name in the project file is the same as the job class name. 2.) Ensure that the task class is "public" and implements the Microsoft.Build.Framework.ITask interface. 3) * in the project file or in the directory "C:\Program Files (x86)\Microsoft Visual Studio\2017\Commonity\MSBuild\15.0\Bin".Use <UsingTask> in the tasks file to verify that the job is declared correctly. Object.LokSim
Error "GetReferenceNearestTargetFrameworkTask" operation not found. Check out the following: 1) Verify that the job name in the project file is the same as the job class name. 2.) Ensure that the task class is "public" and implements the Microsoft.Build.Framework.ITask interface. 3) * in the project file or in the directory "C:\Program Files (x86)\Microsoft Visual Studio\2017\Commonity\MSBuild\15.0\Bin".Use <UsingTask> in the tasks file to verify that the job is declared correctly. Object.Msts
Error "GetReferenceNearestTargetFrameworkTask" operation not found. Check out the following: 1) Verify that the job name in the project file is the same as the job class name. 2.) Ensure that the task class is "public" and implements the Microsoft.Build.Framework.ITask interface. 3) * in the project file or in the directory "C:\Program Files (x86)\Microsoft Visual Studio\2017\Commonity\MSBuild\15.0\Bin".Use <UsingTask> in the tasks file to verify that the job is declared correctly. Object.Wavefront
Error "GetReferenceNearestTargetFrameworkTask" operation not found. Check out the following: 1) Verify that the job name in the project file is the same as the job class name. 2.) Ensure that the task class is "public" and implements the Microsoft.Build.Framework.ITask interface. 3) * in the project file or in the directory "C:\Program Files (x86)\Microsoft Visual Studio\2017\Commonity\MSBuild\15.0\Bin".Use <UsingTask> in the tasks file to verify that the job is declared correctly.


---

<!-- source=github_issue; title=Add and Get Struct is bug; url=https://github.com/alec1o/Byter/issues/28 -->

# Add and Get Struct is bug

- Source: github_issue
- URL: https://github.com/alec1o/Byter/issues/28

I try to send struct with byter but error, the data is null. Tks
```cs
private void Start()
{
// set data
Primitive primitive = new();
var a = new ServerResponse() { typeResponse = TypeResponse.WebSocketConnectSucces, message = "xxx1" };
primitive.Add.Struct(a);
// get data
byte[] buffer = primitive.GetBytes();
var message = Encoding.UTF8.GetString(buffer);
Debug.Log(message);
}
```


---

<!-- source=github_issue; title=[BUG] - Knarr cannot resolve YML when installed through R2/Thunderstore; url=https://github.com/sbtoonz/Trader_2.0/issues/18 -->

# [BUG] - Knarr cannot resolve YML when installed through R2/Thunderstore

- Source: github_issue
- URL: https://github.com/sbtoonz/Trader_2.0/issues/18

Continuing from the discord thread: https://discord.com/channels/252172638670028803/1087170976401338468
Updated server and client to 0.4.1 but still not able to get anything to show up in Knarrs buy/sell window (see screenshot)
![image](https://user-images.githubusercontent.com/23404043/227385342-7906b975-eb66-4528-9d1d-ec4ee7578d91.png)
No errors or relevant information in the log file.
Installed client mods (server has only what's needed, the client-only mods are removed):
Dependency string list
denikson-BepInExPack_Valheim-5.4.2100
Smoothbrain-Jewelcrafting-1.4.6
Smoothbrain-CreatureLevelAndLootControl-4.5.5
Smoothbrain-InstantEquip-1.0.5
Smoothbrain-Cooking-1.1.11
Smoothbrain-Resurrection-1.0.5
Smoothbrain-Blacksmithing-1.2.2
Smoothbrain-PassivePowers-1.0.9
Smoothbrain-Farming-2.1.8
Smoothbrain-SteadyRegeneration-1.0.1
Smoothbrain-Tenacity-1.0.2
Smoothbrain-Evasion-1.0.2
Smoothbrain-Vitality-1.1.0
Smoothbrain-StaminaRegenerationFromFood-1.5.3
Smoothbrain-PackHorse-1.0.2
Smoothbrain-Building-1.2.4
Smoothbrain-Lumberjacking-1.0.3
Smoothbrain-Ranching-1.1.1
Smoothbrain-Mining-1.1.3
Smoothbrain-Sailing-1.1.5
Smoothbrain-SmoothSave-1.0.0
Smoothbrain-DisableCameraPanning-1.0.0
hyleanlegend-Rune_Magic-1.1.17
Azumatt-Official_BepInEx_ConfigurationManager-18.0.0
Atopy-QuickPing-1.5.7
Advize-PlantEverything-1.13.3
Azumatt-AzuAreaRepair-1.0.1
aedenthorn_nexus-ShowContainerContents-0.3.0
ValheimModding-Jotunn-2.11.0
MSchmoecker-PressurePlate-0.8.1
ComfyMods-LicenseToSkill-1.1.1
MathiasDecrock-Snap_Points_Made_Easy-1.3.2
digitiliad-NotificationTweaks-0.3.2
Azumatt-Build_Camera_Custom_Hammers_Edition-1.1.3
coemt-Belts-1.0.6
ComfyMods-Gizmo-1.5.1
digitiliad-HotbarSwitch-0.1.1
RandyKnapp-MinimalStatusEffects-1.0.3
Korppis-SolidHitboxes-1.0.4
Goldenrevolver-Instantly_Destroy_Boats_And_Carts-1.0.3
WackyMole-WackysDatabase-1.4.2
JereKuusela-Projectile_Collision-1.2.0
JereKuusela-Smoke_Collision-1.5.0
Fragnarok-ImmersiveCompass-1.1.2
Azumatt-DeezMistyBalls-1.0.1
HugotheDwarf-More_and_Modified_Player_Cloth_Colliders-3.1.0
Smoothbrain-Foraging-1.0.3
pipakin-SkillInjector-1.1.1
urgemeuwu-Wagon_Skill-1.0.0
Azumatt-AzuWorkbenchTweaks-1.0.1
Azumatt-ImFRIENDLY_DAMMIT-1.0.8
Digitalroot-Max_Dungeon_Rooms-2.0.9
blacks7ar-SNEAKer-1.0.7
We_Haul-Zero_Cost_Sneaking-1.0.0
Smoothbrain-Groups-1.1.15
Smoothbrain-Network-1.0.1
JereKuusela-Server_devcommands-1.44.0
JereKuusela-Upgrade_World-1.34.0
blacks7ar-BowPlugin-1.3.9
JustMennowar-BeehiveUtils_Revived-1.0.2
aedenthorn_nexus-AutoFeed-0.7.0
blacks7ar-MagicPlugin-1.3.1
NoPetRides-NoPetRides_ModUtils-1.0.0
NoPetRides-CropUtils-1.2.1
RandyKnapp-AdvancedPortals-1.0.3
Smoothbrain-TargetPortal-1.1.6
Therzie-Warfare-1.3.9
Azumatt-AzuAutoStore-1.0.2
MSchmoecker-MultiUserChest-0.4.3
KGvalheim-Soulcatcher_JC_KG_Additions-4.4.1
PhantomGamers-PreventAccidentalInteraction-1.0.9
Azumatt-AzuClock-1.0.0
Azumatt-MagicEitrBase-1.1.3
nearbear-CustomSlotItemLib-1.0.4
nearbear-WishboneSlot-1.0.3
GemHunter1-FastTeleport-1.1.0
Crystal-Pathfinder-2.0.7
blacks7ar-VikingsDoSwim-1.1.4
Rabid_Wolf_Studios-Climbing-1.0.5
Tequila-Dvergr_Pieces-2.0.1
BentoG-MissingPieces-2.0.1
VentureValheim-No_Seasonal_Restrictions-0.1.5
RoundStone-RoundStoneScrollFirstPerson-1.0.0
Azumatt-Recipe_Description_Expansion-1.0.0
MadBuffoon-WeightBase-1.1.0
Goldenrevolver-Sorted_Menus_Cooking_Crafting_and_Skills_Menu-1.2.2
ComfyMods-SearsCatalog-1.2.0
Azumatt-AzuExtendedPlayerInventory-1.0.4
MSchmoecker-HammerTime-0.3.3
TrisTris-LocateEverything-1.0.2
OdinPlus-OdinCampsite-1.5.0
ASharpPen-Drop_That-2.3.5
aedenthorn_mods-InstantMonsterLootDrop-0.5.0
Azumatt-ResourceUnloadOptimizer-1.0.1
blacks7ar-SapExtractor-1.0.5
Azumatt-RunningStaminaBase-1.0.2
OdinPlus-TeleportEverything-2.3.1
Therzie-Monstrum-1.0.5
JereKuusela-Item_Stand_All_Items-1.17.0
zamboni-Gungnir-1.7.1
Neobotics-WolfPack-1.0.2
JereKuusela-Server_Sync_Fix-1.2.0
RobinHood-Candles_LanternsANDbeeswaxx_02050-0.0.1
TastyChickenLegs-BedRules-1.0.1
Vystyk-ValheimDefenders-0.2.4
TastyChickenLegs-TimedTorchesStayLit-1.3.2
TastyChickenLegs-AutomaticFuel-1.3.5
TastyChickenLegs-RecyclePlus-1.2.2
JereKuusela-Render_Limits-1.5.0
JereKuusela-Ruler-1.2.0
JustMennowar-LuckyBranches-1.0.2
OdinPlus-OdinsHorsePen-1.0.4
Meldurson-AllTameableTamingOverhaul-1.1.3
cdymrtn-BuildRestrictionTweaks-0.3.0
OdinPlus-CraftyCartsRemake-3.0.8
MSchmoecker-FenceSnap-0.2.0
MrSerji-Construction-0.2.5
OdinPlus-OdinArchitect-1.2.7
ValheimModding-HookGenPatcher-0.0.3
MathiasDecrock-SeedTotem-4.2.1
OdinPlus-CrystalLights-1.0.7
MSchmoecker-VNEI-0.10.0
blacks7ar-FoodEitrRegen-1.0.1
blacks7ar-CombatOverhaulREwrite-1.0.8
Laudriel_Mods-LeviathanNeverGoesAway-0.0.1
Azumatt-NoHoeDust-1.0.3
Azumatt-NoCultivatorDust-1.0.3
Azumatt-NoBuildDust-1.0.3
TastyChickenLegs-TreesReborn-1.0.2
ComfyMods-Pinnacle-1.2.3
OdinPlus-GoodestBoy-0.1.6
FixItFelix-GrassTweaks_By_Aedenthorn-0.2.0
Nonnnnne-Panocs_HD_Map-1.0.0
KibCorgi-CustomGraphicsSettingsByAedenthorn-0.7.1
MerryValheimMods-NoStumps-1.0.0
Korppis-Spearfishing-1.0.1
Azumatt-Minimal_UI-2.1.9
Marf-FuelEternal-1.2.0
ASharpPen-Fall_Damage_For_Creatures-1.1.0
Pfhoenix-Fartheim-1.2.0
Pfhoenix-ODINFLIGHT-1.3.0
Digitalroot-Heightmap_Unlimited_Remake-1.3.6
Azumatt-AzuHoverStats-1.0.6
ComfyMods-Enhuddlement-1.1.0
Azumatt-WardIsLove-3.0.9
Goldenrevolver-Teleport_Instantly_Updates_Weather_And_Removes_Wet_Debuff-1.0.1
GoldenJude-WeatherStones-0.1.2
Balrond-balrond_shipyard-1.1.5
Azumatt-Where_You_At-1.0.7
OdinPlus-PlantIt-0.1.5
Azumatt-AzuContainerSizes-1.0.1
Thordomr-More_Gates-1.0.10
OdinPlus-OdinsTraps-1.1.8
Azumatt-GiveEmTheBoot-1.0.1
ComfyMods-Chatter-1.4.1
blacks7ar-WeaponHolsterOverhaul-1.0.5
Enta-MuchBetterHotkeys-1.1.0
OdinPlus-KnarrTheTrader-0.4.1
Azumatt-FastLink-1.3.5
Goldenrevolver-Obtainable_Stone_Pickaxe_and_Upgradeable_Antler_Pickaxe-1.0.0
Desires-MoreUpgrades-1.0.0
Vapok-AdventureBackpacks-1.6.15
LVH-IT-UseEquipmentInWater-0.2.3
Therzie-Armory-1.0.3
cazou-QuickerStack-0.0.5
Azumatt-Third_Eye-2.0.3
aedenthorn-Craft From Containers-3.1.2
williammetcalf-Useful Armor Stands-1.0.4
makail-ItemDrawers-0.5.0


---

<!-- source=github_issue; title=serial port trouble with .NET 3.5 in Unity; url=https://github.com/PyramidTechnologies/netPyramid-RS-232/issues/1 -->

# serial port trouble with .NET 3.5 in Unity

- Source: github_issue
- URL: https://github.com/PyramidTechnologies/netPyramid-RS-232/issues/1

I removed System.Threading.Tasks and set it to .NET 3.5 and it compiled the dll without any errors. I then took the code from MainWindow.xaml.cs and put it into Unity 5.1. The LED comes on for about 3 seconds and then go out and I see this error come up.
NullReferenceException: Object reference not set to an instance of an object
System.IO.Ports.WinSerialStream.get_BytesToRead ()
System.IO.Ports.SerialPort.get_BytesToRead ()
(wrapper remoting-invoke-with-check) System.IO.Ports.SerialPort:get_BytesToRead ()
Apex7000_BillValidator.ApexValidator.Read ()
Apex7000_BillValidator.ApexValidator.Connect ()
gameManager.Start () (at Assets/gameManager.cs:72)


---

<!-- source=github_issue; title=Update to .Net Core 3.0; url=https://github.com/VirtualPhotonics/VTS/issues/25 -->

# Update to .Net Core 3.0

- Source: github_issue
- URL: https://github.com/VirtualPhotonics/VTS/issues/25

Hi friends!
On [my fork](https://github.com/dcuccia/VTS), main branch, I've updated projects and references to be fully .Net Core 3.0/.Net Standard 2.0 compatible (it's up to date with the main project), and I've verified "dotnet run" for the mc.exe command line app now works out of the box on a vanilla Ubuntu distro (on WSL). This means (theoretically) we shouldn't need Mono, or any Linux-specific work-arounds. Also, between VS Code and VS for Mac, I don't think we should need to support MonoDevelop anymore.
I _almost_ submitted a PR, but held back because there are multiple deployment assets that need to be updated or deleted. Very willing to do more work on this, but wanted to run by you guys. I've set the nuget package to 5.0.0-alpha01 (I don't have permissions to publish), and I've verified that a linux command line project referencing that alpha also works.
Let me know if you'd like to chat about it,
David


---

<!-- source=github_issue; title=NullReferenceException Crashes the build; url=https://github.com/microsoft/MixedRealityToolkit-Unity/issues/1058 -->

# NullReferenceException Crashes the build

- Source: github_issue
- URL: https://github.com/microsoft/MixedRealityToolkit-Unity/issues/1058

Sorry about the weird opening/closing/editing this post.
When I build to Hololens or to PC on the Universal Windows Platform Building setting, both will build fine but then crash when they run. I tried hitting Play on the Unity editor and I get this error:
```
NullReferenceException: Object reference not set to an instance of an object
HoloToolkit.Sharing.Utilities.AutoJoinSessionAndRoom.SessionTrackerDisconnected () (at Assets/HoloToolkit/Sharing/Scripts/Utilities/AutoJoinSessionAndRoom.cs:91)
HoloToolkit.Sharing.Utilities.AutoJoinSessionAndRoom.Start () (at Assets/HoloToolkit/Sharing/Scripts/Utilities/AutoJoinSessionAndRoom.cs:57)
```
Any advice is appreciated.


---

<!-- source=github_issue; title=Engine crashes on stop; url=https://github.com/InitialPrefabs/nimgui/issues/8 -->

# Engine crashes on stop

- Source: github_issue
- URL: https://github.com/InitialPrefabs/nimgui/issues/8

Hey, I unfortunately cannot use your provided package (latest version), using Unity 6 6000.1.8f1 and following all steps for URP.
```
NullReferenceException: Object reference not set to an instance of an object
InitialPrefabs.NimGui.Loop.ImGuiRunner.ScheduleDraw () (at Assets/InitialPrefabs.ImGui/InitialPrefabs.ImGui/Loop/ImGuiRunner.cs:79)
System.InvalidOperationException: AddNoResize assumes that list capacity is sufficient (Capacity 2048, Length 2048), requested length 1!
This Exception was thrown from a job compiled with Burst, which has limited exception support.
0x00007ffa40fe7b9b (Unity) burst_abort
0x00007ffa551776de (d3374a36bb7d4b51a10878b0fb1ba18) burst_Abort_Trampoline
0x00007ffa551772ce (d3374a36bb7d4b51a10878b0fb1ba18) Unity.Collections.NativeList`1<ushort>.AddNoResize
...
```
Those errors show up on start, but the example UI that i've tried out renders properly, on dispose/stop however, the engine completely crashes.
The error line in ImGuiRunner is the following:
`CommandBuffer commandBuffer = pass.DrawCommand;`
Where it doesn't make sense that the pass is null since I have the added the renderer feature properly and the setup wizard doesn't show any errors either. Did i miss something?
---
On a side note, is there a way for this project to get migrated to the new RenderGraph API so you don't have to turn on the compatibility mode?


---

<!-- source=github_issue; title=AndroidJavaProxy breaks with Unity 2022.2.0+ when using fuw-2022.2.0; url=https://github.com/juicycleff/flutter-unity-view-widget/issues/836 -->

# AndroidJavaProxy breaks with Unity 2022.2.0+ when using fuw-2022.2.0

- Source: github_issue
- URL: https://github.com/juicycleff/flutter-unity-view-widget/issues/836

**Describe the bug**
There was a change in Unity 2022.1.7 to 2022.2.0+ in AndroidJNI, which now requires a reference to `mUnityPlayer` when creating an `AndroidJavaProxy`:
```
public static IntPtr CreateJavaProxy (AndroidJavaProxy proxy)
{
GCHandle value = GCHandle.Alloc (proxy);
try {
return _AndroidJNIHelper.CreateJavaProxy (Permission.GetActivity ().Get<AndroidJavaObject> ("mUnityPlayer").GetRawObject (), GCHandle.ToIntPtr (value), proxy);
} catch {
value.Free ();
throw;
}
}
```
Note that `Permissions.GetActivity()` will return the `currentActivity` from a `UnityPlayer` object. When the FlutterUnityWidget is used to launch Unity (see `CustomUnityPlayer.kt`) it will initialise `UnityPlayer` with `MainActivity`. Hence, `CreateJavaProxy` will fail to find a reference to `mUnityPlayer` and log the following error:
```
Non-fatal Exception: java.lang.Exception: AndroidJavaException : java.lang.NoSuchFieldError: no "Ljava/lang/Object;" field "mUnityPlayer" in class "Lcom/example/app/MainActivity;" or its superclasses
at com.unity3d.player.UnityPlayer.nativeRender(com.unity3d.player.UnityPlayer)
at com.unity3d.player.UnityPlayer.-$$Nest$mnativeRender(com.unity3d.player.UnityPlayer)
at com.unity3d.player.UnityPlayer$C$a.handleMessage(com.unity3d.player.UnityPlayer$C$a)
at android.os.Handler.dispatchMessage(android.os.Handler)
at android.os.Looper.loopOnce(android.os.Looper)
at android.os.Looper.loop(android.os.Looper)
at com.unity3d.player.UnityPlayer$C.run(com.unity3d.player.UnityPlayer$C)
at UnityEngine.AndroidJNISafe.CheckException(AndroidJNISafe.cs:24)
at UnityEngine.AndroidJNISafe.GetFieldID(AndroidJNISafe.cs:87)
at UnityEngine._AndroidJNIHelper.GetFieldID(AndroidJava.cs:1614)
at UnityEngine.AndroidJNIHelper.GetFieldID(AndroidJNI.bindings.cs:91)
at UnityEngine._AndroidJNIHelper.GetFieldID[ReturnType](AndroidJava.cs:1534)
at UnityEngine.AndroidJNIHelper.GetFieldID[FieldType](AndroidJNI.bindings.cs:198)
at UnityEngine.AndroidJavaObject._Get[FieldType](AndroidJava.cs:630)
at UnityEngine.AndroidJavaObject.Get[FieldType](AndroidJava.cs:345)
at UnityEngine.AndroidJNIHelper.CreateJavaProxy(AndroidJNI.bindings.cs:106)
```
Many Unity plugins use an `AndroidJavaProxy` interface to callback to C# methods from Java. There are two proposed workarounds to this problem both with caveats:
- Launch Unity in a native process ie. call `openInNativeProcess()` within `onUnityCreated` within your flutter application, as this will use the `OverrideUnityActivity` that does contain a reference for `mUnityPlayer`. However, the FlutterUnityWidget messaging system between Flutter and Unity will break (this is not documented).
- Add `mUnityPlayer` to `MainActivity`. This is difficult if your `MainActivity` is in java as the `UnityPlayerUtils.kt` does not expose the `unityPlayer` variable as a Jvm field.
**To Reproduce**
Steps to reproduce the behavior:
1. Create an empty Unity 2022.2.0 project, consume fuw-2022.2.0
3. add an AndroidJavaProxy to the project
4. initialise the proxy on a Method exposed to Flutter
5. Create an empty Flutter 3.7.12 project, consume FUW 2022.2.0
6. call the Method in Flutter using `sendMessage`
7. run the project and observe
**Expected behavior**
No error logs should be thrown when any Native code in unity attempts to access `mUnityPlayer`. Unity assumes this reference is always available.
**Unity (please complete the following information):**
- Unity: 2022.2.0+
- FUW: 2022.2.0, 2022.3.0-alpha1
- Flutter: 3.7.12
- OS: Android
- Android Version: Any


---

<!-- source=github_issue; title=Omnisharp Update - Unable to find Mono. Ensure that Mono's '/bin' folder is added to your environment's PATH variable.; url=https://github.com/dotnet/vscode-csharp/issues/4489 -->

# Omnisharp Update - Unable to find Mono. Ensure that Mono's '/bin' folder is added to your environment's PATH variable.

- Source: github_issue
- URL: https://github.com/dotnet/vscode-csharp/issues/4489

## Issue Description ##
Visual Studio Code just automatically updated Omnisharp and now I get the error:
Unable to find Mono. Ensure that Mono's '/bin' folder is added to your environment's PATH variable.
A few hours ago it was working without any problem ...
## Logs ##
### OmniSharp log ###
[ERROR] Error: Unable to find Mono. Ensure that Mono's '/bin' folder is added to your environment's PATH variable.
## Environment information ##
**VSCode version**: 1.55.1
**C# Extension**: 1.23.10
<details><summary>Mono Information</summary>
There is a problem with running OmniSharp on mono: Error: Unable to find Mono. Ensure that Mono's '/bin' folder is added to your environment's PATH variable.</details>
<details><summary>Dotnet Information</summary>
.NET SDK (reflecting any global.json):
Version: 5.0.102
Commit: 71365b4d42
Runtime Environment:
OS Name: Mac OS X
OS Version: 11.0
OS Platform: Darwin
RID: osx.11.0-x64
Base Path: /usr/local/share/dotnet/sdk/5.0.102/
Host (useful for support):
Version: 5.0.2
Commit: cb5f173b96
.NET SDKs installed:
3.1.405 [/usr/local/share/dotnet/sdk]
5.0.102 [/usr/local/share/dotnet/sdk]
.NET runtimes installed:
Microsoft.AspNetCore.App 3.1.11 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
Microsoft.AspNetCore.App 5.0.2 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
Microsoft.NETCore.App 3.1.11 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
Microsoft.NETCore.App 5.0.2 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
To install additional .NET runtimes or SDKs:
https://aka.ms/dotnet-download
</details>
<details><summary>Visual Studio Code Extensions</summary>
|Extension|Author|Version|
|---|---|---|
|Angular2|johnpapa|11.0.0|
|azure-account|ms-vscode|0.9.8|
|azure-pipelines|ms-azure-devops|1.183.0|
|csharp|ms-dotnettools|1.23.10|
|docker-explorer|formulahendry|0.1.7|
|jupyter|ms-toolsai|2021.5.702919634|
|markdown-all-in-one|yzhang|3.4.0|
|python|ms-python|2021.3.680753044|
|remote-containers|ms-vscode-remote|0.166.1|
|rest-client|humao|0.24.5|
|typescript-hero|rbbit|3.0.0|
|vscode-docker|ms-azuretools|1.11.0|
|vscode-mjml|mjmlio|1.0.4|
|vscode-todo-highlight|jgclark|2.0.1|
|vscode-yaml|redhat|0.17.0|;
</details>


---

<!-- source=github_issue; title=SendCodeRequest Method Failed; url=https://github.com/sochix/TLSharp/issues/17 -->

# SendCodeRequest Method Failed

- Source: github_issue
- URL: https://github.com/sochix/TLSharp/issues/17

Hi, Ilya. Thank you for the great work.
AuthUser test has failed because SendCodeRequest method thrown a exception in mscorlib.dll and i can't receive SMS code to my phone number. I try 0,1 and 5 value in sms_type parameter.
TestConnection and AutheficationWorks works fine.
Visual Studio 2015 Community, Win7 32-bit
Regards, Egor


---

<!-- source=github_issue; title=Releases?; url=https://github.com/HelloKitty/RS317.Sharp/issues/7 -->

# Releases?

- Source: github_issue
- URL: https://github.com/HelloKitty/RS317.Sharp/issues/7

Are you planning to publish builds using GitHub's releases feature?
I'm not having access to my development machine right now as I'm away with just my pleb laptop, but I was curious to check out this project and see what it's capable of.
If you do, please include builds for linux/linux-x64 and linux-arm/linux-arm64 , if it is compatible with those.


---

<!-- source=github_issue; title=Beta Testing: X360CE 4.8.x.x Alpha; url=https://github.com/x360ce/x360ce/issues/818 -->

# Beta Testing: X360CE 4.8.x.x Alpha

- Source: github_issue
- URL: https://github.com/x360ce/x360ce/issues/818

This issue is for reporting bugs found in Beta Testing: X360CE 4.8.x.x Alpha.
This release contains better exception logging. Removed more old GDB/INI/DLL code. Start with Windows and support for Profiles added. Rest of the focus was on cloud database and multiple profiles support. Default build is AnyCPU now (one x360ce.exe for 32-bit and 64-bit OS). Exclusive 32-bit and 64-bit are still available and I can supply them in the future if there will be problems with MSIL (AnyCPU) builds. Other fixes are listed on release page.
Alpha is intended to test Virtual Emulation. Download links and instructions can be found here:
https://github.com/x360ce/x360ce/blob/master/Wiki/BetaTesting.md
More details about last release here:
https://github.com/x360ce/x360ce/releases


---

<!-- source=github_issue; title=The sample app crashes on Samsung 22 Ultra; url=https://github.com/homuler/MediaPipeUnityPlugin/issues/821 -->

# The sample app crashes on Samsung 22 Ultra

- Source: github_issue
- URL: https://github.com/homuler/MediaPipeUnityPlugin/issues/821

### Plugin Version or Commit ID
0.10.1
### Unity Version
2021.3.3f1
### Your Host OS
Windows
### Target Platform
Windows Standalone
### Description
I am trying to build sample scenes on Windows. I am using pre-compiled version.
Imported to my project via Packet Manager - Import Folder.
It didn't import Samples so I have copied them manually from the GitHub (In the pre-compiled package there was no Start Scene).
I started Start Scene in Unity but there was exception `(...)/AppData/LocalLow/DefaultCompany/TestMediapipe\pose_detection.bytes is not found`. When I copied all .bytes files to that folder it started working. My question is how can I ensure that it works without copying to this folder and is part of compilation?
Also I want to ask how can I ensure that on Android and iOS cause I have compiled also Android version some time ago and it just show me camera. I am assuming the problem was similar.
Thanks for your help.
### Code to Reproduce the issue
_No response_
### Additional Context
_No response_


---

<!-- source=github_issue; title=Assembly-CSharp.dll breaks game. Update Folder breaks game; url=https://github.com/07th-mod/watanagashi/issues/66 -->

# Assembly-CSharp.dll breaks game. Update Folder breaks game

- Source: github_issue
- URL: https://github.com/07th-mod/watanagashi/issues/66

Windows 8 Machine
Followed every step in the Install Instructions TO THE LETTER on a fresh install of the game. Created voice folder, moved voices into it, moved all appropriate cg and cgalt folders, installed streaming assets update patch, installed everything according to the instructions in your guide with no liberties taken and it breaks the game to the level of not even turning on anymore, when running the .exe it won't even start the game anymore.
I narrowed it down to a file in the "managed" folder called Assembly-CSharp.dll which if you overwrite it with your patched version the game won't even start, but even if you don't transfer that file what happens is the game will load a black screen and never do anything. Then pressing alt+f4 will show the "are you sure" dialogue box and exit.
So basically if you install any of the files in the update folder or the "Managed" folder it completely breaks the game. I successfully moved all cg and voices into the folder and it does not break the game, but when installing the scripts in the update folder this is when the problem happens. Yet no one online has talked about this and the only way I even got the Onikakushi chapter to work properly is by using someone else's streaming assets folder.
Is there any way you can please upload your complete patched streaming assets folder to google drive or megaupload? Because seriously I have literally tried 50 different methods with no results other than a black screen.


---

<!-- source=github_issue; title=Users crashing when world is closed while using Steam Sockets; url=https://github.com/Yellow-Dog-Man/Resonite-Issues/issues/6216 -->

# Users crashing when world is closed while using Steam Sockets

- Source: github_issue
- URL: https://github.com/Yellow-Dog-Man/Resonite-Issues/issues/6216

### Describe the bug?
Was in an instance with a bunch of users/friends and the world crashed when I closed down the world for us to go back into another instance that we were in previously.
### To Reproduce
Host world 1 and enter world 2 then close world 2 and have users come back to world 1.
### Reproduction Item/World
https://api.resonite.com/open/world/U-1jyAhmMP0yW/R-73771a4f-e4d7-409d-8664-11bbbc670fb2
### Expected behavior
To close down worlds without crashing
### Screenshots
_No response_
### Resonite Version Number
Beta 2026.1.28.1247
### What Platforms does this occur on?
Windows
### What headset if any do you use?
_No response_
### Log Files
[CRIMSONFOX - 2026.1.28.1247 - 2026-02-02 21_28_11.log](https://github.com/user-attachments/files/25034077/CRIMSONFOX.-.2026.1.28.1247.-.2026-02-02.21_28_11.log)
### Additional Context
_No response_
### Reporters
Nexulan, Sharkmare "Flux" / Eldritchkaiju


---

<!-- source=github_issue; title=RegsiterAssembly("{executingAssembly"}) fails the first time when a custom composition root is used.; url=https://github.com/seesharper/LightInject/issues/59 -->

# RegsiterAssembly("{executingAssembly"}) fails the first time when a custom composition root is used.

- Source: github_issue
- URL: https://github.com/seesharper/LightInject/issues/59

RegisterAssembly(Assembly.GetExecutingAssembly());
-> The above calls doesn't scan the assembly the first time its called. However it scan if the same call is repeated again.
This is an issue only with the current assembly, when called explicitly. If it is by design, its seems quite misleading.


---

<!-- source=github_issue; title=Get binding as a friendly user string; url=https://github.com/ValveSoftware/openvr/issues/1017 -->

# Get binding as a friendly user string

- Source: github_issue
- URL: https://github.com/ValveSoftware/openvr/issues/1017

I'm looking into making our tutorial work with the new API, after looking into https://github.com/ValveSoftware/steamvr_unity_plugin/issues/167 i fixed so the `GetDeviceComponentName` method returned what it should. I guess **scroll_wheel** is just a bug and it Should return **touchpad**.
Lets say action **Release magazine** is bound to D Pad North. Then a text saying Touchpad wont do. Maybe you guys can add a method, `GetUserFriendlyDescription` which will return something like 'D Pad North' but maybe thats not enough, maybe it even needs to return "Touch D Pad North" or "Click D Pad North",
edit: This is a fork from https://github.com/ValveSoftware/steamvr_unity_plugin/issues/165


---

<!-- source=github_issue; title=UPDATE_APP_TO_LOGIN; url=https://github.com/egramtel/tdsharp/issues/94 -->

# UPDATE_APP_TO_LOGIN

- Source: github_issue
- URL: https://github.com/egramtel/tdsharp/issues/94

Login prompt Error UPDATE_APP_TO_LOGIN
Related comments:
Sorry, it is unclear what you are asking. Could you please elaborate?
Can I speak Chinese？
前几天程序调用 tdsharp 正常，今天突然登录的时候报错了，Telegram 提示错误：UPDATE_APP_TO_LOGIN。这个错误是不是因为要升级 TDLib 的版本过低，需要升级自后才能使用？
调用代码：
mTdClient.SetAuthenticationPhoneNumberAsync(AppConfig.LoginConfig.PhoneNumber).ContinueWith(delegate (Task<TdApi.Ok> result)
{
if (result.Exception != null)
{
//这里异常 UPDATE_APP_TO_LOGIN
}
});
@ForNeVeR
The Telegram team disabled login functionality for all libraries what use outdated tdlib versions.
Currently it is not possible to invoke `TdApi.SetAuthenticationPhoneNumber` request without updating to tdlib 1.7.9. https://github.com/tdlib/td/issues/1758.
Any chance to get it works soon? Update TDLib.Native nuget package, etc. ?


---

<!-- source=github_issue; title=Issues using the keyboard prefab on PC; url=https://github.com/microsoft/MixedRealityToolkit-Unity/issues/1370 -->

# Issues using the keyboard prefab on PC

- Source: github_issue
- URL: https://github.com/microsoft/MixedRealityToolkit-Unity/issues/1370

## Overview
When using a uGUI text field and the virtual keyboard prefab on PC, both the virtual keyboard and OS keyboard shows up in the application.
HoloLens is unaffected.
## Expected Behavior
A single keyboard
## Actual Behavior
OS and keyboard prefab shows up
## Steps to reproduce
- Open keyboard test scene
- Play in editor
- Attempt to write in text field
## Unity Editor Version
2017.2.0p1 MRTP4
## Mixed Reality Toolkit Release Version
db59a1c7fa0c0c463466028c5f3e70088bbfda52


---

<!-- source=github_issue; title=BUG?!; url=https://github.com/suriyun-production/mmorpg-kit-docs/issues/964 -->

# BUG?!

- Source: github_issue
- URL: https://github.com/suriyun-production/mmorpg-kit-docs/issues/964

1.65d . After starting the server starts to restart constantly. I only changed the character models. But it restarts even if you do not enter the game. Logs:
[log.zip](https://github.com/suriyun-production/mmorpg-kit-docs/files/6487402/log.zip)


---

<!-- source=github_issue; title=Crash on F5; url=https://github.com/unitycontainer/microsoft-dependency-injection/issues/40 -->

# Crash on F5

- Source: github_issue
- URL: https://github.com/unitycontainer/microsoft-dependency-injection/issues/40

Hello!
After fixing issue #38 or #39 I run example ASP.Net.Core.Unity.Example.
It's started! But if I trying reload page I got exception:
An unhandled exception occurred while processing the request.
InvalidOperationException: No service for type 'Microsoft.AspNetCore.Routing.IEndpointAddressScheme`1[Microsoft.AspNetCore.Routing.RouteValuesAddress]' has been registered.
Microsoft.Extensions.DependencyInjection.ServiceProviderServiceExtensions.GetRequiredService(IServiceProvider provider, Type serviceType)
Stack Query Cookies Headers
InvalidOperationException: No service for type 'Microsoft.AspNetCore.Routing.IEndpointAddressScheme`1[Microsoft.AspNetCore.Routing.RouteValuesAddress]' has been registered.
Microsoft.Extensions.DependencyInjection.ServiceProviderServiceExtensions.GetRequiredService(IServiceProvider provider, Type serviceType)
Microsoft.Extensions.DependencyInjection.ServiceProviderServiceExtensions.GetRequiredService<T>(IServiceProvider provider)
Microsoft.AspNetCore.Routing.DefaultLinkGenerator.GetEndpoints<TAddress>(TAddress address)
Microsoft.AspNetCore.Routing.DefaultLinkGenerator.GetPathByAddress<TAddress>(HttpContext httpContext, TAddress address, RouteValueDictionary values, RouteValueDictionary ambientValues, Nullable<PathString> pathBase, FragmentString fragment, LinkOptions options)
Microsoft.AspNetCore.Routing.LinkGeneratorRouteValuesAddressExtensions.GetPathByRouteValues(LinkGenerator generator, HttpContext httpContext, string routeName, object values, Nullable<PathString> pathBase, FragmentString fragment, LinkOptions options)
Microsoft.AspNetCore.Mvc.Routing.EndpointRoutingUrlHelper.Action(UrlActionContext urlActionContext)
Microsoft.AspNetCore.Mvc.UrlHelperExtensions.Action(IUrlHelper helper, string action, string controller, object values, string protocol, string host, string fragment)
Microsoft.AspNetCore.Mvc.ViewFeatures.DefaultHtmlGenerator.GenerateActionLink(ViewContext viewContext, string linkText, string actionName, string controllerName, string protocol, string hostname, string fragment, object routeValues, object htmlAttributes)
Microsoft.AspNetCore.Mvc.TagHelpers.AnchorTagHelper.Process(TagHelperContext context, TagHelperOutput output)
Microsoft.AspNetCore.Razor.TagHelpers.TagHelper.ProcessAsync(TagHelperContext context, TagHelperOutput output)
Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner.RunAsync(TagHelperExecutionContext executionContext)
AspNetCore.Views_Shared__Layout.<ExecuteAsync>b__44_1()
Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperExecutionContext.SetOutputContentAsync()
AspNetCore.Views_Shared__Layout.ExecuteAsync()
Microsoft.AspNetCore.Mvc.Razor.RazorView.RenderPageCoreAsync(IRazorPage page, ViewContext context)
Microsoft.AspNetCore.Mvc.Razor.RazorView.RenderPageAsync(IRazorPage page, ViewContext context, bool invokeViewStarts)
Microsoft.AspNetCore.Mvc.Razor.RazorView.RenderLayoutAsync(ViewContext context, ViewBufferTextWriter bodyWriter)
Microsoft.AspNetCore.Mvc.Razor.RazorView.RenderAsync(ViewContext context)
Microsoft.AspNetCore.Mvc.ViewFeatures.ViewExecutor.ExecuteAsync(ViewContext viewContext, string contentType, Nullable<int> statusCode)
Microsoft.AspNetCore.Mvc.ViewFeatures.ViewExecutor.ExecuteAsync(ActionContext actionContext, IView view, ViewDataDictionary viewData, ITempDataDictionary tempData, string contentType, Nullable<int> statusCode)
Microsoft.AspNetCore.Mvc.ViewFeatures.ViewResultExecutor.ExecuteAsync(ActionContext context, ViewResult result)
Microsoft.AspNetCore.Mvc.ViewResult.ExecuteResultAsync(ActionContext context)
Microsoft.AspNetCore.Mvc.Internal.ResourceInvoker.InvokeResultAsync(IActionResult result)
Microsoft.AspNetCore.Mvc.Internal.ResourceInvoker.InvokeNextResultFilterAsync<TFilter, TFilterAsync>()
Microsoft.AspNetCore.Mvc.Internal.ResourceInvoker.Rethrow(ResultExecutedContext context)
Microsoft.AspNetCore.Mvc.Internal.ResourceInvoker.ResultNext<TFilter, TFilterAsync>(ref State next, ref Scope scope, ref object state, ref bool isCompleted)
Microsoft.AspNetCore.Mvc.Internal.ResourceInvoker.InvokeResultFilters()
Microsoft.AspNetCore.Mvc.Internal.ResourceInvoker.InvokeNextResourceFilter()
Microsoft.AspNetCore.Mvc.Internal.ResourceInvoker.Rethrow(ResourceExecutedContext context)
Microsoft.AspNetCore.Mvc.Internal.ResourceInvoker.Next(ref State next, ref Scope scope, ref object state, ref bool isCompleted)
Microsoft.AspNetCore.Mvc.Internal.ResourceInvoker.InvokeFilterPipelineAsync()
Microsoft.AspNetCore.Mvc.Internal.ResourceInvoker.InvokeAsync()
Microsoft.AspNetCore.Routing.EndpointMiddleware.Invoke(HttpContext httpContext)
Microsoft.AspNetCore.Routing.EndpointRoutingMiddleware.Invoke(HttpContext httpContext)
Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware.Invoke(HttpContext context)
Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)
ServiceProvider trying to call GetService on already Disposed instance with _container = null.
My loaded assemblies:
github\examples\src\web\ASP.Net.Unity.Example\bin\Debug\netcoreapp2.2\ASP.Net.Core.Unity.Example.dll
packages\unity.container\5.10.0\lib\netcoreapp2.0\Unity.Container.dll
packages\unity.abstractions\4.1.1\lib\netcoreapp2.0\Unity.Abstractions.dll
packages\unity.microsoft.dependencyinjection\5.10.0\lib\netcoreapp1.1\Unity.Microsoft.DependencyInjection.dll
github\examples\src\web\ASP.Net.Unity.Example\bin\Debug\netcoreapp2.2\ASP.Net.Core.Unity.Example.Views.dll


---

<!-- source=github_issue; title=Mac OS: Firebase crashing Unity2017.4.1f1 with .NET 4.6; url=https://github.com/firebase/quickstart-unity/issues/160 -->

# Mac OS: Firebase crashing Unity2017.4.1f1 with .NET 4.6

- Source: github_issue
- URL: https://github.com/firebase/quickstart-unity/issues/160

Hi,
I just moved my project to .NET 4.6 and noticed that Firebase is crashing the Editor under MacOS.
Is there ay way to fix this?
Thanks,
Related comments:
Could you share the editor log with the crash?
What version of the SDK are you using?
[Editor-prev.log](https://github.com/firebase/quickstart-unity/files/1963783/Editor-prev.log)
[Editor.log](https://github.com/firebase/quickstart-unity/files/1963784/Editor.log)
Here are the files, hope it helps
I'm having the same problem, my logs look nearly identical. Unity editor is crashing about every 3 to 5th play. Anyone else?


---

<!-- source=github_issue; title=RemoteTech: no connection - Kerbalism throws exceptions; url=https://github.com/Kerbalism/Kerbalism/issues/221 -->

# RemoteTech: no connection - Kerbalism throws exceptions

- Source: github_issue
- URL: https://github.com/Kerbalism/Kerbalism/issues/221

```
NullReferenceException: Object reference not set to an instance of an object
at KERBALISM.ConnectionInfo..ctor (.Vessel v, Boolean powered, Boolean storm) [0x00000] in <filename unknown>:0
at KERBALISM.Vessel_info..ctor (.Vessel v, UInt32 vessel_id, UInt64 inc) [0x00000] in <filename unknown>:0
at KERBALISM.Cache.VesselInfo (.Vessel v) [0x00000] in <filename unknown>:0
at KERBALISM.Kerbalism.FixedUpdate () [0x00000] in <filename unknown>:0
(Filename: Line: -1)
```
btw there were several schedules commands in the RT flight computer ...
Using the latest master valid as of time of posting.


---

<!-- source=github_issue; title=Flash export; url=https://github.com/coolboy1/dotween/issues/2 -->

# Flash export

- Source: github_issue
- URL: https://github.com/coolboy1/dotween/issues/2

```
Make DOTween compatible with Flash export.
The only problem should be a Unity Flash bug that doesn't recognize optional
parameters correctly when inside a method that has a "where".
The attached file contains a Unity package with a compatibility test, which
will hopefully work on Flash.
```
Original issue reported on code.google.com by `daniele....@gmail.com` on 9 Aug 2014 at 8:11
Attachments:
- [DOTween_platformCompatibilityTest_0_7_250.zip](https://storage.googleapis.com/google-code-attachments/dotween/issue-2/comment-0/DOTween_platformCompatibilityTest_0_7_250.zip)


---

<!-- source=github_issue; title=Flash export; url=https://github.com/kanon1109/dotween/issues/2 -->

# Flash export

- Source: github_issue
- URL: https://github.com/kanon1109/dotween/issues/2

```
Make DOTween compatible with Flash export.
The only problem should be a Unity Flash bug that doesn't recognize optional
parameters correctly when inside a method that has a "where".
The attached file contains a Unity package with a compatibility test, which
will hopefully work on Flash.
```
Original issue reported on code.google.com by `daniele....@gmail.com` on 9 Aug 2014 at 8:11
Attachments:
- [DOTween_platformCompatibilityTest_0_7_250.zip](https://storage.googleapis.com/google-code-attachments/dotween/issue-2/comment-0/DOTween_platformCompatibilityTest_0_7_250.zip)


---

<!-- source=github_issue; title=Flash export; url=https://github.com/tothegons/dotween/issues/2 -->

# Flash export

- Source: github_issue
- URL: https://github.com/tothegons/dotween/issues/2

```
Make DOTween compatible with Flash export.
The only problem should be a Unity Flash bug that doesn't recognize optional
parameters correctly when inside a method that has a "where".
The attached file contains a Unity package with a compatibility test, which
will hopefully work on Flash.
```
Original issue reported on code.google.com by `daniele....@gmail.com` on 9 Aug 2014 at 8:11
Attachments:
- [DOTween_platformCompatibilityTest_0_7_250.zip](https://storage.googleapis.com/google-code-attachments/dotween/issue-2/comment-0/DOTween_platformCompatibilityTest_0_7_250.zip)


---

<!-- source=github_issue; title=Flash export; url=https://github.com/MoDDiB/dotween/issues/2 -->

# Flash export

- Source: github_issue
- URL: https://github.com/MoDDiB/dotween/issues/2

```
Make DOTween compatible with Flash export.
The only problem should be a Unity Flash bug that doesn't recognize optional
parameters correctly when inside a method that has a "where".
The attached file contains a Unity package with a compatibility test, which
will hopefully work on Flash.
```
Original issue reported on code.google.com by `daniele....@gmail.com` on 9 Aug 2014 at 8:11
Attachments:
- [DOTween_platformCompatibilityTest_0_7_250.zip](https://storage.googleapis.com/google-code-attachments/dotween/issue-2/comment-0/DOTween_platformCompatibilityTest_0_7_250.zip)


---

<!-- source=github_issue; title=Game stops progressing, no textboxes, no menu, just music; url=https://github.com/07th-mod/onikakushi/issues/11 -->

# Game stops progressing, no textboxes, no menu, just music

- Source: github_issue
- URL: https://github.com/07th-mod/onikakushi/issues/11

In Chapter 7, specifically after this text box http://i.imgur.com/wmJXP0h.jpg and in chapter 12 at http://i.imgur.com/gEis6eE.jpg after this text box and once again in chapter 12 at this part: http://i.imgur.com/AZb2Pi4.jpg the game stops progressing entirely. No new text boxes appear, the menu is inaccessible, just the background music keeps playing and alt f4 brings up the quit dialog.
The output log for the Chapter 7 stoppage is here: http://pastebin.com/A4pJ7Rk0 (I don't think all the loading stuff before is important, but if it is, I can give an entire output log)
The output log for the first Chapter 12 stoppage is http://pastebin.com/sLxP3s0f
The output log for the second Chapter 12 stoppage is http://pastebin.com/xPcakQgG
I don't know how the output log works but I don't think it needs all of those loading/unloading messages... correct me if I'm wrong and I'll paste it in its entirety.
I'm running the PS3 Voices and the Updated Steam Sprites, with the 1.1 patch.
I got around it by uninstalling the mod and game entirely, reinstalling and playing a good deal past the stoppage, making a save, reapplying the patch, and loading the save.. It appears that saves in the patched game are further ahead than in the unpatched game, so I have to play a good bit ahead for a saved game in the unpatched version to progress past the broken text box.
Here is a saved file that loads the patched game almost immediately after the first stopped point in Chapter 12: http://a.pomf.se/mlxaoe.zip
Make sure you change the filename if you have a saved game in the 27th slot.


---

<!-- source=github_issue; title=dll not found; url=https://github.com/labstreaminglayer/LSL4Unity/issues/15 -->

# dll not found

- Source: github_issue
- URL: https://github.com/labstreaminglayer/LSL4Unity/issues/15

Hi,
I get this error on start:
DllNotFoundException: Assets/Extensions/LSL4Unity/lib/liblsl64.dll
I simply followed the instructions from the wiki. I added the package and add a LSLMarkerStream Component on a GameObject. Then I use the marker stream just like in the instructions.
Did I miss something or do I have to consider something while importing the package?


---

<!-- source=github_issue; title=[VMC protocol] Possible bug: VSeeFace sometimes ignores the sender and resets the pose; url=https://github.com/emilianavt/VSeeFaceReleases/issues/15 -->

# [VMC protocol] Possible bug: VSeeFace sometimes ignores the sender and resets the pose

- Source: github_issue
- URL: https://github.com/emilianavt/VSeeFaceReleases/issues/15

Currently i am writing [VMC protocol support for ROMP](https://github.com/Arthur151/ROMP/issues/193), as you know.
The communication seems to work sometimes.
But sometimes VSeeFace ignores the data and instead resets the pose:
![VMC_protokol](https://user-images.githubusercontent.com/1502082/173229726-64df3891-f330-441e-b0c7-58d45d7653e6.png)
Do you have any ideas, what's my mistake? 🙂
Or is it maybe possibly an bug? 🤔
For my testing i am sending again and again the same data (captured by [Protokol](https://hexler.net/protokol)):
```
CONNECT | ENDPOINT([::]:39539)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Root/Pos) STRING(root) FLOAT(-0.017495353) FLOAT(0.3001184) FLOAT(1.3419644) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(Hips) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.7916114) FLOAT(0.092278905) FLOAT(-0.5999143) FLOAT(0.07027662)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftUpperLeg) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.569858) FLOAT(-0.06745373) FLOAT(0.21782088) FLOAT(0.7894719)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightUpperLeg) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0.09012153) FLOAT(-0.08178122) FLOAT(-0.20650071) FLOAT(0.9708488)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(Spine) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0.15954086) FLOAT(0.056978386) FLOAT(-0.01746822) FLOAT(0.9853908)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftLowerLeg) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0.51568484) FLOAT(0.071990184) FLOAT(-0.080458954) FLOAT(0.84994876)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightLowerLeg) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0.64322734) FLOAT(0.124634884) FLOAT(-0.03805522) FLOAT(0.75450414)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(Chest) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.009237677) FLOAT(-0.00467792) FLOAT(-0.015887119) FLOAT(0.9998202)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftFoot) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.014397013) FLOAT(0.055690825) FLOAT(-0.11832434) FLOAT(0.9913075)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightFoot) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.10581176) FLOAT(-0.046522453) FLOAT(0.08669153) FLOAT(0.989507)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(UpperChest) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.014591641) FLOAT(0.038391713) FLOAT(-0.0090085715) FLOAT(0.9991156)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftToes) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.14389484) FLOAT(0.09746717) FLOAT(0.2301151) FLOAT(0.9575184)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightToes) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.17262207) FLOAT(-0.05242086) FLOAT(-0.11825366) FLOAT(0.9764578)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(Neck) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.08807893) FLOAT(-0.010544569) FLOAT(-0.009392015) FLOAT(0.9960134)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftIndexProximal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.073637694) FLOAT(-0.14232136) FLOAT(-0.026770841) FLOAT(0.9867145)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightIndexProximal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.062228765) FLOAT(0.19211994) FLOAT(0.015868997) FLOAT(0.97926795)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(Head) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0.03832356) FLOAT(-0.024623983) FLOAT(-0.002712541) FLOAT(0.9989583)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftShoulder) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.05442533) FLOAT(-0.32393435) FLOAT(-0.309805) FLOAT(0.8922585)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightShoulder) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.10145097) FLOAT(0.30820185) FLOAT(0.25927484) FLOAT(0.909668)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftUpperArm) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.007941601) FLOAT(-0.78527176) FLOAT(0.33539173) FLOAT(0.5203821)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightUpperArm) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.0941422) FLOAT(0.67905384) FLOAT(-0.2797612) FLOAT(0.67212856)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftLowerArm) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.07618274) FLOAT(-0.07240124) FLOAT(0.11218269) FLOAT(0.988114)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightLowerArm) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(-0.0491007) FLOAT(0.05441978) FLOAT(-0.09431752) FLOAT(0.9928403)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftHand) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightHand) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftEye) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightEye) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(Jaw) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftThumbProximal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftThumbIntermediate) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftThumbDistal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftIndexIntermediate) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftIndexDistal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftMiddleProximal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftMiddleIntermediate) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftMiddleDistal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftRingProximal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftRingIntermediate) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftRingDistal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftLittleProximal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftLittleIntermediate) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(LeftLittleDistal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightThumbProximal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightThumbIntermediate) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightThumbDistal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightIndexIntermediate) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightIndexDistal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightMiddleProximal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightMiddleIntermediate) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightMiddleDistal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightRingProximal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightRingIntermediate) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightRingDistal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightLittleProximal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightLittleIntermediate) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/Bone/Pos) STRING(RightLittleDistal) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(0) FLOAT(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/OK) INT32(1)
RECEIVE | ENDPOINT([::1]:53734) ADDRESS(/VMC/Ext/T) FLOAT(0.045448303)
```


---

<!-- source=github_issue; title=Pass custom callback as parameter when invoking a method; url=https://github.com/vfsfitvnm/frida-il2cpp-bridge/issues/283 -->

# Pass custom callback as parameter when invoking a method

- Source: github_issue
- URL: https://github.com/vfsfitvnm/frida-il2cpp-bridge/issues/283

I want to pass a function `onWindow` from typescript as an argument to a method, how can I do this?
code:
```
function onWindow(id: number) {
}
function gui() {
Il2Cpp.perform(() => {
const AssemblyCSharp = Il2Cpp.Domain.assembly("Assembly-CSharp").image;
const ImGui = Il2Cpp.Domain.assembly("UnityEngine.IMGUIModule").image;
const UnityEngine = Il2Cpp.Domain.assembly("UnityEngine.CoreModule").image;
const Rect = UnityEngine.class("UnityEngine.Rect");
const GUI = ImGui.class("UnityEngine.GUI");
const size = Rect.alloc();
size.method(".ctor").overload("System.Single", "System.Single", "System.Single", "System.Single").invoke(100, 100, 100, 100);
const snapshot = Il2Cpp.MemorySnapshot.capture();
//some code
instance.method("FixedUpdate").implementation = function() {
this.method("FixedUpdate").invoke();
GUI.method("Window").invoke(1, size, onWindow, Il2Cpp.String.from("imgui window"));
}
//some code
});
}
```
unity docs for `UnityEngine.GUI.Window`: https://docs.unity3d.com/ScriptReference/GUI.Window.html


---

<!-- source=github_issue; title=Could we have unitypackage; url=https://github.com/couchbase/couchbase-lite-net/issues/1018 -->

# Could we have unitypackage

- Source: github_issue
- URL: https://github.com/couchbase/couchbase-lite-net/issues/1018

[As of unity 2018.1](https://blogs.unity3d.com/2018/03/28/updated-scripting-runtime-in-unity-2018-1-what-does-the-future-hold/) there are dotnet runtime 4.7 with netstandard 2.0
It seem possible to use this library in unity. Could you provide unitypackage for us?


---

<!-- source=github_issue; title=Unity : S3Example GetObjects not working. User-Agent header issue; url=https://github.com/aws/aws-sdk-net/issues/643 -->

# Unity : S3Example GetObjects not working. User-Agent header issue

- Source: github_issue
- URL: https://github.com/aws/aws-sdk-net/issues/643

I downloaded latest unity SDK "aws-sdk-unity_3.3.83.0.zip" and installed S3 unitypackage.
but in GetObjects function I am getting error. Following is trace of the problem
```
ArgumentException: Cannot set Request Header User-Agent - name contains illegal characters or is not user-overridable
UnityEngine.Networking.UnityWebRequest.SetRequestHeader (System.String name, System.String value) (at /Users/builduser/buildslave/unity/build/artifacts/generated/common/modules/UnityWebRequest/WebRequestBindings.gen.cs:473)
UnityEngine.WWW..ctor (System.String url, System.Byte[] postData, System.Collections.Generic.Dictionary`2 headers) (at /Users/builduser/buildslave/unity/build/Runtime/WebRequestWWW/UWRWWW.cs:60)
Amazon.Runtime.Internal.UnityMainThreadDispatcher+<InvokeRequest>d__7.MoveNext ()
UnityEngine.SetupCoroutine.InvokeMoveNext (IEnumerator enumerator, IntPtr returnValueAddress) (at /Users/builduser/buildslave/unity/build/Runtime/Export/Coroutines.cs:17)
UnityEngine.MonoBehaviour:StartCoroutine(IEnumerator)
Amazon.Runtime.Internal.UnityMainThreadDispatcher:ProcessRequests()
Amazon.Runtime.Internal.UnityMainThreadDispatcher:Update()
```
Expected Behavior
It used to work seamlessly in Unity version 5.6
Steps to Reproduce
Simply running example scene can reproduce issue
Your Environment
I am currently using Unity 2017.1.0b2 and building for MAC platform.
.NET version in Unity build settings: 3.5


---

<!-- source=github_issue; title=windows store apps (phone 8.1 sdk); url=https://github.com/strangeioc/strangeioc/issues/153 -->

# windows store apps (phone 8.1 sdk)

- Source: github_issue
- URL: https://github.com/strangeioc/strangeioc/issues/153

Hello. I am trying to build project for windows store (phone 8.1 sdk).
And i have big problems with integration.
I have 43 +~ errors, that connected with reflection, like:
Assets\StrangeIoC\scripts\strange\extensions\command\impl\SignalCommandBinder.cs(129,52): error CS1061: 'System.Type' does not contain a definition for 'IsAssignableFrom' and no extension method 'IsAssignableFrom' accepting a first argument of type 'System.Type' could be found (are you missing a using directive or an assembly reference?
Assets\StrangeIoC\scripts\strange\extensions\dispatcher\eventdispatcher\impl\EventBinding.cs(110,34): error CS1061: 'System.Delegate' does not contain a definition for 'Method' and no extension method 'Method' accepting a first argument of type 'System.Delegate' could be found (are you missing a using directive or an assembly reference?)
Assets\StrangeIoC\scripts\strange\extensions\implicitBind\impl\ImplicitBinder.cs(49,24): error CS0117: 'System.Reflection.Assembly' does not contain a definition for 'GetExecutingAssembly'
Assets\StrangeIoC\scripts\strange\extensions\implicitBind\impl\ImplicitBinder.cs(78,31): error CS1929: Instance argument: cannot convert from 'System.Type' to 'System.Reflection.MemberInfo'
and others. Would you fix it and support this platform in future?


---

<!-- source=github_issue; title=[patch 1.5.12459] Port DebugMod baseline startup and UI compatibility; url=https://github.com/jhearom/HollowKnight.DebugMod/issues/4 -->

# [patch 1.5.12459] Port DebugMod baseline startup and UI compatibility

- Source: github_issue
- URL: https://github.com/jhearom/HollowKnight.DebugMod/issues/4

Related comments:
Plan for initial 1.5.12459 DebugMod baseline port
Patch scope:
- Primary target: Hollow Knight `1.5.12459`
- Branch: `feature/port-1512-baseline`
Initial findings from repo triage:
- Early persistence suspects exist in `DebugMod.Initialize()` and preload handling:
- root UI object persistence
- persisted preloaded pantheon door objects
- `DebugEasterEgg` root object
- `Hitbox/ShadeSpawnLocation` persistent compass object
- DebugMod uses custom Modding API menu integration (`GetMenuScreen` + `ModMenu.CreateMenuScreen`) and may be sensitive to the newer menu lifecycle.
- Object lookup assumptions (`GameObject.Find`, `transform.Find`) are widespread and may break later, but startup/UI is the first priority.
- Build/reference alignment needs to be retargeted to the verified `1.5.12459` environment before deeper runtime triage.
Implementation phases for this pass:
1. Reference/build alignment
- build DebugMod against verified `1.5.12459` refs
- fix compile/API drift first
2. Startup persistence audit
- make `DontDestroyOnLoad` usage root-safe where needed
- eliminate any immediate persistence warnings/exceptions
3. Menu/UI bring-up
- verify custom mod menu path against current Modding API behavior
- fix early menu construction/navigation breakage if present
4. First runtime smoke test
- launch against the Steam install environment
- confirm discovery/init and inspect `ModLog.txt` / startup output
Acceptance checks for this pass:
- DebugMod builds against `1.5.12459`
- no high-priority startup persistence warning from DebugMod
- DebugMod initializes under the current local Modding API port
- baseline menu/UI entry point is reachable or the blocking failure is isolated precisely
Constraints/reminders:
- `/codex/ModdingAPI` is read-only from this workflow
- use `/codex/ModdingAPI/.codex/steam-managed-pristine` as the stable vanilla managed snapshot when a clean assembly reference is needed
- if DebugMod clearly requires Modding API changes, stop and escalate rather than patching API-side code
Discovery from first 1.5.12459 build attempt
Build command used:
- `DOTNET_CLI_HOME=/tmp/dotnet_home NUGET_PACKAGES=/tmp/nuget dotnet build /codex/HollowKnight.DebugMod/Source/DebugMod.csproj -t:Rebuild -p:HollowKnightFolder=/codex/ModdingAPI/.codex/steam-managed-pristine -p:OutputDirectory=/tmp/debugmod_out_1512 -v minimal`
Current blocker:
- build fails before runtime triage because `DebugMod.csproj` hardcodes:
- `Newtonsoft.Json, Version=11.0.0.0, Culture=neutral, PublicKeyToken=null`
- the verified `1.5.12459` environment provides:
- `Newtonsoft.Json, Version=13.0.0.0, PublicKeyToken=30ad4fe6b2a6aeed`
- result: the reference is not resolved and all `Newtonsoft` usages fail to compile.
Implication:
- first code change should be reference-alignment in `DebugMod.csproj`, not gameplay/runtime logic yet.
- this does not currently indicate a Modding API code change requirement; it is DebugMod-side build metadata drift.
Discovery: 1.5.12459 needs split assembly references
Findings from assembly inspection:
- `/codex/ModdingAPI/.codex/steam-managed-pristine/Assembly-CSharp.dll` is appropriate as a stable vanilla reference snapshot, but it does not provide the `Modding` namespace/types DebugMod compiles against.
- The Modding API build artifacts do provide the required modding surface:
- `/codex/ModdingAPI/Assembly-CSharp/obj/Release/net472/Assembly-CSharp.mm.dll`
- `/codex/ModdingAPI/OutputFinal/Assembly-CSharp.dll`
- `TeamCherry.TK2D` is also an explicit dependency on `1.5.12459` and is not currently referenced by `DebugMod.csproj`, which explains the `tk2dSprite` failures.
Next implementation step:
- update `DebugMod.csproj` so the baseline 1.5.12459 build can use:
- the pristine managed snapshot for vanilla game/Unity references, and
- a separate explicit property/path for Modding API-patched `Assembly-CSharp` / `MMHOOK_Assembly-CSharp` references.
- add the missing `TeamCherry.TK2D` reference.
This remains a DebugMod-side build/reference alignment change only; no Modding API repo edits are implied by this step.


---

<!-- source=github_issue; title=Problem spawning an object with a parent; url=https://github.com/FirstGearGames/FishNet/issues/435 -->

# Problem spawning an object with a parent

- Source: github_issue
- URL: https://github.com/FirstGearGames/FishNet/issues/435

**General**
Unity version: 2021.3.22f1
Fish-Networking version: 3.10.4Pro and 3.10.5Pro
Discord link:
https://discord.com/channels/424284635074134018/1132864946275876864
**Description**
When trying to set an object's parent when the object is created some problems arise depending on what method is used.
If the object's parent is set with the `transform.SetParent` method before `Spawn` is called on the object, then the parent will be correct on the host and all clients, but non-host clients will receive a warning like this:
```
Spawned NetworkObject was expected to exist but does not for Id 4. This may occur if you sent a NetworkObject reference which does not exist, be it destroyed or if the client does not have visibility.
UnityEngine.Debug:LogWarning (object)
FishNet.Managing.Logging.LevelLoggingConfiguration:LogWarning (string) (at Assets/FishNet/Runtime/Managing/Logging/LevelLoggingConfiguration.cs:118)
FishNet.Managing.NetworkManager:LogWarning (string) (at Assets/FishNet/Runtime/Managing/NetworkManager.Logging.cs:102)
FishNet.Serializing.Reader:LogWarning (string) (at Assets/FishNet/Runtime/Serializing/Reader.cs:1502)
FishNet.Managing.Client.ClientObjects:ReadSpawnedObject (FishNet.Serializing.PooledReader,System.Nullable`1<int>&,System.Nullable`1<byte>&,System.Nullable`1<int>&) (at Assets/FishNet/Runtime/Managing/Client/Object/ClientObjects.cs:716)
FishNet.Managing.Client.ClientObjects:CacheSpawn (FishNet.Serializing.PooledReader) (at Assets/FishNet/Runtime/Managing/Client/Object/ClientObjects.cs:444)
FishNet.Managing.Client.ClientManager:ParseReader (FishNet.Serializing.PooledReader,FishNet.Transporting.Channel,bool) (at Assets/FishNet/Runtime/Managing/Client/ClientManager.cs:388)
FishNet.Managing.Client.ClientManager:ParseReceived (FishNet.Transporting.ClientReceivedDataArgs) (at Assets/FishNet/Runtime/Managing/Client/ClientManager.cs:317)
FishNet.Managing.Client.ClientManager:Transport_OnClientReceivedData (FishNet.Transporting.ClientReceivedDataArgs) (at Assets/FishNet/Runtime/Managing/Client/ClientManager.cs:283)
FishNet.Transporting.Tugboat.Tugboat:HandleClientReceivedDataArgs (FishNet.Transporting.ClientReceivedDataArgs) (at Assets/FishNet/Runtime/Transporting/Transports/Tugboat/Tugboat.cs:219)
FishNet.Transporting.Tugboat.Client.ClientSocket:IterateIncoming () (at Assets/FishNet/Runtime/Transporting/Transports/Tugboat/Core/ClientSocket.cs:287)
FishNet.Transporting.Tugboat.Tugboat:IterateIncoming (bool) (at Assets/FishNet/Runtime/Transporting/Transports/Tugboat/Tugboat.cs:192)
FishNet.Managing.Transporting.TransportManager:IterateIncoming (bool) (at Assets/FishNet/Runtime/Managing/Transporting/TransportManager.cs:536)
FishNet.Managing.Timing.TimeManager:TryIterateData (bool) (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:1034)
FishNet.Managing.Timing.TimeManager:IncreaseTick () (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:693)
FishNet.Managing.Timing.TimeManager:<TickUpdate>g__MethodLogic|102_0 () (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:368)
FishNet.Managing.Timing.TimeManager:TickUpdate () (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:358)
FishNet.Transporting.NetworkReaderLoop:Update () (at Assets/FishNet/Runtime/Transporting/NetworkReaderLoop.cs:28)
```
If the object is `Spawned` and then immediately has `NetworkObject.SetParent` used on it instead, then the following issues occur:
1. The object will be correctly spawned on its parent on the server, but solo clients will not see previously spawned objects with the correct parent and this warning will be logged for them:
```
Spawned NetworkObject was expected to exist but does not for Id 4. This may occur if you sent a NetworkObject reference which does not exist, be it destroyed or if the client does not have visibility.
UnityEngine.Debug:LogWarning (object)
FishNet.Managing.Logging.LevelLoggingConfiguration:LogWarning (string) (at Assets/FishNet/Runtime/Managing/Logging/LevelLoggingConfiguration.cs:118)
FishNet.Managing.NetworkManager:LogWarning (string) (at Assets/FishNet/Runtime/Managing/NetworkManager.Logging.cs:102)
FishNet.Serializing.Reader:LogWarning (string) (at Assets/FishNet/Runtime/Serializing/Reader.cs:1502)
FishNet.Managing.Client.ClientObjects:ReadSpawnedObject (FishNet.Serializing.PooledReader,System.Nullable`1<int>&,System.Nullable`1<byte>&,System.Nullable`1<int>&) (at Assets/FishNet/Runtime/Managing/Client/Object/ClientObjects.cs:716)
FishNet.Managing.Client.ClientObjects:CacheSpawn (FishNet.Serializing.PooledReader) (at Assets/FishNet/Runtime/Managing/Client/Object/ClientObjects.cs:444)
FishNet.Managing.Client.ClientManager:ParseReader (FishNet.Serializing.PooledReader,FishNet.Transporting.Channel,bool) (at Assets/FishNet/Runtime/Managing/Client/ClientManager.cs:388)
FishNet.Managing.Client.ClientManager:ParseReceived (FishNet.Transporting.ClientReceivedDataArgs) (at Assets/FishNet/Runtime/Managing/Client/ClientManager.cs:317)
FishNet.Managing.Client.ClientManager:Transport_OnClientReceivedData (FishNet.Transporting.ClientReceivedDataArgs) (at Assets/FishNet/Runtime/Managing/Client/ClientManager.cs:283)
FishNet.Transporting.Tugboat.Tugboat:HandleClientReceivedDataArgs (FishNet.Transporting.ClientReceivedDataArgs) (at Assets/FishNet/Runtime/Transporting/Transports/Tugboat/Tugboat.cs:219)
FishNet.Transporting.Tugboat.Client.ClientSocket:IterateIncoming () (at Assets/FishNet/Runtime/Transporting/Transports/Tugboat/Core/ClientSocket.cs:287)
FishNet.Transporting.Tugboat.Tugboat:IterateIncoming (bool) (at Assets/FishNet/Runtime/Transporting/Transports/Tugboat/Tugboat.cs:192)
FishNet.Managing.Transporting.TransportManager:IterateIncoming (bool) (at Assets/FishNet/Runtime/Managing/Transporting/TransportManager.cs:536)
FishNet.Managing.Timing.TimeManager:TryIterateData (bool) (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:1034)
FishNet.Managing.Timing.TimeManager:IncreaseTick () (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:693)
FishNet.Managing.Timing.TimeManager:<TickUpdate>g__MethodLogic|102_0 () (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:368)
FishNet.Managing.Timing.TimeManager:TickUpdate () (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:358)
FishNet.Transporting.NetworkReaderLoop:Update () (at Assets/FishNet/Runtime/Transporting/NetworkReaderLoop.cs:28)
```
2. If the object has a NetworkTransform with the "SyncParent" option enabled, the following warning appears on the server and the parent is not set at all:
```
PrefabWithNT(Clone) parent object was removed without calling UnsetParent. Use networkObject.UnsetParent() to remove a NetworkObject from it's parent. This is being made a requirement in Fish-Networking v4.
UnityEngine.Debug:LogWarning (object)
FishNet.Component.Transforming.NetworkTransform:TimeManager_OnPostTick () (at Assets/FishNet/Runtime/Generated/Component/NetworkTransform/NetworkTransform.cs:837)
FishNet.Managing.Timing.TimeManager:IncreaseTick () (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:712)
FishNet.Managing.Timing.TimeManager:<TickUpdate>g__MethodLogic|102_0 () (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:368)
FishNet.Managing.Timing.TimeManager:TickUpdate () (at Assets/FishNet/Runtime/Managing/Timing/TimeManager.cs:358)
FishNet.Transporting.NetworkReaderLoop:Update () (at Assets/FishNet/Runtime/Transporting/NetworkReaderLoop.cs:28)
```
**Replication**
Steps to reproduce the behavior:
1. Using the example script or a custom one, attempt to spawn a network object with a given parent.
2. See the behaviour on non-host clients.
**Expected behavior**
It's expected that one of these methods should work correctly.
**Example code used**
```cs
using FishNet.Object;
using System.Collections;
using UnityEngine;
namespace ParentingProblems
{
public class SpawnAsChild : NetworkBehaviour
{
// A child of this object that contains a NetworkBehaviour. Objects will be spawned on it.
[SerializeField] NetworkObject hand;
// An empty prefab with only a NetworkObject.
[SerializeField] NetworkObject prefabWithNOB;
// A prefab with only a NetworkObject and NetworkTransform set to "SyncParents"
[SerializeField] NetworkObject prefabWithNT;
public override void OnStartServer()
{
StartCoroutine(nameof(SpawnChildren));
}
IEnumerator SpawnChildren()
{
yield return new WaitUntil(() => hand.IsSpawned);
ParentAndSpawnObject();
ParentAndSpawnObjectWithNT();
SpawnAndParentObject();
SpawnAndParentObjWithNT();
}
private void ParentAndSpawnObject()
{
var obj = Instantiate(prefabWithNOB);
obj.transform.SetParent(hand.transform);
Spawn(obj);
}
private void ParentAndSpawnObjectWithNT()
{
var obj = Instantiate(prefabWithNT);
obj.transform.SetParent(hand.transform);
Spawn(obj);
}
private void SpawnAndParentObject()
{
var obj = Instantiate(prefabWithNOB);
Spawn(obj);
obj.SetParent(hand.GetComponent<NetworkObject>());
}
private void SpawnAndParentObjWithNT()
{
var obj = Instantiate(prefabWithNT);
Spawn(obj);
obj.SetParent(hand.GetComponent<NetworkObject>());
}
}
}
```
**Example package**
[ParentingProblems.zip](https://github.com/FirstGearGames/FishNet/files/12245169/ParentingProblems.zip)


---

<!-- source=github_issue; title=Does this UA .Net standard support Unity's IL2CPP Scripting Backend? HELP !!!!; url=https://github.com/OPCFoundation/UA-.NETStandard/issues/760 -->

# Does this UA .Net standard support Unity's IL2CPP Scripting Backend? HELP !!!!

- Source: github_issue
- URL: https://github.com/OPCFoundation/UA-.NETStandard/issues/760

I am developing a UWP application that allows HoloLens to connect to the OPC UA server. So I want to confirm, is the current version of UA .Net Standard now supporting Unity IL2CPP scripting backend, or can it only support .Net/Mono scripting backend?
I hope someone can reply to me as soon as possible. This question is very important to me, thanks a lot.


---

<!-- source=github_issue; title=Upgrade to Prism 8.1.97; url=https://github.com/AvaloniaCommunity/Prism.Avalonia/issues/9 -->

# Upgrade to Prism 8.1.97

- Source: github_issue
- URL: https://github.com/AvaloniaCommunity/Prism.Avalonia/issues/9

As a user, I'd like to use the latest Prism framework with Prism.Avalonia which supports .NET 5, Linux and includes newer features. Figured this story would help keep the ball rolling and a discussion flowing. 👍
Thus far, the upgrade is nearly straightforward comparing [Prism Library v7.2.0.1422...v8.1.97](https://github.com/PrismLibrary/Prism/compare/v7.2.0.1422...v8.1.97). However, there are some speedbumps that were bound to happen. The focus of comparison thus far is the project, `Prism.Wpf`.
Upgrade Progress: [Upgrade-Prism-7.2-to-8.1.md](https://github.com/AvaloniaCommunity/Prism.Avalonia/blob/feature-Prism8197/Upgrade-Prism-7.2-to-8.1.md)
Local Pull Request: #11
If any of you have some insight into issues found along the way denoted by the `⚠️` symbol in the [Upgrade file](https://github.com/AvaloniaCommunity/Prism.Avalonia/blob/feature-Prism8197/Upgrade-Prism-7.2-to-8.1.md), please join in to help keep this moving.
### Action Items
* [X] Upgrade Prism.Avalonia
* [X] Upgrade Prism.DryIoc
* [x] Upgrade Prism.Unity
* [X] Remove IOCs not supported by Prism v8.1
* [X] Upgrade Samples
* [x] Add Unit Tests, matching PrismLibrary
### Out of Scope
* Restructure folders to match PrismLibrary
* Add Prism Dialogs for Avalonia
### Speedbumps
* `ModuleCatalog.cs`
* Cannot use ContentPropertyAttribute such as `[ContentProperty("Items")]` - (_Already addressed in 7.2.x_)
* Cause: ContentPropertyAttribute references System.Windows.Markup and Avalonia.Markup.Xaml doesn't have one
### Updates
* 2021-09-07 - Changed links to point at this repo's branch, now that it is housed here.


---

<!-- source=github_issue; title=Unable to load mods on macOS 10.14; url=https://github.com/javisar/ONI-Modloader/issues/22 -->

# Unable to load mods on macOS 10.14

- Source: github_issue
- URL: https://github.com/javisar/ONI-Modloader/issues/22

## Prerequisites
- [x] I've made sure the game files are ok before installing injector/mods (https://support.steampowered.com/kb_article.php?ref=2037-QEUH-3335)
- [x] I am running the latest version (Master Branch in github)
- [x] I've checked the logs to see if I can find the problematic mod (test the mods one by one if needed)
- [x] I checked the documentation and forums and found no answer
- [x] I checked to make sure that this issue has not already been filed
- [x] I'm reporting the issue to the correct repository (for multi-repository projects)
## Describe the bug
On macOS 10.14 with ONI Build RU-285480 and ONI-Modloader 0.4.9, after injecting `Assembly-CSharp.dll` and `Assembly-CSharp-firstpass.dll` via mono, `MoreMaterialsMod.dll` and `ONI-Common.dll` are placed under the Mods directory. `debug` in `ONI-CommonState.json` is set to `true`. The mods do not load and no log are generated.
## Expected behavior
* Build building with arbitrary material.
* Generate logs for mods.
## Current behavior
* The material limits are unaffected.
* No logs are generated.
## To Reproduce
Steps to reproduce the behavior:
1. Install ONI Build RU-285480 via Steam.
2. Inject ONI-Modloader 0.4.9 via `mono injector.exe` while under `$HOME/Library/Application Support/Steam/steamapps/common/OxygenNotIncluded/OxygenNotIncluded.app/Contents/Resources/Data/Managed`.
3. Place `MoreMaterialsMod.dll`, `ONI-Common.dll`, and `ONI-Common/Config/ONI-CommonState.json` in `$HOME/Library/Application Support/Steam/steamapps/common/OxygenNotIncluded/OxygenNotIncluded.app/Contents/Resources/Mods`.
4. Set `debug` in `ONI-CommonState.json` to `true`.
5. Run ONI.
## Environment
- OS: macOS 10.14
- ONI Version RU-285480
- ONI-Modloader Version 0.4.9
## Output log
No log is generated.


---

<!-- source=github_issue; title=Object reference not set to an instance of an object.; url=https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/2279 -->

# Object reference not set to an instance of an object.

- Source: github_issue
- URL: https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/2279

1.
```
[12/26/2020 15:21:30] [Error] Object reference not set to an instance of an object
[12/26/2020 15:22:26] [Error] at SDG.Unturned.PlayerEquipment.simulate (System.UInt32 simulation, System.Boolean inputPrimary, System.Boolean inputSecondary, System.Boolean inputSteady) [0x002c4] in <f84ca727c6224c6da32cb2702db0177c>:0
```
2.
```
[12/26/2020 20:35:37] [Error] Object reference not set to an instance of an object
[12/26/2020 20:35:37] [Error] at Pathfinding.ABPath.Cleanup () [0x00027] in <f84ca727c6224c6da32cb2702db0177c>:0
at AstarPath.CalculatePathsThreaded (System.Object _threadInfo) [0x00177] in <f84ca727c6224c6da32cb2702db0177c>:0
[12/26/2020 20:35:37] [Error] Unhandled exception during pathfinding. Terminating.
[12/26/2020 20:35:37] [Error] Error : This part should never be reached.
```


---

<!-- source=github_issue; title=[BUG]: It is not possible to make connection between different (public) networks; url=https://github.com/Unity-Technologies/UnityRenderStreaming/issues/907 -->

# [BUG]: It is not possible to make connection between different (public) networks

- Source: github_issue
- URL: https://github.com/Unity-Technologies/UnityRenderStreaming/issues/907

### Package version
3.1.0-exp.6
### Environment
```markdown
* OS: Windows 10 and Windows 11, Linux Ubuntu 22.04 Docker env.
* Unity version: 2021.3 and 2022.3 all LTS versions
* Graphics API: SRP, URP, HDRP
* Browser: Chrome, Firefox, Edge, Safari ( all latest )
```
### Steps To Reproduce
1. Open bidirectional examples on the web and unity with different networks ( ask your friend for help )
2. Try to make a connection.
### Current Behavior
It will look like there is a connection at least half of it but it will not detect the encoders and will not show up any data as the stream does not start. And disconnects in 60 seconds at max. If you try in the local network ( both web and unity apps ) it will connect yet get disconnected at an unmeasured time.
### Expected Behavior
It should connect and stay connected as long as the connection is closed by one of the peers.
### Anything else?
I have tried 3 different Turn server solutions with various configurations, with and without authentication.
All tests passed on ICE serves when I tested trickle ( except chrome with the known issues but it is considered passed )
I tried Coturn and Eturnal servers. Then I decided to try free and paid 3rd party servers ( metered.ca ). All passed the trickle and peer-to-peer tests.
I believe there is a race condition between negotiation and state changes. I couldn't see any rollback scenario so cable tangling may be the problem.


---

<!-- source=github_issue; title=BUG: Plugins Failing to Detect CWD; url=https://github.com/Flow-Launcher/Flow.Launcher/issues/2299 -->

# BUG: Plugins Failing to Detect CWD

- Source: github_issue
- URL: https://github.com/Flow-Launcher/Flow.Launcher/issues/2299

### Checks
- [X] I have checked that this issue has not already been reported.
- [X] I am using the latest version of Flow Launcher.
### Problem Description
I've been using FlowLauncher on Windows 10 for a couple weeks now, with a bunch of plugins installed. It's been working great, and before now, I hadn't run into any issues, I booted up Flow Launcher today, and I got a strange error saying that lots of plugins were unable to be initialized. I rebooted a few times and tried several other things, but I couldn't get the error to go away. Upon investigation, I landed in one of the `lib\flox\__init.py__` files that every python plugin has. After reading the code and debugging the error, I came to this code:
```py
while True:
if len(path.parts) == 1:
raise FileNotFoundError("Unable to locate Launcher directory")
if path.joinpath('Settings').exists():
USER_DIR = path
if USER_DIR.name == 'UserData':
APP_DIR = USER_DIR.parent
elif str(CURRENT_WORKING_DIR).startswith(str(APPDATA)):
APP_DIR = LOCALAPPDATA.joinpath(launcher_name)
else:
raise FileNotFoundError("Unable to locate Launcher directory")
break
path = path.parent
```
This code searches for FlowLauncher's `Settings` folder. In a normal installation, this code will work fine and succeed on the first loop, as the `Settings` folder should be in this path.
But for me, the code loops until it gets all the way to the top of the path (`C:\`). There, it hits the `len(path.parts) == 1` check and throws an exception. That's because my FlowLauncher directory is, upon checking it out, very strange.
I have two FlowLauncher folders - one in AppData (`C:\Users\zachy\AppData\Roaming\FlowLauncher`):
![flowlauncherfolderstructure](https://github.com/Flow-Launcher/Flow.Launcher/assets/105762560/ebab7a8c-adc2-4c32-a00f-071153ea7f4c)
and one in LocalAppData (`C:\Users\zachy\AppData\Local\FlowLauncher`):
![flowlauncherfolderstructure2](https://github.com/Flow-Launcher/Flow.Launcher/assets/105762560/da35ea49-be96-4ba9-bdfd-2ad1380e7ad2)
As you can see, the program's code / executables and data are split into two separate paths. The CWD that the plugin's __init__.py sees is the latter. I don't know if this is supposed to be the case, but I can't imagine why any developer would make it this way, and it clearly doesn't make the program itself very happy (at least, in terms of plugins). However, everything except plugins appears to be functioning fine, including settings.
Even stranger, the majority of plugins load and work fine. What language the plugin is coded in doesn't seem to matter either, but I may be wrong.
Here's all the plugins that don't work (all of them encounter the same issue, AFAICT):
![notworkingplugins](https://github.com/Flow-Launcher/Flow.Launcher/assets/105762560/26337ec1-7138-48f6-ac68-dd614bf4d3e0)
*TenorGIF plugin too; I couldn't fit it into the screenshot.*
This is an incredibly weird issue, and I've never encountered anything like it. I don't really have anything to test against, and I have no idea what's going on, so I apologize if this issue isn't very well written.
### To Reproduce
1. Install FlowLauncher.
2. Install one of the plugins that's encountering this error.
3. Somehow get this weird directory structure to occur (I don't know how this happened for me, or maybe I'm just confused and this is actually how it's supposed to do).
4. Start FlowLauncher and maybe this behavior will occur???
### Screenshots
![screenshot1](https://github.com/Flow-Launcher/Flow.Launcher/assets/105762560/f56a4b4d-1bda-45f3-abd6-c1672dfe0394)
*Error encountered starting FlowLauncher*
![errorpart1](https://github.com/Flow-Launcher/Flow.Launcher/assets/105762560/f041bbee-b7de-4da8-b8cd-be3b7526c11a)
![errorpart2](https://github.com/Flow-Launcher/Flow.Launcher/assets/105762560/1554be7b-fc86-4a7f-a61c-d1422edcea1c)
![errorpart3](https://github.com/Flow-Launcher/Flow.Launcher/assets/105762560/6488aee7-a220-4fc5-adf5-abde0ca173bf)
*Error encountered after manually turning one of the plugins on, even though it failed to load on FlowLauncher startup,
and trying to search something. I showed the relevant parts of the error log.*
### Flow Launcher Version
1.16.1
### Windows Build Number
10.0.19045.3324
### Error Log
Here's my FlowLauncher log, but it doesn't seem to contain anything relevant:
<details>
```shell
12:25:27.1552-04:00 - INFO - App.OnStartup - Begin Flow Launcher startup ----------------------------------------------------
12:25:27.1552-04:00 - INFO - App.OnStartup - Runtime info:
Flow Launcher version: 1.16.1
OS Version: 19045.3324
IntPtr Length: 8
x64: True
12:25:29.5570-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <System Commands> is <19ms>
12:25:29.5570-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Process Killer> is <18ms>
12:25:29.5570-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Plugin Indicator> is <18ms>
12:25:29.5570-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <URL> is <114ms>
12:25:29.5570-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <ClipboardR> is <129ms>
12:25:29.5708-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Shell> is <48ms>
12:25:29.5708-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Web Searches> is <39ms>
12:25:29.5708-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <CPPreference> is <4ms>
12:25:29.5708-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Windows Settings> is <76ms>
12:25:29.5708-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <EmailTo> is <4ms>
12:25:29.5708-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Flow.Plugin.UrlEncode> is <4ms>
12:25:29.5708-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <GitHub> is <15ms>
12:25:29.5708-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <IP Address> is <4ms>
12:25:29.5708-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <JetBrainsIDEProjects> is <5ms>
12:25:29.5708-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Plugin Runner> is <7ms>
12:25:29.6065-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Clipboard History> is <56ms>
12:25:29.6065-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Registry> is <4ms>
12:25:29.6065-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <SpotifyPremium> is <7ms>
12:25:29.6224-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Colors> is <57ms>
12:25:29.6224-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <StringUtils> is <6ms>
12:25:29.6224-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://fastly.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
12:25:29.6432-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Explorer> is <400ms>
12:25:29.6488-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <VS Code Workspaces> is <26ms>
12:25:29.6488-04:00 - INFO - Flow.Launcher.Plugin.Program.Main - Preload programs cost <89ms>
12:25:29.6488-04:00 - INFO - Flow.Launcher.Plugin.Program.Main - Number of preload win32 programs <1247>
12:25:29.6488-04:00 - INFO - Flow.Launcher.Plugin.Program.Main - Number of preload uwps <38>
12:25:29.6785-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Calculator> is <142ms>
12:25:29.7023-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <CkFlow> is <41ms>
12:25:29.7231-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Todos> is <257ms>
12:25:29.7499-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <DdFlow> is <0ms>
12:25:29.7499-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <DevToys Launcher> is <0ms>
12:25:29.7499-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <ElementFlow> is <0ms>
12:25:29.7575-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Browser Bookmarks> is <225ms>
12:25:29.7943-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Program> is <328ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <CurrencyPP> is <159ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Epic Games Store Launcher> is <103ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <FlowYouTube> is <82ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Browser History> is <217ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Emoji+> is <110ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <ChatGPT> is <212ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Currency Converter> is <182ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Google Translate> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Gitmoji> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Google Calendar> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Number Converter> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <isPrime> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <QrFlow> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Statis> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Timestamp> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <UUID Generator> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Window Services> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Windows Startup> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <WinsFlow> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Youtube Downloader> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <General Converter> is <66ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <DateDiff> is <0ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Search npm> is <1ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Github Notifications> is <2ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <TenorGIF> is <1ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Github Quick Launcher> is <2ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Steam Search> is <1ms>
12:25:29.8614-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Search MDN> is <3ms>
12:25:29.8796-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Quick Uninstaller> is <296ms>
12:25:29.9276-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Unit converter> is <312ms>
12:25:29.9862-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://gcore.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
12:25:29.9862-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://cdn.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
12:25:29.9862-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://raw.githubusercontent.com/Flow-Launcher/Flow.Launcher.PluginsManifest/plugin_api_v2/plugins.json
12:25:30.3604-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Dictionary> is <788ms>
12:25:30.3807-04:00 - INFO - CommunityPluginSource.FetchAsync - Loaded 113 plugins from https://raw.githubusercontent.com/Flow-Launcher/Flow.Launcher.PluginsManifest/plugin_api_v2/plugins.json
12:25:30.3850-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Plugins Manager> is <847ms>
12:25:30.5215-04:00 - INFO - ImageLoader.Initialize - Preload images cost <2893ms>
12:25:30.5233-04:00 - INFO - ImageLoader.Initialize - Number of preload images is <67>, Images Number: 67, Unique Items 31
12:25:30.7302-04:00 - INFO - App.OnStartup - Dependencies Info:
Python Path: C:\Users\zachy\AppData\Roaming\FlowLauncher\Environments\Python\PythonEmbeddable-v3.8.9\pythonw.exe
Node Path: C:\Users\zachy\AppData\Roaming\FlowLauncher\Environments\Node.js\Node-v16.18.0\node-v16.18.0-win-x64\node.exe
12:25:31.0008-04:00 - INFO - App.OnStartup - End Flow Launcher startup ----------------------------------------------------
12:25:31.0008-04:00 - INFO - App.OnStartup - Startup cost <4567ms>
12:25:32.5670-04:00 - INFO - Updater.UpdateApp - Future Release <{
"SHA1": "375B438F6693203DD599DDE0117294EF3AA743A0",
"BaseUrl": null,
"Filename": "FlowLauncher-1.16.1-full.nupkg",
"Query": null,
"Filesize": 93451616,
"IsDelta": false,
"StagingPercentage": null,
"EntryAsString": "375B438F6693203DD599DDE0117294EF3AA743A0 FlowLauncher-1.16.1-full.nupkg 93451616",
"Version": {
"Version": "1.16.1.0",
"SpecialVersion": ""
},
"PackageName": "FlowLauncher"
}>
12:27:22.9544-04:00 - INFO - App.OnStartup - Begin Flow Launcher startup ----------------------------------------------------
12:27:22.9594-04:00 - INFO - App.OnStartup - Runtime info:
Flow Launcher version: 1.16.1
OS Version: 19045.3324
IntPtr Length: 8
x64: True
12:27:25.3172-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Plugin Indicator> is <11ms>
12:27:25.3527-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://fastly.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
12:27:25.3947-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Process Killer> is <10ms>
12:27:25.3965-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <System Commands> is <8ms>
12:27:25.3965-04:00 - INFO - Flow.Launcher.Plugin.Program.Main - Preload programs cost <58ms>
12:27:25.3965-04:00 - INFO - Flow.Launcher.Plugin.Program.Main - Number of preload win32 programs <1247>
12:27:25.3965-04:00 - INFO - Flow.Launcher.Plugin.Program.Main - Number of preload uwps <38>
12:27:25.3965-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <URL> is <77ms>
12:27:25.4292-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Calculator> is <151ms>
12:27:25.4292-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Web Searches> is <49ms>
12:27:25.4292-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Shell> is <60ms>
12:27:25.4433-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Explorer> is <202ms>
12:27:25.4433-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Program> is <179ms>
12:27:25.4433-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <CPPreference> is <10ms>
12:27:25.4643-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <ClipboardR> is <265ms>
12:27:25.4643-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <EmailTo> is <6ms>
12:27:25.4643-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Flow.Plugin.UrlEncode> is <8ms>
12:27:25.4643-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <IP Address> is <14ms>
12:27:25.4643-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <JetBrainsIDEProjects> is <10ms>
12:27:25.4643-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Plugin Runner> is <16ms>
12:27:25.4643-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Clipboard History> is <64ms>
12:27:25.4752-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Registry> is <11ms>
12:27:25.4752-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <SpotifyPremium> is <19ms>
12:27:25.4752-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <StringUtils> is <14ms>
12:27:25.4752-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <GitHub> is <150ms>
12:27:25.4752-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Windows Settings> is <60ms>
12:27:25.5142-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Todos> is <416ms>
12:27:25.5142-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <VS Code Workspaces> is <46ms>
12:27:25.5302-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Colors> is <22ms>
12:27:25.5302-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Browser Bookmarks> is <274ms>
12:27:25.5302-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <CkFlow> is <21ms>
12:27:25.5302-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <DdFlow> is <5ms>
12:27:25.5302-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <DevToys Launcher> is <3ms>
12:27:25.5302-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <ElementFlow> is <0ms>
12:27:25.6165-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://gcore.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
12:27:25.6165-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://cdn.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
12:27:25.6165-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://raw.githubusercontent.com/Flow-Launcher/Flow.Launcher.PluginsManifest/plugin_api_v2/plugins.json
12:27:25.6830-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Quick Uninstaller> is <226ms>
12:27:25.6830-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Gitmoji> is <0ms>
12:27:25.6830-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Google Calendar> is <0ms>
12:27:25.6830-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Google Translate> is <0ms>
12:27:25.6830-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <isPrime> is <0ms>
12:27:25.6830-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Number Converter> is <0ms>
12:27:25.6830-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <QrFlow> is <0ms>
12:27:25.6830-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Statis> is <0ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Browser History> is <301ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Currency Converter> is <273ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Github Notifications> is <141ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <TenorGIF> is <107ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Timestamp> is <0ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <UUID Generator> is <0ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Window Services> is <0ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Windows Startup> is <0ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <WinsFlow> is <0ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Youtube Downloader> is <0ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Search npm> is <1ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <DateDiff> is <0ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Unit converter> is <355ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Emoji+> is <259ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <CurrencyPP> is <270ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <General Converter> is <178ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Epic Games Store Launcher> is <259ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <ChatGPT> is <306ms>
12:27:25.7906-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Github Quick Launcher> is <113ms>
12:27:25.8475-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Steam Search> is <53ms>
12:27:25.8475-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Search MDN> is <55ms>
12:27:25.8475-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <FlowYouTube> is <310ms>
12:27:26.3044-04:00 - INFO - CommunityPluginSource.FetchAsync - Loaded 113 plugins from https://fastly.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
12:27:26.3044-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Plugins Manager> is <1004ms>
12:27:26.6307-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Dictionary> is <1188ms>
12:27:26.8449-04:00 - INFO - ImageLoader.Initialize - Preload images cost <3700ms>
12:27:26.8449-04:00 - INFO - ImageLoader.Initialize - Number of preload images is <67>, Images Number: 67, Unique Items 31
12:27:27.1341-04:00 - INFO - App.OnStartup - Dependencies Info:
Python Path: C:\Users\zachy\AppData\Roaming\FlowLauncher\Environments\Python\PythonEmbeddable-v3.8.9\pythonw.exe
Node Path: C:\Users\zachy\AppData\Roaming\FlowLauncher\Environments\Node.js\Node-v16.18.0\node-v16.18.0-win-x64\node.exe
12:27:28.0323-04:00 - INFO - App.OnStartup - End Flow Launcher startup ----------------------------------------------------
12:27:28.0323-04:00 - INFO - App.OnStartup - Startup cost <5413ms>
12:27:29.8246-04:00 - INFO - Updater.UpdateApp - Future Release <{
"SHA1": "375B438F6693203DD599DDE0117294EF3AA743A0",
"BaseUrl": null,
"Filename": "FlowLauncher-1.16.1-full.nupkg",
"Query": null,
"Filesize": 93451616,
"IsDelta": false,
"StagingPercentage": null,
"EntryAsString": "375B438F6693203DD599DDE0117294EF3AA743A0 FlowLauncher-1.16.1-full.nupkg 93451616",
"Version": {
"Version": "1.16.1.0",
"SpecialVersion": ""
},
"PackageName": "FlowLauncher"
}>
13:19:34.0748-04:00 - INFO - App.OnStartup - Begin Flow Launcher startup ----------------------------------------------------
13:19:34.0748-04:00 - INFO - App.OnStartup - Runtime info:
Flow Launcher version: 1.16.1
OS Version: 19045.3324
IntPtr Length: 8
x64: True
13:19:35.4652-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Plugin Indicator> is <20ms>
13:19:35.4652-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Process Killer> is <12ms>
13:19:35.4652-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <URL> is <39ms>
13:19:35.4860-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Shell> is <47ms>
13:19:35.4860-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://fastly.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Clipboard History> is <21ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Web Searches> is <41ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <System Commands> is <13ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <CPPreference> is <12ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <EmailTo> is <10ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Flow.Plugin.UrlEncode> is <10ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <ClipboardR> is <128ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <IP Address> is <12ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <JetBrainsIDEProjects> is <10ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Plugin Runner> is <10ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <GitHub> is <58ms>
13:19:35.4914-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Registry> is <9ms>
13:19:35.5062-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <SpotifyPremium> is <12ms>
13:19:35.5062-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Colors> is <20ms>
13:19:35.5062-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <StringUtils> is <11ms>
13:19:35.5062-04:00 - INFO - Flow.Launcher.Plugin.Program.Main - Preload programs cost <19ms>
13:19:35.5062-04:00 - INFO - Flow.Launcher.Plugin.Program.Main - Number of preload win32 programs <1247>
13:19:35.5062-04:00 - INFO - Flow.Launcher.Plugin.Program.Main - Number of preload uwps <38>
13:19:35.5062-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Windows Settings> is <55ms>
13:19:35.5062-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Calculator> is <68ms>
13:19:35.5527-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Browser Bookmarks> is <105ms>
13:19:35.5527-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <CkFlow> is <0ms>
13:19:35.5527-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Todos> is <182ms>
13:19:35.5877-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <DdFlow> is <0ms>
13:19:35.5877-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <DevToys Launcher> is <0ms>
13:19:35.5877-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <ElementFlow> is <0ms>
13:19:35.5995-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Explorer> is <179ms>
13:19:35.6238-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Program> is <213ms>
13:19:35.6238-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <VS Code Workspaces> is <131ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Browser History> is <155ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Epic Games Store Launcher> is <67ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <CurrencyPP> is <109ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Emoji+> is <68ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <FlowYouTube> is <65ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Currency Converter> is <114ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <ChatGPT> is <149ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Gitmoji> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <isPrime> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Google Calendar> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Number Converter> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <QrFlow> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Statis> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Timestamp> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <General Converter> is <40ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <UUID Generator> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Window Services> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Windows Startup> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <WinsFlow> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Youtube Downloader> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Google Translate> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <DateDiff> is <0ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Search npm> is <1ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Github Quick Launcher> is <2ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <TenorGIF> is <2ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Github Notifications> is <3ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Steam Search> is <2ms>
13:19:35.6690-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Search MDN> is <4ms>
13:19:35.7146-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://gcore.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
13:19:35.7146-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://cdn.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
13:19:35.7146-04:00 - INFO - CommunityPluginSource.FetchAsync - Loading plugins from https://raw.githubusercontent.com/Flow-Launcher/Flow.Launcher.PluginsManifest/plugin_api_v2/plugins.json
13:19:35.7426-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Quick Uninstaller> is <247ms>
13:19:35.7834-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Unit converter> is <304ms>
13:19:36.0216-04:00 - INFO - CommunityPluginSource.FetchAsync - Loaded 113 plugins from https://cdn.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
13:19:36.0216-04:00 - INFO - CommunityPluginSource.FetchAsync - Loaded 113 plugins from https://fastly.jsdelivr.net/gh/Flow-Launcher/Flow.Launcher.PluginsManifest@plugin_api_v2/plugins.json
13:19:36.0216-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Plugins Manager> is <580ms>
13:19:36.3415-04:00 - INFO - PluginManager.InitializePlugins - Total init cost for <Dictionary> is <857ms>
13:19:36.6980-04:00 - INFO - App.OnStartup - Dependencies Info:
Python Path: C:\Users\zachy\AppData\Roaming\FlowLauncher\Environments\Python\PythonEmbeddable-v3.8.9\pythonw.exe
Node Path: C:\Users\zachy\AppData\Roaming\FlowLauncher\Environments\Node.js\Node-v16.18.0\node-v16.18.0-win-x64\node.exe
13:19:37.2870-04:00 - INFO - App.OnStartup - End Flow Launcher startup ----------------------------------------------------
13:19:37.2870-04:00 - INFO - App.OnStartup - Startup cost <3495ms>
13:19:38.4137-04:00 - INFO - ImageLoader.Initialize - Preload images cost <4064ms>
13:19:38.4137-04:00 - INFO - ImageLoader.Initialize - Number of preload images is <94>, Images Number: 94, Unique Items 59
13:19:39.0203-04:00 - INFO - Updater.UpdateApp - Future Release <{
"SHA1": "375B438F6693203DD599DDE0117294EF3AA743A0",
"BaseUrl": null,
"Filename": "FlowLauncher-1.16.1-full.nupkg",
"Query": null,
"Filesize": 93451616,
"IsDelta": false,
"StagingPercentage": null,
"EntryAsString": "375B438F6693203DD599DDE0117294EF3AA743A0 FlowLauncher-1.16.1-full.nupkg 93451616",
"Version": {
"Version": "1.16.1.0",
"SpecialVersion": ""
},
"PackageName": "FlowLauncher"
}>
18:19:36.8737-04:00 - INFO - Updater.UpdateApp - Future Release <{
"SHA1": "375B438F6693203DD599DDE0117294EF3AA743A0",
"BaseUrl": null,
"Filename": "FlowLauncher-1.16.1-full.nupkg",
"Query": null,
"Filesize": 93451616,
"IsDelta": false,
"StagingPercentage": null,
"EntryAsString": "375B438F6693203DD599DDE0117294EF3AA743A0 FlowLauncher-1.16.1-full.nupkg 93451616",
"Version": {
"Version": "1.16.1.0",
"SpecialVersion": ""
},
"PackageName": "FlowLauncher"
}>
23:19:35.0186-04:00 - ERROR - Updater.UpdateApp - Check your connection and proxy settings to github-cloud.s3.amazonaws.com.
EXCEPTION OCCURS: System.Net.Http.HttpRequestException: No such host is known. (api.github.com:443)
---> System.Net.Sockets.SocketException (11001): No such host is known.
at void System.Net.Sockets.Socket+AwaitableSocketAsyncEventArgs.ThrowException(SocketError error, CancellationToken cancellationToken)
at async bool System.Net.Sockets.Socket.ConnectAsync(SocketAsyncEventArgs e)+WaitForConnectWithCancellation(?)
at async ValueTask<Stream> System.Net.Http.HttpConnectionPool.ConnectToTcpHostAsync(string host, int port, HttpRequestMessage initialRequest, bool async, CancellationToken cancellationToken)
--- End of inner exception stack trace ---
at async ValueTask<Stream> System.Net.Http.HttpConnectionPool.ConnectToTcpHostAsync(string host, int port, HttpRequestMessage initialRequest, bool async, CancellationToken cancellationToken)
at async ValueTask<ValueTuple<Stream, TransportContext>> System.Net.Http.HttpConnectionPool.ConnectAsync(HttpRequestMessage request, bool async, CancellationToken cancellationToken)
at async ValueTask<HttpConnection> System.Net.Http.HttpConnectionPool.CreateHttp11ConnectionAsync(HttpRequestMessage request, bool async, CancellationToken cancellationToken)
at async Task System.Net.Http.HttpConnectionPool.AddHttp11ConnectionAsync(QueueItem queueItem)
at async ValueTask<T> System.Threading.Tasks.TaskCompletionSourceWithCancellation<T>.WaitWithCancellationAsync(CancellationToken cancellationToken)
at async ValueTask<T> System.Net.Http.HttpConnectionPool+HttpConnectionWaiter<T>.WaitForConnectionAsync(bool async, CancellationToken requestCancellationToken)
at async ValueTask<HttpResponseMessage> System.Net.Http.HttpConnectionPool.SendWithVersionDetectionAndRetryAsync(HttpRequestMessage request, bool async, bool doRequestAuth, CancellationToken cancellationToken)
at async ValueTask<HttpResponseMessage> System.Net.Http.RedirectHandler.SendAsync(HttpRequestMessage request, bool async, CancellationToken cancellationToken)
at async Task<Stream> System.Net.Http.HttpClient.GetStreamAsyncCore(HttpRequestMessage request, CancellationToken cancellationToken)
at async Task<Stream> Flow.Launcher.Infrastructure.Http.Http.GetStreamAsync(Uri url, CancellationToken token) in C:/projects/flow-launcher/Flow.Launcher.Infrastructure/Http/Http.cs:line 161
at async Task<UpdateManager> Flow.Launcher.Core.Updater.GitHubUpdateManagerAsync(string repository) in C:/projects/flow-launcher/Flow.Launcher.Core/Updater.cs:line 127
at async Task Flow.Launcher.Core.Updater.UpdateAppAsync(IPublicAPI api, bool silentUpdate) in C:/projects/flow-launcher/Flow.Launcher.Core/Updater.cs:line 43
```
</details>


---

<!-- source=github_issue; title=Game Crashes Whenever Entering A Battle Scene; url=https://github.com/suriyun-production/turnbase-rpg-docs/issues/246 -->

# Game Crashes Whenever Entering A Battle Scene

- Source: github_issue
- URL: https://github.com/suriyun-production/turnbase-rpg-docs/issues/246

As the title displays; "Game Crashes Whenever Entering A Battle Scene". I'm not missing any files, whether it be in a build or the unity editor; and upon entering the 'BattleScene', the game crashes! No log/or error is displayed.


---

<!-- source=github_issue; title=On Unity, compiling the Android version to il2cpp causes an ExecutionEngineException at runtime; url=https://github.com/aws/aws-sdk-net/issues/477 -->

# On Unity, compiling the Android version to il2cpp causes an ExecutionEngineException at runtime

- Source: github_issue
- URL: https://github.com/aws/aws-sdk-net/issues/477

My code is working fine on Android, with Mono, and on iOS with il2cpp but I wanted to try compiling my Unity game on Android with il2cpp, as it is now supported, but I have encountered an error which causes the UnityMainThreadDispatcher to be null.
In my GameController object I have a script which attaches the UnityInitialiser to itself, as instructed:
``` C#
UnityInitializer.AttachToGameObject(gameObject);
```
Compiling this and running it will cause this exception to occur:
```
I/Unity ( 7756): (Filename: ./artifacts/generated/Android/runtime/UnityEngineDebugBindings.gen.cpp Line: 45)
I/Unity ( 7756):
I/Unity ( 7756): ExecutionEngineException: Attempting to call method 'UnityEngine.AndroidJavaObject::Get' for which no ahead of time (AOT) code was generated.
I/Unity ( 7756):
I/Unity ( 7756): Rethrow as TargetInvocationException: Exception has been thrown by the target of an invocation.
```
Which disrupts the initialisation and UnityMainThreadDispatcher is not correctly added as a component to my GameController. (It will be null if I attempt to retrieve it).
Searching about this error lead me to [this](https://docs.unity3d.com/Manual/ScriptingRestrictions.html) (CTRL+F "ExecutionEngineException") if that helps.
It is hard for me to debug this more as I am just using the provided DLLs on a non-Windows machine. I am guessing this is just a case of Android il2cpp not being supported, if that is the case then I hope it will be supported in the future.


---

<!-- source=github_issue; title=Unity clients fail with IL2CPP builds; url=https://github.com/nats-io/nats.net.v1/issues/361 -->

# Unity clients fail with IL2CPP builds

- Source: github_issue
- URL: https://github.com/nats-io/nats.net.v1/issues/361

**Update:** The problem is with Unity. See https://github.com/nats-io/nats.net/issues/361#issuecomment-581632837 (below) for a workaround...
**Update 2:** The workaround doesn't work, at least on iOS devices.
**Update 3:** Got it to work. See https://github.com/nats-io/nats.net/issues/361#issuecomment-593048632 (below)...
**Update 4:** It still fails sometimes even when the `UseOldRequestStyle` option is `true`.
**Update 5:** The problem has been solved. See: https://github.com/nats-io/nats.net/pull/370
I have a Unity project using NATS that works fine if built using Mono on Android or if using IL2CPP development build. If built as a release build with IL2CPP for Android or iOS, the NATS connection disconnects on the second request/reply and attempts to reconnect.
This appears to be similar to issue #358.
Here's the NATS server log...
```
[8125] 2020/01/27 10:19:42.095095 [DBG] 66.60.161.134:40560 - cid:9 - Client connection created
[8125] 2020/01/27 10:19:42.158135 [TRC] 66.60.161.134:40560 - cid:9 - <<- [CONNECT {"verbose":false,"pedantic":false,"user":"","pass":"[REDACTED]","ssl_required":false,"name":"","auth_token":"","lang":".NET","version":"0.0.1","protocol":1,"jwt":"","nkey":"","sig":"","echo":false}]
[8125] 2020/01/27 10:19:42.158195 [TRC] 66.60.161.134:40560 - cid:9 - <<- [PING]
[8125] 2020/01/27 10:19:42.158216 [TRC] 66.60.161.134:40560 - cid:9 - ->> [PONG]
[8125] 2020/01/27 10:19:42.359824 [TRC] 66.60.161.134:40560 - cid:9 - <<- [SUB _INBOX.ec2db33d7faf4825ad7bba87047defaf.* 1]
[8125] 2020/01/27 10:19:42.359986 [TRC] 66.60.161.134:40560 - cid:9 - <<- [PUB Citizen.Login _INBOX.ec2db33d7faf4825ad7bba87047defaf.1 15]
[8125] 2020/01/27 10:19:42.360003 [TRC] 66.60.161.134:40560 - cid:9 - <<- MSG_PAYLOAD: ["\x92\xa4Frog\xa8blobblob"]
[8125] 2020/01/27 10:19:42.360016 [TRC] 127.0.0.1:45964 - cid:1 - ->> [MSG Citizen.Login 2 _INBOX.ec2db33d7faf4825ad7bba87047defaf.1 15]
[8125] 2020/01/27 10:19:42.361726 [TRC] 127.0.0.1:45964 - cid:1 - <<- [PONG]
[8125] 2020/01/27 10:19:42.361753 [TRC] 127.0.0.1:45964 - cid:1 - <<- [PUB _INBOX.ec2db33d7faf4825ad7bba87047defaf.1 11]
[8125] 2020/01/27 10:19:42.361767 [TRC] 127.0.0.1:45964 - cid:1 - <<- MSG_PAYLOAD: ["\x92\x00\xcf\x01\xf7\xf3w\xe6\x00\x00\x00"]
[8125] 2020/01/27 10:19:42.361786 [TRC] 66.60.161.134:40560 - cid:9 - ->> [MSG _INBOX.ec2db33d7faf4825ad7bba87047defaf.1 1 11]
[8125] 2020/01/27 10:19:42.804264 [TRC] 66.60.161.134:40560 - cid:9 - <<- [SUB Avatar.Pose.test 2]
[8125] 2020/01/27 10:19:42.804320 [TRC] 66.60.161.134:40560 - cid:9 - <<- [SUB Avatar.Select.test 3]
[8125] 2020/01/27 10:19:42.804352 [TRC] 66.60.161.134:40560 - cid:9 - <<- [SUB Prop.OnAdd.test 4]
[8125] 2020/01/27 10:19:42.804365 [TRC] 66.60.161.134:40560 - cid:9 - <<- [SUB Prop.OnMove.test 5]
[8125] 2020/01/27 10:19:42.804380 [TRC] 66.60.161.134:40560 - cid:9 - <<- [SUB Prop.OnRemove.test 6]
[8125] 2020/01/27 10:19:42.911325 [TRC] 66.60.161.134:40560 - cid:9 - <<- [PUB Prop.Look.test _INBOX.ec2db33d7faf4825ad7bba87047defaf.2 10]
[8125] 2020/01/27 10:19:42.911356 [TRC] 66.60.161.134:40560 - cid:9 - <<- MSG_PAYLOAD: ["\x91\xcf\x01\xf7\xf3w\xe6\x00\x00\x00"]
[8125] 2020/01/27 10:19:42.911371 [TRC] 127.0.0.1:46110 - cid:2 - ->> [MSG Prop.Look.test 2 _INBOX.ec2db33d7faf4825ad7bba87047defaf.2 10]
[8125] 2020/01/27 10:19:42.914473 [TRC] 127.0.0.1:46110 - cid:2 - <<- [PONG]
[8125] 2020/01/27 10:19:42.914499 [TRC] 127.0.0.1:46110 - cid:2 - <<- [PUB _INBOX.ec2db33d7faf4825ad7bba87047defaf.2 74]
[8125] 2020/01/27 10:19:42.914518 [TRC] 127.0.0.1:46110 - cid:2 - <<- MSG_PAYLOAD: ["\x92\x00\x81\xcf\x01\xeao_\x93\x01\x00\x00\x92\x02\x95\x93\xca\x00\x00\x00\x00\xca\x00\x00\x00\x00\xca\x00\x00\x00\x00\x94\xca\x00\x00\x00\x00\xca\x00\x00\x00\x00\xca\x00\x00\x00\x00\xca?\x80\x00\x00\xacTrackedImage\xa3Bar\xca>L\xcc\xcd"]
[8125] 2020/01/27 10:19:42.914534 [TRC] 66.60.161.134:40560 - cid:9 - ->> [MSG _INBOX.ec2db33d7faf4825ad7bba87047defaf.2 1 74]
[8125] 2020/01/27 10:19:42.967805 [DBG] 66.60.161.134:40560 - cid:9 - Client connection closed
[8125] 2020/01/27 10:19:42.967893 [TRC] 66.60.161.134:40560 - cid:9 - <-> [DELSUB 1]
[8125] 2020/01/27 10:19:42.967910 [TRC] 66.60.161.134:40560 - cid:9 - <-> [DELSUB 2]
[8125] 2020/01/27 10:19:42.967933 [TRC] 66.60.161.134:40560 - cid:9 - <-> [DELSUB 3]
[8125] 2020/01/27 10:19:42.967939 [TRC] 66.60.161.134:40560 - cid:9 - <-> [DELSUB 4]
[8125] 2020/01/27 10:19:42.967944 [TRC] 66.60.161.134:40560 - cid:9 - <-> [DELSUB 5]
[8125] 2020/01/27 10:19:42.967950 [TRC] 66.60.161.134:40560 - cid:9 - <-> [DELSUB 6]
[8125] 2020/01/27 10:19:43.241501 [DBG] 66.60.161.134:40562 - cid:10 - Client connection created
[8125] 2020/01/27 10:19:43.285678 [TRC] 66.60.161.134:40562 - cid:10 - <<- [CONNECT {"verbose":false,"pedantic":false,"user":"","pass":"[REDACTED]","ssl_required":false,"name":"","auth_token":"","lang":".NET","version":"0.0.1","protocol":1,"jwt":"","nkey":"","sig":"","echo":false}]
[8125] 2020/01/27 10:19:43.285773 [TRC] 66.60.161.134:40562 - cid:10 - <<- [PING]
[8125] 2020/01/27 10:19:43.285788 [TRC] 66.60.161.134:40562 - cid:10 - ->> [PONG]
[8125] 2020/01/27 10:19:43.352220 [TRC] 66.60.161.134:40562 - cid:10 - <<- [SUB _INBOX.ec2db33d7faf4825ad7bba87047defaf.* 1]
[8125] 2020/01/27 10:19:43.352270 [TRC] 66.60.161.134:40562 - cid:10 - <<- [SUB Avatar.Pose.test 2]
[8125] 2020/01/27 10:19:43.352300 [TRC] 66.60.161.134:40562 - cid:10 - <<- [SUB Avatar.Select.test 3]
[8125] 2020/01/27 10:19:43.352309 [TRC] 66.60.161.134:40562 - cid:10 - <<- [SUB Prop.OnAdd.test 4]
[8125] 2020/01/27 10:19:43.352374 [TRC] 66.60.161.134:40562 - cid:10 - <<- [SUB Prop.OnMove.test 5]
[8125] 2020/01/27 10:19:43.352406 [TRC] 66.60.161.134:40562 - cid:10 - <<- [SUB Prop.OnRemove.test 6]
[8125] 2020/01/27 10:19:43.444747 [TRC] 66.60.161.134:40562 - cid:10 - <<- [PING]
[8125] 2020/01/27 10:19:43.444806 [TRC] 66.60.161.134:40562 - cid:10 - ->> [PONG]
[8125] 2020/01/27 10:19:45.450564 [DBG] 66.60.161.134:40562 - cid:10 - Client Ping Timer
[8125] 2020/01/27 10:19:45.450651 [TRC] 66.60.161.134:40562 - cid:10 - ->> [PING]
```


---

<!-- source=github_issue; title=PostAsync method does not work in WebGL due to System.Reflection.Emit reference; url=https://github.com/graphql-dotnet/graphql-client/issues/133 -->

# PostAsync method does not work in WebGL due to System.Reflection.Emit reference

- Source: github_issue
- URL: https://github.com/graphql-dotnet/graphql-client/issues/133

I am trying to use graphql-client to build WebGL Client which communicates with graphql server.
Currently WebGL in Unity does not support System.Reflection.Emit.
Call from line https://github.com/graphql-dotnet/graphql-client/blob/9511133bc922af7ef0cb1f760b7885a9243275e2/src/GraphQL.Client.Http/Internal/GraphQLHttpHandler.cs#L65 is using Newtonsoft.Json which internally use not supported functionality from System.Reflection.Emit.
Here is Stack trace:
```
System.NotSupportedException: System.Reflection.Emit.DynamicMethod::.ctor
UnityLoader.js:1043 at System.Reflection.Emit.DynamicMethod..ctor (System.String name, System.Type returnType, System.Type[] parameterTypes, System.Type owner, System.Boolean skipVisibility) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.Utilities.DynamicReflectionDelegateFactory.CreateDynamicMethod (System.String name, System.Type returnType, System.Type[] parameterTypes, System.Type owner) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.Utilities.DynamicReflectionDelegateFactory.CreateDefaultConstructor[T] (System.Type type) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.Serialization.DefaultContractResolver.GetDefaultCreator (System.Type createdType) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.Serialization.DefaultContractResolver.InitializeContract (Newtonsoft.Json.Serialization.JsonContract contract) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.Serialization.DefaultContractResolver.CreateObjectContract (System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.Serialization.DefaultContractResolver.CreateContract (System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.Serialization.CamelCasePropertyNamesContractResolver.ResolveContract (System.Type type) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.GetContractSafe (System.Object value) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.Serialize (Newtonsoft.Json.JsonWriter jsonWriter, System.Object value, System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.JsonSerializer.SerializeInternal (Newtonsoft.Json.JsonWriter jsonWriter, System.Object value, System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.JsonSerializer.Serialize (Newtonsoft.Json.JsonWriter jsonWriter, System.Object value, System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.JsonConvert.SerializeObjectInternal (System.Object value, System.Type type, Newtonsoft.Json.JsonSerializer jsonSerializer) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.JsonConvert.SerializeObject (System.Object value, System.Type type, Newtonsoft.Json.JsonSerializerSettings settings) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at Newtonsoft.Json.JsonConvert.SerializeObject (System.Object value, Newtonsoft.Json.JsonSerializerSettings settings) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at GraphQL.Client.GraphQLClient+<PostAsync>d__22.MoveNext () [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1[TResult].Start[TStateMachine] (TStateMachine& stateMachine) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at GraphQL.Client.GraphQLClient.PostAsync (GraphQL.Common.Request.GraphQLRequest request, System.Threading.CancellationToken cancellationToken) [0x00000] in <00000000000000000000000000000000>:0
UnityLoader.js:1043 at GraphQL.Client.GraphQLClient.PostAsync (GraphQL.Common.Request.GraphQLRequest request) [0x00000] in <00000000000000000000000000000000>:0
```
Would it be possible to use another serialization/deserialization package, which would replace Newtonsoft.Json, which functionality is not supported in WebGL? (Going to try other one)
Maybe in the future there could be option to replace hardcoded Newtonsoft.json


---

<!-- source=github_issue; title=Vive input utility make all my actions not work anymore; url=https://github.com/ViveSoftware/ViveInputUtility-Unity/issues/154 -->

# Vive input utility make all my actions not work anymore

- Source: github_issue
- URL: https://github.com/ViveSoftware/ViveInputUtility-Unity/issues/154

I had all the actions working and after updating to last version in Unity all my actions dont work anymore. I can see them in vr input but dont work anymore
Related comments:
Found the reason, i see the bindings were deleted, i had to make them again
@dpggit bindings deleted? By who?
By Vive input when i updated


---

<!-- source=github_issue; title=Rider Inop in 2019.2b6?; url=https://github.com/JetBrains/resharper-unity/issues/1233 -->

# Rider Inop in 2019.2b6?

- Source: github_issue
- URL: https://github.com/JetBrains/resharper-unity/issues/1233

Rider version is latest as installed by Toolbox.
JetBrains Rider 2019.1.2
Build #RD-191.7141.355, built on June 4, 2019
Apologies if this has been reported, but I scanned the first few pages of issues and didn't see it which kind of surprised me.
I installed Unity 2019.2b6 from the Unity Hub, and created a new project from the HDRP template. When I go to Preferences -> External Tools or Preferences -> Rider, the preferences pane is blank and the log is spammed with Rider errors.
Manually loading the project in Rider, which in the past would auto install the Rider plugin also does not seem to do so anymore.
There are a lot of console errors and they dont' stop, so I'm not sure which ones are the right ones to post and which are knock ons.
```
NullReferenceException: Object reference not set to an instance of an object
Packages.Rider.Editor.EditorPluginInterop.InitEntryPoint () (at <072369e179f6469db1efdb207452957c>:0)
Packages.Rider.Editor.RiderInitializer.Initialize (System.String editorPath) (at <072369e179f6469db1efdb207452957c>:0)
Packages.Rider.Editor.RiderScriptEditor..cctor () (at <072369e179f6469db1efdb207452957c>:0)
Rethrow as TypeInitializationException: The type initializer for 'Packages.Rider.Editor.RiderScriptEditor' threw an exception.
Packages.Rider.Editor.PluginSettings+<>c.<RiderPreferencesItem>b__35_0 (System.String searchContext) (at <072369e179f6469db1efdb207452957c>:0)
UnityEditor.SettingsProvider.OnGUI (System.String searchContext) (at C:/buildslave/unity/build/Editor/Mono/Settings/SettingsProvider.cs:103)
UnityEditor.SettingsWindow.DrawControls () (at C:/buildslave/unity/build/Editor/Mono/Settings/SettingsWindow.cs:322)
UnityEditor.SettingsWindow.DrawSettingsPanel () (at C:/buildslave/unity/build/Editor/Mono/Settings/SettingsWindow.cs:313)
UnityEngine.UIElements.IMGUIContainer.DoOnGUI (UnityEngine.Event evt, UnityEngine.Matrix4x4 parentTransform, UnityEngine.Rect clippingRect, System.Boolean isComputingLayout, UnityEngine.Rect layoutSize) (at C:/buildslave/unity/build/Modules/UIElements/IMGUIContainer.cs:281)
UnityEngine.GUIUtility:ProcessEvent(Int32, IntPtr)
```


---

<!-- source=github_issue; title=System.NullReferenceException: Object reference not set to an instance of an object. in latest nuget; url=https://github.com/unitycontainer/microsoft-dependency-injection/issues/12 -->

# System.NullReferenceException: Object reference not set to an instance of an object. in latest nuget

- Source: github_issue
- URL: https://github.com/unitycontainer/microsoft-dependency-injection/issues/12

```
var c = new UnityContainer();
var spf = new ServiceProviderFactory(c);
var cc = spf.CreateBuilder(new ServiceCollection());
```
throws the following exceptions
```
Test Name: ShouldUseDefaultValue
Test FullName: SInnovations.ServiceFabric.Unity.UnitTests.UnitTest1.ShouldUseDefaultValue
Test Source: C:\dev\S-Innovations\S-Innovations.ServiceFabric.Unity\test\S-Innovations.ServiceFabric.Unity.UnitTests\UnitTest1.cs : line 33
Test Outcome: Failed
Test Duration: 0:00:00.1743851
Result StackTrace:
at Unity.Strategies.ArrayResolveStrategy.RequiredToBuildType(IUnityContainer container, INamedType namedType, InjectionMember[] injectionMembers)
at Unity.UnityContainer.GetBuilders(InternalRegistration registration)
at Unity.UnityContainer.CreateRegistration(Type type, String name, Type policyInterface, IBuilderPolicy policy)
at Unity.UnityContainer.Set(Type type, String name, Type policyInterface, IBuilderPolicy policy)
at Unity.UnityContainer.CreateAndSetPolicy(Type type, String name, Type policyInterface, IBuilderPolicy policy)
at Unity.UnityContainer.ContainerContext.Set(Type type, String name, Type policyInterface, IBuilderPolicy policy)
at Unity.Policy.PolicyListExtensions.SetDefault[TPolicyInterface](IPolicyList policies, TPolicyInterface policy)
at Unity.Microsoft.DependencyInjection.MdiExtension.Initialize()
at Unity.Extension.UnityContainerExtension.InitializeExtension(ExtensionContext context)
at Unity.UnityContainer.AddExtension(UnityContainerExtension extension)
at Unity.Microsoft.DependencyInjection.ServiceProviderFactory.CreateBuilder(IServiceCollection services)
at SInnovations.ServiceFabric.Unity.UnitTests.UnitTest1.ShouldUseDefaultValue()
Result Message:
Test method SInnovations.ServiceFabric.Unity.UnitTests.UnitTest1.ShouldUseDefaultValue threw exception:
System.NullReferenceException: Object reference not set to an instance of an object.
```


---

<!-- source=github_issue; title=Cast Exception when using EF5 (with Autofac?) and MVC; url=https://github.com/Glimpse/Glimpse/issues/321 -->

# Cast Exception when using EF5 (with Autofac?) and MVC

- Source: github_issue
- URL: https://github.com/Glimpse/Glimpse/issues/321

I'm using EF5 with the repository pattern - I have a Context and a bunch of interfaces and repository classes in my DAL project.
My MVC web project initialises by registering all my repo's and my DBFactory from the DAL project and all my controllers with Autofac.
Each Controller has constructor parameter(s) for the repo interfaces required. Autofac provides runtime instances.
When I turn on Glimpse my initial view crashes when it tries to display -
Unable to cast object of type 'Glimpse.Ado.AlternateType.GlimpseDbConnection' to type 'System.Data.SqlClient.SqlConnection'.
Glimpse works fine with just MVC, or MVC + Autofac. Only the addition of Glimpse.EF5 causes the problem.


---

<!-- source=github_issue; title=Bhaptic not triggering; url=https://github.com/Yellow-Dog-Man/Resonite-Issues/issues/5385 -->

# Bhaptic not triggering

- Source: github_issue
- URL: https://github.com/Yellow-Dog-Man/Resonite-Issues/issues/5385

### Describe the bug?
When interacting with any haptics, the Bhaptic gear does not trigger. Shows the point triggering in game, but the gear in real life does nothing.
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/d0e27c6a-6b9c-497e-abe1-bc8d7af9f92d" />
### To Reproduce
Turn on bhaptic gear, and move into haptic trigger.
### Reproduction Item/World
i suggest using items from here, due to them being all haptic resrec:///U-1NjOEykfqEq/R-8B1D6CA2B72144A3FBE938451609765825601CD626C9B015B23489F565F6B37D
### Expected behavior
haptic points on vest vibrate according to game
### Screenshots
<img width="1077" height="744" alt="Image" src="https://github.com/user-attachments/assets/fa493f70-7ed6-432b-be64-0ced718ccdfa" />
### Resonite Version Number
Beta 2025.8.22.607
### What Platforms does this occur on?
Windows
### What headset if any do you use?
quest 3
### Log Files
[DESKTOP-NHBNSCC - 2025.8.22.607 - 2025-08-23 07_23_15.log](https://github.com/user-attachments/files/21949042/DESKTOP-NHBNSCC.-.2025.8.22.607.-.2025-08-23.07_23_15.log)
### Additional Context
_No response_
### Reporters
navy3001


---

<!-- source=github_issue; title=Unable to use DocFx on Unity; url=https://github.com/NormandErwan/DocFxForUnity/issues/9 -->

# Unable to use DocFx on Unity

- Source: github_issue
- URL: https://github.com/NormandErwan/DocFxForUnity/issues/9

Hi, following your README instructions I can display some Scripting API site if I use your own repo.
But if I try to make the same steps on a new project (empty for the exception of 1 .cs script) that is not uploaded on github I get the following errors:
![image](https://user-images.githubusercontent.com/15261880/71646359-93fb2a00-2ce7-11ea-8974-f8811d8a4fdc.png)
I let the docfx.json exactly like yours and filterConfig.yml looks like:
![image](https://user-images.githubusercontent.com/15261880/71646366-b1c88f00-2ce7-11ea-99f6-c5d9f9f0990d.png)
Apparently seems to have one problem trying to create/find api folder, how can I solve this?
Thanks!


---

<!-- source=github_issue; title=[BUG] Solution explorer not showing; url=https://github.com/microsoft/vscode-dotnettools/issues/808 -->

# [BUG] Solution explorer not showing

- Source: github_issue
- URL: https://github.com/microsoft/vscode-dotnettools/issues/808

### Describe the Issue
Probably related to #704 (closed)
When opening the solution explorer the following error appears.
![image](https://github.com/microsoft/vscode-dotnettools/assets/122781544/3b36bc14-d0ed-4962-b71b-a58d87c157c3)
And the solution explorer will fail to open:
![image](https://github.com/microsoft/vscode-dotnettools/assets/122781544/1ef74576-346f-44fe-9429-3aae3809820d)
**C# log output**
```
Using dotnet configured on PATH
Dotnet path: C:\Program Files\dotnet\dotnet.exe
Activating C# + C# Dev Kit + C# IntelliCode...
waiting for named pipe information from server...
[stdout] {"pipeName":"\\\\.\\pipe\\e8f7761c"}
received named pipe information from server
attempting to connect client to server...
client has connected to server
[Info - 12:00:34 PM] [Program] Language server initialized
```
**C# Dev Kit log output:**
```
Starting Spawn .NET server...
Starting Open a solution...
Starting Open a solution with environment service...
Starting Clear environment...
Using preinstalled .NET runtime at "C:\Program Files\dotnet\dotnet.exe"
Using runtime installed in SDK.
.NET server started and IPC established in 1917ms
Completed Spawn .NET server (4392ms)
Completed Clear environment (4766ms)
Completed Open a solution with environment service (4811ms)
Starting Restore solution...
Completed Open a solution (4835ms)
Starting NuGet restore for the solution.
Starting command: "dotnet.exe" restore C:\src\mySolution.sln --interactive...
Failed to listen to project initialization status: Error: Activating the "Microsoft.VisualStudio.ProjectSystem.ProjectInitializationStatusService (0.1)" service failed.
Completed command: "dotnet.exe" restore C:\src\mySolution.sln --interactive (3076ms)
Completed NuGet restore.
Completed Restore solution (3079ms)
```
**C# Dev Kit - Text Explorer log output**
```
Created Test Controller
unable to create test controller for c# extension: Error: Activating the "Microsoft.VisualStudio.TestWindow.VSCode.Service (0.1)" service failed.
```
The `dotnet restore` failing might be related to https://github.com/dotnet/sdk/issues/10189 which I've resolved manually via https://github.com/dotnet/sdk/issues/10189#issuecomment-884117116 this however did not fix the solution explorer.
```
PS C:\src> iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/microsoft/artifacts-credprovider/master/helpers/installcredprovider.ps1'))
PS C:\src> dotnet restore .\mySolution.sln --interactive
Determining projects to restore...
All projects are up-to-date for restore.
PS C:\src>
```
### Steps To Reproduce
No specific reproduction steps known other than a clean install.
### Expected Behavior
No errors or UI bugs.
### Environment Information
- Windows 10 (22H2 19045.3693)
- VS Code (in portable mode; `data` directory)
![image](https://github.com/microsoft/vscode-dotnettools/assets/122781544/fe3a06d6-8eee-43cc-89af-5535ad6bc0fb)
- System also runs Visual Studio 2022
- dotnet sdk's
```
PS C:\src> dotnet --list-sdks
6.0.406 [C:\Program Files\dotnet\sdk]
7.0.200 [C:\Program Files\dotnet\sdk]
8.0.100 [C:\Program Files\dotnet\sdk]
```


---

<!-- source=github_issue; title=[Unity][S3] No way to measure download progress; url=https://github.com/aws/aws-sdk-net/issues/547 -->

# [Unity][S3] No way to measure download progress

- Source: github_issue
- URL: https://github.com/aws/aws-sdk-net/issues/547

Using GetObjectAsync() in the Unity package there is no callback to measure download progress as there is with PostObjectAsync(). There seems to be WriteObjectProgressEvent in the normal .Net S3 package but this is missing from the Unity package.


---

<!-- source=github_issue; title=Preventing being ran over by other mods; url=https://github.com/TweakScale/TweakScale/issues/31 -->

# Preventing being ran over by other mods

- Source: github_issue
- URL: https://github.com/TweakScale/TweakScale/issues/31

This isn't exact an issue but an Task.
Since some more Mods are currently mangling GameDatabase on the Main Menu Scene, and since TweakScale must be last of the Manglers on that event chain, and since TweakScale **needs** to have their internal affairs in order **before** the user loads a savegame (what's inevitably happens before loading the Space Center!) due the prefab being applied too on craft from savegames (novelty on 1.5.1 **or** 1.6.1, last time I checked it I was playing 1.4.x).


---

<!-- source=github_issue; title=Cannot build AAR on Windows; url=https://github.com/homuler/MediaPipeUnityPlugin/issues/80 -->

# Cannot build AAR on Windows

- Source: github_issue
- URL: https://github.com/homuler/MediaPipeUnityPlugin/issues/80

I've run it successfully in windows ,
but Build android libraries has a error.
hope you can give me some suggest.
`ERROR: C:/msys64/home/wujinliang/_bazel_wujinliang/2pedqfuc/external/XNNPACK/BUILD.bazel:4629:19: Compiling src/subgraph/leaky-relu.c failed: (Exit 1): clang failed: error executing command external/androidndk/ndk/toolchains/llvm/prebuilt/windows-x86_64/bin/clang -gcc-toolchain external/androidndk/ndk/toolchains/aarch64-linux-android-4.9/prebuilt/windows-x86_64 -target ... (remaining 112 argument(s) skipped)
clang: error: no such file or directory: '/w'
clang: error: no such file or directory: '/D_USE_MATH_DEFINES'
INFO: Elapsed time: 275.955s, Critical Path: 133.97s
INFO: 1378 processes: 619 internal, 759 local.
FAILED: Build did NOT complete successfully
make: *** [Makefile:52: android_arm64] Error 1`


---

<!-- source=github_issue; title=Dooblys big ̶d̶̶̶a̶̶̶y̶̶̶ days of bug squashin B: 220; url=https://github.com/unitystation/unitystation/issues/3863 -->

# Dooblys big ̶d̶̶̶a̶̶̶y̶̶̶ days of bug squashin B: 220

- Source: github_issue
- URL: https://github.com/unitystation/unitystation/issues/3863

Throw your bugs in this thread and I'll squash them so help me god:
Current bugs:
- Wirecutters no longer work - done
- Department battery NRE spam -done
- Can't throw in space - done
- Machine connector is broken - not doing this one, it is going to be apart of a job to simplify wiring
- Camera focus is lost when entering cupboard of dna scanner - done
- Cloner doesn't work on pog - not broken, works on latest
- Pog directional windows are rotated for no reason - done


---

<!-- source=github_issue; title=[PLEASE READ] Some Unity v6.3 games imcompatibility; url=https://github.com/yukieiji/UnityExplorer/issues/104 -->

# [PLEASE READ] Some Unity v6.3 games imcompatibility

- Source: github_issue
- URL: https://github.com/yukieiji/UnityExplorer/issues/104

> [!Important]
> PLEASE READ ALL SECTIONS THOROUGHLY BEFORE CREATING A NEW TICKET.
## Overview
Certain Unity v6.3 games are currently incompatible with UE.
Due to various underlying technical complexities, these cannot be addressed simply as bugs within the UE core. A coordinated fix involving integration with `Il2CppInerOps` and `Mono` is required.
All the proposed fixes for these issues are complex and would significantly increase technical debt. While they are easy to merge, the long-term support and maintenance costs make them completely unacceptable.
This ticket will serve as a guideline for handling breaking changes leading up to Unity v6.8(The version in which Mono is deprecated).
If we were to create a dedicated UE for v6.3 now, it would imply that I must do the same whenever another breaking change occurs in v6.4 or beyond. This would ultimately mean managing up to **70 different UE variants** (since I currently have 14 variants, maintaining them across 5 specific Unity versions would multiply the workload by five).
### Confirmed Incompatible Games
- My Dystopian Robot Girlfriend
- RUMBLE
- Polytoria
- skinface
- Eminence in Shadow - Master of Garden
- ATLYSS
- The Planet Crafter
- Rhythm Doctor
- MallRivals
## Issues
### System.MissingMethodException: Method not found: 'System.String UnityEngine.SceneManagement.Scene.GetNameInternal(Int32)'
Cause: This is due to the `Screen` handle being changed to a specialized type in recent Unity updates.
I have fixed the bug where internal APIs prone to breaking changes were being called directly. However, my analysis confirms that although an implicit conversion to `int` is defined, it is currently failing to trigger. Consequently, even the officially supported external APIs are non-functional.
#### Related Tickets
#105 , #102 , #100 , #95 , #94 , #85 , #81
### `AssetBundle.XXX` can't work
Resolved in [v4.13.6](https://github.com/yukieiji/UnityExplorer/releases/tag/v4.13.6)
~~Cause: Due to optimizations, the `AssetBundle` loading logic has been transitioned to the `Span` family. This change is not being handled correctly, leading to numerous reports specifically in Il2Cpp-based games. While a provisional workaround has been implemented, stable operation is not yet guaranteed.~~
~~#### Related Tickets~~
~~https://github.com/BepInEx/Il2CppInterop/issues/202~~
~~#103 , #92 , #89 , #88 , #75~~


---

<!-- source=github_issue; title=Quest 2 Crashes on Selecting NDI Source - Unity 2022 Build; url=https://github.com/keijiro/KlakNDI/issues/200 -->

# Quest 2 Crashes on Selecting NDI Source - Unity 2022 Build

- Source: github_issue
- URL: https://github.com/keijiro/KlakNDI/issues/200

Upon selecting an NDI source on Quest 2, the system crashes instead of rendering the source.
This was tested with many different variables, the constant one being Unity version:
- The sample Klak NDI scene that comes with the package (with a dropdown, receiver, sender, and canvas to render the video)
- Unity 2022.3.4f1
- Android API 30, 31, 32, 33
- URP
- No URP
- ARM64
- NDI Launcher Tools Test Pattern for Windows, same Wi-fi network
- NDI Launcher Tools VLC video that is confirmed to work in Editor and Standalone builds
- MSAA on
- MSAA off
- Color Space: Gamma
- Color Space: Linear
- Graphics API: OpenGLES3 (which works in our 2020 version of the project)
Notes:
1. NDI rendering works fine in Editor (2022) and in desktop standalone builds (Windows, Mac).
2. Our project includes the changes from [PR191](https://github.com/keijiro/KlakNDI/pull/191), which were needed in order to detect sources in API 31+.
3. Also includes changes from [PR186](https://github.com/keijiro/KlakNDI/pull/186).
4. The changes from PR191 and PR186 work when we make builds from Unity 2020, API 30, 31, 32.
Logcat logs from when I select an NDI source:
![ndiScene_systemLogsQuest](https://github.com/keijiro/KlakNDI/assets/10697313/3cdaacc0-6749-4b49-a1fc-c3d4b48e6310)
Any suggestions or help would be greatly appreciated. We want to update our project to Unity 2022, but we need NDI streaming to work on Quest 2 builds.
Thanks in advance!


---

<!-- source=github_issue; title=AuthServiceDemo. GetCurrentUser I always get a null pointer exception.; url=https://github.com/EvilMindDevs/hms-unity-plugin/issues/352 -->

# AuthServiceDemo. GetCurrentUser I always get a null pointer exception.

- Source: github_issue
- URL: https://github.com/EvilMindDevs/hms-unity-plugin/issues/352

I have a similar issue when trying to run the AuthServiceDemo. I always get a null pointer exception.
Steps Done:
1- Creating an App in the AppConnect
2- Creating Keystore for my Unity Project and adding the SHA key to the App in the AppConnect
3- Enablilng the Auth Service, Game Service, and Account Service Kits
4- Making and API Key
5- Installing Unity HMS Plugin, enabling the kits mentioned, connected the API, and obtained a token
6- Adjusting the AndroidManifest.xml with the app id, cpid, and package name (also updated the package name in Unity) and added the providers (not sure of the variables though as it wasn't clear in any forum or documentation)
7- Re-installing the agconnect-service.json after enabling the kits
What am I missing? Why does it always give me a null pointer exception when trying to call any built in functions from the package such as authServiceManager.GetCurrentUser()
Here is the error:
NullReferenceException: Object reference not set to an instance of an object
HuaweiMobileServices.Utils.JavaObjectWrapper.Call[T] (System.String methodName, System.Object[] args) (at <d01331c41e7b42f29a927fdf5bb0c9bc>:0)
HuaweiMobileServices.Utils.JavaObjectWrapper.CallAsWrapper[T] (System.String methodName, System.Object[] args) (at <d01331c41e7b42f29a927fdf5bb0c9bc>:0)
HuaweiMobileServices.AuthService.AGConnectAuth.GetCurrentUser () (at <d01331c41e7b42f29a927fdf5bb0c9bc>:0)
HmsPlugin.HMSAuthServiceManager.GetCurrentUser () (at Assets/Huawei/Scripts/AuthService/HMSAuthServiceManager.cs:83)
AuthServiceDemo.Start () (at Assets/Huawei/Demos/AuthService/AuthServiceDemo.cs:50)
Can you please help me with this? I tried disabling the kits, restarting Unity, then enabling them again. Didn't work
_Originally posted by @CarolineEhabAnwar in https://github.com/EvilMindDevs/hms-unity-plugin/issues/341#issuecomment-1213074485_


---

<!-- source=github_issue; title=KSP 1.9.x resets resources to prefab while cloning parts; url=https://github.com/net-lisias-ksp/KSP-Recall/issues/1 -->

# KSP 1.9.x resets resources to prefab while cloning parts

- Source: github_issue
- URL: https://github.com/net-lisias-ksp/KSP-Recall/issues/1

Tried updating to 1.9 since most mods behave reasonably on updates nowadays. Began noticing some parts drifting each time I loaded my craft (either in flight or VAB). Seems any parts that have been tweaked start to wander when loading.
Also noticed that when copying a part that had been altered, the new part retained the correct appearance and size, but was given the default values for the original part. (FL-T400 tank scaled to 3.75 has almost 2k LOx, copy has 360). Tweakscale seems to be applying itself at the wrong time or somehow affecting the "assembly order" upon load in. The most interesting fact is that if I load a craft and a part wanders, then reload the same craft without saving, the part will have wandered farther than before.
I am using other mods such as mechjeb, but afaik none would be interfering with TS or craft loading. Hope I have been of some service, TS has been very nice to me, would like to return the favor.


---

<!-- source=github_issue; title=Unity package path & dlls; url=https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/34 -->

# Unity package path & dlls

- Source: github_issue
- URL: https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/34

I know there is no common practice for this but, that would be nice if like some other packages, MLAPI would target a `Plugins/MLAPI` path when installing.
Related comments:
The reason I did not do this was that I was unable to put the Gizmos folder anywhere except the root folder.
If you know how to get around this, I'd gladly fix it.
Oh i see.
I use a few packages that use gizmos out of the root folder, so it's definitely possible, i'll try to find a way.
_"You can only have one Gizmos folder and it must be placed in the root of the Project; directly within the Assets folder. Place the needed Asset files in this Gizmos folder or a subfolder within it. Always include the subfolder path in the path passed to the Gizmos.DrawIcon function if your Asset files are in subfolders."_
https://docs.unity3d.com/Manual/SpecialFolders.html
But FinalIK somehow have it in their Plugins folder.


---

<!-- source=github_issue; title=Unity 2019 UWP Hololens compatibility; url=https://github.com/dwhit/ros-sharp/issues/3 -->

# Unity 2019 UWP Hololens compatibility

- Source: github_issue
- URL: https://github.com/dwhit/ros-sharp/issues/3

The README instructions mention using the 2017 version of MRTK, which is not compatible with Unity 2019.x out of the box. MRTKv2 works fine but does not include the Newtonsoft.json.dlls needed by this repository (at least for commits before the 2019 update on master). I noticed that by default the Newtonsoft.json.dll included in this repo is now set to "any platforms" which leads me to think the dependency on MRTK 2017 has been removed? When I try to build for the Hololens using Unity 2019.1.7f1, the latest version of MRTKv2 (RC2.1), and the latest commit on master for this repository (4ccf45fc) I see the following error when running in debug mode on the Hololens. Everything works fine in the Editor:
```
NotSupportedException: System.Reflection.Emit.DynamicMethod::.ctor
at System.Reflection.Emit.DynamicMethod..ctor (System.String name, System.Type returnType, System.Type[] parameterTypes, System.Type owner, System.Boolean skipVisibility) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Utilities.DynamicReflectionDelegateFactory.CreateDynamicMethod (System.String name, System.Type returnType, System.Type[] parameterTypes, System.Type owner) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Utilities.DynamicReflectionDelegateFactory.CreateGet[T] (System.Reflection.FieldInfo fieldInfo) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Utilities.ReflectionDelegateFactory.CreateGet[T] (System.Reflection.MemberInfo memberInfo) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Serialization.DynamicValueProvider.GetValue (System.Object target) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.CalculatePropertyValues (Newtonsoft.Json.JsonWriter writer, System.Object value, Newtonsoft.Json.Serialization.JsonContainerContract contract, Newtonsoft.Json.Serialization.JsonProperty member, Newtonsoft.Json.Serialization.JsonProperty property, Newtonsoft.Json.Serialization.JsonContract& memberContract, System.Object& memberValue) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.SerializeObject (Newtonsoft.Json.JsonWriter writer, System.Object value, Newtonsoft.Json.Serialization.JsonObjectContract contract, Newtonsoft.Json.Serialization.JsonProperty member, Newtonsoft.Json.Serialization.JsonContainerContract collectionContract, Newtonsoft.Json.Serialization.JsonProperty containerProperty) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.SerializeValue (Newtonsoft.Json.JsonWriter writer, System.Object value, Newtonsoft.Json.Serialization.JsonContract valueContract, Newtonsoft.Json.Serialization.JsonProperty member, Newtonsoft.Json.Serialization.JsonContainerContract containerContract, Newtonsoft.Json.Serialization.JsonProperty containerProperty) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.Serialize (Newtonsoft.Json.JsonWriter jsonWriter, System.Object value, System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.JsonSerializer.SerializeInternal (Newtonsoft.Json.JsonWriter jsonWriter, System.Object value, System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.JsonSerializer.Serialize (Newtonsoft.Json.JsonWriter jsonWriter, System.Object value, System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.JsonConvert.SerializeObjectInternal (System.Object value, System.Type type, Newtonsoft.Json.JsonSerializer jsonSerializer) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.JsonConvert.SerializeObject (System.Object value, System.Type type, Newtonsoft.Json.JsonSerializerSettings settings) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.JsonConvert.SerializeObject (System.Object value) [0x00000] in <00000000000000000000000000000000>:0
at RosSharp.RosBridgeClient.RosSocket.Serialize[T] (T obj) [0x00000] in <00000000000000000000000000000000>:0
at RosSharp.RosBridgeClient.RosSocket.Send[T] (T communication) [0x00000] in <00000000000000000000000000000000>:0
at RosSharp.RosBridgeClient.RosSocket.Subscribe[T] (System.String topic, RosSharp.RosBridgeClient.SubscriptionHandler`1[T] subscriptionHandler, System.Int32 throttle_rate, System.Int32 queue_length, System.Int32 fragment_size, System.String compression) [0x00000] in <00000000000000000000000000000000>:0
at RosSharp.RosBridgeClient.Subscriber`1[T].Start () [0x00000] in <00000000000000000000000000000000>:0
...
Rethrow as JsonSerializationException: Error getting value from 'topic' on 'RosSharp.RosBridgeClient.Subscription'.
at Newtonsoft.Json.Serialization.DynamicValueProvider.GetValue (System.Object target) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.CalculatePropertyValues (Newtonsoft.Json.JsonWriter writer, System.Object value, Newtonsoft.Json.Serialization.JsonContainerContract contract, Newtonsoft.Json.Serialization.JsonProperty member, Newtonsoft.Json.Serialization.JsonProperty property, Newtonsoft.Json.Serialization.JsonContract& memberContract, System.Object& memberValue) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.SerializeObject (Newtonsoft.Json.JsonWriter writer, System.Object value, Newtonsoft.Json.Serialization.JsonObjectContract contract, Newtonsoft.Json.Serialization.JsonProperty member, Newtonsoft.Json.Serialization.JsonContainerContract collectionContract, Newtonsoft.Json.Serialization.JsonProperty containerProperty) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.SerializeValue (Newtonsoft.Json.JsonWriter writer, System.Object value, Newtonsoft.Json.Serialization.JsonContract valueContract, Newtonsoft.Json.Serialization.JsonProperty member, Newtonsoft.Json.Serialization.JsonContainerContract containerContract, Newtonsoft.Json.Serialization.JsonProperty containerProperty) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.Serialize (Newtonsoft.Json.JsonWriter jsonWriter, System.Object value, System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.JsonSerializer.SerializeInternal (Newtonsoft.Json.JsonWriter jsonWriter, System.Object value, System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.JsonSerializer.Serialize (Newtonsoft.Json.JsonWriter jsonWriter, System.Object value, System.Type objectType) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.JsonConvert.SerializeObjectInternal (System.Object value, System.Type type, Newtonsoft.Json.JsonSerializer jsonSerializer) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.JsonConvert.SerializeObject (System.Object value, System.Type type, Newtonsoft.Json.JsonSerializerSettings settings) [0x00000] in <00000000000000000000000000000000>:0
at Newtonsoft.Json.JsonConvert.SerializeObject (System.Object value) [0x00000] in <00000000000000000000000000000000>:0
at RosSharp.RosBridgeClient.RosSocket.Serialize[T] (T obj) [0x00000] in <00000000000000000000000000000000>:0
at RosSharp.RosBridgeClient.RosSocket.Send[T] (T communication) [0x00000] in <00000000000000000000000000000000>:0
at RosSharp.RosBridgeClient.RosSocket.Subscribe[T] (System.String topic, RosSharp.RosBridgeClient.SubscriptionHandler`1[T] subscriptionHandler, System.Int32 throttle_rate, System.Int32 queue_length, System.Int32 fragment_size, System.String compression) [0x00000] in <00000000000000000000000000000000>:0
at RosSharp.RosBridgeClient.Subscriber`1[T].Start () [0x00000] in <00000000000000000000000000000000>:0
...
```
After doing some poking around it seems like this might be an issue related to the IL2CPP scripting backend ( Unity 2019.1 deprecates the .NET scripting backend). Not sure if there's a few steps missing from the README, or if the Newtonsoft.json.dll needs to be updated. Any help is greatly appreciated!


---

<!-- source=github_issue; title=[LSP] languageserver not working with vim/neovim+lsp plugins; url=https://github.com/OmniSharp/omnisharp-roslyn/issues/1191 -->

# [LSP] languageserver not working with vim/neovim+lsp plugins

- Source: github_issue
- URL: https://github.com/OmniSharp/omnisharp-roslyn/issues/1191

The version I use is the prebuilt binary package downloaded from github release page, v1.30.1 omnisharp-mono.tar.gz. linux-x86_64 package behaves exactly the same. Here is the relevant configurations in my .vimrc:
```
let g:LanguageClient_serverCommands = {
\ 'cs': ['mono', '/opt/omnisharp-roslyn/OmniSharp.exe', '--languageserver', '--verbose'],
\ }
let g:LanguageClient_rootMarkers = {
\ 'cs': ['.git', '*.csproj'],
\ }
let g:deoplete#enable_at_startup = 1
let g:LanguageClient_loggingLevel = 'DEBUG'
let g:LanguageClient_loadSettings = 0
```
And here is the relevant log when error occurs:
```
17:31:24 INFO reader-cs src/vim.rs:379 <= Some("cs") {"protocolVersion":"2.0","method":"window/logMessage","params":{"type":4,"message":"Starting server..."}}
17:31:24 ERROR reader-cs src/vim.rs:384 Failed to deserialize output: data did not match any variant of untagged enum RawMessage
Message: {"protocolVersion":"2.0","method":"window/logMessage","params":{"type":4,"message":"Starting server..."}}
Error: ErrorImpl { code: Message("data did not match any variant of untagged enum RawMessage"), line: 0, column: 0 }
...
17:31:24 INFO main src/vim.rs:90 => Some("cs") {"jsonrpc":"2.0","method":"initialize","params":{"capabilities":{"textDocument":{"completion":{"completionItem":{"commitCharactersSupport":null,"documentationFormat":null,"snippetSupport":false},"dynamicRegistration":null}}},"initializationOptions":null,"processId":24814,"rootPath":"/home/shihira/Program/Unity/Vitruvius","rootUri":"file:///home/shihira/Program/Unity/Vitruvius","trace":"off"},"id":9}
Unhandled Exception:
Newtonsoft.Json.JsonSerializationException: Error converting value {null} to type 'System.Boolean'. Path 'params.capabilities.textDocument.completion.dynamicRegistration', line 1, position 221. ---> System.InvalidCastException: Null object cannot be converted to a value type.
at System.Convert.ChangeType (System.Object value, System.Type conversionType, System.IFormatProvider provider) [0x00029] in <cae080c8689e4af39d0ab2b313d012f5>:0
at Newtonsoft.Json.Serialization.JsonSerializerInternalReader.EnsureType (Newtonsoft.Json.JsonReader reader, System.Object value, System.Globalization.CultureInfo culture, Newtonsoft.Json.Serialization.JsonContract contract, System.Type targetType) [0x000aa] in <dc86da7fc46c487ba6c7ab826da479cc>:0
--- End of inner exception stack trace ---
...
17:31:37 WARN main src/languageclient.rs:1910 Failed to start language server automatically. timed out waiting on channel
```
I noticed the key "protocolVersion", which is usually "jsonrpc" in many other LSPs. Is it the reason why LanguageClient failed to deserialize it?
Another problem causes the server crashing. I believe this is about what's been mentioned and solved in <https://github.com/OmniSharp/csharp-language-server-protocol/issues/75>. If that's true please merge them.
Thank you for your great work.


---

<!-- source=github_issue; title=NullReferenceException: Object reference not set to an instance of an object Unity.Netcode.FixedStringSerializer`1[T].WriteDelta; url=https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/2920 -->

# NullReferenceException: Object reference not set to an instance of an object Unity.Netcode.FixedStringSerializer`1[T].WriteDelta

- Source: github_issue
- URL: https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/2920

### Description
It's hard to be precise with this issue as I'm unsure exactly what's causing it.
But in one of my scenes, I get the following error:
![Screenshot 2024-05-07 114130](https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/assets/22588585/25bb0a2f-aa59-4162-a874-7e4a64bd7fe5)
It continuously spams the log while the game is playing.
I've attempted to track down which object it is related to, and I've managed to delete an object, and even a script, which then stops the issue, but then it seems to come back again after a restart related to a different object. I couldn't track down any code that could've caused this - and with the stacktrace being entirely inside of Netcode, it's hard to figure it out.
The weird part is, as far as I remember, I had netcode 1.9.1 working in this exact scene with no errors for a while. I keep a full git history, so I went back to a point where it was working previously, and it is no longer working.
I've deleted the Library, obj and other folders and still no luck.
There are cases where I've been trying to narrow down the object thats creating this bug - and I play the game with that object deleted, and still get the bug. But then I play the game again, and then the bug isn't there - and I haven't changed anything since the last play.
If I leave said object deleted, restart Unity, then the first play will have this error, subsequent ones will not...
This scene works completely fine in NGO 1.7.1 & 1.8.1
### Environment
Windows 11
NGO 1.9.1
Unity 2023.2.9f1


---

<!-- source=github_issue; title=[10.0.4][Server/User issue] Black Screen when logging in. Only server restart fixes it.; url=https://github.com/StrangeLoopGames/EcoIssues/issues/24511 -->

# [10.0.4][Server/User issue] Black Screen when logging in. Only server restart fixes it.

- Source: github_issue
- URL: https://github.com/StrangeLoopGames/EcoIssues/issues/24511

Version 0.10.0.3 beta release-547
Sometimes when players are logging in they get just the UI and see black screen.
It happens randomly to some people. They can be fine for several days and then that one time when they log-in they get black screen and they will not be able to properly play until server is restarted.
They can still chat with everyone, they just can't see what they are doing.
Other people don't see their avatars, just their names.
I've received Player.log from 2 people affected by this:
[Player (8).log](https://github.com/StrangeLoopGames/EcoIssues/files/13812491/Player.8.log)
[Player (7).log](https://github.com/StrangeLoopGames/EcoIssues/files/13812493/Player.7.log)
Both player.log files have this kind common of error:
```
Uploading Crash Report
ArgumentNullException: Value cannot be null.
Parameter name: source
at System.Linq.Enumerable.FirstOrDefault[TSource] (System.Collections.Generic.IEnumerable`1[T] source) [0x00000] in <00000000000000000000000000000000>:0
at Eco.Client.Tools.Utility.AvatarAttachedItemsDisplayer.UpdateAttachedItems () [0x00000] in <00000000000000000000000000000000>:0
at Eco.Client.PlayerAvatar.Components.AvatarSkeleton.CacheBoneMap () [0x00000] in <00000000000000000000000000000000>:0
at Eco.Shared.Utils.Initializer.Initialize () [0x00000] in <00000000000000000000000000000000>:0
at Eco.Avatar.Avatar.CreateAvatar (Eco.Avatar.Avatar avatarPrefab, UnityEngine.GameObject parentObject, UnityEngine.GameObject playerObject, AvatarView avatarView, ClothingInventoryView clothingView, SelectionInventoryView toolbarView, UserView avatarUser) [0x00000] in <00000000000000000000000000000000>:0
at ThirdPersonController.Initialize () [0x00000] in <00000000000000000000000000000000>:0
at Eco.UI.ConnectionUI.<FadeAndClose>b__66_0 () [0x00000] in <00000000000000000000000000000000>:0
at Fader.DoComplete () [0x00000] in <00000000000000000000000000000000>:0
EcoEngine.Logging.LogManager:LogException(Exception, Object)
UnityEngine.Logger:LogException(Exception, Object)
UnityEngine.Debug:LogException(Exception)
Eco.Shared.Utils.Log:WriteErrorPrivate(String, Exception, Boolean)
Eco.Shared.Utils.Log:WriteError(LocString, Exception, Boolean)
Fader:DoComplete()
```
Logging into the game from a completely diffrent PC that never had Eco installed on it does not fix the issue.


---

<!-- source=github_issue; title=Server wont start since new update; url=https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/2935 -->

# Server wont start since new update

- Source: github_issue
- URL: https://github.com/SmartlyDressedGames/Unturned-3.x-Community/issues/2935

(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)
NullReferenceException: Object reference not set to an instance of an object
at SDG.Unturned.Provider.listenClient () [0x0000f] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.listen () [0x00568] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
at SDG.Unturned.Provider.Update () [0x000b9] in <f26d1dadc8834d62b8f7bf7a2fe293ca>:0
(Filename: <f26d1dadc8834d62b8f7bf7a2fe293ca> Line: 0)


---

<!-- source=github_issue; title=D435i hand tracking Python; url=https://github.com/realsenseai/librealsense/issues/7877 -->

# D435i hand tracking Python

- Source: github_issue
- URL: https://github.com/realsenseai/librealsense/issues/7877

Hi everyone and @MartyG-RealSense ))
I'm not sure what I'm writing in the right section, but how can I use hand tracking?
I saw your project for C++. Maybe there is one for python?
The essence of the task is to control the tablet with your hands.
Required Info |
-- | --
Camera Model | D435i
Operating System & Version | Windows 10
Language | Python 3.7
And another question about the camera, in the description of the D435i it is written that it has a built-in neural network for recognizing objects, including hands. What does it mean? Or it applies exclusively to the SDK. Did I understand correctly that if, for example, I work with a camera using python, then I need to search for datasets myself and write code for recognition? Or does the realsense library already have everything?


---

<!-- source=github_issue; title=NREs in pointer inspectors; url=https://github.com/XRTK/com.xrtk.sdk/issues/89 -->

# NREs in pointer inspectors

- Source: github_issue
- URL: https://github.com/XRTK/com.xrtk.sdk/issues/89

# XRTK - Mixed Reality Toolkit Bug Report
## Describe the bug
Errors when Right_DefaultControllerPointer(Clone) or Right_ParabolicPointer(Clone) are selected in scene during play mode. UWP or OpenVR mode
## To Reproduce
1. Unity Hub > New project > 3D
2. Modify manifest to include `"com.xrtk.core": "https://github.com/XRTK/XRTK-Core.git#0.1.18"`,
3. Press Play
4. Under MixedRealityPlayspace GO select one of the pointer objects and view their configurations in the inspector.
## Expected behavior
Does not show error. I believe these were rendering a line in previous version of XRTK. I'm not sure what the purpose of these objects are
## Actual behavior
If I click that Right_DefaultControllerPointer(Clone)
```
NullReferenceException: Object reference not set to an instance of an object
UnityEditor.PropertyHandler.OnGUILayout (UnityEditor.SerializedProperty property, UnityEngine.GUIContent label, System.Boolean includeChildren, UnityEngine.GUILayoutOption[] options) (at C:/buildslave/unity/build/Editor/Mono/ScriptAttributeGUI/PropertyHandler.cs:203)
UnityEditor.EditorGUILayout.PropertyField (UnityEditor.SerializedProperty property, UnityEngine.GUIContent label, System.Boolean includeChildren, UnityEngine.GUILayoutOption[] options) (at C:/buildslave/unity/build/Editor/Mono/EditorGUI.cs:9341)
UnityEditor.EditorGUILayout.PropertyField (UnityEditor.SerializedProperty property, UnityEngine.GUILayoutOption[] options) (at C:/buildslave/unity/build/Editor/Mono/EditorGUI.cs:9325)
XRTK.SDK.Inspectors.UX.Pointers.BaseControllerPointerInspector.OnInspectorGUI () (at Library/PackageCache/com.xrtk.sdk@2a5ea7c69c675a92e54c82216e78960289cc1bf2/Inspectors/UX/Pointers/BaseControllerPointerInspector.cs:65)
XRTK.SDK.Inspectors.UX.Pointers.LinePointerInspector.OnInspectorGUI () (at Library/PackageCache/com.xrtk.sdk@2a5ea7c69c675a92e54c82216e78960289cc1bf2/Inspectors/UX/Pointers/LinePointerInspector.cs:40)
UnityEditor.UIElements.InspectorElement+<CreateIMGUIInspectorFromEditor>c__AnonStorey1.<>m__0 () (at C:/buildslave/unity/build/Editor/Mono/Inspector/InspectorElement.cs:462)
UnityEngine.GUIUtility:ProcessEvent(Int32, IntPtr)
```
If I click Right_ParabolicPointer(Clone)
```
NullReferenceException: Object reference not set to an instance of an object
UnityEditor.PropertyHandler.OnGUILayout (UnityEditor.SerializedProperty property, UnityEngine.GUIContent label, System.Boolean includeChildren, UnityEngine.GUILayoutOption[] options) (at C:/buildslave/unity/build/Editor/Mono/ScriptAttributeGUI/PropertyHandler.cs:203)
UnityEditor.EditorGUILayout.PropertyField (UnityEditor.SerializedProperty property, UnityEngine.GUIContent label, System.Boolean includeChildren, UnityEngine.GUILayoutOption[] options) (at C:/buildslave/unity/build/Editor/Mono/EditorGUI.cs:9341)
UnityEditor.EditorGUILayout.PropertyField (UnityEditor.SerializedProperty property, UnityEngine.GUILayoutOption[] options) (at C:/buildslave/unity/build/Editor/Mono/EditorGUI.cs:9325)
XRTK.SDK.Inspectors.UX.Pointers.BaseControllerPointerInspector.OnInspectorGUI () (at Library/PackageCache/com.xrtk.sdk@2a5ea7c69c675a92e54c82216e78960289cc1bf2/Inspectors/UX/Pointers/BaseControllerPointerInspector.cs:65)
XRTK.SDK.Inspectors.UX.Pointers.LinePointerInspector.OnInspectorGUI () (at Library/PackageCache/com.xrtk.sdk@2a5ea7c69c675a92e54c82216e78960289cc1bf2/Inspectors/UX/Pointers/LinePointerInspector.cs:40)
XRTK.SDK.Inspectors.UX.Pointers.TeleportPointerInspector.OnInspectorGUI () (at Library/PackageCache/com.xrtk.sdk@2a5ea7c69c675a92e54c82216e78960289cc1bf2/Inspectors/UX/Pointers/TeleportPointerInspector.cs:48)
XRTK.SDK.Inspectors.UX.Pointers.ParabolicTeleportPointerInspector.OnInspectorGUI () (at Library/PackageCache/com.xrtk.sdk@2a5ea7c69c675a92e54c82216e78960289cc1bf2/Inspectors/UX/Pointers/ParabolicTeleportPointerInspector.cs:28)
UnityEditor.UIElements.InspectorElement+<CreateIMGUIInspectorFromEditor>c__AnonStorey1.<>m__0 () (at C:/buildslave/unity/build/Editor/Mono/Inspector/InspectorElement.cs:462)
UnityEngine.GUIUtility:ProcessEvent(Int32, IntPtr)
```
thrown at each frame
## Screenshots
![Screenshot (78)](https://user-images.githubusercontent.com/5231547/64831588-678a9900-d5a4-11e9-8038-ccf19239f177.png)
## Your Setup (please complete the following information)
- Unity Version 2019.1.14f1
- XRTK Version e.g. 0.1.8
## Target Platform (please complete the following information)
- WMR immersive
- OpenVR
## Additional context
- HP Windows Mixed Reality headset
- Win 1903


---

<!-- source=github_issue; title=zh-cn zh-tw; url=https://github.com/bbepis/XUnity.AutoTranslator/issues/2 -->

# zh-cn zh-tw

- Source: github_issue
- URL: https://github.com/bbepis/XUnity.AutoTranslator/issues/2

it will take chinese as japanese,so it will translate many times.
Related comments:
+1
if the target language is set to zh-cn or zh-tw, it will take the translated text as untranslated because the program will check if the text is in japanese which contains chinese characters.
however, i think the real reason why it will translate multiple times is that we have many hooks installed, so an extra translating sequence will be triggered after the first one.
to solve it, we should check if the text is in `_translatedTexts` in `shouldTranslate` method in `XUnity.AutoTranslator/src/XUnity.AutoTranslator.Plugin.Core/AutoTranslationPlugin.cs`.
more over, i think we should't check whether a text is in japanese, or the `FromLanguage` setting will be useless.
Two things:
1. Which version was this a problem in? From 3.3.0+, an anti-spam safeguard was implemented that *SHOULD* prevent the exact thing that is described here. Basically, it is the function "IsTranslatable":
```C#
private bool IsTranslatable( string str )
{
return TextHelper.ContainsJapaneseSymbols( str ) && str.Length <= Settings.MaxCharactersPerTranslation && !_translatedTexts.Contains( str );
}
```
As you can can see, there is a check that disallows the plugin from translating something that is has already translated something else into. (the exact solution described by Tidyzq, except it is in a different method).
2. I see your point about ContainsJapanese. Tbh, I hope there is a better way to implement this, but the check is rather important right now because often games outputs a crapton of trash to text UI (depending on the game!), that there is no meaning in translating.
Here's a solution I see. If the FromLanguage is ja(-JP), then the check will be made. If we really want this to be generic, we should consider adding a check for languages that uses different alphabets. Perhaps this is overkill though. :)
Could you try the following version and report back with whether or not you have the same problem, as you previously reported?
[XUnity.AutoTranslator-IPA-2.3.2.zip](https://github.com/bbepis/XUnity.AutoTranslator/files/1964259/XUnity.AutoTranslator-IPA-2.3.2.zip)
[XUnity.AutoTranslator-BepIn-2.3.2.zip](https://github.com/bbepis/XUnity.AutoTranslator/files/1964260/XUnity.AutoTranslator-BepIn-2.3.2.zip)
The fix Tidyzq suggested is absolutely present in this version (although it should have been present in 2.3.0 as well). In addition I have changed the "ContainsJapaneseCharacters" check to a check that is based on the "FromLanguage" param.


---

<!-- source=github_issue; title=New Mk1 Cockpit IVA; url=https://github.com/Mihara/RasterPropMonitor/issues/428 -->

# New Mk1 Cockpit IVA

- Source: github_issue
- URL: https://github.com/Mihara/RasterPropMonitor/issues/428

The new IVA model requires a new RPM IVA...
Related comments:
Whats the criteria? I can quickly put one together if you want
The only requirement I have is that is uses the props that come in the basic RPM package (the repurposed Squad IVA props + the MFDs alexustas made). It can't have external dependencies, such as ASET props / avionics. It'd be nice to have one or two MFDs, but from the 5 minutes I spent in that cockpit, it's really cramped, so there may not be room for more than one.
ok, I'm having problems with unity and my computer hard crashing.
I found the issue. When I try and open the mk1cockpit unity stops responding then task manager shows that unity starts using more and more memory until it get to 100% at which point my computer is a brick, the off button wouldn't even work.
After removing the power cable and battery then restarting the computer unity won't work with part tools at all now. So I'm reinstalling unity!


---

<!-- source=github_issue; title=Update 2.75.5 breaks saving the game; url=https://github.com/Touhma/DSP_Galactic_Scale/issues/250 -->

# Update 2.75.5 breaks saving the game

- Source: github_issue
- URL: https://github.com/Touhma/DSP_Galactic_Scale/issues/250

Hi Galactic Scale Team,
Since the update to 2.75.5 i cannot save my game anymore.
Whenever the game autosaves, I get the following error message:
```ini
Error report: Game version 0.10.32.25783 with 67 mods used.
possible candidates: [Galactic Scale 2 Plug-In2.75.5][Galactic Scale 2 Nebula Compatibility Plug-In1.0.0.0]
NullReferenceException: Object reference not set to an instance of an object
GalacticScale.PatchOnUnspecified_Debug.ExportRuntime_Prefix (PlanetData __instance); (IL_000F)
PlanetData.ExportRuntime (System.IO.BinaryWriter w); (IL_0005)
PlanetFactory.Export (System.IO.Stream s, System.IO.BinaryWriter w); (IL_0054)
GameData.Export (System.IO.BinaryWriter w); (IL_017A)
GameSave.SaveCurrentGame (string saveName); (IL_028E)
UnityEngine.Debug:LogException(Exception)
GameSave:SaveCurrentGame(String)
GameSave:AutoSave()
UIAutoSave:_OnLateUpdate()
ManualBehaviour:_LateUpdate()
UIGame:_OnLateUpdate()
ManualBehaviour:_LateUpdate()
UIRoot:_OnLateUpdate()
ManualBehaviour:_LateUpdate()
UIRunner:LateUpdate()
[== Mods on stack trace ==]: [GalacticScale]
bool GalacticScale.PatchOnUnspecified_Debug::ExportRuntime_Prefix(PlanetData __instance); ExportRuntime(Prefix)
```
And manually saving either breaks the savegame, or fails with a message that it failed and I should check the permissions (although I think it just reacts to the underlying issue).
I would really like to know whether this is fixable or if somebody else experiences this problem.


---

<!-- source=github_issue; title=Use ARCamera as input for MediaPipe?; url=https://github.com/homuler/MediaPipeUnityPlugin/issues/343 -->

# Use ARCamera as input for MediaPipe?

- Source: github_issue
- URL: https://github.com/homuler/MediaPipeUnityPlugin/issues/343

Hi,
So for a project I'm working on I got the mediapipe sample to work with the webcam as done in the Sample project as well. However in my project I use the ARCameraManager from Unity to render the camera image to the screen. I need this camera because I am also trying to get the depth from this camera.
This is currently giving me issues as MediaPipe tries to start and access the webcam, while ARCamera is already using the camera. I tried to make the MediaPipe sample to work with the ARCamera but failed. It's tightly coupled to the webcam as for now. Is there any input or help I could get regarding this issue? Perhaps someone has already managed to get it to work with the ARFoundation ARCameraManager?
In short what I'm trying to achieve: Give MediaPipe the texture2D I get from ARCameraManager(I managed to get this texture already) and get the pose from that source.


---

<!-- source=github_issue; title=V2 - Deferred Alpha 2 - Train bypasses station and halts with "no longer has stations selected" & Potential Null Exception; url=https://github.com/Erabior/RouteManager/issues/67 -->

# V2 - Deferred Alpha 2 - Train bypasses station and halts with "no longer has stations selected" & Potential Null Exception

- Source: github_issue
- URL: https://github.com/Erabior/RouteManager/issues/67

Went to test [V2.0 Alpha 1](https://github.com/Erabior/RouteManager/releases/tag/2.0.0.x_Alpha-1) today. Train was at the coal/water in Whittier with full passenger load from Whittier. Toggled all stations (Whittier, Ela, Bryson, Hemingway, Alarka Jct) then enabled route manager. Train backed up some then went correct direction. Everything but Whittier and Ela were unchecked on passengers cars. I saw and fixed so passengers were not lost. I also unchecked Whittier on route list to attempt to avoid it going back there after Ela. Drove right past Whittier to Ela. Stopped at Ela and never continued after exchanging passengers.
When I saw it wasn't going anywhere I turned route manager off and back on. It proceeded to uncheck everything but Whittier (which was still unchecked on the route manager list) on the passenger cars so I gave up and quit to menu at that point.
[railloader.log](https://github.com/Erabior/RouteManager/files/13839689/railloader.log)
I decided to give it another try, and moved the train up to Whittier station first. Selected all stations again, and enabled route manager. It immediately unchecked all but Whittier and Ela again. Backed up a little, went forward, and completely ignored Whittier again to go to Ela. When it got to Ela it just sat and never moved again.
[railloader.log](https://github.com/Erabior/RouteManager/files/13839910/railloader.log)


---

<!-- source=github_issue; title=The com3d2 mod seems not work with version 1.55-, maybe consider work out two version of the plugin?; url=https://github.com/Sauceke/LoveMachine/issues/92 -->

# The com3d2 mod seems not work with version 1.55-, maybe consider work out two version of the plugin?

- Source: github_issue
- URL: https://github.com/Sauceke/LoveMachine/issues/92

When I play animation the game always show me the error:
[Error :LoveMachine] Coroutine failed with exception: System.NullReferenceException: Object reference not set to an instance of an object
at LoveMachine.COM3D2.Com3d2ButtplugController.GetFemaleBones (Int32 girlIndex) [0x00000] in <filename unknown>:0
at LoveMachine.Core.AnimationAnalyzer+<AnalyzeAnimation>d__16.MoveNext () [0x00000] in <filename unknown>:0
at LoveMachine.Core.CoroutineHandler.TryNext (IEnumerator coroutine, Boolean suppressExceptions) [0x00000] in <filename unknown>:0
my game version is 1.551
Because COM3D2 works different with the version under 1.555 and above 2.0.0, maybe considered work out two version of the game?


---

<!-- source=github_issue; title=안녕하세요 InfiniteScroll 시스템 중 Dynamic Item Size에 대한 궁금증입니다.; url=https://github.com/nhn/gpm.unity/issues/165 -->

# 안녕하세요 InfiniteScroll 시스템 중 Dynamic Item Size에 대한 궁금증입니다.

- Source: github_issue
- URL: https://github.com/nhn/gpm.unity/issues/165

<!--
When it comes to write an issue, please, use the template below.
To use the template is mandatory for submit new issue and we won't reply the issue that without the template.
To make it easier for us to help you, please include as much useful information as possible.
And you can write template's contents in Korean also.
Before opening a new issue, please search existing issues.
https://github.com/nhn/gpm.unity/issues
-->
## Service
* [ ] Adapter
* [ ] AssetManagement
* [ ] Communicator
* [ ] DLST
* [ ] LogViewer
* [ ] Manager
* [x] UI
* [ ] WebView
## Version
2.0.7
## Summary
가변길이의 텍스트를 스크롤로 출력하려고 하는데 잘 구현되지 않아 질문 드립니다.
## Screenshots
![InfiniteScrollItem](https://user-images.githubusercontent.com/89391503/142808964-5175533a-8bab-4153-8977-560ee78414db.PNG)
## Additional context
제가 구현하고자 하는 시스템은 가변길이의 텍스트를 스크롤로 출력 기능입니다.
해당 텍스트는 스크린샷과 같이 텍스트 갯수에 따라 가변적으로 오브젝트 사이즈가 늘어나도록
UGUI에서 자동으로 정렬해주는 컴포넌트인
Contents Size Filter 및 Vertical Layout Group 두가지를 부착하였습니다.
ex1) 오브젝트1의 텍스트는 3라인의 길이 : 높이가 150size
ex2) 오브젝트2의 텍스트는 2라인의 길이 : 높이가 100size
즉 이러한 오브젝트 10개를 텍스트 길이에 따라 가변적으로 InfiniteScroll을 구현하려고 했는데
에러로 인해 잘 구현이 되지 않아서
현재 제가 생각하고있는 기능이 InfiniteScroll을 통해 구현이 가능한 것인지
혹은 다른 방법을 통해 구현할 수 있을지 도움을 얻고자 문의 드립니다.
(에러는 InsertData호출 시 itemShowDataIndex변수가 null이라는 에러였습니다.)


---

<!-- source=github_issue; title=Sample scenes not working in 1.1.4; url=https://github.com/push-pop/Unity-MVVM/issues/78 -->

# Sample scenes not working in 1.1.4

- Source: github_issue
- URL: https://github.com/push-pop/Unity-MVVM/issues/78

I've got these errors in sample scenes:
```
NullReferenceException: Object reference not set to an instance of an object
UnityMVVM.Binding.DataBindingBase.FindViewModel () (at Library/PackageCache/com.push-pop.unitymvvm@6ea25b4f7d/Scripts/Binding/DataBindingBase.cs:78)
UnityMVVM.Binding.DataBindingBase.Awake () (at Library/PackageCache/com.push-pop.unitymvvm@6ea25b4f7d/Scripts/Binding/DataBindingBase.cs:100)
```


---

<!-- source=github_issue; title=Matmul error - shapes (4,) and (4, 4) not aligned!; url=https://github.com/Quansight-Labs/numpy.net/issues/11 -->

# Matmul error - shapes (4,) and (4, 4) not aligned!

- Source: github_issue
- URL: https://github.com/Quansight-Labs/numpy.net/issues/11

Sorry to bother you, I found another difference with Numpy.NET results, maybe a bug.
Your library gives me error, while the other gives me the result.
Code with your library:
```
public static double _get_lambda_next(ndarray am, ndarray bs, ndarray bm, ndarray cs, ndarray cm, ndarray rq)
{
Console.WriteLine($"\n rq :\n{rq}");
Console.WriteLine($"\n rq.T :\n{rq.T}");
Console.WriteLine($"\n am :\n{am}");
var temp1 = np.matmul(rq.T, am);
Console.WriteLine($"\n np.matmul(rq.T, am) :\n{temp1}");
var expr_1 = np.matmul(np.matmul(rq.T, am), rq);
var expr_2 = (1 / cs) * np.matmul(np.matmul(np.matmul(rq.T, bm.T), cm), rq);
var expr_3 = (1 / cs) * np.matmul(np.matmul(np.matmul(rq.T, cm.T), cm), rq);
var lambda_next = (expr_1 - expr_2) / (bs - expr_3);
return getFloatValue((ndarray)lambda_next);
}
```
Code with Numpy.NET:
```
public static float _get_lambda_next(NDarray am, NDarray bs, NDarray bm, NDarray cs, NDarray cm, NDarray rq) {
Console.WriteLine($"\n rq :\n{rq}");
Console.WriteLine($"\n rq.T :\n{rq.T}");
Console.WriteLine($"\n am :\n{am}");
var temp1 = np.matmul(rq.T, am);
Console.WriteLine($"\n np.matmul(rq.T, am) :\n{temp1}");
var expr_1 = np.matmul(np.matmul(rq.T, am), rq);
var expr_2 = (1 / cs) * np.matmul(np.matmul(np.matmul(rq.T, bm.T), cm), rq);
var expr_3 = (1 / cs) * np.matmul(np.matmul(np.matmul(rq.T, cm.T), cm), rq);
var lambda_next = (expr_1 - expr_2) / (bs - expr_3);
return getFloatValue(lambda_next);
}
```
You library's results to the left, the Numpy.NET ones to the right:
![image](https://user-images.githubusercontent.com/69966660/115013392-450fde80-9eb1-11eb-9914-33e74deb3256.png)
Here the error your library gives:
![image](https://user-images.githubusercontent.com/69966660/115013598-899b7a00-9eb1-11eb-8685-1301f5ba6df3.png)


---

<!-- source=github_issue; title=Not correctly using Watson service URLs; url=https://github.com/snhwang/Unity-Watson-STT-Assistant-TTS/issues/1 -->

# Not correctly using Watson service URLs

- Source: github_issue
- URL: https://github.com/snhwang/Unity-Watson-STT-Assistant-TTS/issues/1

As of 01/28/2020 7PM CDT time zone, this Unity Project works with Unity 2017.2.8f1, IBM Unity SDK 4.1.1, and Unity SDK core 1.2.0. I'm pretty sure it will work with IBM Unity SDK 4.3.0. You just need to delete the unity-sdk-4.1.1 folder and replace it with unity-sdk-4.3.0. I fixed the mistake of not using the Watson service URLs correctly. So, it should now work with different IBM cloud regions. I've only tried it using the Dallas, Washington DC, and London regions.


---

<!-- source=github_issue; title=Cannot export to fbx anymore with 2018.3b10; url=https://github.com/LogicalError/realtime-CSG-for-unity/issues/277 -->

# Cannot export to fbx anymore with 2018.3b10

- Source: github_issue
- URL: https://github.com/LogicalError/realtime-CSG-for-unity/issues/277

Exporting any model to the fbx fails with the following errors:
> NullReferenceException: Object reference not set to an instance of an object
InternalRealtimeCSG.GeneratedMeshInstance.OnEnable () (at Assets/Plugins/RealtimeCSG/Runtime/Scripts/Components/GeneratedMeshInstance.cs:186)
UnityEngine.Object:Instantiate(GameObject, Vector3, Quaternion)
InternalRealtimeCSG.MeshInstanceManager:Export(CSGModel, ExportType, Boolean) (at Assets/Plugins/RealtimeCSG/Editor/Scripts/Control/Managers/MeshInstanceManager.Export.cs:113)
RealtimeCSG.CSGModelComponentInspectorGUI:OnInspectorGUI(Object[]) (at Assets/Plugins/RealtimeCSG/Editor/Scripts/View/GUI/ComponentEditorWindows/CSGModelComponent.Inspector.GUI.cs:370)
RealtimeCSG.EditModeSelectionGUI:OnInspectorGUI(Editor, Object[]) (at Assets/Plugins/RealtimeCSG/Editor/Scripts/View/GUI/EditModeGUI/EditModeSelection.GUI.cs:244)
EditModeToolWindowEditor:OnInspectorGUI() (at Assets/Plugins/RealtimeCSG/Editor/Scripts/View/GUI/EditModeGUI/EditModeToolWindow.Editor.cs:15)
UnityEngine.GUIUtility:ProcessEvent(Int32, IntPtr)
> Mesh indices of Floor_1_Diffuse (1) are out of range!
UnityEditor.AssetDatabase:ImportAsset()
UnityFBXExporter.FBXExporter:ExportGameObjToFBX(GameObject, String, Boolean, Boolean, Boolean) (at Assets/Plugins/RealtimeCSG/Editor/Thirdparty/UnityFBXExporter/FBXExporter.cs:78)
InternalRealtimeCSG.MeshInstanceManager:Export(CSGModel, ExportType, Boolean) (at Assets/Plugins/RealtimeCSG/Editor/Scripts/Control/Managers/MeshInstanceManager.Export.cs:233)
RealtimeCSG.CSGModelComponentInspectorGUI:OnInspectorGUI(Object[]) (at Assets/Plugins/RealtimeCSG/Editor/Scripts/View/GUI/ComponentEditorWindows/CSGModelComponent.Inspector.GUI.cs:370)
RealtimeCSG.EditModeSelectionGUI:OnInspectorGUI(Editor, Object[]) (at Assets/Plugins/RealtimeCSG/Editor/Scripts/View/GUI/EditModeGUI/EditModeSelection.GUI.cs:244)
EditModeToolWindowEditor:OnInspectorGUI() (at Assets/Plugins/RealtimeCSG/Editor/Scripts/View/GUI/EditModeGUI/EditModeToolWindow.Editor.cs:15)
UnityEngine.GUIUtility:ProcessEvent(Int32, IntPtr)
This is on 2018.3b10 & RealtimeCSG v1.540
Nothing too fancy on the model as well. It's plain cube with 20 verts. This happens to any model I try to export. Exporting produces empty fbx with 0 tris / verts.


---

<!-- source=github_issue; title=No sound heard if audio source clips through solid geometry; url=https://github.com/ValveSoftware/steam-audio/issues/12 -->

# No sound heard if audio source clips through solid geometry

- Source: github_issue
- URL: https://github.com/ValveSoftware/steam-audio/issues/12

Example here: http://steamcommunity.com/app/596420/discussions/0/133258092241133882/
Related comments:
Just to be clear, the entire sound engine crashes. No sound from any audiosource is heard after this point.
Any ETA when this will be fixed now that its reproduced?
The fix will be available with next release. Until then, consider using raycast occlusion instead of partial occlusion to sidestep the issue.


---

<!-- source=github_issue; title=Jar Resolver (provided in 0.9.35) doesn't work; url=https://github.com/playgameservices/play-games-plugin-for-unity/issues/1428 -->

# Jar Resolver (provided in 0.9.35) doesn't work

- Source: github_issue
- URL: https://github.com/playgameservices/play-games-plugin-for-unity/issues/1428

I've removed old `play-services-*-8.4.0.aar`s, restarted Unity. Manually invoked menu item Assets > Play Services Resolver > Android Resolver > Resolve Client Jars. No `play-services-*-9.6.1.aar`s appeared.
```
KeyNotFoundException: The given key was not present in the dictionary.
System.Collections.Generic.Dictionary`2[System.String,System.Collections.Generic.HashSet`1[System.String]].get_Item (System.String key) (at /Users/builduser/buildslave/mono/build/mcs/class/corlib/System.Collections.Generic/Dictionary.cs:150)
Google.JarResolver.PlayServicesSupport.ResolveDependencies (Boolean useLatest)
GooglePlayServices.ResolverVer1_1.DoResolutionNoAndroidPackageChecks (Google.JarResolver.PlayServicesSupport svcSupport, System.String destinationDirectory, Google.JarResolver.OverwriteConfirmation handleOverwriteConfirmation)
GooglePlayServices.ResolverVer1_1+<DoResolution>c__AnonStorey1.<>m__0 ()
GooglePlayServices.ResolverVer1_1.DoResolution (Google.JarResolver.PlayServicesSupport svcSupport, System.String destinationDirectory, Google.JarResolver.OverwriteConfirmation handleOverwriteConfirmation, System.Action resolutionComplete)
GooglePlayServices.PlayServicesResolver.Resolve (System.Action resolutionComplete)
GooglePlayServices.PlayServicesResolver.MenuResolve ()
```
---
Unity 5.3.6p6 on Windows 10 Pro targeting Android. Latest Android SDK installed with all components updated via Android SDK Manager.


---

<!-- source=github_issue; title=Node Editor in Android; url=https://github.com/Seneral/Node_Editor_Framework/issues/55 -->

# Node Editor in Android

- Source: github_issue
- URL: https://github.com/Seneral/Node_Editor_Framework/issues/55

Hi everyone :)
I am trying to build a Android application with Node Editor features to perform basic logical application (e.g. if / else)
However since Smartphone only allows pressing operation, I am trying to figure out how to add node (e.g. AllRoundNode) by pressing a button on SideGui() as demonstrated in RunTimeNodeEditor.
Could anyone please guide me a way to achieve such operation? I am a bit lost after reading the "ContextCallback" function ....


---

<!-- source=github_issue; title=Can't build in Unity; url=https://github.com/JoshClose/CsvHelper/issues/1390 -->

# Can't build in Unity

- Source: github_issue
- URL: https://github.com/JoshClose/CsvHelper/issues/1390

I've import dll from example Untiy project.
Version : Unity 2017.4.15 with .NET46
It's works in Editor . But can't pass build .
Maybe because the dlls requeires net45 or netstandard
I reprogrammed the CsvHelper project with Net4.6 and disabled System.ValueTuple . Reimported to Unity ,then it works.


---

<!-- source=github_issue; title=[BUG] KeyNotFoundException: The given key was not present in the dictionary; url=https://github.com/ValveSoftware/steamvr_unity_plugin/issues/596 -->

# [BUG] KeyNotFoundException: The given key was not present in the dictionary

- Source: github_issue
- URL: https://github.com/ValveSoftware/steamvr_unity_plugin/issues/596

I created binding for both the Valve and Index controller for my project and ran into an issue with steam seeming to try and bind to another project. (Restarting SteamVR and/or the PC then reopening the project from the Unity HUB seemed to work but now any time i open any project I get a key binding error.
```
KeyNotFoundException: The given key was not present in the dictionary.
System.Collections.Generic.Dictionary`2[TKey,TValue].get_Item (TKey key) (at <ad04dee02e7e4a85a1299c7ee81c79f6>:0)
Valve.VR.SteamVR_Input.GetBaseActionFromPath (System.String path, System.Boolean caseSensitive) (at Assets/SteamVR/Input/SteamVR_Input.cs:470)
Valve.VR.SteamVR_Action.FindExistingActionForPartialPath (System.String path) (at Assets/SteamVR/Input/SteamVR_Action.cs:521)
Valve.VR.SteamVR_Action`2[SourceMap,SourceElement].TryNeedsInitData () (at Assets/SteamVR/Input/SteamVR_Action.cs:134)
Valve.VR.SteamVR_Action`2[SourceMap,SourceElement].InitAfterDeserialize () (at Assets/SteamVR/Input/SteamVR_Action.cs:219)
Valve.VR.SteamVR_Action_Vector2.UnityEngine.ISerializationCallbackReceiver.OnAfterDeserialize () (at Assets/SteamVR/Input/SteamVR_Action_Vector2.cs:179)
```
and
```
KeyNotFoundException: The given key was not present in the dictionary.
System.Collections.Generic.Dictionary`2[TKey,TValue].get_Item (TKey key) (at <ad04dee02e7e4a85a1299c7ee81c79f6>:0)
Valve.VR.SteamVR_Input.GetBaseActionFromPath (System.String path, System.Boolean caseSensitive) (at Assets/SteamVR/Input/SteamVR_Input.cs:470)
Valve.VR.SteamVR_Action.FindExistingActionForPartialPath (System.String path) (at Assets/SteamVR/Input/SteamVR_Action.cs:521)
Valve.VR.SteamVR_Action`2[SourceMap,SourceElement].TryNeedsInitData () (at Assets/SteamVR/Input/SteamVR_Action.cs:134)
Valve.VR.SteamVR_Action`2[SourceMap,SourceElement].InitAfterDeserialize () (at Assets/SteamVR/Input/SteamVR_Action.cs:219)
Valve.VR.SteamVR_Action_Boolean.UnityEngine.ISerializationCallbackReceiver.OnAfterDeserialize () (at Assets/SteamVR/Input/SteamVR_Action_Boolean.cs:222)
```
Also while the binding is set up in the web dashboard on the left controller and mirrored to the right controller for some reason only the right controller works and the left controller can only be used to teleport?
This was made in Unity 2019.2.2


---

<!-- source=github_issue; title=[Issue] Map markers disappearing after exiting and entering world; url=https://github.com/Mydayyy/Valheim-ServerSideMap/issues/47 -->

# [Issue] Map markers disappearing after exiting and entering world

- Source: github_issue
- URL: https://github.com/Mydayyy/Valheim-ServerSideMap/issues/47

Hey Mydayyy :)
Since the Mistlands update, the markers you place on the map are no longer shared or even saved. You can place them and they'll be gone the next time you log in.
**Reproducing**
1. Enable the `EnableMarkerShare` in the config file
2. Go into a world
3. Place some markers
4. Log out
5. Log back in, and realize the markers are gone
I guess you probably don't maintain this mod anymore, but I'd really appreciate it if you had the time to look into it.
Thanks a lot!


---

<!-- source=github_issue; title=Null reference exception in WebGL glb export but works fine in Editor; url=https://github.com/KhronosGroup/UnityGLTF/issues/782 -->

# Null reference exception in WebGL glb export but works fine in Editor

- Source: github_issue
- URL: https://github.com/KhronosGroup/UnityGLTF/issues/782

I am working on a Unity WebGL project. My scene consists of a single lightweight model with a standard material. I am exporting at runtime the object as a byte array to send it after to a web API. Everything works correctly in the editor but not in the browser after the build.
```
public GLTFSettings settings;
public GameObject objectToExport;
public void ExportToGLB()
{
var exportContext = new ExportContext(settings);
GLTFSceneExporter gltfExporter = new GLTFSceneExporter(new[] { objectToExport.transform }, exportContext);
Debug.Log(gltfExporter);
byte[] glbData = gltfExporter.SaveGLBToByteArray("CustomedModel");
Debug.Log(glbData.Length);
StartCoroutine(ExportAndUploadGLB(glbData));
}
```
After debugging, the error seems to occur during the call to SaveGLBToByteArray (the second Debug.Log() does not appear in the console) and appears in the console as :
```
NullReferenceException: Object reference not set to an instance of an object.
at UnityGLTF.Plugins.CanvasExportContext.AfterNodeExport (UnityGLTF.GLTFSceneExporter exporter, GLTF.Schema.GLTFRoot root, UnityEngine.Transform transform, GLTF.Schema.Node node) [0x00000] in <00000000000000000000000000000000>:0
at UnityGLTF.GLTFSceneExporter.ExportNode (UnityEngine.Transform nodeTransform) [0x00000] in <00000000000000000000000000000000>:0
at UnityGLTF.GLTFSceneExporter.ExportNode (UnityEngine.Transform nodeTransform) [0x00000] in <00000000000000000000000000000000>:0
at UnityGLTF.GLTFSceneExporter.ExportNode (UnityEngine.Transform nodeTransform) [0x00000] in <00000000000000000000000000000000>:0
at UnityGLTF.GLTFSceneExporter.ExportNode (UnityEngine.Transform nodeTransform) [0x00000] in <00000000000000000000000000000000>:0
at UnityGLTF.GLTFSceneExporter.ExportScene (System.String name, UnityEngine.Transform[] rootObjTransforms) [0x00000] in <00000000000000000000000000000000>:0
at UnityGLTF.GLTFSceneExporter.SaveGLBToStream (System.IO.Stream stream, System.String sceneName) [0x00000] in <00000000000000000000000000000000>:0
at UnityGLTF.GLTFSceneExporter.SaveGLBToByteArray (System.String sceneName) [0x00000] in <00000000000000000000000000000000>:0
at ExportGLB.ExportToGLB () [0x00000] in <00000000000000000000000000000000>:0
```
How do I make it work please ?


---

<!-- source=github_issue; title=MA Proxy Renderer for "object name"としてアバター内の全てのSkinned MeshがScene内に生成される; url=https://github.com/bdunderscore/modular-avatar/issues/1055 -->

# MA Proxy Renderer for "object name"としてアバター内の全てのSkinned MeshがScene内に生成される

- Source: github_issue
- URL: https://github.com/bdunderscore/modular-avatar/issues/1055

例えばPrefabの編集モードに入ったり戻ったりするタイミングで該当Prefab内に存在するSkinned Meshの全て（のように見える）がMA Proxy Renderer for "object name"という名前で意図に反して作成されます。(Scene上、マテリアルエラー状態のSkinned Meshが表示されます)
エラーメッセージもコンソールに出力されていてMA ScaleAdjusterの処理中のように見えます。
アバターはprefab variantの多重で運用していて、[1 元prefab]→[2 沢山の衣装を投入したprefab]→[3 全体scaleやMA ScaleAdjusterで調整したprefab]→[4 アップロードするための衣装だけにしたprefab]のようにしていて、3では素体Amatureの他にEditor Onlyにしている衣装のAmatureへもMA ScaleAdjusterを適用しています。
![image](https://github.com/user-attachments/assets/3208ab39-607c-493f-a040-a1a1cb7ab5fa)
エラーメッセージ内容
ArgumentException: An element with the same key but a different value already exists. Key: 'Kikyo_Blouse (UnityEngine.SkinnedMeshRenderer)'
System.Collections.Immutable.ImmutableDictionary`2+HashBucket[TKey,TValue].Add (TKey key, TValue value, System.Collections.Generic.IEqualityComparer`1[T] keyOnlyComparer, System.Collections.Generic.IEqualityComparer`1[T] valueComparer, System.Collections.Immutable.ImmutableDictionary`2+KeyCollisionBehavior[TKey,TValue] behavior, System.Collections.Immutable.ImmutableDictionary`2+OperationResult[TKey,TValue]& result) (at <85bee8cbddb7458fb7e9ff936e888708>:0)
System.Collections.Immutable.ImmutableDictionary`2[TKey,TValue].Add (TKey key, TValue value, System.Collections.Immutable.ImmutableDictionary`2+KeyCollisionBehavior[TKey,TValue] behavior, System.Collections.Immutable.ImmutableDictionary`2+MutationInput[TKey,TValue] origin) (at <85bee8cbddb7458fb7e9ff936e888708>:0)
System.Collections.Immutable.ImmutableDictionary`2+Builder[TKey,TValue].Add (TKey key, TValue value) (at <85bee8cbddb7458fb7e9ff936e888708>:0)
nadena.dev.modular_avatar.core.ProxyManager.BuildRenderers () (at ./Packages/nadena.dev.modular-avatar/Runtime/ScaleAdjuster/ProxyManager.cs:167)
nadena.dev.modular_avatar.core.ProxyManager.OnPreCull (UnityEngine.Camera camera) (at ./Packages/nadena.dev.modular-avatar/Runtime/ScaleAdjuster/ProxyManager.cs:269)
UnityEngine.Camera.FireOnPreCull (UnityEngine.Camera cam) (at <b41119cc6741409ea29f63c7f98de938>:0)


---

<!-- source=github_issue; title=NullReferenceException: Object reference not set to an instance of an object Fish; url=https://github.com/thedefside/BetterUI/issues/39 -->

# NullReferenceException: Object reference not set to an instance of an object Fish

- Source: github_issue
- URL: https://github.com/thedefside/BetterUI/issues/39

Stack trace:
Fish.GetPointDepth (UnityEngine.Vector3 p) (at <035307060cbb4b30b916cd82ebd80490>:0)
Fish.RandomizeWaypoint (System.Boolean canHook) (at <035307060cbb4b30b916cd82ebd80490>:0)
Fish.onCollision () (at <035307060cbb4b30b916cd82ebd80490>:0)
Fish.OnCollisionEnter (UnityEngine.Collision collision) (at <035307060cbb4b30b916cd82ebd80490>:0)
I have only betterUI 2.3.1


---

<!-- source=github_issue; title=Unity.ResolutionFailedException: RestSharp.Athuenticators.IAuthenticator, is an interface....Are you missing a type mapping?; url=https://github.com/AutomateThePlanet/BELLATRIX/issues/16 -->

# Unity.ResolutionFailedException: RestSharp.Athuenticators.IAuthenticator, is an interface....Are you missing a type mapping?

- Source: github_issue
- URL: https://github.com/AutomateThePlanet/BELLATRIX/issues/16

Taken from Master code 29/03/22
Within the ApiClientService.cs class:
`var authenticator = ServicesCollection.Current.Resolve<IAuthenticator>(); `
Triggers the following exception against any test (TableWithHeader_GetItems) for example:
Unity.ResolutionFailedException
HResult=0x80131500
Message=The current type, RestSharp.Authenticators.IAuthenticator, is an interface and cannot be constructed. Are you missing a type mapping?
_____________________________________________________
Exception occurred while:
• while resolving: IAuthenticator
Source=Unity.Container
StackTrace:
at Unity.UnityContainer.ExecuteValidatingPlan(BuilderContext& context)
at Unity.UnityContainer.Unity.IUnityContainer.Resolve(Type type, String name, ResolverOverride[] overrides)
at Unity.UnityContainerExtensions.Resolve[T](IUnityContainer container, ResolverOverride[] overrides)
at Bellatrix.ServicesCollection.Resolve[T](Boolean shouldThrowResolveException) in C:\BELLATRIX-master\src\Bellatrix.Core\infrastructure\ioc\ServicesCollection.cs:line 120
Inner Exception 1:
InvalidOperationException: The current type, RestSharp.Authenticators.IAuthenticator, is an interface and cannot be constructed. Are you missing a type mapping?
Inner Exception 2:
InvalidRegistrationException: Exception of type 'Unity.Exceptions.InvalidRegistrationException' was thrown.
I currently don't have a fix, but will continue reading up on it. The .cs file contains an interesting TODO: // TODO: is this going to be accessible in the service container?
Thanks again,
Rich


---

<!-- source=github_issue; title=Version 3.5.25.0 has dependency on Microsoft.Bcl.AsyncInterfaces [This breaks Unity Support]; url=https://github.com/aws/aws-sdk-net/issues/1722 -->

# Version 3.5.25.0 has dependency on Microsoft.Bcl.AsyncInterfaces [This breaks Unity Support]

- Source: github_issue
- URL: https://github.com/aws/aws-sdk-net/issues/1722

When attempting to use the AWS .NET SDK in Unity, the latest version supplied on [this page](https://aws.amazon.com/blogs/developer/referencing-the-aws-sdk-for-net-standard-2-0-from-unity-xamarin-or-uwp/) links to the latest version of the SDK, however this latest version's _AWSSDK.Core.dll_ file has a dependency on _Microsoft.Bcl.AsyncInterfaces_, and this breaks Unity support as attempting to find some workaround such as using a NUGET Package Manager (the only available one is unofficial, [linked here](https://github.com/GlitchEnzo/NuGetForUnity)) with Unity and then adding that package (Microsoft.Bcl.AsyncInterfaces) just leads to more dependencies and a never ending rabbit hole.
This dependency does not exist with the prior versions (specifically V3.3) of the SDK, so is this intentional? This creates a large issue when all of the few Unity tutorials and workshops that AWS provides use a 3.3 version of the SDK.
[I have successfully replicated this in 2019.4.9f1 and 2020.1.6f1. As this dependency is on AWS' side however, I would imagine that it is not dependent upon a Unity Version]


---

<!-- source=github_issue; title=ArrayElementReference<T> variant of the new Span<T> / Memory<T>; url=https://github.com/dotnet/corefxlab/issues/2417 -->

# ArrayElementReference<T> variant of the new Span<T> / Memory<T>

- Source: github_issue
- URL: https://github.com/dotnet/corefxlab/issues/2417

Hello, here's an interesting idea.
The new "Span" and "Memory" in C# 7.2 could potentially be used to solve the problem of the garbage collection cost of creating a very large quantity of objects. An app could manage GC cost by allocating objects in groups, that is arrays. We can already make an array of structs, but it is rather limited because we cannot make a field that contains a reference to one of these structs in an array. So, what if Memory<T> is used to make such a reference?
Memory<T> internally contains _object, _index, _length, but if it is reference to a single struct in an array, then _length == 1. I suggest making a variation of Memory<T> like this:
```
public readonly struct ArrayElementReference<T>
{
private readonly T[] _array;
private readonly int _index;
}
```
or like this:
```
public readonly struct ArrayElementReference<T>
{
private readonly T[] _array;
private readonly System.UIntPtr _offsetInBytes;
}
```
Likewise, Span<T> contains _pointer and _length and in this case, we don't need _length because it is always 1. Thus make a corresponding variation of Span<T> like this:
```
public readonly ref struct FastArrayElementReference<T>
{
private readonly ref T _pointer;
}
```
or like this:
```
public readonly ref struct FastArrayElementReference<T>
{
private readonly System.UIntPtr _pointer;
}
```
Thus the next version of C# could give us the ability to define a field (in a class or struct) that contains a reference to a struct element in an array, and this is implemented like ArrayElementReference<T> as shown above. When this field is copied to a local variable or method parameter on the stack, then it is converted to FastArrayElementReference<T> as shown above -- the same idea as how Span<T> is the fast version of Memory<T>.
Thanks for considering it.


---

<!-- source=github_issue; title=OmniSharpRestartServer error: channel 0 closed: '<feff>'; url=https://github.com/OmniSharp/omnisharp-vim/issues/629 -->

# OmniSharpRestartServer error: channel 0 closed: '<feff>'

- Source: github_issue
- URL: https://github.com/OmniSharp/omnisharp-vim/issues/629

When I issue a `:OmniSharpRestartServer` command, I get `channel 0 closed: '<feff>'`.
MacVim 8.2.539 (163)
OmniSharp-Roslyn v1.37.1
Related comments:
Possibly a previous request in progress. Apart from that error message, is anything going wrong? Does the server restart correctly as expected?
> Possibly a previous request in progress
With debug mode enabled, I waited for everything to finish, then triggered the restart.
> Does the server restart correctly as expected?
It looks like, yes. Although I didn't make specific tests e.g. remove a class from the project/sln > restart > try to look up type.
I think I've seen the error message before but it doesn't happen for me in regular restart situations (which I do daily, as a result of working in solutions depending on other solutions). I'll keep an eye out and see if I can repro.


---

<!-- source=github_issue; title=diagnostics cannot build using the .net backend; url=https://github.com/microsoft/MixedRealityToolkit-Unity/issues/2874 -->

# diagnostics cannot build using the .net backend

- Source: github_issue
- URL: https://github.com/microsoft/MixedRealityToolkit-Unity/issues/2874

Mixed Reality Toolkit
**Describe the bug**
I need to build a project using the .net backend (unity 2018.1) for debugging purposes. Currently, I am blocked by the diagnostics feature being unable to locate the Process type (it builds for il2cpp)
**To Reproduce**
1. Edit > Project Settings > Player > Other Settings > Scripting Backend == .NET
2. File > Build Settings > Build
**Expected behavior**
To be able to build the project against the .NET backend for as long as Unity ships it.
**Actual behavior**
Assets\MixedRealityToolkit-SDK\Features\Diagnostics\MemoryUseTracker.cs(12,17): error CS0246: The type or namespace name 'Process' could not be found (are you missing a using directive or an assembly reference?)
Assets\MixedRealityToolkit-SDK\Features\Diagnostics\CpuUseTracker.cs(13,17): error CS0246: The type or namespace name 'Process' could not be found (are you missing a using directive or an assembly reference?)
**Unity Editor Version**
2018.1.9f2


---

<!-- source=github_issue; title=Model trained with Tensorflow 1.7.1 not working; url=https://github.com/Syn-McJ/TFClassify-Unity/issues/11 -->

# Model trained with Tensorflow 1.7.1 not working

- Source: github_issue
- URL: https://github.com/Syn-McJ/TFClassify-Unity/issues/11

Hi , i was checking your classify example, it works perfectly. But i trained a model using [Google code labs](https://github.com/googlecodelabs/tensorflow-for-poets-2) and i followed these [steps](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/index.html?index=..%2F..%2Findex#0). I downloaded tensorflow 1.7.1 same as tfcsharp plugin . testing works perfectly on python level . but when i load retrained_graph.bytes in your code is dosent load this model . Architecture is mobilenet_0.50_224 and image size is 224 .
this is my retrained model and label
https://www.dropbox.com/s/vw34zpkg2a5klrw/retrained.zip?dl=0
i am not sure what i am doing wrong here
thanks


---

<!-- source=github_issue; title=Building error; url=https://github.com/umasteeringgroup/UMA/issues/8 -->

# Building error

- Source: github_issue
- URL: https://github.com/umasteeringgroup/UMA/issues/8

Hi,
I downloaded UMA 2.6 to my project (Unity 5.6) and tried to build I got the error:
NullReferenceException
UMA.UMAAssetIndexer.ForceSave () (at Assets/UMA/Core/Extensions/DynamicCharacterSystem/Scripts/UMAAssetIndexer.cs:199)
UMA.UMAAssetIndexer.UnityEditor.Build.IPreprocessBuild.OnPreprocessBuild (BuildTarget target, System.String path) (at Assets/UMA/Core/Extensions/DynamicCharacterSystem/Scripts/UMAAssetIndexer.cs:804)
UnityEditor.Build.BuildPipelineInterfaces.OnBuildPreProcess (BuildTarget platform, System.String path, Boolean strict) (at C:/buildslave/unity/build/Editor/Mono/BuildPipeline/BuildPipelineInterfaces.cs:232)
UnityEditor.HostView:OnGUI()
Assets/UMA/Examples/Extensions Examples/DynamicCharacterSystem/Scripts/Scene4/PhotoBooth.cs(645,0): error CS1525: Unexpected symbol `}'
![builderror](https://cloud.githubusercontent.com/assets/5631906/24829841/bfd4dbf2-1c79-11e7-9cc0-fc6d636899ee.jpg)
I must say that in the UMAAssetIndexer script I added lines:
```
#if UNITY_EDITOR
using UnityEditor.Build;
#endif
```
because when I downloaded UMA to Unity, I got errors and suggestion to add "using UnityEditor.Build".


---

<!-- source=github_issue; title=Banner Ad is OK, but RewardBasedAd doesn't show; url=https://github.com/googleads/googleads-mobile-unity/issues/377 -->

# Banner Ad is OK, but RewardBasedAd doesn't show

- Source: github_issue
- URL: https://github.com/googleads/googleads-mobile-unity/issues/377

When I remove the test device option, it prints log warns me that I should add that test option. Of course, I tried the test ad units [here](https://github.com/googleads/googleads-mobile-unity/issues/374), it still does not work.


---

<!-- source=github_issue; title=BobDoleOwndU If you can help me, I can support you with a good amount through PayPal.; url=https://github.com/BobDoleOwndU/FMDL-Studio-v2/issues/26 -->

# BobDoleOwndU If you can help me, I can support you with a good amount through PayPal.

- Source: github_issue
- URL: https://github.com/BobDoleOwndU/FMDL-Studio-v2/issues/26

Hi. mate
Do you know how to add or change new mesh in fmdl?
If you can help me, I can support you with a good amount through PayPal.
I recently learned that I can modify PES2020's face mesh in Unity using fmdl studio.
I either get a mesh from another PES2020 fmdl file or
I would like to know how to add a new mesh file to the fmdl file.
I simply copied '1 - MESH_hair_high' from 'hair_high.fmdl' and replaced it with '1 - MESH_hair_high' in another 'hair_high.fmdl' and exported the file via fmdl Studio. But it didn't apply.
And when I re-imported the exported fdml to Unity, '1 - MESH_har_high' disappeared.
And new items such as 'New Game Object' and 'sk_head' were created.
Is this an error related to the things in the [Root] folder?
Among the FMDL files on PES2020, 'hair_high.fmdl' includes [Root] ,0 - MESH_hair_high', '1 - MESH_hair_high', '2 - MESH_hair_high', and '3 - MESH_hair_high_high'. Can I add 4 - MESH_hair_high?
Do you know what kind of method it is it possible?
Do you know how to replace a new 3D model file with '1 - MESH_hair_high' or add a new '4 - MESH_hair_high' instead of the 3D model file included in the existing PES?
If you want to check the 'hair_high.fmdl' file, I can send you the file.
Please I hope you can help me.


---

<!-- source=github_issue; title=Unity3D - iOS is not supported on LiteDB v4.1; url=https://github.com/litedb-org/LiteDB/issues/844 -->

# Unity3D - iOS is not supported on LiteDB v4.1

- Source: github_issue
- URL: https://github.com/litedb-org/LiteDB/issues/844

latest version 4.1 is working just fine with unity android and windows, but on iOS its not working because of reflection.emit. Can we build a version without of reflection.emit? i need the latest version v4.1 working on iOS because i use the ignore case function and its only supported in version v4 and above.


---

<!-- source=github_issue; title=Status of this project; url=https://github.com/arcadia-unity/Arcadia/issues/388 -->

# Status of this project

- Source: github_issue
- URL: https://github.com/arcadia-unity/Arcadia/issues/388

Just curious -- what's the status of Arcadia? It hasn't been updated for a few years. Is it complete at this point?
Related comments:
It seems to have been abandoned by the developers, although it still works as it should on Unity 2021.3 LTS (not on 2022.1 though). Some people in the community have considered forking it for continued maintenance, but nothing has come of it so far. I do not have the experience to do that at the moment and others seem not to have the time.
For now, Arcadia is largely abandonware, but I hope that this will change in the future. If I ever get to a point where I have both the skill and the time to fork/maintain it, I will, but for now I can't do much.
Any idea how difficult it would be to make it work on 2022.1, or what are the reasons for it not working there? I'm relatively new to Clojure but know a bit about Unity, so I'm curious what change Unity introduced that caused Arcadia to break.
I don't know the details. All I can tell you is that Arcadia is now prevented from running play mode. I wish I could help you more.


---

<!-- source=github_issue; title=AssetDatabase.Refresh() - NullReferenceException; url=https://github.com/playgameservices/play-games-plugin-for-unity/issues/1713 -->

# AssetDatabase.Refresh() - NullReferenceException

- Source: github_issue
- URL: https://github.com/playgameservices/play-games-plugin-for-unity/issues/1713

That issue was resolved in 9.35, but still present in 9.37
My plugin works well but that is boring to see this error everytime
In GPGSUpgrader
AssetDatabase.Refresh();
ullReferenceException: Object reference not set to an instance of an object
UnityEditor.UI.ImageEditor.OnDisable () (at C:/buildslave/unity/build/Extensions/guisystem/UnityEditor.UI/UI/ImageEditor.cs:69)
UnityEditor.AssetDatabase:Refresh()
GooglePlayGames.Editor.GPGSUpgrader:.cctor() (at Assets/GooglePlayGames/Editor/GPGSUpgrader.cs:110)
UnityEditor.EditorAssemblies:ProcessInitializeOnLoadAttributes()


---

<!-- source=github_issue; title=Error on "Create an AR game using Unity's AR Foundation"-example; url=https://github.com/google-ar/arcore-unity-extensions/issues/57 -->

# Error on "Create an AR game using Unity's AR Foundation"-example

- Source: github_issue
- URL: https://github.com/google-ar/arcore-unity-extensions/issues/57

Hi!
I've followed the steps on example "Create an AR game using Unity's AR" which you can find here: https://codelabs.developers.google.com/arcore-unity-ar-foundation#3
At step 4 when editing the ReticleBehaviour script, the code editor and unity show mistakes in the copied script snippet.
![image](https://user-images.githubusercontent.com/80107934/128702317-0aba639b-e059-4f69-8a13-5c8a465aa69c.png)
I've installed the same packages as shown in the first step (ARFoundation 4.1.5, ARCore XR Plugin 4.1.5) and I'm using the Unity version which is recommended in the tutorial, 2020.3 LTS.
![image](https://user-images.githubusercontent.com/80107934/128703165-b28bf348-46c0-42c5-90d0-04f8a58c0327.png)
![image](https://user-images.githubusercontent.com/80107934/128703231-a609e343-0c79-40b6-8e3f-7440256d2680.png)
Changing the XRRaycastHit? in line 45 to ARRaycastHit? gets rid of the errors, and I can build the app, but it doesn't work properly, so I think this isn't the right way to tackle this problem. The reticle gets stuck in the position the smartphone is first held when starting the app, and doesn't move along the planes like it should according to the tutorial.
I've checked everything multiple times, and I don't know what to do. I've tried to use different versions of packages to no avail.
Can anyone please take a look?
Thank you so much!
Heislbesen


---

<!-- source=github_issue; title=Doesn't seem to work on MacOS Sonoma; url=https://github.com/timkurvers/valheim-macos/issues/40 -->

# Doesn't seem to work on MacOS Sonoma

- Source: github_issue
- URL: https://github.com/timkurvers/valheim-macos/issues/40

I know it's a beta OS but I wanted to try if there is any performance differences between Ventura and Sonoma but couldn't get it run on Sonoma. Did a clean install but it is the same the game opens the logo shows but crashes right after. Also tried running on crossover and GPTK but the performance seems very very bad.


---

<!-- source=github_issue; title=Unity and IL2CPP build; url=https://github.com/ably/ably-dotnet/issues/1110 -->

# Unity and IL2CPP build

- Source: github_issue
- URL: https://github.com/ably/ably-dotnet/issues/1110

Hi,
It's impossible to use Ably with a IL2CPP build it always crashs at Init with this error :
NullReferenceException: Object reference not set to an instance of an object.
at IO.Ably.IoC.get_MobileDevice () [0x00000] in <00000000000000000000000000000000>:0
at IO.Ably.AblyRealtime..ctor (IO.Ably.ClientOptions options) [0x00000] in <00000000000000000000000000000000>:0
at Ably.Start () [0x00000] in <00000000000000000000000000000000>:0
It works perfectly well with a Mono backend build. I use Unity 2020.3 currently.
┆Issue is synchronized with this [Jira Uncategorised](https://ably.atlassian.net/browse/SDK-1540) by [Unito](https://www.unito.io)


---

<!-- source=github_issue; title=Unable to record audio of the video rendered on 3D mesh using third party plugins like NatCorder; url=https://github.com/RenderHeads/UnityPlugin-AVProVideo/issues/1314 -->

# Unable to record audio of the video rendered on 3D mesh using third party plugins like NatCorder

- Source: github_issue
- URL: https://github.com/RenderHeads/UnityPlugin-AVProVideo/issues/1314

**Describe the issue**
I want to record game play along with the video played on a 3D mesh in the game play. I am able to record the video rendered on a 3D mesh, but I am unable to record the audio coming from the video player. I am using a third party plugin called NatCorder for recording the game play in which I am recording the output of main camera and audio listener attached to the main camera. The audio coming from the audio sources in the game play is recorded, but the audio coming from the video is not.
**Your Setup (please complete the following information):**
- Unity version: 2021.1.28f1
- AVPro Video version (number and edition (trial/core/ultra/enterprise)): Core 2.6.4
- Operating system version: Windows
- Device model: Xiomi Poco X3 Pro, Oneplus Nord 2
- Video specs (resolution, frame-rate, codec, file size): MP4, 100 MB
**To Reproduce**
1. Put Media player on a 3D cube and place it in the scene
2. Record camera and audio listener output of main camera and create a video
3. The newly recorded video does not have the audio output of the video played on the 3D cube


---

<!-- source=github_issue; title=Noobie question about MSBuildForUnity; url=https://github.com/microsoft/MSBuildForUnity/issues/44 -->

# Noobie question about MSBuildForUnity

- Source: github_issue
- URL: https://github.com/microsoft/MSBuildForUnity/issues/44

Hello everyone I wondering if is it possible to use MSBuildForUnity and Fody.
I have created a `.csproj` file under Assets/Scripts/Library
added :
```xml
<Project Sdk="Microsoft.NET.Sdk">
<PropertyGroup>
<TargetFramework>netstandard2.0</TargetFramework>
</PropertyGroup>
<ItemGroup>
<PackageReference Include="Fody" Version="6.0.3"/>
<PackageReference Include="MethodTimer.Fody" Version="3.1.0"/>
</ItemGroup>
</Project>
```
But it throws:
```
PrecompiledAssemblyException: Multiple precompiled assemblies with the same name Library.dll included for the current platform. Only one assembly with the same name is allowed per platform. Assembly paths: Assets/Scripts/Library/bin/Debug/netstandard2.0/Library.dll, Assets/Scripts/Library/obj/Debug/netstandard2.0/Library.dll
```
**In fact I'm looking for a tool that would allow me to use weaving code on unity, like Fody**
Thanks for reply


---

<!-- source=github_issue; title=ApprovalCheck function might need update on your Wiki; url=https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/131 -->

# ApprovalCheck function might need update on your Wiki

- Source: github_issue
- URL: https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/131

### Question
### Description
I have downloaded your latest release and try to create a server and a client from scratch based on your Wiki.
```csharp
private void ApprovalCheck(byte[] connectionData, uint clientId, Action<uint, bool, Vector3, Quaternion> callback)
{
//Your logic here
bool approve = true;
//If approve is true, the connection gets added. If it's false. The client gets disconnected
callback(clientId, approve, new Vector3(0,0,0), Quaternion.identity);
}
```
However, the following line
```csharp
NetworkingManager.singleton.ConnectionApprovalCallback = ApprovalCheck;
```
complains that "No overload for ApprovalCheck matches delegate 'Action<byte[], uint, NetworkingManager.ConnectionApprovedDelegate>"
Could you give me some hint how to resolve this issue?
### Your Environment
- Unity Version: {2018.2.10f1}
- MLAPI Version (2.1.0}


---

<!-- source=github_issue; title=Proposal: user-defined null/default check (non-defaultable value types / nullable-like types); url=https://github.com/dotnet/roslyn/issues/15108 -->

# Proposal: user-defined null/default check (non-defaultable value types / nullable-like types)

- Source: github_issue
- URL: https://github.com/dotnet/roslyn/issues/15108

Nullable types - `Nullable<T>` or any reference types - are specially treated with some syntax:
- propagate an invalid value with a `?.` operator
- serve an alternative value with a `??` operator
- [planned] Flow-analysis based validity checking like non-nullable reference types
There are some types behaving like nullable types, and I would like these "nullable-like" types to be "first-class" in terms of special treatment like `?.`, `??`, and flow-analysis.
## Nullable-like types examples
### 1. value-constrained struct
Suppose that you implement a type which value has some constraints: for instance, an integer type which is constrained to be positive:
```cs
struct PositiveInt
{
public int Value { get; }
public PositiveInt(int value)
{
if (value <= 0) throw new InvalidOperationException();
Value = value;
}
}
```
If C# compiler would have DbC and record types, this sample would be written like:
```cs
struct PositiveInt(int Value) requires Value > 0;
```
This struct is meant not to be zero or less, but can be zero if and only if using `default(PositiveInt)`. The `default` should be treated as an invalid value like null.
### 2. Expected<T>
There is a problem with using null as an invalid value, it does not tell why the operation returned null. To solve this problem, some people prefer a type similar to `expected<T>` in C++ - it is a union type of `T` and `Exception` as following:
```cs
struct Expected<T>
{
public T Value { get; }
public Exception Exception { get; }
public bool HasValue => Exception == null;
}
```
When I use such a type, I want to write as following:
```cs
Expected<string> s;
Expected<int> len = s?.Length;
int x = len ?? 0;
```
This code uses "exception propagating operator" `?.` and "exception coalescing operator" `??` by analogy with null propagating/coalescing operator.
## Proposed syntax
I want some syntax to introduce "nullable-like" types to C#; One idea is "operator null":
```cs
// definition
struct Expected<T>
{
public T Value { get; }
public Exception Exception { get; }
public static bool operator null => Exception != null;
}
// usage
Expected<int> e;
int x = e ?? 0;
// generated code
Expected<int> e;
int x = operator null(e) ? 0 : e.Value;
```


---

<!-- source=github_issue; title=LINUX SUPPORT FOR SERVERS (NOT WINE); url=https://github.com/StunlockStudios/vrising-dedicated-server-instructions/issues/157 -->

# LINUX SUPPORT FOR SERVERS (NOT WINE)

- Source: github_issue
- URL: https://github.com/StunlockStudios/vrising-dedicated-server-instructions/issues/157

How you started a game with "window server" only, are you crazy guys?
Related comments:
I mean, the last message you posted that you were going to support "linux" was 2 years ago, it is impossible for me to start the server and have it be seen in the list of servers, since I have a Ubuntu VPS without an interface, this bothers me a lot and not just me, there are many reddit users who complain about this, you should take these types of problems more into account, because it seems exaggerated to me that you do not have support for linux server, do something about this...
@TH3AL3X Hey, relax bro. I managed to host a V Rising server on an Ubuntu server without a GUI, and I was able to see my server in the server list in the game. Maybe you did something wrong?
> @TH3AL3X Hey, relax bro. I managed to host a V Rising server on an Ubuntu server without a GUI, and I was able to see my server in the server list in the game. Maybe you did something wrong?
With docker?


---

<!-- source=github_issue; title=Topic: OpenClass Room à Unity3D:; url=https://github.com/EloiStree/HelloSharpForUnity3D/issues/447 -->

# Topic: OpenClass Room à Unity3D:

- Source: github_issue
- URL: https://github.com/EloiStree/HelloSharpForUnity3D/issues/447

![image](https://github.com/user-attachments/assets/831688ff-de72-4f05-aaea-eb4afc02f422)
![image](https://github.com/user-attachments/assets/361c66b6-0091-40de-8ca8-af2af1c4f7a1)
Code Monkey guide: https://www.youtube.com/watch?v=pReR6Z9rK-o
Site du Zero guide: https://synchronicales.eu/sdz/sdz/apprenez-a-developper-en-c.html PDF: [SiteDuZeroC#.pdf](https://github.com/user-attachments/files/17318958/SiteDuZeroC.pdf)
W3C: https://www.w3schools.com/cs/index.php


---

<!-- source=github_issue; title=I cant see the wishexplanation; url=https://github.com/danielstegink/Silksong.SilkAndSong/issues/15 -->

# I cant see the wishexplanation

- Source: github_issue
- URL: https://github.com/danielstegink/Silksong.SilkAndSong/issues/15

When I go with my controler to the Silk and Song wish it just shows nothing and in the console it prints:
[Error : Unity Log] NullReferenceException: Object reference not set to an instance of an object
Stack trace:
QuestItemManager.SetDisplay (InventoryItemSelectable selectable) (at <9e13ef150cb143cfab0aea0766c64843>:0)
InventoryItemSelectable.UpdateDisplay () (at <9e13ef150cb143cfab0aea0766c64843>:0)
InventoryItemUpdateable.UpdateDisplay () (at <9e13ef150cb143cfab0aea0766c64843>:0)
InventoryItemSelectable.Select (System.Nullable`1[T] direction) (at <9e13ef150cb143cfab0aea0766c64843>:0)
InventoryItemUpdateable.Select (System.Nullable`1[T] direction) (at <9e13ef150cb143cfab0aea0766c64843>:0)
InventoryItemQuest.Select (System.Nullable`1[T] direction) (at <9e13ef150cb143cfab0aea0766c64843>:0)
InventoryItemManager.SetSelected (InventoryItemSelectable selectable, System.Nullable`1[T] direction, System.Boolean justDisplay) (at <9e13ef150cb143cfab0aea0766c64843>:0)
InventoryItemManager.TrySelectOrdered (System.Collections.Generic.IEnumerable`1[T] collection, System.Nullable`1[T] direction, System.Boolean justDisplay) (at <9e13ef150cb143cfab0aea0766c64843>:0)
InventoryItemManager.SetSelected (InventoryItemManager+SelectedActionType selectedAction, System.Boolean justDisplay) (at <9e13ef150cb143cfab0aea0766c64843>:0)
SetInventoryItemSelected.DoAction (InventoryItemManager itemManager) (at <9e13ef150cb143cfab0aea0766c64843>:0)
FSMUtility+GetComponentFsmStateAction`1[T].OnEnter () (at <9e13ef150cb143cfab0aea0766c64843>:0)
HutongGames.PlayMaker.FsmState.ActivateActions (System.Int32 startIndex) (at <46c7fbbaa3a1440d8ba53ce9dd09b77b>:0)
HutongGames.PlayMaker.FsmState.OnEnter () (at <46c7fbbaa3a1440d8ba53ce9dd09b77b>:0)
HutongGames.PlayMaker.Fsm.EnterState (HutongGames.PlayMaker.FsmState state) (at <46c7fbbaa3a1440d8ba53ce9dd09b77b>:0)
HutongGames.PlayMaker.Fsm.SwitchState (HutongGames.PlayMaker.FsmState toState) (at <46c7fbbaa3a1440d8ba53ce9dd09b77b>:0)
HutongGames.PlayMaker.Fsm.UpdateStateChanges () (at <46c7fbbaa3a1440d8ba53ce9dd09b77b>:0)
HutongGames.PlayMaker.Fsm.UpdateState (HutongGames.PlayMaker.FsmState state) (at <46c7fbbaa3a1440d8ba53ce9dd09b77b>:0)
HutongGames.PlayMaker.Fsm.Update () (at <46c7fbbaa3a1440d8ba53ce9dd09b77b>:0)
PlayMakerFSM.Update () (at <46c7fbbaa3a1440d8ba53ce9dd09b77b>:0)
I tried every version but its always the same error
<img width="1918" height="1064" alt="Image" src="https://github.com/user-attachments/assets/4558a294-3644-476e-845a-5e48305c44a8" />


---

<!-- source=github_issue; title=Destroy / Disable nob bug; url=https://github.com/FirstGearGames/FishNet/issues/649 -->

# Destroy / Disable nob bug

- Source: github_issue
- URL: https://github.com/FirstGearGames/FishNet/issues/649

**General**
Unity version: 2021.3.30f1
Fish-Networking version: 4.2.0 Pro
Discord link:
https://discord.com/channels/424284635074134018/1034477094731784302/1228664103296303166
**Description**
After update my main project from 3.x version to 4.2.0, i start to have weird thing. I have items and enemies in game. Enemies nob started to not despawn. I faced situation when ResetState for SyncVars called, but gameobject nob not disabled (enemies nobs pooled, but also true for simple destroy). Ive found that it happens only at Host. And idk how to replicate it, because items nobs working fine. I did expose some values from ManagedObjects.cs and log them to console. just added 2 vars for tracking `NetworkManager.ServerManager.Objects.AddToPending(nob);` and `NetworkManager.ServerManager.Objects.RemoveFromPending(nob.ObjectId);`
code:
`Debug.Log($"destroy: {destroy}, nested: {nob.IsNested}, asServer: {asServer}, IsSceneObject: {nob.IsSceneObject}, AddToPending: {addToPending}, RemoveFromPending: {removeFromPending}");`
here is a log of this issue:
`destroy: False, nested: False, asServer: False, IsSceneObject: False, AddToPending: False, RemoveFromPending: False`
This log calling once (edited) per each nob.
I checked how this log working in normal case, and it should have asServer true, or AddToPending true, and RemoveFromPending true on next call, but it never happens in Host for some reason
**Expected behavior**
nobs disabling or destroying depends of pool or derstroy setting
**Screenshots**
[Video](https://drive.google.com/file/d/1uacn0WnPXeCBwD3rpbcP0HdQR-O1th05/view?usp=sharing)


---

<!-- source=github_issue; title=Bepin Configuration Manager Not Showing Any Plugins; url=https://github.com/BepInEx/BepInEx.ConfigurationManager/issues/90 -->

# Bepin Configuration Manager Not Showing Any Plugins

- Source: github_issue
- URL: https://github.com/BepInEx/BepInEx.ConfigurationManager/issues/90

Hi, I"m having the same trouble now as this fellow had in 2021: https://github.com/BepInEx/BepInEx.ConfigurationManager/issues/29
Any suggestions?
Related comments:
Update to latest version.
Did.
On Mon, Apr 22, 2024 at 1:07 AM ManlyMarco ***@***.***> wrote:
> Update to latest version.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/BepInEx/BepInEx.ConfigurationManager/issues/90#issuecomment-2068640806>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/BH2QRGUSRI5A2QPD7MU2SO3Y6SZJTAVCNFSM6AAAAABGSB3IPSVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDANRYGY2DAOBQGY>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>
Or rather, I had. I must be missing something.


---

<!-- source=github_issue; title=Server Breaking B: 65; url=https://github.com/unitystation/unitystation/issues/2646 -->

# Server Breaking B: 65

- Source: github_issue
- URL: https://github.com/unitystation/unitystation/issues/2646

## Description
We've noticed on the headless servers we have running 24/7, that the server can end up in a sort of broken state where there appears to be lots of bugs and many things don't work properly. This ticket is for tracking this sort of problem, even if it may actually be due to multiple problems.
This probably has one or a few root causes that causes the server to stop working constantly. It might not even be the same symptoms each time. I believe a round restart usually fixes these.
For example, when the server was once in this state I joined as a new player and spawned apparently at hiddenpos and suffocated.
Most likely the root cause will reveal itself in the server logs. So just look at the logs and try to see what went wrong prior to the issues appearing. It may even be reproducible locally if you just leave a local headless running long enough.


---

<!-- source=github_issue; title=Python API: Simulation time starts automatically when run() is not called and reset() does not work properly; url=https://github.com/lgsvl/simulator/issues/1867 -->

# Python API: Simulation time starts automatically when run() is not called and reset() does not work properly

- Source: github_issue
- URL: https://github.com/lgsvl/simulator/issues/1867

Hi, I am using the simulator with Python API. I also use a custom binary to run the simulator. I realise that after loading the scene and spawning the vehicles, the run time is started automatically when the run() function is not called yet. What could be the problem and how can I solve it?
Also, when I try to call the reset() function, the scene is reloaded, but the Python code execution is stuck forever and I cannot spawn a vehicle when I use the add_agent() function. What could be the cause?
Thank you in advance.


---

<!-- source=github_issue; title=The "Decluttering" Feature from 2.5.4.4 is breaking KCT; url=https://github.com/TweakScale/TweakScale/issues/201 -->

# The "Decluttering" Feature from 2.5.4.4 is breaking KCT

- Source: github_issue
- URL: https://github.com/TweakScale/TweakScale/issues/201

Fellow Kerbonaut [JebIsDeadBaby ](https://forum.kerbalspaceprogram.com/index.php?/profile/185823-jebisdeadbaby/) found a problem and reported it on [Forum](https://forum.kerbalspaceprogram.com/index.php?/topic/179030-144/&do=findComment&comment=4030858):
KCT is, apparently, copying nodes itself and since this happens on Editor, TweakScale gets confused and apply the Decluttering over KCT, that so borks on a NRE:
```
[EXC 13:56:07.455] NullReferenceException: Object reference not set to an instance of an object
ConfigNode.CopyToRecursive (ConfigNode node, System.Boolean overwrite) (at <cd473063d3a2482f8d93d388d0c95035>:0)
ConfigNode.CopyToRecursive (ConfigNode node, System.Boolean overwrite) (at <cd473063d3a2482f8d93d388d0c95035>:0)
ConfigNode.CopyToRecursive (ConfigNode node, System.Boolean overwrite) (at <cd473063d3a2482f8d93d388d0c95035>:0)
ConfigNode.CopyTo (ConfigNode node) (at <cd473063d3a2482f8d93d388d0c95035>:0)
KerbalConstructionTime.KCT_KSC.AsConfigNode () (at <27327b2825ca4e69a9d134bb5cd0383e>:0)
KerbalConstructionTime.KerbalConstructionTimeData.OnSave (ConfigNode node) (at <27327b2825ca4e69a9d134bb5cd0383e>:0)
ScenarioModule.Save (ConfigNode node) (at <cd473063d3a2482f8d93d388d0c95035>:0)
ProtoScenarioModule..ctor (ScenarioModule module) (at <cd473063d3a2482f8d93d388d0c95035>:0)
ScenarioRunner.UpdateModules () (at <cd473063d3a2482f8d93d388d0c95035>:0)
ScenarioRunner.GetUpdatedProtoModules () (at <cd473063d3a2482f8d93d388d0c95035>:0)
Game.Updated (GameScenes startSceneOverride) (at <cd473063d3a2482f8d93d388d0c95035>:0)
GamePersistence.SaveGame (System.String saveFileName, System.String saveFolder, SaveMode saveMode, GameScenes startScene) (at <cd473063d3a2482f8d93d388d0c95035>:0)
GamePersistence.SaveGame (System.String saveFileName, System.String saveFolder, SaveMode saveMode) (at <cd473063d3a2482f8d93d388d0c95035>:0)
EditorLogic.onExitConfirm () (at <cd473063d3a2482f8d93d388d0c95035>:0)
EditorLogic.onExitContinue () (at <cd473063d3a2482f8d93d388d0c95035>:0)
EditorLogic.exitEditor () (at <cd473063d3a2482f8d93d388d0c95035>:0)
UnityEngine.Events.InvokableCall.Invoke () (at <12e76cd50cc64cf19e759e981cb725af>:0)
UnityEngine.Events.UnityEvent.Invoke () (at <12e76cd50cc64cf19e759e981cb725af>:0)
UnityEngine.UI.Button.Press () (at <aa3a227ee8664797a8194ab8e2ed2249>:0)
UnityEngine.UI.Button.OnPointerClick (UnityEngine.EventSystems.PointerEventData eventData) (at <aa3a227ee8664797a8194ab8e2ed2249>:0)
UnityEngine.EventSystems.ExecuteEvents.Execute (UnityEngine.EventSystems.IPointerClickHandler handler, UnityEngine.EventSystems.BaseEventData eventData) (at <aa3a227ee8664797a8194ab8e2ed2249>:0)
UnityEngine.EventSystems.ExecuteEvents.Execute[T] (UnityEngine.GameObject target, UnityEngine.EventSystems.BaseEventData eventData, UnityEngine.EventSystems.ExecuteEvents+EventF
unction`1[T1] functor) (at <aa3a227ee8664797a8194ab8e2ed2249>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.EventSystems.EventSystem:Update()
```
The exception is raised at clicking on the Launch Button (Green Button Top/Right)


---

<!-- source=github_issue; title=[Question] Looong distance sync optimisation; url=https://github.com/insthync/LiteNetLibManager/issues/11 -->

# [Question] Looong distance sync optimisation

- Source: github_issue
- URL: https://github.com/insthync/LiteNetLibManager/issues/11

Hi, may i ask quick question after some time? :) ... i never know what is proper channel to do that, hopefully its ok here. Im trying to figure out if this library is suitable for case when i have position driven by some third party stuff due avoiding floating point precission problems with large maps (i have position stored elsewhere than transform - im not sure if thats relevant) and what i want is to sync only object/player with positional variables close enough to current player - I know about two features - those subscribers and there is also some visibility checker if i remember correctly. My question is - what is best approach for something like that? I can do it from scratch the old fashioned way with commands if its too problematic but that spawning logic with automatic syncing of vars and lists is very helpfull :)
PS: Im very greatfull you found some time to expand docs, thanks for that. There are still some thing not that clear to me (like when subscribers gets rebuilded/recalculated) but overall there is lot of new usefull info there. 👍


---

<!-- source=github_issue; title=Cannot access protected member `UnityEngine.Texture.Texture()`; url=https://github.com/ExtendRealityLtd/VRTK/issues/1796 -->

# Cannot access protected member `UnityEngine.Texture.Texture()`

- Source: github_issue
- URL: https://github.com/ExtendRealityLtd/VRTK/issues/1796

### Environment
* VRTK imported from the Unity Asset Store.
* VRTK Version: 3.2.1
* Version of Unity3D: 2018.1.0f2
* Hardware used: HTC Vive
* SDK used: SteamVR
### Steps to reproduce
* Import VRTK to the assets
### Expected behavior
* No error should come up.
### Current behavior
* I am getting two errors:
```
Assets/VRTK/Scripts/Interactions/Highlighters/VRTK_MaterialColorSwapHighlighter.cs(146,66): error CS1540: Cannot access protected member `UnityEngine.Texture.Texture()' via a qualifier of type `UnityEngine.Texture'. The qualifier must be of type `VRTK.Highlighters.VRTK_MaterialColorSwapHighlighter' or derived from it
```
```
Assets/VRTK/Scripts/Interactions/Highlighters/VRTK_MaterialColorSwapHighlighter.cs(146,66): error CS0122: `UnityEngine.Texture.Texture()' is inaccessible due to its protection level
```


---

<!-- source=github_issue; title=AR Scene Switches crash AR(Black screen); url=https://github.com/Unity-Technologies/arfoundation-samples/issues/94 -->

# AR Scene Switches crash AR(Black screen)

- Source: github_issue
- URL: https://github.com/Unity-Technologies/arfoundation-samples/issues/94

When we are using AR Foundation, while trying to switch between AR Scenes, we see black screen in 2nd,3rd... scenes. AR only works in first scene( in terms of order, not a scene specific issue). So when we look through logs, it appears to be arsubsystems crash when we change scenes on iOS only. It works on ARCore(Android) regardless. We think sessions are not restarted between scene switches. We need a fix.


---

<!-- source=github_issue; title=Firebase 5.3.1 sdk is working normal in editor , but can't work in mobile device .; url=https://github.com/firebase/quickstart-unity/issues/224 -->

# Firebase 5.3.1 sdk is working normal in editor , but can't work in mobile device .

- Source: github_issue
- URL: https://github.com/firebase/quickstart-unity/issues/224

I'm using unity 2018.1.1 and the firebase sdk 5.3.1 to build on my Android Device .
Project is quickstart-unity-auth's sample .
I try this sapmle to test firebase and working normal in unity editor .
But I build sapmle project to Android Device trying to login account is not working anymore .
And I change Build System , Scripting Runtime Version still not to solve ; therefore , I comes to help .


---

<!-- source=github_issue; title=World Anchor Store never ready; url=https://github.com/microsoft/MixedRealityToolkit-Unity/issues/640 -->

# World Anchor Store never ready

- Source: github_issue
- URL: https://github.com/microsoft/MixedRealityToolkit-Unity/issues/640

I stumbled upon this problem yesterday, when i first got into world anchors. Basically what i tried is to get the World Anchor Manager working, but the problem i had is that the callback when the anchor store is ready never got called. So i thought maybe i just messed up and created a new project with just the spatialmapping and world anchor store manager in it. Well the end of the story was that it still didnt work.
So i fiddled around a little bit and changed:
```
protected override void Awake()
{
base.Awake();
AnchorStore = null;
WorldAnchorStore.GetAsync(AnchorStoreReady);
}
```
to
```
void Start()
{
AnchorStore = null;
WorldAnchorStore.GetAsync(AnchorStoreReady);
}
```
Basically i let the code in the Awake() function run in the Start() function. Maybe there is something not yet initialized when Awake() gets called, cause i also got an NullReference Error.
Is this a bug? Should the code in Awake() run in the Start() function?


---

<!-- source=github_issue; title=About those NREs ...; url=https://github.com/TweakScale/TweakScale/issues/2 -->

# About those NREs ...

- Source: github_issue
- URL: https://github.com/TweakScale/TweakScale/issues/2

We were dealing with NREs on pellior0's repo (https://github.com/pellinor0/TweakScale/issues/81#issue-364296922). Since you've done gone jumped in the deep-end, I'm closing out that issue and re-igniting the fire over here.
Linux 18.04
KSP 1.4.5
ModList: [KSP_test_TC.ckan.txt](https://github.com/net-lisias-ksp/TweakScale/files/2498672/KSP_test_TC.ckan.txt)
Something you may find of use...
If you add in 'Decouple With Control' to the above install, generates 436 NREs, starting with the original ...
[ERR 17:07:00.380] [TweakScale] Exception on writeDryCost: System.NullReferenceException: Object reference not set to an instance of an object
at PartModuleList.Contains (Int32 classID) [0x00000] in <filename unknown>:0
at PartModuleList.Contains (System.String className) [0x00000] in <filename unknown>:0
at TweakScale.PrefabDryCostWriter.WriteDryCost () [0x00000] in <filename unknown>:0
[LOG 17:07:00.380] [TweakScale] part=kerbalEVA ()
and ending with ...
[ERR 17:07:00.557] [TweakScale] Exception on writeDryCost: System.NullReferenceException: Object reference not set to an instance of an object
at PartModuleList.Contains (Int32 classID) [0x00000] in <filename unknown>:0
at PartModuleList.Contains (System.String className) [0x00000] in <filename unknown>:0
at TweakScale.PrefabDryCostWriter.WriteDryCost () [0x00000] in <filename unknown>:0
[LOG 17:07:00.557] [TweakScale] part=roverWheel3 (RoveMax Model XL3)


---

<!-- source=github_issue; title=Getting intermittent null ref on SetGlobalListener; url=https://github.com/microsoft/MixedRealityToolkit-Unity/issues/1189 -->

# Getting intermittent null ref on SetGlobalListener

- Source: github_issue
- URL: https://github.com/microsoft/MixedRealityToolkit-Unity/issues/1189

Using the new MixedRealityCameraParent prefab, InputManager, etc. with updated code (both on master and 2017.2.0 versions) I'm getting an intermittent null ref exception on
InputManager.Instance.AddGlobalListener(gameObject)
```
NullReferenceException: Object reference not set to an instance of an object
HoloToolkit.Unity.InputModule.SetGlobalListener.OnEnable () (at Assets/HoloToolkit/Input/Scripts/Utilities/SetGlobalListener.cs:16)
```
Specifically, the instance variable is null.
In the current version of the script, OnDisable and OnDestroy wrap the RemoveGlobalListener call in an if statement
private void OnDisable()
{
if (InputManager.Instance != null)
{
InputManager.Instance.RemoveGlobalListener(gameObject);
}
}
But OnEnable does not:
private void OnEnable()
{
InputManager.Instance.AddGlobalListener(gameObject);
}
Presumably, this should be
private void OnEnable()
{
if (InputManager.Instance != null)
{
InputManager.Instance.AddGlobalListener(gameObject);
}
}


---

<!-- source=github_issue; title=InvalidOperationException: Error: Attempted to call Initialize on a HlapiCommsNetwork; url=https://github.com/Placeholder-Software/Dissonance/issues/36 -->

# InvalidOperationException: Error: Attempted to call Initialize on a HlapiCommsNetwork

- Source: github_issue
- URL: https://github.com/Placeholder-Software/Dissonance/issues/36

## Context
I have purchased dissonance from unity asset store and I wanted to try it. however for some reason while following the guidlines and other tutorials, it seems I can not even get the voice chat working and I do get an error which does not make any sense
## Expected Behavior
_just wanted the voice chat to work_
## Actual Behavior
_voicechat not working_
## Workaround
_N/A_
## Fix
_N/A_
## Steps to Reproduce
_Provide a detailed set of steps to reproduce the problem_
I get this error:
InvalidOperationException: Error: Attempted to call Initialize on a HlapiCommsNetwork, but it is not in the correct state (expected Ready|Initializing, got Disconnected)! This is probably a bug in Dissonance, we're sorry! Please report the bug on the issue tracker "https://github.com/Placeholder-Software/Dissonance/issues". You could also seek help on the community at "http://placeholder-software.co.uk/dissonance/community" to get help for a temporary workaround. Error ID: 3E7F2D4C-0F13-4324-83A1-97874221B99B
Dissonance.Networking.BaseCommsNetwork`3[Dissonance.Integrations.UNet_HLAPI.HlapiServer,Dissonance.Integrations.UNet_HLAPI.HlapiClient,Dissonance.Integrations.UNet_HLAPI.HlapiConn].Initialize (System.String playerName, Dissonance.Rooms rooms, Dissonance.PlayerChannels playerChannels, Dissonance.RoomChannels roomChannels, System.Action`1 connectionCallback) (at Assets/Plugins/Dissonance/Core/Networking/BaseCommsNetwork.cs:319)
Dissonance.DissonanceComms.Start () (at Assets/Plugins/Dissonance/DissonanceComms.cs:352)
## Your Environment
- **Dissonance version used**: 1.1.1_
- **Unity version**: e.g. 5.6.1f1 professional_(Help > About Unity)_
- win10_
- **Link to your project**: If your project source code is available, link it here


---

<!-- source=github_issue; title=Error on EventTrack when method is null; url=https://github.com/ddionisio/MateAnimator/issues/18 -->

# Error on EventTrack when method is null

- Source: github_issue
- URL: https://github.com/ddionisio/MateAnimator/issues/18

Hi @ddionisio! It's been a long time :octocat:
Just today I realized if I put nothing on GameObject parameter in Event track it would return error. Here's the error I've got
`NullReferenceException: Object reference not set to an instance of an object
MateAnimator.AMActionMethodCall.Apply (Single t, Boolean backwards) (at Assets/Plugins/MateAnimator/Scripts/Classes/AMActionTween.cs:471)
MateAnimator.AMActionTween.DoUpdate (Single p_totElapsed) (at Assets/Plugins/MateAnimator/Scripts/Classes/AMActionTween.cs:92)
Holoville.HOTween.Plugins.Core.ABSTweenPlugin.Update (Single p_totElapsed) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__HOTween.Assembly/HOTweenV1/Plugins/Core/ABSTweenPlugin.cs:469)
Holoville.HOTween.Tweener.Update (Single p_shortElapsed, Boolean p_forceUpdate, Boolean p_isStartupIteration, Boolean p_ignoreCallbacks, Boolean p_ignoreDelay) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__HOTween.Assembly/HOTweenV1/Tweener.cs:844)
Holoville.HOTween.Tweener.GoTo (Single p_time, Boolean p_play, Boolean p_forceUpdate, Boolean p_ignoreCallbacks) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__HOTween.Assembly/HOTweenV1/Tweener.cs:951)
Holoville.HOTween.Core.ABSTweenComponent.GoTo (Single p_time, Boolean p_forceUpdate) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__HOTween.Assembly/HOTweenV1/Core/ABSTweenComponent.cs:659)
Holoville.HOTween.Sequence.Update (Single p_shortElapsed, Boolean p_forceUpdate, Boolean p_isStartupIteration, Boolean p_ignoreCallbacks) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__HOTween.Assembly/HOTweenV1/Sequence.cs:749)
Holoville.HOTween.Core.ABSTweenComponent.Update (Single p_elapsed) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__HOTween.Assembly/HOTweenV1/Core/ABSTweenComponent.cs:954)
Holoville.HOTween.HOTween.DoUpdate (UpdateType p_updateType, Single p_elapsed) (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__HOTween.Assembly/HOTweenV1/HOTween.cs:2252)
Holoville.HOTween.HOTween.Update () (at D:/DG/_Develop/__UNITY3_CLASSES/_Holoville/__HOTween.Assembly/HOTweenV1/HOTween.cs:734)
`


---

<!-- source=github_issue; title=Appending dependency implementations via handlers.; url=https://github.com/simpleinjector/SimpleInjector/issues/203 -->

# Appending dependency implementations via handlers.

- Source: github_issue
- URL: https://github.com/simpleinjector/SimpleInjector/issues/203

I have a plugin/module based desktop application where the modules are discovered/added dynamically.
After the bootstrap phase they are injected into the `ShellViewModel`.
I am wondering how can I register the modules in the container such that when the collection is requested it gets resolved correctly.
something like `container.AppendHandler(typeof(IModule), c => instance);` This code gets called inside the module of course.


---

<!-- source=github_issue; title=Wolfs don't do anything; url=https://github.com/Syclamoth/GamesAI6/issues/4 -->

# Wolfs don't do anything

- Source: github_issue
- URL: https://github.com/Syclamoth/GamesAI6/issues/4

They just sit there. I'm 99% sure this was happening before I added pathfinding and turned them into prefabs. Please fix ASAP urgent.
Related comments:
Ofc they won't do anything because I've updated the their states. You should go to the FSM editor and link them again.
However, about the new states for wolf and sheep i.e. wolf_eating and sheep_beingeaten. They don't show on the FSM editor and I don't know why.
Also, with the new scene update last night. I got this error.
transform.position assign attempt for 'Wolf' is not valid. Input position is { NaN, 0.496794, NaN }.
UnityEngine.Transform:set_position(Vector3)
Legs:Update() (at Assets/Scripts/Interaction/Legs.cs:93)
I'm fixing some/all of these now.
1: There's no reason why you can't set up the links on the FSM editor yourself, they're very straightforward.
2: They don't show up on the editor for a very good reason, which is that _you haven't put them there_ (fixed now)
3: This error occurs if a wolf spawns inside a building. It basically screws up the steering behaviours and stops it from moving. Presumably when the wolf prefabs are being spawned in streets procedurally, it will no longer be an issue.
They are being spawned in streets automatically.
On 01/09/2012, at 7:27 PM, Kieren Wallace notifications@github.com wrote:
> I'm fixing some/all of these now.
>
> 1: There's no reason why you can't set up the links on the FSM editor yourself, they're very straightforward.
>
> 2: They don't show up on the editor for a very good reason, which is that you haven't put them there (fixed now)
>
> 3: This error occurs if a wolf spawns inside a building. It basically screws up the steering behaviours and stops it from moving. Presumably when the wolf prefabs are being spawned in streets procedurally, it will no longer be an issue.
>
> —
> Reply to this email directly or view it on GitHub.


---

<!-- source=github_issue; title=Stuck loading Inspector GUI.; url=https://github.com/bdunderscore/modular-avatar/issues/1843 -->

# Stuck loading Inspector GUI.

- Source: github_issue
- URL: https://github.com/bdunderscore/modular-avatar/issues/1843

My friend has a issue with his avatar that when he clicks on some Asset (which have MA Scripts) in the Avatar hierarchy that it switches to the "Hold on" screen forever. (Not every asset does it.)
<img width="523" height="130" alt="Image" src="https://github.com/user-attachments/assets/c028d0c3-ef6e-48ed-ba1d-980f43868003" />
I tested around a lot and found out that it has something to do with "protected override void OnInnerInspectorGUI()" from "MenuInstallerEditor"
If i delete the "MenuInstallerEditor" file the menus work fine again.
I found it it has to be "OnInnerInspectorGUI" because if i comment it out in "MAEditorBase" the issue does not occur anymore.
```cs
public sealed override void OnInspectorGUI()
{
InspectorCommon.DisplayOutOfAvatarWarning(targets);
//OnInnerInspectorGUI();
}
protected abstract void OnInnerInspectorGUI();
```
Because the Application opens the "Hold on" window the console output does not refresh/generate.
Is there any log i can upload that would help in finding out what is wrong here?
This asset is one that breaks unity when clicking with Inspector open:
<img width="564" height="1080" alt="Image" src="https://github.com/user-attachments/assets/f37a18e4-bd5e-4a52-8cf3-5f1b641be5dc" />


---

<!-- source=github_issue; title=[Bug][Shell] Shell.Current.GoToAsync exception on certain navigation sequence; url=https://github.com/xamarin/Xamarin.Forms/issues/12958 -->

# [Bug][Shell] Shell.Current.GoToAsync exception on certain navigation sequence

- Source: github_issue
- URL: https://github.com/xamarin/Xamarin.Forms/issues/12958

<!-- Bug report best practices: https://github.com/xamarin/Xamarin.Forms/wiki/Submitting-Issues -->
### Description
The ```Shell.Current.GoToAsync``` method fails on a particular navigation sequence with Exception
```
System.ArgumentNullException: 'Shell Content Page is Null
Parameter name: page'
```
Inner Stack Trace:
```
at Xamarin.Forms.Platform.Android.ShellSectionRenderer.UpdateCurrentItem (Xamarin.Forms.ShellContent content) [0x00013] in D:\a\1\s\Xamarin.Forms.Platform.Android\Renderers\ShellSectionRenderer.cs:95
at Xamarin.Forms.Platform.Android.ShellSectionRenderer.Android.Support.V4.View.ViewPager.IOnPageChangeListener.OnPageScrolled (System.Int32 position, System.Single positionOffset, System.Int32 positionOffsetPixels) [0x0001c] in D:\a\1\s\Xamarin.Forms.Platform.Android\Renderers\ShellSectionRenderer.cs:38
at Android.Support.V4.View.ViewPager+IOnPageChangeListenerInvoker.n_OnPageScrolled_IFI (System.IntPtr jnienv, System.IntPtr native__this, System.Int32 position, System.Single positionOffset, System.Int32 positionOffsetPixels) [0x00008] in <c4d4704d3494459fba644f7558bc2b06>:0
at (wrapper dynamic-method) Android.Runtime.DynamicMethodNameCounter.50(intptr,intptr,int,single,int)
```
### Steps to Reproduce
1. Create an App with the following Shell Hierarchy
```
<TabBar>
<Tab Title="Tab 1" Route="welcome" Icon="icon_about">
<ShellContent Title="MainPage" Route="landing" ContentTemplate="{DataTemplate local:Page1}" />
</Tab>
<Tab Title="Tab 2" Route="profile" Icon="icon_about">
<ShellContent Title="Page 2" Route="main" ContentTemplate="{DataTemplate local:Page2}" />
<ShellContent Title="Page 3" Route="details" ContentTemplate="{DataTemplate local:Page3}" />
<ShellContent Title="Page 4" Route="settings" ContentTemplate="{DataTemplate local:Page4}" />
</Tab>
</TabBar>
```
2. Put two Buttons onto Page2 with the following event handlers
```
private async void BtnGotoPage3(object sender, EventArgs e)
{
await Shell.Current.GoToAsync("//profile/details");
}
private async void BtnGotoPage4(object sender, EventArgs e)
{
await Shell.Current.GoToAsync("//profile/settings");
}
```
3. Start the App and do exactly the following Navigation Steps:
3.1. App is opened -> Page1 is shown initially
3.2. Click in the bottom Tab bar onto the second Tab labeled "Tab 2" -> Page2 is shown
3.3. Now click the second Button that triggers the ```BtnGotoPage4```event handler
### Expected Behavior
The App navigates to Page 4
### Actual Behavior
The above mentioned exception is thrown in the EventHandler at line ```await Shell.Current.GoToAsync("//profile/settings");``` when the navigation steps are executed exactly in the written order.
**Please note:**
The navigation works + exception is **not** thrown when
- After Step 3.2 you first go to Page 3 manually by using the top Tab-Bar, go back to Page 2 and then click the second Button
- After Step 3.2 you first go to Page 4 manually by using the top Tab-Bar, go back to Page 2 and then click the second Button
- After Step 3.2 you first go to Page 3 by using the first Button (```await Shell.Current.GoToAsync("//profile/details");``` is executed), go back to Page 2 and then click the second button
Also the navigation to Page 3 with the first Button (```await Shell.Current.GoToAsync("//profile/details");```) works in all cases. It never throws an exception.
### Basic Information
- Version with issue:
- Last known good version: n/a
- Platform Target Frameworks: <!-- All that apply -->
- Android: 9.0 / 10.0
- NuGet Packages: Xamarin.Forms 4.8.0.1687
- Affected Devices: Nokia 8, Google Pixel 4, Android Emulator
### Environment
<!--
1.
Visual Studio: Help > About Microsoft Visual Studio > Copy Info [button]
Visual Studio for Mac: Visual Studio > About Visual Studio > Show Details > Copy Information [button]
2. Paste into the code block below (between ```)
-->
```
Microsoft Visual Studio Professional 2019
Version 16.8.2
VisualStudio.16.Release/16.8.2+30717.126
Microsoft .NET Framework
Version 4.8.04084
Installed Version: Professional
Visual C++ 2019 00435-20000-00004-AA461
Microsoft Visual C++ 2019
ADL Tools Service Provider 1.0
This package contains services used by Data Lake tools
ASA Service Provider 1.0
ASP.NET and Web Tools 2019 16.8.553.28003
ASP.NET and Web Tools 2019
ASP.NET Core Razor Language Services 16.1.0.2052803+84e121f1403378489b842e1797df2f3f5a49ac3c
Provides languages services for ASP.NET Core Razor.
ASP.NET Web Frameworks and Tools 2019 16.8.553.28003
For additional information, visit https://www.asp.net/
Azure App Service Tools v3.0.0 16.8.553.28003
Azure App Service Tools v3.0.0
Azure Data Lake Node 1.0
This package contains the Data Lake integration nodes for Server Explorer.
Azure Data Lake Tools for Visual Studio 2.6.3000.0
Microsoft Azure Data Lake Tools for Visual Studio
Azure Functions and Web Jobs Tools 16.8.553.28003
Azure Functions and Web Jobs Tools
Azure Stream Analytics Tools for Visual Studio 2.6.3000.0
Microsoft Azure Stream Analytics Tools for Visual Studio
C# Tools 3.8.0-5.20567.16+53c5d7d3cf13d88978744a32a27c5f8350a8400a
C# components used in the IDE. Depending on your project type and settings, a different version of the compiler may be used.
Common Azure Tools 1.10
Provides common services for use by Azure Mobile Services and Microsoft Azure Tools.
Cookiecutter 16.8.20241.2
Provides tools for finding, instantiating and customizing templates in cookiecutter format.
Extensibility Message Bus 1.2.6 (master@34d6af2)
Provides common messaging-based MEF services for loosely coupled Visual Studio extension components communication and integration.
Fabric.DiagnosticEvents 1.0
Fabric Diagnostic Events
GitHub.VisualStudio 2.11.106.19330
A Visual Studio Extension that brings the GitHub Flow into Visual Studio.
IntelliCode Extension 1.0
IntelliCode Visual Studio Extension Detailed Info
JetBrains ReSharper 2020.2.4 Build 202.0.20200925.65451
JetBrains ReSharper package for Microsoft Visual Studio. For more information about ReSharper, visit http://www.jetbrains.com/resharper. Copyright © 2020 JetBrains, Inc.
Microsoft Azure HDInsight Azure Node 2.6.3000.0
HDInsight Node under Azure Node
Microsoft Azure Hive Query Language Service 2.6.3000.0
Language service for Hive query
Microsoft Azure Service Fabric Tools for Visual Studio 16.0
Microsoft Azure Service Fabric Tools for Visual Studio
Microsoft Azure Stream Analytics Language Service 2.6.3000.0
Language service for Azure Stream Analytics
Microsoft Azure Stream Analytics Node 1.0
Azure Stream Analytics Node under Azure Node
Microsoft Azure Tools 2.9
Microsoft Azure Tools for Microsoft Visual Studio 2019 - v2.9.30924.1
Microsoft Continuous Delivery Tools for Visual Studio 0.4
Simplifying the configuration of Azure DevOps pipelines from within the Visual Studio IDE.
Microsoft JVM Debugger 1.0
Provides support for connecting the Visual Studio debugger to JDWP compatible Java Virtual Machines
Microsoft Library Manager 2.1.113+g422d40002e.RR
Install client-side libraries easily to any web project
Microsoft MI-Based Debugger 1.0
Provides support for connecting Visual Studio to MI compatible debuggers
Microsoft Visual C++ Wizards 1.0
Microsoft Visual C++ Wizards
Microsoft Visual Studio Tools for Containers 1.1
Develop, run, validate your ASP.NET Core applications in the target environment. F5 your application directly into a container with debugging, or CTRL + F5 to edit & refresh your app without having to rebuild the container.
Microsoft Visual Studio VC Package 1.0
Microsoft Visual Studio VC Package
Mono Debugging for Visual Studio 16.8.43 (00471f8)
Support for debugging Mono processes with Visual Studio.
Node.js Tools 1.5.20902.1 Commit Hash:b474efcb6f92db52a8f8e2e6a8cb9648476885cc
Adds support for developing and debugging Node.js apps in Visual Studio
NuGet Package Manager 5.8.0
NuGet Package Manager in Visual Studio. For more information about NuGet, visit https://docs.nuget.org/
ProjectServicesPackage Extension 1.0
ProjectServicesPackage Visual Studio Extension Detailed Info
Python 16.8.20241.2
Provides IntelliSense, projects, templates, debugging, interactive windows, and other support for Python developers.
Python - Conda support 16.8.20241.2
Conda support for Python projects.
Python - Django support 16.8.20241.2
Provides templates and integration for the Django web framework.
Python - IronPython support 16.8.20241.2
Provides templates and integration for IronPython-based projects.
Python - Profiling support 16.8.20241.2
Profiling support for Python projects.
SettingsCommands Extension 1.0
SettingsCommands Visual Studio Extension Detailed Info
SQL Server Data Tools 16.0.62010.06180
Microsoft SQL Server Data Tools
Test Adapter for Boost.Test 1.0
Enables Visual Studio's testing tools with unit tests written for Boost.Test. The use terms and Third Party Notices are available in the extension installation directory.
Test Adapter for Google Test 1.0
Enables Visual Studio's testing tools with unit tests written for Google Test. The use terms and Third Party Notices are available in the extension installation directory.
ToolWindowHostedEditor 1.0
Hosting json editor into a tool window
TypeScript Tools 16.0.21016.2001
TypeScript Tools for Microsoft Visual Studio
Visual Basic Tools 3.8.0-5.20567.16+53c5d7d3cf13d88978744a32a27c5f8350a8400a
Visual Basic components used in the IDE. Depending on your project type and settings, a different version of the compiler may be used.
Visual C++ for Cross Platform Mobile Development (Android) 16.0.30608.117
Visual C++ for Cross Platform Mobile Development (Android)
Visual C++ for Cross Platform Mobile Development (iOS) 16.0.30608.117
Visual C++ for Cross Platform Mobile Development (iOS)
Visual C++ for Linux Development 1.0.9.30608
Visual C++ for Linux Development
Visual F# Tools 16.8.0-beta.20507.4+da6be68280c89131cdba2045525b80890401defd
Microsoft Visual F# Tools
Visual Studio Code Debug Adapter Host Package 1.0
Interop layer for hosting Visual Studio Code debug adapters in Visual Studio
Visual Studio Container Tools Extensions 1.0
View, manage, and diagnose containers within Visual Studio.
Visual Studio Tools for CMake 1.0
Visual Studio Tools for CMake
Visual Studio Tools for Containers 1.0
Visual Studio Tools for Containers
Visual Studio Tools for Kubernetes 1.0
Visual Studio Tools for Kubernetes
Visual Studio Tools for Unity 4.8.2.0
Visual Studio Tools for Unity
VisualStudio.DeviceLog 1.0
Information about my package
VisualStudio.Foo 1.0
Information about my package
VisualStudio.Mac 1.0
Mac Extension for Visual Studio
Xamarin 16.8.000.255 (d16-8@d002176)
Visual Studio extension to enable development for Xamarin.iOS and Xamarin.Android.
Xamarin Designer 16.8.0.507 (remotes/origin/d16-8@e87b24884)
Visual Studio extension to enable Xamarin Designer tools in Visual Studio.
Xamarin Templates 16.8.112 (86385a3)
Templates for building iOS, Android, and Windows apps with Xamarin and Xamarin.Forms.
Xamarin.Android SDK 11.1.0.17 (d16-8/c0e2b8e)
Xamarin.Android Reference Assemblies and MSBuild support.
Mono: be2226b
Java.Interop: xamarin/java.interop/d16-8@79d9533
ProGuard: Guardsquare/proguard/proguard6.2.2@ebe9000
SQLite: xamarin/sqlite/3.32.1@1a3276b
Xamarin.Android Tools: xamarin/xamarin-android-tools/d16-8@2fb1cbc
Xamarin.iOS and Xamarin.Mac SDK 14.4.1.3 (e30c41de3)
Xamarin.iOS and Xamarin.Mac Reference Assemblies and MSBuild support.
```
### Screenshots
![Screenshot 2020-11-24 120347](https://user-images.githubusercontent.com/54247971/100086166-4cc0df00-2e4d-11eb-8f28-03fc82c2e4bf.png)
![Screenshot 2020-11-24 120443](https://user-images.githubusercontent.com/54247971/100086168-4d597580-2e4d-11eb-8c8c-df359e52ef98.png)
### Reproduction Link
[ShellNavigationSample.zip](https://github.com/xamarin/Xamarin.Forms/files/5589403/ShellNavigationSample.zip)


---

<!-- source=github_issue; title=md-mods v31 got "multiform" problems...; url=https://github.com/bnfour/md-mods/issues/32 -->

# md-mods v31 got "multiform" problems...

- Source: github_issue
- URL: https://github.com/bnfour/md-mods/issues/32

after update, i download newest release, unzip it, _replace files in folder_
then i start TRY ( or call it **test**
(btw the _environment of language_, is **Chinese**
and problems show those self obo
<img width="979" height="582" alt="Image" src="https://github.com/user-attachments/assets/6c32cd61-42f6-4a92-8b04-bfb297cb5973" />
> New score! but the chinese ui, the words(新纪录!), is that something weird on drop shadow effects?
<img width="1081" height="773" alt="Image" src="https://github.com/user-attachments/assets/c160f40c-a324-444f-8fb4-2a33c6926026" />
> where s my rank!?
it's ridiculous, unbelievable, so i restart it twice and changed my language setting temp
<img width="1110" height="732" alt="Image" src="https://github.com/user-attachments/assets/eb3275f6-18d7-4272-a03c-4713508b454e" />
> i knew it~
<img width="1076" height="752" alt="Image" src="https://github.com/user-attachments/assets/5fc3aca4-cf1b-4eb8-93a3-94a22f327656" />
> but where's my rank😭😭, i cant live without her😭😭😭😭😭😭😭😭😭
the rank panel just "loading" for a moment when u open a album and disappeared, everything s gone but empty(🥲
but have to say ui and every is fixed!~ (maybe?
i need rank back🥲
i ll run more test and troubleshoots to make sure the module which caused this problem is, and keep my update


---

<!-- source=github_issue; title=Unable to import a .glb file on Android; url=https://github.com/atteneder/glTFast/issues/576 -->

# Unable to import a .glb file on Android

- Source: github_issue
- URL: https://github.com/atteneder/glTFast/issues/576

**Describe the bug**
Hello there!
I'm trying to import a .glb file using the "Gltf asset" script with all option on default. No custom code.
It's working fine on the editor, but on Android I'm getting the following :
`2023/02/27 17:16:43.283 19335 19365 Error Unity NullReferenceException: Object reference not set to an instance of an object.
2023/02/27 17:16:43.283 19335 19365 Error Unity at GLTFast.Materials.BuiltInMaterialGenerator.GenerateDefaultMaterial (System.Boolean pointsSupport) [0x00000] in <00000000000000000000000000000000>:0
2023/02/27 17:16:43.283 19335 19365 Error Unity at GLTFast.Materials.MaterialGenerator.GetDefaultMaterial (System.Boolean pointsSupport) [0x00000] in <00000000000000000000000000000000>:0
2023/02/27 17:16:43.283 19335 19365 Error Unity at GLTFast.GameObjectInstantiator.AddPrimitive (System.UInt32 nodeIndex, System.String meshName, UnityEngine.Mesh mesh, System.Int32[] materialIndices, System.UInt32[] joints, System.Nullable`1[T] rootJoint, System.Single[] morphTargetWeights, System.Int32 primitiveNumeration) [0x00000] in <00000000000000000000000000000000>:0
2023/02/27 17:16:43.283 19335 19365 Error Unity at GLTFast.GltfImport+<>c__DisplayClass116_0.<InstantiateSceneInternal>g__PopulateHierarchy|2 (System.UInt32 nodeIndex, System.Nullable`1[T] parentIndex) [0x00000] in <00000000000000000000000000000000>:0
2023/02/27 17:16:43.283 19335 19365 Error Unity at GLTFast.GltfImport+<>c__DisplayClass116_0.<InstantiateSceneInternal>g__IterateNodes|0 (System.UInt32 nodeI
`
The .GLB file in question is attached.
> Unity 2022.2.2f1
> Galaxy Tab S7 with Android 13
[haha-63f797eb227eb(2).zip](https://github.com/atteneder/glTFast/files/10852681/haha-63f797eb227eb.2.zip)
I've also tried all the manual way to import a .GLB following the documentation, but they all end with the same error message.
Thanks !


---

<!-- source=github_issue; title=There is a issue about androidmanifest.xml; url=https://github.com/TLabAltoh/TLabWebViewVR/issues/11 -->

# There is a issue about androidmanifest.xml

- Source: github_issue
- URL: https://github.com/TLabAltoh/TLabWebViewVR/issues/11

Form the your TLabWebViewVR Asset migration tutorial (https://www.youtube.com/watch?v=_Tj6pHsAz6M)
I followed your guidelines, but encountered four problems while building.
I am currently working through the Quest 2 and I think there is a problem with androidmanifest XML file. The following is my problem code.
1) NullReferenceException: Object reference not set to an instance of an object
AndroidManifest.SetHardwareAccelerated (System.Boolean enabled) (at Assets/TLab/TLabWebView/Editor/UnityWebViewPostprocessBuild.cs:145)
UnityWebViewPostprocessBuild.OnPostGenerateGradleAndroidProject (System.String basePath) (at Assets/TLab/TLabWebView/Editor/UnityWebViewPostprocessBuild.cs:25)
UnityEditor.Android.PostProcessor.Tasks.ProcessGenerateProjectCallbacks.OnGeneratePlatformProjectPostprocess (System.String path, System.Boolean strict) (at <0f901cb1488646d79bc8fbaad188a860>:0)
UnityEngine.GUIUtility:ProcessEvent(Int32, IntPtr, Boolean&)
2) NullReferenceException: Object reference not set to an instance of an object
AndroidManifest.SetHardwareAccelerated (System.Boolean enabled) (at Assets/TLab/TLabWebView/Editor/UnityWebViewPostprocessBuild.cs:145)
UnityWebViewPostprocessBuild.OnPostGenerateGradleAndroidProject (System.String basePath) (at Assets/TLab/TLabWebView/Editor/UnityWebViewPostprocessBuild.cs:25)
UnityEditor.Android.PostProcessor.Tasks.ProcessGenerateProjectCallbacks.OnGeneratePlatformProjectPostprocess (System.String path, System.Boolean strict) (at <0f901cb1488646d79bc8fbaad188a860>:0)
UnityEditor.Android.PostProcessor.Tasks.ProcessGenerateProjectCallbacks.Execute (UnityEditor.Android.PostProcessor.PostProcessorContext context) (at <0f901cb1488646d79bc8fbaad188a860>:0)
3) Build completed with a result of 'Failed' in 7 seconds (6973 ms)2 errorsUnityEngine.GUIUtility:ProcessEvent (int,intptr,bool&)
Can you help me?


---

<!-- source=github_issue; title=NullReferenceException spamming from RSE_PartAudioManager.LateUpdate; url=https://github.com/KSPModStewards/RocketSoundEnhancement/issues/24 -->

# NullReferenceException spamming from RSE_PartAudioManager.LateUpdate

- Source: github_issue
- URL: https://github.com/KSPModStewards/RocketSoundEnhancement/issues/24

Rapidly getting `NullReferenceException` at `RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate()` on flight.
The exception doesn't pop at KSC. Flying a stock Kerbal X doesn't cause it to pop. Once switch to a vessel with KSPInterstellarExtended parts, it starts to pop.
Installed many mods. All mods are installed by CKAN. [mod-list.zip](https://github.com/ensou04/RocketSoundEnhancement/files/11003387/mod-list.zip)
```
[LOG 00:18:15.231] [KnowledgeBase] OnAppLauncherReady 122806
[LOG 00:18:15.243] ScaleModList: listSize 533 maxListSize 870
[LOG 00:18:15.243] [Kopernicus]: StarLightSwitcher: Set active star => Sun
[LOG 00:18:15.337] [UIApp] OnDestroy: Contracts
[LOG 00:18:16.401] 3/18/2023 12:18:16 AM,KerbalAlarmClock,Adding DrawGUI to PostRender Queue
[LOG 00:18:16.401] 3/18/2023 12:18:16 AM,KerbalAlarmClock,Skipping version check
[LOG 00:18:16.412] ScaleModList: listSize 574 maxListSize 870
[LOG 00:18:16.414] [MessageSystem] Reposition 0.02 122807
[LOG 00:18:16.414] [GenericAppFrame] Reposition 0.02 122807
[LOG 00:18:16.414] [GenericAppFrame] Reposition 0.02 122807
[LOG 00:18:16.428] [KSPI]: ThermalNozzleController - Found 20 compatible fuel modes out of 39 available
[LOG 00:18:16.429] [KSPI]: ThermalNozzleController - Setup propellant chosen propellant 19 / 39
[LOG 00:18:16.429] [KSPI]: ThermalNozzleController set propellant name: LiquidFuel ratio: 0.9 resourceFlowMode: STACK_PRIORITY_SEARCH
[LOG 00:18:16.429] [KSPI]: ThermalNozzleController set propellant name: Oxidizer ratio: 1.1 resourceFlowMode: STACK_PRIORITY_SEARCH
[LOG 00:18:16.430] Cannot assign AudioClip 'sound_GenericFlameout' to AudioFX
[EXC 00:18:16.433] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:16.455] [FlightIntegrator]: Reloaded drag cube for zeroed cube root part mk1-3pod (Nuke) on vessel Nuke
[LOG 00:18:16.455] [FlightIntegrator]: Vessel Nuke has been unloaded 280.120000006114, applying analytic temperature 192.243514124605
[LOG 00:18:16.458] [KSPI]: ModuleEngineWarp on TRN23R was Force Activated
[LOG 00:18:16.458] [KSPI]: ThermalNozzleController - Found 20 compatible fuel modes out of 39 available
[LOG 00:18:16.458] [KSPI]: ThermalNozzleController - Setup propellant chosen propellant 19 / 39
[LOG 00:18:16.458] [KSPI]: ThermalNozzleController set propellant name: LiquidFuel ratio: 0.9 resourceFlowMode: STACK_PRIORITY_SEARCH
[LOG 00:18:16.458] [KSPI]: ThermalNozzleController set propellant name: Oxidizer ratio: 1.1 resourceFlowMode: STACK_PRIORITY_SEARCH
[LOG 00:18:16.458] [KSPI]: ThermalNozzleController - Setup propellant chosen propellant 19 / 39
[LOG 00:18:16.458] [KSPI]: ThermalNozzleController set propellant name: LiquidFuel ratio: 0.9 resourceFlowMode: STACK_PRIORITY_SEARCH
[LOG 00:18:16.458] [KSPI]: ThermalNozzleController set propellant name: Oxidizer ratio: 1.1 resourceFlowMode: STACK_PRIORITY_SEARCH
[EXC 00:18:16.472] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:16.528] [Scatterer][Info] Running in unified camera mode
[LOG 00:18:16.529] [Scatterer][Debug] Adding TweakShadowCascades: (0.002, 0.015, 0.150) to Camera Camera 00
[LOG 00:18:16.529] [Scatterer][Debug] Default split: (0.002, 0.022, 0.178)
[LOG 00:18:16.529] [Scatterer][Debug] Set shadow distance: 50000
[LOG 00:18:16.529] [Scatterer][Debug] Number of shadow cascades detected 4
[LOG 00:18:16.529] [Scatterer][Debug] Setting shadowmap resolution to: 8192 on SunLight
[LOG 00:18:16.545] [Scatterer][Debug] No sunflare syntax version found, defaulting to version 1 for retro-compatibility
[LOG 00:18:16.546] [Scatterer][Debug] Added custom sun flare for Sun
[LOG 00:18:16.546] [Scatterer][Debug] mapping EVE clouds
[LOG 00:18:16.555] [Scatterer][Debug] Eve assembly type found
[LOG 00:18:16.555] [Scatterer][Debug] Eve assembly version: Atmosphere, Version=1.11.7.1, Culture=neutral, PublicKeyToken=null
[LOG 00:18:16.555] [Scatterer][Info] Successfully grabbed EVE Instance
[LOG 00:18:16.555] [Scatterer][Debug] layer2d not found for layer on planet :Kerbin
[LOG 00:18:16.555] [Scatterer][Debug] layer2d not found for layer on planet :Laythe
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Moho
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Moho
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Moho
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Eve
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Eve
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Eve
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Eve
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Eve
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Eve
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Eve
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Kerbin
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Kerbin
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Kerbin
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Mun
[LOG 00:18:16.555] [Scatterer][Debug] layer2d not found for layer on planet :Minmus
[LOG 00:18:16.555] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Duna
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Duna
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Duna
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Ike
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Dres
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Jool
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Jool
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Jool
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Laythe
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Laythe
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Laythe
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Laythe
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Vall
[LOG 00:18:16.556] [Scatterer][Debug] layer2d not found for layer on planet :Vall
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Tylo
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Pol
[LOG 00:18:16.556] [Scatterer][Debug] layer2d not found for layer on planet :Pol
[LOG 00:18:16.556] [Scatterer][Debug] Detected EVE 2d cloud layer for planet: Eeloo
[LOG 00:18:16.556] [Scatterer][Debug] layer2d not found for layer on planet :Eeloo
[LOG 00:18:16.556] [Scatterer][Debug] layer2d not found for layer on planet :Minmus
[LOG 00:18:16.556] [Scatterer][Debug] Core setup done
[LOG 00:18:16.565] [Scatterer][Debug] Disabling stock sunflare for Sun
[LOG 00:18:16.568] [Scatterer][Debug] Setting shadowmap resolution to: 8192 on SunLight
[LOG 00:18:16.568] [Scatterer][Debug] Added eclipse caster Mun for Kerbin
[LOG 00:18:16.568] [Scatterer][Debug] Added eclipse caster Minmus for Kerbin
[LOG 00:18:16.568] [Scatterer][Debug] Atmosphere config found for: Kerbin
[LOG 00:18:16.667] [Scatterer][Debug] layer2d not found for layer on planet: Kerbin
[LOG 00:18:16.667] [EVE CloudsManager]: Clouds2D is now MACRO
[LOG 00:18:16.667] [EVE CloudsManager]: Clouds2D is now MACRO
[LOG 00:18:16.667] [EVE CloudsManager]: Clouds2D is now MACRO
[LOG 00:18:16.667] [Scatterer][Debug] Skynode initiated for Kerbin
[LOG 00:18:16.668] [Scatterer][Debug] Ocean config found for: Kerbin
[LOG 00:18:16.683] [Scatterer][Info] Caustics texture E:/Games/SteamLibrary/steamapps/common/Kerbal Space Program/KSP_x64_Data/../GameData/scatterer/config/Planets/Caustics.png not found, disabling caustics for current planet
[LOG 00:18:16.683] [Scatterer][Info] Caustics texture E:/Games/SteamLibrary/steamapps/common/Kerbal Space Program/KSP_x64_Data/../GameData/scatterer/config/Planets/Caustics.png not found, disabling caustics light rays for current planet
[LOG 00:18:17.390] [Scatterer][Debug] Effects loaded for Kerbin
[LOG 00:18:17.650] [PlanetariumCamera]: Focus: Nuke
[LOG 00:18:17.658] [EVE CloudsManager]: CloudsPQS: (EVE Clouds: KerbinAurora) OnSphereActive
[LOG 00:18:17.658] [EVE CloudsManager]: Clouds2D is now MACRO
[LOG 00:18:17.658] [EVE CloudsManager]: CloudsPQS: (EVE Clouds: KerbinSnow) OnSphereActive
[LOG 00:18:17.658] [EVE CloudsManager]: CloudsPQS: (EVE Clouds: KerbinHigh) OnSphereActive
[LOG 00:18:17.658] [EVE CloudsManager]: Clouds2D is now MACRO
[LOG 00:18:17.658] [EVE CloudsManager]: CloudsPQS: (EVE Clouds: KerbinMain) OnSphereActive
[LOG 00:18:17.658] [EVE CloudsManager]: Clouds2D is now MACRO
[EXC 00:18:17.661] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:17.666] [Scatterer][Debug] Added reflection probe fixer to Reflection Probes Camera
[LOG 00:18:17.666] [Scatterer][Debug] Ocean effects disabled from reflections Camera Reflection Probes Camera
[EXC 00:18:17.668] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:17.677] [Scatterer][Info] Skynode switch effects to local mode Kerbin
[LOG 00:18:17.678] [Scatterer][Debug] Setting shadowmap resolution to: 8192 on SunLight
[LOG 00:18:17.678] [Scatterer][Debug] Atmosphere config found for: Minmus
[LOG 00:18:17.773] [Scatterer][Debug] Skynode initiated for Minmus
[LOG 00:18:17.773] [Scatterer][Debug] Effects loaded for Minmus
[LOG 00:18:18.036] [UIApp] Adding ResourceDisplay to Application Launcher
[LOG 00:18:18.038] ScaleModList: listSize 574 maxListSize 829
[LOG 00:18:18.038] [UIApp] Adding ResourceDisplay to Application Launcher
[LOG 00:18:18.040] ScaleModList: listSize 574 maxListSize 788
[EXC 00:18:18.043] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.047] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:18.057] [ResourceDisplay] OnAppStarted(): id: -971864
[LOG 00:18:18.058] [GenericAppFrame] Reposition 0.1721366 122811
[LOG 00:18:18.058] [ResourceDisplay] OnAppStarted(): id: 238440
[LOG 00:18:18.058] ResourceDisplay already exist, destroying this instance
[LOG 00:18:18.058] [UIApp] OnDestroy: ResourceDisplay
[LOG 00:18:18.059] ScaleModList: listSize 574 maxListSize 788
[EXC 00:18:18.062] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.066] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:18.081] [UIApp] Adding AlarmClock to Application Launcher
[LOG 00:18:18.083] ScaleModList: listSize 574 maxListSize 788
[LOG 00:18:18.083] [UIApp] Adding ActionGroupsApp to Application Launcher
[LOG 00:18:18.085] ScaleModList: listSize 574 maxListSize 747
[LOG 00:18:18.085] [UIApp] Adding Missions App to Application Launcher
[LOG 00:18:18.087] ScaleModList: listSize 574 maxListSize 706
[LOG 00:18:18.087] CURRENCY WIDGET False False False
[EXC 00:18:18.089] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:18.090] [UIApp] OnDestroy: CurrencyWidgetsApp
[EXC 00:18:18.094] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:18.102] [Scatterer][Debug] Mapping EVE volumetrics for planet: Kerbin
[LOG 00:18:18.102] [Scatterer][Debug] No volumetric cloud for layer on planet: Kerbin
[LOG 00:18:18.102] [Scatterer][Debug] No volumetric cloud for layer on planet: Kerbin
[LOG 00:18:18.102] [Scatterer][Debug] Raymarched volumetric clouds error on planet: KerbinSystem.NullReferenceException: Object reference not set to an instance of an object
at scatterer.EVEReflectionHandler.mapEVEVolumetrics (System.String celestialBodyName, System.Collections.Generic.List`1[T] EVEvolumetrics) [0x00156] in <684aa87c0d2345f8a9e4739403f4afff>:0
[LOG 00:18:18.102] [Scatterer][Debug] Raymarched volumetric clouds error on planet: KerbinSystem.NullReferenceException: Object reference not set to an instance of an object
at scatterer.EVEReflectionHandler.mapEVEVolumetrics (System.String celestialBodyName, System.Collections.Generic.List`1[T] EVEvolumetrics) [0x00156] in <684aa87c0d2345f8a9e4739403f4afff>:0
[LOG 00:18:18.103] [Scatterer][Debug] Raymarched volumetric clouds error on planet: KerbinSystem.NullReferenceException: Object reference not set to an instance of an object
at scatterer.EVEReflectionHandler.mapEVEVolumetrics (System.String celestialBodyName, System.Collections.Generic.List`1[T] EVEvolumetrics) [0x00156] in <684aa87c0d2345f8a9e4739403f4afff>:0
[LOG 00:18:18.103] [Scatterer][Debug] Raymarched volumetric clouds error on planet: KerbinSystem.NullReferenceException: Object reference not set to an instance of an object
at scatterer.EVEReflectionHandler.mapEVEVolumetrics (System.String celestialBodyName, System.Collections.Generic.List`1[T] EVEvolumetrics) [0x00156] in <684aa87c0d2345f8a9e4739403f4afff>:0
[LOG 00:18:18.103] [Scatterer][Debug] Detected 2 EVE volumetric layers for planet: Kerbin
[LOG 00:18:18.120] [GenericAppFrame] Reposition 0.218537 122813
[LOG 00:18:18.124] [ActionGroupsApp] OnAppStarted(): id: -971888
[LOG 00:18:18.125] [GenericAppFrame] Reposition 0.218537 122813
[LOG 00:18:18.125] [UIApp] Adding DeltaVApp to Application Launcher
[LOG 00:18:18.128] ScaleModList: listSize 574 maxListSize 665
[LOG 00:18:18.128] [MissionsApp] OnAppStarted(): id: -971876
[LOG 00:18:18.128] MissionsApp does not execute in this game mode, destroying this instance
[LOG 00:18:18.128] [UIApp] OnDestroy: Missions App
[LOG 00:18:18.128] ScaleModList: listSize 574 maxListSize 665
[EXC 00:18:18.133] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.140] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:18.150] [GenericAppFrame] Reposition 0.258537 122814
[EXC 00:18:18.156] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.161] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:18.168] [UIApp] Adding Cargo to Application Launcher
[LOG 00:18:18.170] ScaleModList: listSize 574 maxListSize 665
[LOG 00:18:18.171] [UIApp] Adding Construction to Application Launcher
[LOG 00:18:18.173] ScaleModList: listSize 574 maxListSize 624
[LOG 00:18:18.174] [UIApp] Adding KSPedia to Application Launcher
[LOG 00:18:18.176] ScaleModList: listSize 574 maxListSize 583
[WRN 00:18:18.176] HighlightingSystem : Edge Highlighting requires AA to work!
[EXC 00:18:18.178] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.183] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:18.192] [UIApp] Adding ManeuverTool to Application Launcher
[LOG 00:18:18.197] ScaleModList: listSize 574 maxListSize 542
[LOG 00:18:18.197] [ApplicationLauncher] SetHidden:
[LOG 00:18:18.199] ScaleModList: listSize 574 maxListSize 551
[EXC 00:18:18.205] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.210] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:18.223] [GenericAppFrame] Reposition 0.3284564 122817
[LOG 00:18:18.235] [ManeuverTool]: Found 1 transfer types
[EXC 00:18:18.243] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.247] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.259] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.262] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.272] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.276] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[LOG 00:18:18.293] Flight State Captured
[LOG 00:18:18.293] Saving Achievements Tree...
[LOG 00:18:18.293] Saving Achievements Tree...
[LOG 00:18:18.293] Saving Achievements Tree...
[LOG 00:18:18.293] [MessageSystem] Save Messages
[LOG 00:18:18.303] [KSPI]: GameEventSubscriber - detected OnGameStateSaved
[LOG 00:18:18.365] Game State Saved as persistent
[LOG 00:18:18.365] Flight ready at frame 122820
[EXC 00:18:18.368] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.373] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.387] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.391] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.415] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.418] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.435] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.439] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.449] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.452] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.460] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.472] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.490] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.492] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.500] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.504] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.523] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.526] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.539] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.542] NullReferenceException: Object reference not set to an instance of an object
scatterer.OceanNode.OnPreCull () (at <684aa87c0d2345f8a9e4739403f4afff>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
[EXC 00:18:18.575] NullReferenceException
RocketSoundEnhancement.RSE_PartAudioManager.LateUpdate () (at <291f40d3d6db4209b489483e9d4aa7c3>:0)
UnityEngine.DebugLogHandler:LogException(Exception, Object)
ModuleManager.UnityLogHandle.InterceptLogHandler:LogException(Exception, Object)
UnityEngine.Debug:CallOverridenDebugHandler(Exception, Object)
```


---

<!-- source=github_issue; title=Error in WorldGenStep: System.TypeLoadException; url=https://github.com/vegapnk/RJW-Genes/issues/159 -->

# Error in WorldGenStep: System.TypeLoadException

- Source: github_issue
- URL: https://github.com/vegapnk/RJW-Genes/issues/159

```
Error in WorldGenStep: System.TypeLoadException: Could not resolve type with token 01000081 (from typeref, class/assembly rjw.CompHediffBodyPart, RJW, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null)
[Ref B367D339]
at RJW_Genes.Gene_ChangeCumAmount.PostMake ()
at RimWorld.GeneMaker.MakeGene (Verse.GeneDef def, Verse.Pawn pawn)
- TRANSPILER net.pardeike.rimworld.lib.harmony: IEnumerable`1 VisualExceptions.ExceptionsAndActivatorHandler:Transpiler(IEnumerable`1 instructions, MethodBase original)
at RimWorld.Pawn_GeneTracker.AddGene (Verse.GeneDef geneDef, System.Boolean xenogene)
at RimWorld.Pawn_GeneTracker.SetXenotype (RimWorld.XenotypeDef xenotype)
- PREFIX rimworld.erdelf.alien_race.main: Boolean AlienRace.HarmonyPatches:SetXenotypePrefix(XenotypeDef xenotype, Pawn ___pawn)
at Verse.PawnGenerator.GenerateGenes (Verse.Pawn pawn, RimWorld.XenotypeDef xenotype, Verse.PawnGenerationRequest request)
- TRANSPILER rimworld.erdelf.alien_race.main: IEnumerable`1 AlienRace.HarmonyPatches:GenerateGenesTranspiler(IEnumerable`1 instructions)
- PREFIX rimworld.erdelf.alien_race.main: Void AlienRace.HarmonyPatches:GenerateGenesPrefix(Pawn pawn, PawnGenerationRequest& request)
- POSTFIX OskarPotocki.VFECore: Void VanillaGenesExpanded.PawnGenerator_GenerateGenes_Patch:Postfix(Pawn pawn)
- POSTFIX rimworld.erdelf.alien_race.main: Void AlienRace.HarmonyPatches:GenerateGenesPostfix(Pawn pawn)
- POSTFIX rjw_genes: Void RJW_Genes.Genes.Patch_AddNotifyOnGeneration:PawnGenerator_GenerateGenes_Postfix(Pawn pawn)
at Verse.PawnGenerator.TryGenerateNewPawnInternal (Verse.PawnGenerationRequest& request, System.String& error, System.Boolean ignoreScenarioRequirements, System.Boolean ignoreValidator)
- TRANSPILER rimworld.erdelf.alien_race.main: IEnumerable`1 AlienRace.HarmonyPatches:TryGenerateNewPawnInternalTranspiler(IEnumerable`1 instructions)
- PREFIX rimworld.erdelf.alien_race.main: Void AlienRace.HarmonyPatches:TryGenerateNewPawnInternalPrefix(PawnGenerationRequest& request)
- POSTFIX com.NewRatkin.rimworld.mod: Void NewRatkin.PawnGeneratorPatch:Postfix(Pawn __result)
at Verse.PawnGenerator.GenerateNewPawnInternal (Verse.PawnGenerationRequest& request)
- PREFIX rjw: Void rjw.Patch_PawnGenerator:Generate_Nymph(PawnGenerationRequest& request)
- POSTFIX OskarPotocki.VFECore: Void VFECore.Abilities.PawnGen_Patch:Postfix(Pawn __result)
- POSTFIX rjw: Void rjw.Patch_PawnGenerator:Fix_Nymph(PawnGenerationRequest& request, Pawn& __result)
- POSTFIX rjw: Void rjw.Patch_PawnGenerator:Sexualize_GenerateNewPawnInternal(PawnGenerationRequest& request, Pawn& __result)
- POSTFIX rjw: Void rjw.Patch_PawnGenerator:Fix_Newborn_styles(PawnGenerationRequest& request, Pawn& __result)
at Verse.PawnGenerator.GenerateOrRedressPawnInternal (Verse.PawnGenerationRequest request)
- PREFIX BreadMoFuckIdeoApprelAM: Void BreadMoFuckIdeoApprelAM.FuckIdeoApparel:FuckingIdeoApparel(PawnGenerationRequest& request)
at Verse.PawnGenerator.GeneratePawn (Verse.PawnGenerationRequest request)
- TRANSPILER net.pardeike.rimworld.lib.harmony: IEnumerable`1 VisualExceptions.ExceptionsAndActivatorHandler:Transpiler(IEnumerable`1 instructions, MethodBase original)
- PREFIX rimworld.erdelf.alien_race.main: Void AlienRace.HarmonyPatches:GeneratePawnPrefix(PawnGenerationRequest& request)
- PREFIX SmashPhil.VehicleFramework: Boolean Vehicles.Construction:GenerateVehiclePawn(PawnGenerationRequest request, Pawn& __result)
- POSTFIX rimworld.erdelf.alien_race.main: Void AlienRace.HarmonyPatches:GeneratePawnPostfix(Pawn __result)
- POSTFIX Ancot.MiliraRaceHarmonyPatch: Void Milira.Milira_MilianPawnGenerator_Patch:Postfix(Pawn& __result, PawnGenerationRequest request)
- POSTFIX AOBA.TheDeadManSwitch: Void DMS.Patch_GeneratePawnTitle:Postfix(Pawn& __result)
- POSTFIX RJW_Sexperience: Void RJWSexperience.Rimworld_Patch_GeneratePawn:Postfix(Pawn& __result)
- POSTFIX rjw.std: Void rjwstd.PawnGenerator_STD_spreader:PawnGenerator_STD_spreader_Patch(PawnGenerationRequest& request, Pawn& __result)
at RimWorld.Faction.TryGenerateNewLeader ()
at RimWorld.FactionGenerator.NewGeneratedFaction (RimWorld.FactionGeneratorParms parms)
at RimWorld.FactionGenerator.CreateFactionAndAddToManager (RimWorld.FactionDef facDef)
at RimWorld.FactionGenerator.AddFactionToManager (RimWorld.FactionDef facDef)
at RimWorld.FactionGenerator.GenerateFactionsIntoWorld (System.Collections.Generic.List`1[T] factions)
at RimWorld.Planet.WorldGenStep_Factions.GenerateFresh (System.String seed)
at RimWorld.Planet.WorldGenerator.GenerateWorld (System.Single planetCoverage, System.String seedString, RimWorld.Planet.OverallRainfall overallRainfall, RimWorld.Planet.OverallTemperature overallTemperature, RimWorld.Planet.OverallPopulation population, System.Collections.Generic.List`1[T] factions, System.Single pollution)
- TRANSPILER net.pardeike.rimworld.lib.harmony: IEnumerable`1 VisualExceptions.ExceptionsAndActivatorHandler:Transpiler(IEnumerable`1 instructions, MethodBase original)
VanillaGenesExpanded.PawnGenerator_GenerateGenes_Patch was patched by:
VFECore.Abilities.PawnGen_Patch was patched by:
Milira.Milira_MilianPawnGenerator_Patch was patched by:
RJWSexperience.Rimworld_Patch was patched by:
rjwstd.PawnGenerator_STD_spreader:PawnGenerator_STD_spreader_Patch was patched by:
```
This problem occurs when generating a new world, most of the factions disappear, and it still occurs when I only enable RJW and RJW_Gene (and the dependencies of these two mods)


---

<!-- source=github_issue; title=[Bug]: The autorejoin breaks when there is too many players.; url=https://github.com/winstxnhdw/lc-hax/issues/332 -->

# [Bug]: The autorejoin breaks when there is too many players.

- Source: github_issue
- URL: https://github.com/winstxnhdw/lc-hax/issues/332

### What happened?
When a lobby has many players, the auto rejoin spits an error stating that "An error occured while spawning into the game. Please report the glitch!"
### Current Commit Hash
f21ba203b2797757b1f376bbac7dd68ec9b8ac63
### Injector
- [X] SharpMonoInjectorCore
- [ ] Others
### If you selected "Others" above, please specify the injector you are using.
_No response_
### Log output
The bepinex logs the following:
[Info : Unity Log] NEW CLIENT JOINED THE SERVER!!; clientId: 29
[Info : Unity Log] adding value to ClientPlayerList at value of index 0: 0
[Info : Unity Log] adding value to ClientPlayerList at value of index 1: 1
[Info : Unity Log] adding value to ClientPlayerList at value of index 2: 7
[Info : Unity Log] adding value to ClientPlayerList at value of index 3: 3
[Info : Unity Log] adding value to ClientPlayerList at value of index 4: 4
[Info : Unity Log] adding value to ClientPlayerList at value of index 5: 29
[Info : Unity Log] adding value to ClientPlayerList at value of index 6: 6
[Info : Unity Log] adding value to ClientPlayerList at value of index 7: 8
[Info : Unity Log] adding value to ClientPlayerList at value of index 8: 9
[Info : Unity Log] adding value to ClientPlayerList at value of index 9: 11
[Info : Unity Log] adding value to ClientPlayerList at value of index 10: 12
[Info : Unity Log] adding value to ClientPlayerList at value of index 11: 15
[Info : Unity Log] adding value to ClientPlayerList at value of index 12: 14
[Info : Unity Log] Skipping at index 13
[Info : Unity Log] Skipping at index 14
[Info : Unity Log] Skipping at index 15
[Info : Unity Log] Skipping at index 16
[Info : Unity Log] Skipping at index 17
[Info : Unity Log] Skipping at index 18
[Info : Unity Log] Skipping at index 19
[Info : Unity Log] Skipping at index 20
[Info : Unity Log] Skipping at index 21
[Info : Unity Log] Skipping at index 22
[Info : Unity Log] Skipping at index 23
[Info : Unity Log] ClientId already in ClientPlayerList!
[Info : Unity Log] clientplayerlist count for client: 13
[Info : Unity Log] level id: 0
[Info : Unity Log] Changing level
[Info : Unity Log] New player: Player (5)
[Error : Unity Log] Failed to assign new player with client id #29: System.IndexOutOfRangeException: Index was outside the bounds of the array.
at (wrapper dynamic-method) StartOfRound.DMD<StartOfRound::OnPlayerConnectedClientRpc>(StartOfRound,ulong,int,ulong[],int,int,int,int,int,int,int,bool)
[Info : Unity Log] Leaving current lobby
[Info : Unity Log] Disconnecting and setting networkobjects to destroy with owner
[Info : Unity Log] Shutting down and disconnecting from server. Is host?: False
[Info : Unity Log] Current lobby is null. (Attempted to set lobby joinable False.)
[Info : Unity Log] Taking control of player Player (5) and enabling camera!
[Info : Unity Log] Message Received =>Snaa joined the ship.
[Info : Unity Log] !!!! ENABLING CAMERA FOR PLAYER: Player (5)
[Info : Unity Log] !!!! connectedPlayersAmount: 12
[Info : Unity Log] Has beta?: {hasBeta}
[Info : Unity Log] Has beta save data: True
[Warning: Unity Log] [Netcode] Deferred messages were received for a trigger of type OnSpawn with key 37, but that trigger was not received within within 1 second(s).
[Warning: Unity Log] [Netcode] Deferred messages were received for a trigger of type OnSpawn with key 41, but that trigger was not received within within 1 second(s).
[Warning: Unity Log] [Netcode] Deferred messages were received for a trigger of type OnSpawn with key 42, but that trigger was not received within within 1 second(s).
[Info : Unity Log] Resetting unlockables list!
[Info : Unity Log] Scene manager is null
[Error : Unity Log] NullReferenceException: Object reference not set to an instance of an object
Stack trace:
StartOfRound+<StartSpatialVoiceChat>d__217.MoveNext () (at <af9b1eec498a45aebd42601d6ab85015>:0)
UnityEngine.SetupCoroutine.InvokeMoveNext (System.Collections.IEnumerator enumerator, System.IntPtr returnValueAddress) (at <e27997765c1848b09d8073e5d642717a>:0)
[Error : Unity Log] NullReferenceException
Stack trace:
UnityEngine.Renderer.get_bounds () (at <e27997765c1848b09d8073e5d642717a>:0)
ESPMod+<>c__DisplayClass26_0.<OnGUI>b__3 (UnityEngine.Renderer renderer) (at <714989db4c1d4199b6072c5884679085>:0)
Extensions.ForEach[T] (System.Collections.Generic.IEnumerable`1[T] array, System.Action`1[T] action) (at <714989db4c1d4199b6072c5884679085>:0)
ESPMod.OnGUI () (at <714989db4c1d4199b6072c5884679085>:0)
[Error : Unity Log] NullReferenceException
Stack trace:
UnityEngine.Renderer.get_bounds () (at <e27997765c1848b09d8073e5d642717a>:0)
ESPMod+<>c__DisplayClass26_0.<OnGUI>b__3 (UnityEngine.Renderer renderer) (at <714989db4c1d4199b6072c5884679085>:0)
Extensions.ForEach[T] (System.Collections.Generic.IEnumerable`1[T] array, System.Action`1[T] action) (at <714989db4c1d4199b6072c5884679085>:0)
ESPMod.OnGUI () (at <714989db4c1d4199b6072c5884679085>:0)
[Info : Unity Log] DISABLING connection callbacks in round manager
[Info : Unity Log] Terminal disabled, disabling ESC key listener
[Info : Unity Log] Displaying menu message
[Info : Unity Log] Displaying menu message 3
[Info : Unity Log] Displaying menu notification: An error occured while spawning into the game. Please report the glitch!
### Acknowledgement
- [X] I have confirmed that my anti-virus is not blocking any of the relevant programs
- [X] I have done my due diligence to check for similar issues


---

<!-- source=github_issue; title=NFAuthentication error; url=https://github.com/CastagnaIT/plugin.video.netflix/issues/1020 -->

# NFAuthentication error

- Source: github_issue
- URL: https://github.com/CastagnaIT/plugin.video.netflix/issues/1020

## Bug report
#### Your Environment
- Netflix add-on version: 1.6.0
- Operating system version/name: LibreElec 9.6.2
- Device model: <!--- if appropriate -->
Used Operating system:
* [ ] Android
* [ ] iOS
* [x ] Linux
* [ ] OSX
* [x ] Raspberry-Pi
* [ ] Windows
### Describe the bug
<!--- A bug report that is not clear or not have a log will be closed -->
<!--- Put your text below this line -->
Hello.
I have tried to generate the key from NFAuthenticationKey.py using python and python3 on a desktop running Linux Mint 18 but get this error every time:
An error is occurred:
argument of type 'builtin_function_or_method' is not iterable_
I am completely at a loss as to what to do. Any help would be appreciated, thank you.
#### Expected behavior
<!--- Tell us what should happen -->
<!--- Put your text below this line -->
A code should be generated
#### Actual behavior
<!--- Tell us what happens instead -->
<!--- Put your text below this line -->
The above error message is displayed and the script finishes.
#### Steps to reproduce the behavior
<!--- Put your text below this line -->
1.
2.
3.
#### Possible fix
<!--- Not obligatory, but suggest a fix or reason for the bug -->
<!--- Put your text below this line -->
### Debug log
<!--- MANDATORY ATTACH/LINK A LOG:
1) Go to add-on settings, in Expert page and change "Debug logging level" to "Verbose"
2) Enable Kodi debug: go to Kodi Settings > System Settings > Logging, and enable "Enable debug logging"
3) How to get the log file? Read Kodi wiki: https://kodi.wiki/view/Log_file/Easy
4) You can attach the log file here or use http://paste.kodi.tv/
-->
The debug log can be found here:
<!--- PLEASE RESPECT THE RULES! DO NOT PASTE THE CONTENT OF THE LOG HERE AND DO NOT CUT THE LOG INFO -->
I do not think this is relevant in this case
### Additional context or screenshots (if appropriate)
I don't think here is any log information as I am not actually running Kodi when I try to run the script.
#### Other information
<!--- E.g. related issues, suggestions, links for us to have context, etc... -->
<!--- Put your text below this line -->
#### Screenshots
<!--- Add some screenshots if that helps understanding your problem -->
![Screenshot from 2021-01-02 16-56-55](https://user-images.githubusercontent.com/42699534/103461082-c46f0d00-4d1b-11eb-958d-59b12cffe5b4.png)
<!---
This addon respects the same rules used in the Kodi forum
https://kodi.wiki/view/Official:Forum_rules
therefore the single violation will eliminate your request
-->


---

<!-- source=github_issue; title=Intellisense (omnisharp) crashes after typing.; url=https://github.com/dotnet/vscode-csharp/issues/5017 -->

# Intellisense (omnisharp) crashes after typing.

- Source: github_issue
- URL: https://github.com/dotnet/vscode-csharp/issues/5017

I posted this in the Visual Studio Code issues and they told me to post it here saying that it's the C# extension's issue. I basically try to use Intellisense and it crashes. I can use it for 1 second and then it crashes every time, giving me this error: **"Unhandled Exception: System.NullReferenceException: Object reference not set to an instance of an object."** This error happens in every project & every script. I have already done an uninstall and reinstall. I have also tried different versions of Visual Studio Code. I have also tried 3 different versions of the C# extension.
I have also used the most recent version, and neither work (currently reverted to 1.23 to see if that fixed it, but nope).
This is my entire error log:
Starting OmniSharp server at 1/21/2022, 4:57:14 PM
Target: c:\Users\nicep\Documents\Game Projects\Legend-Maker\Legend Maker\Legend Maker.sln
OmniSharp server started.
Path: c:\Users\nicep\.vscode\extensions\ms-dotnettools.csharp-1.23.17\.omnisharp\1.38.1-beta.44\OmniSharp.exe
PID: 9444
[info]: OmniSharp.Stdio.Host
Starting OmniSharp on Windows 6.2.9200.0 (x64)
[info]: OmniSharp.Services.DotNetCliService
Checking the 'DOTNET_ROOT' environment variable to find a .NET SDK
[info]: OmniSharp.Services.DotNetCliService
Using the 'dotnet' on the PATH.
[info]: OmniSharp.Services.DotNetCliService
DotNetPath set to dotnet
[info]: OmniSharp.MSBuild.Discovery.MSBuildLocator
Located 1 MSBuild instance(s)
1: StandAlone 17.0.0 - "c:\Users\nicep\.vscode\extensions\ms-dotnettools.csharp-1.23.17\.omnisharp\1.38.1-beta.44\.msbuild\Current\Bin"
[info]: OmniSharp.MSBuild.Discovery.MSBuildLocator
MSBUILD_EXE_PATH environment variable set to 'c:\Users\nicep\.vscode\extensions\ms-dotnettools.csharp-1.23.17\.omnisharp\1.38.1-beta.44\.msbuild\Current\Bin\MSBuild.exe'
[info]: OmniSharp.MSBuild.Discovery.MSBuildLocator
Registered MSBuild instance: StandAlone 17.0.0 - "c:\Users\nicep\.vscode\extensions\ms-dotnettools.csharp-1.23.17\.omnisharp\1.38.1-beta.44\.msbuild\Current\Bin"
CscToolExe = csc.exe
CscToolPath = c:\Users\nicep\.vscode\extensions\ms-dotnettools.csharp-1.23.17\.omnisharp\1.38.1-beta.44\.msbuild\Current\Bin\Roslyn
MSBuildExtensionsPath = c:\Users\nicep\.vscode\extensions\ms-dotnettools.csharp-1.23.17\.omnisharp\1.38.1-beta.44\.msbuild
MSBuildToolsPath = c:\Users\nicep\.vscode\extensions\ms-dotnettools.csharp-1.23.17\.omnisharp\1.38.1-beta.44\.msbuild\Current\Bin
[info]: OmniSharp.WorkspaceInitializer
Invoking Workspace Options Provider: OmniSharp.Roslyn.CSharp.Services.CSharpFormattingWorkspaceOptionsProvider, Order: 0
[info]: OmniSharp.WorkspaceInitializer
Invoking Workspace Options Provider: OmniSharp.Roslyn.CSharp.Services.Completion.CompletionOptionsProvider, Order: 0
[info]: OmniSharp.WorkspaceInitializer
Invoking Workspace Options Provider: OmniSharp.Roslyn.CSharp.Services.RenameWorkspaceOptionsProvider, Order: 100
[info]: OmniSharp.WorkspaceInitializer
Invoking Workspace Options Provider: OmniSharp.Roslyn.CSharp.Services.ImplementTypeWorkspaceOptionsProvider, Order: 110
[info]: OmniSharp.WorkspaceInitializer
Invoking Workspace Options Provider: OmniSharp.Roslyn.CSharp.Services.BlockStructureWorkspaceOptionsProvider, Order: 140
[info]: OmniSharp.Cake.CakeProjectSystem
Detecting Cake files in 'c:\Users\nicep\Documents\Game Projects\Legend-Maker\Legend Maker'.
[info]: OmniSharp.Cake.CakeProjectSystem
Did not find any Cake files
[info]: OmniSharp.MSBuild.ProjectSystem
Detecting projects in 'c:\Users\nicep\Documents\Game Projects\Legend-Maker\Legend Maker\Legend Maker.sln'.
[info]: OmniSharp.MSBuild.ProjectManager
Queue project update for 'c:\Users\nicep\Documents\Game Projects\Legend-Maker\Legend Maker\Assembly-CSharp.csproj'
[info]: OmniSharp.Script.ScriptProjectSystem
Detecting CSX files in 'c:\Users\nicep\Documents\Game Projects\Legend-Maker\Legend Maker'.
[info]: OmniSharp.Script.ScriptProjectSystem
Did not find any CSX files
[info]: OmniSharp.WorkspaceInitializer
Configuration finished.
[info]: OmniSharp.Stdio.Host
Omnisharp server running using Stdio at location 'c:\Users\nicep\Documents\Game Projects\Legend-Maker\Legend Maker' on host 15756.
[info]: OmniSharp.MSBuild.ProjectManager
Loading project: c:\Users\nicep\Documents\Game Projects\Legend-Maker\Legend Maker\Assembly-CSharp.csproj
[info]: OmniSharp.MSBuild.ProjectManager
Successfully loaded project file 'c:\Users\nicep\Documents\Game Projects\Legend-Maker\Legend Maker\Assembly-CSharp.csproj'.
[info]: OmniSharp.MSBuild.ProjectManager
Adding project 'c:\Users\nicep\Documents\Game Projects\Legend-Maker\Legend Maker\Assembly-CSharp.csproj'
[info]: OmniSharp.MSBuild.ProjectManager
Update project: Assembly-CSharp
Received response for /quickinfo but could not find request.
Received response for /v2/getcodeactions but could not find request.
Received response for /v2/blockstructure but could not find request.
Received response for /v2/getcodeactions but could not find request.
Unhandled Exception: System.NullReferenceException: Object reference not set to an instance of an object.
at OmniSharp.Helpers.DiagnosticExtensions.<>c.<DistinctDiagnosticLocationsByProject>b__2_0(DocumentDiagnostics x) in D:\a\1\s\src\OmniSharp.Roslyn.CSharp\Helpers\DiagnosticExtensions.cs:line 38
at System.Linq.Enumerable.<SelectManyIterator>d__23`3.MoveNext()
at System.Linq.Enumerable.WhereSelectEnumerableIterator`2.MoveNext()
at System.Linq.Lookup`2.Create[TSource](IEnumerable`1 source, Func`2 keySelector, Func`2 elementSelector, IEqualityComparer`1 comparer)
at System.Linq.GroupedEnumerable`3.GetEnumerator()
at System.Linq.Enumerable.WhereSelectEnumerableIterator`2.MoveNext()
at System.Linq.Enumerable.WhereEnumerableIterator`1.MoveNext()
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.SerializeList(JsonWriter writer, IEnumerable values, JsonArrayContract contract, JsonProperty member, JsonContainerContract collectionContract, JsonProperty containerProperty)
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.SerializeObject(JsonWriter writer, Object value, JsonObjectContract contract, JsonProperty member, JsonContainerContract collectionContract, JsonProperty containerProperty)
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.SerializeObject(JsonWriter writer, Object value, JsonObjectContract contract, JsonProperty member, JsonContainerContract collectionContract, JsonProperty containerProperty)
at Newtonsoft.Json.Serialization.JsonSerializerInternalWriter.Serialize(JsonWriter jsonWriter, Object value, Type objectType)
at Newtonsoft.Json.JsonSerializer.SerializeInternal(JsonWriter jsonWriter, Object value, Type objectType)
at Newtonsoft.Json.JsonConvert.SerializeObjectInternal(Object value, Type type, JsonSerializer jsonSerializer)
at OmniSharp.Protocol.Packet.ToString() in D:\a\1\s\src\OmniSharp.Host\Protocol\Packet.cs:line 22
at System.IO.TextWriter.WriteLine(Object value)
at System.IO.TextWriter.SyncTextWriter.WriteLine(Object value)
at OmniSharp.Services.SharedTextWriter.ProcessWriteQueue() in D:\a\1\s\src\OmniSharp.Host\Services\SharedTextWriter.cs:line 48
at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
at System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
at System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state)
at System.Threading.ThreadHelper.ThreadStart()


---

<!-- source=github_issue; title=[Bug] FirebaseRemoteConfigurations crash; url=https://github.com/firebase/quickstart-unity/issues/1082 -->

# [Bug] FirebaseRemoteConfigurations crash

- Source: github_issue
- URL: https://github.com/firebase/quickstart-unity/issues/1082

<!-- DO NOT DELETE
validate_template=true
template_path=.github/ISSUE_TEMPLATE/issue.md
-->
### [REQUIRED] Please fill in the following fields:
* Unity editor version: 2020.3.4
* Firebase Unity SDK version: 7.0
* Source you installed the SDK: .unitypackage
* Problematic Firebase Component: Remote Configurations (Auth, Database, etc.)
* Other Firebase Components in use: Analytics, Crashandler (Auth, Database, etc.)
* Additional SDKs you are using: Facebook, AdMob, Avpro, etc
* Platform you are using the Unity editor on: Windows
* Platform you are targeting: iOS/Android
* Scripting Runtime: IL2CPP
### [REQUIRED] Please describe the issue here:
I have updated my app. and now getting some crashes connected with Remote config.
here is the stack trace.
Is it something that I did wrong?
Non-fatal Exception: java.lang.Exception: NullReferenceException : Object reference not set to an instance of an object.
at FirebaseRemoteConfigurations+d__11.MoveNext(FirebaseRemoteConfigurations+d__11)
at System.Threading.ContextCallback.Invoke(System.Threading.ContextCallback)
at System.Threading.ExecutionContext.RunInternal(System.Threading.ExecutionContext)
at System.Runtime.CompilerServices.AsyncMethodBuilderCore+MoveNextRunner.Run(System.Runtime.CompilerServices.AsyncMethodBuilderCore+MoveNextRunner)
at System.Action.Invoke(System.Action)
at System.Threading.ThreadPoolWorkQueue.Dispatch(System.Threading.ThreadPoolWorkQueue)
at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw(System.Runtime.ExceptionServices.ExceptionDispatchInfo)
at System.Threading.WaitCallback.Invoke(System.Threading.WaitCallback)
at System.Threading.ContextCallback.Invoke(System.Threading.ContextCallback)
at System.Threading.ExecutionContext.RunInternal(System.Threading.ExecutionContext)
at System.Threading.ThreadPoolWorkQueue.Dispatch(System.Threading.ThreadPoolWorkQueue)
#### Steps to reproduce:
Have no idea how to reproduce. I have published app for 10% of my user, got crashes from them. Never got problem on local test.
#### Relevant Code:


---

<!-- source=github_issue; title=How to visualize data from rviz to Unity?; url=https://github.com/siemens/ros-sharp/issues/79 -->

# How to visualize data from rviz to Unity?

- Source: github_issue
- URL: https://github.com/siemens/ros-sharp/issues/79

Issue Template © Siemens AG, 2017-2018
Author: Dr. Martin Bischoff (martin.bischoff@siemens.com)
-->
* [ ] I am at the right place and my issue is directly related to ROS#. General technical questions I would post e.g. at [ROS Answers](https://answers.ros.org/) or [Stackoverflow](https://stackoverflow.com). For library-specific questions I would look for help in the corresponding library forums.
* [ ] I have throughly read [the Contributing Guideline](Contributing.md) and writing this issue is the right thing to do in my case.
---
## I have a question! ##
* [ ] I searched the [Wiki](https://github.com/siemens/ros-sharp/wiki), [open](https://github.com/siemens/ros-sharp/issues) and [closed](https://github.com/siemens/ros-sharp/issues?q=is%3Aissue+is%3Aclosed) issues for an answer. I tried my best in finding the answer by myself without success. I believe that the discussion we will have in this issue, and the solutions we might find, will help me, and likely other community members who have a similar problem.
**Here is my question:**
Hi all,
I am completely new to Ros and Unity and was searching for a way to visualize rviz sensor data like laser scan or mapping data in Unity to deploy to the Hololens. Fortunately I found ROS# which makes that possible. I would like to ask which are the approaches to visualize data from rviz especially the laser scan data. I would subscribe to the topic /base_scan but obviously I have to find a way to convert the data from that topic to a format to appropriately visualize in Unity (so that the Unity scene looks like Rviz). I saw the video 'ROS#: Robot Teleoperation via Unity ' - (https://www.youtube.com/watch?v=OytzagQirrk) from you and would like to achieve something similar. Is there any code available because in the wiki there is no part explaining that demo. I hope for your reply and many thanks in advance!
Best regards


---

<!-- source=github_issue; title=Stopped polling job due to exception: System.MissingMethodException: UnityEditor.VersionControl.Task; url=https://github.com/googlesamples/unity-jar-resolver/issues/262 -->

# Stopped polling job due to exception: System.MissingMethodException: UnityEditor.VersionControl.Task

- Source: github_issue
- URL: https://github.com/googlesamples/unity-jar-resolver/issues/262

I updated Play Services Resolver to v1.2.123 and am getting this error on every auto-resolve.
Using Unity 2019.1.11f1
> `Stopped polling job due to exception: System.MissingMethodException: UnityEditor.VersionControl.Task UnityEditor.VersionControl.Provider.Checkout(string,UnityEditor.VersionControl.CheckoutMode)
> at Google.ProjectSettings.Set[T] (System.String name, T value) [0x00024] in /Users/smiles/dev/src/unity-jar-resolver/source/VersionHandlerImpl/src/ProjectSettings.cs:119
> at Google.ProjectSettings+<SetBool>c__AnonStorey2.<>m__5 () [0x00000] in /Users/smiles/dev/src/unity-jar-resolver/source/VersionHandlerImpl/src/ProjectSettings.cs:154
> at Google.ProjectSettings.SavePreferences (Google.ProjectSettings+SettingsSave saveLevel, System.Action saveToProject, System.Action saveToEditor) [0x00035] in /Users/smiles/dev/src/unity-jar-resolver/source/VersionHandlerImpl/src/ProjectSettings.cs:135
> at Google.ProjectSettings.SetBool (System.String name, System.Boolean value) [0x00014] in /Users/smiles/dev/src/unity-jar-resolver/source/VersionHandlerImpl/src/ProjectSettings.cs:153
> at GooglePlayServices.SettingsDialog.set_UseJetifier (System.Boolean value) [0x00000] in /Users/smiles/dev/src/unity-jar-resolver/source/PlayServicesResolver/src/SettingsDialog.cs:225
> at GooglePlayServices.PlayServicesResolver.CanEnableJetifierOrPromptUser (System.String titlePrefix) [0x00179] in /Users/smiles/dev/src/unity-jar-resolver/source/PlayServicesResolver/src/PlayServicesResolver.cs:2270
> at GooglePlayServices.PlayServicesResolver.ResolveUnsafe (System.Action`1[T] resolutionComplete, System.Boolean forceResolution, System.Boolean isAutoResolveJob, System.Boolean closeWindowOnCompletion) [0x00012] in /Users/smiles/dev/src/unity-jar-resolver/source/PlayServicesResolver/src/PlayServicesResolver.cs:1610
> at GooglePlayServices.PlayServicesResolver+<ScheduleResolve>c__AnonStorey1E.<>m__40 () [0x00000] in /Users/smiles/dev/src/unity-jar-resolver/source/PlayServicesResolver/src/PlayServicesResolver.cs:1579
> at GooglePlayServices.PlayServicesResolver.ExecuteNextResolveJob () [0x00069] in /Users/smiles/dev/src/unity-jar-resolver/source/PlayServicesResolver/src/PlayServicesResolver.cs:1438
> at GooglePlayServices.PlayServicesResolver.ScheduleResolve (System.Boolean forceResolution, System.Boolean closeWindowOnCompletion, System.Action`1[T] resolutionCompleteWithResult, System.Boolean isAutoResolveJob) [0x000a7] in /Users/smiles/dev/src/unity-jar-resolver/source/PlayServicesResolver/src/PlayServicesResolver.cs:1592
> at GooglePlayServices.PlayServicesResolver.AutoResolve (System.Action resolutionComplete) [0x00017] in /Users/smiles/dev/src/unity-jar-resolver/source/PlayServicesResolver/src/PlayServicesResolver.cs:1113
> at GooglePlayServices.PlayServicesResolver.<ScheduleAutoResolve>m__48 () [0x00016] in /Users/smiles/dev/src/unity-jar-resolver/source/PlayServicesResolver/src/PlayServicesResolver.cs:1092
> at Google.RunOnMainThread.ExecutePollingJobs () [0x0004a] in /Users/smiles/dev/src/unity-jar-resolver/source/VersionHandlerImpl/src/RunOnMainThread.cs:300
> UnityEngine.Debug:LogError(Object)
> Google.RunOnMainThread:ExecutePollingJobs() (at /Users/smiles/dev/src/unity-jar-resolver/source/VersionHandlerImpl/src/RunOnMainThread.cs:303)
> Google.RunOnMainThread:<ExecuteAll>m__17() (at /Users/smiles/dev/src/unity-jar-resolver/source/VersionHandlerImpl/src/RunOnMainThread.cs:414)
> Google.RunOnMainThread:RunAction(Action) (at /Users/smiles/dev/src/unity-jar-resolver/source/VersionHandlerImpl/src/RunOnMainThread.cs:234)
> Google.RunOnMainThread:ExecuteAll() (at /Users/smiles/dev/src/unity-jar-resolver/source/VersionHandlerImpl/src/RunOnMainThread.cs:406)
> UnityEditor.EditorApplication:Internal_CallUpdateFunctions()`
