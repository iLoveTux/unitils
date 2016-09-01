Rationale
*********

Abstract
========

This document outlines in detail why I believe this library is a worthwhile investment in time and resources.

Where the idea originated
-------------------------

There is a slight disconnect between DevOps engineers (particularly Operations personele, Administration personele and Security Analysists) caused by a difference in language, culture and tools. Over and over, people are being asked to transition to a DevOps work cycle but something as simple as learning the new tools and mindset can be overwhelming. Most non-development IT professionals are familiar with basic linux commands, so we decided to explore that.

A lot of the work being done in the DevOps space are written in Python, and because Python is a great language for automation, we decided that it would be almost a gift to allow people making the DevOps transition. Automation is nothing new and lots of people have experience making shell scripts or batch files to acomplish the same task. If these people were given a familiar toolset with which to work in Python their transition will be just that much easier.

At the same time, we realized that "shelling out" commands was a real option, but the overhead of spawing shells and the limitation of using OS-specific system calls makes this unusable for cross-platform automation. Instead what we needed was a native Python function to mirror how these commands work on the outside.

About the time we made this realization, a few of my co-workers along with myself found ourselves working in a Windows environment. We agonized about having our basic toolset taken away from us (Imagine a carpenter working in a shop that forbids hammers). We would have loved to just be able to tail a file and grep the logs (I know there are Windows ways of doing the above tasks, but I only make use of them every couple of years).

This is when our idea was made to not only make a library which provides functions mirroring Linux commands, but to also provide these functions with a Command Line Interface. The dual interfaces (programatic and command line) allow great flexibility.

The commands we are targeting
-----------------------------

Please see `this issue <https://github.com/iLoveTux/unitils/issues/5>`_ for the
current state of our progress.
