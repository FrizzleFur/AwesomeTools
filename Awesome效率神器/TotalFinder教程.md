## TotalFinder教程


You must boot into the Recovery OS. You do this by restarting your machine, and holding Command+R until the Apple logo appears. Then select Terminal from the Utilities menu. It looks like this:

In the window that opens, type csrutil disable and press return. This turns off System Integrity Protection so that TotalFinder can be installed.

Reboot your machine and you may install and run the latest version of TotalFinder.

* **Unfortunately you have to keep SIP disabled to allow TotalFinder**. In earlier macOS versions it was possible to turn SIP off only to complete TotalFinder installation steps and enable it back again. **That is no longer possible with macOS 10.14 (Mojave) due to hardened macOS security settings**.

* (System Integrity Protection ），它禁止让软件以 root 身份来在 Mac 上运行，在
* 为了可以在Mojave使用TotalFinder，只能关闭macOS security settings

To remove TotalFinder from your system, run the uninstaller found on the latest dmg download of TotalFinder.



## TotalFinder does not launch

A WORKAROUND is to restart appleventsd process.

In Terminal.app execute this command (it will ask for your password, that is ok):

 sudo killall -KILL appleeventsd
Note: Terminal.app can be launched from /Applications/Utilities/Terminal.app


## 参考

1. [System Integrity Protection under macOS 10.14 (Mojave)](https://totalfinder.binaryage.com/sip)
2. [TotalFinder does not launch](https://discuss.binaryage.com/t/totalfinder-does-not-launch/3744)