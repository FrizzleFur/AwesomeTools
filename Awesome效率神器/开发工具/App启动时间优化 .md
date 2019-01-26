
[一次立竿见影的启动时间优化 - 简书](https://www.jianshu.com/p/c1734cbdf39b)

之前公司的 UI 设计师和我们提过好几次启动时间的事情，当时在开发业务，所以没有时间去做这件事。最近发完版本，终于有时间搞一搞启动时间了。

一般而言，启动时间是指从用户点击 APP 那一刻开始到用户看到第一个界面这中间的时间。我们进行优化的时候，我们将启动时间分为 `pre-main` 时间和 `main` 函数到第一个界面渲染完成时间这两个部分。

为什么这么划分呢？大家都知道 APP 的入口是 `main` 函数，在 `main` 之前，我们自己的代码是不会执行的。而进入到 `main` 函数以后，我们的代码都是从

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions;

```

开始执行的，所以很明显，优化这两部分的思路是不一样的。

为了方便起见，我们将 `pre-main` 时间成为 `t1` 时间，而将`main` 函数到第一个界面渲染完成这段时间称为 `t2` 时间。

## 01.磨刀不误砍柴工

我们先来看第一部分，也就是从 `main` 函数到第一个界面渲染完成这段时间。在开始之前，我们先来磨练一个我们自己的工具。

生活中，我们计量一段时间一般是用计时器。这里我们要想知道哪些操作，或者说哪些代码是耗时的，我们也需要一个打点计时器。用过 `profile` 的朋友都知道这个工具很强大，可以使用它来分析出哪些代码是耗时的。但是它不够灵活，我们来看一下我们的这个计时器应该怎么设计。

![](https://i.imgur.com/1aSqFq8.jpg)

如上图所示，在时间轴上，我们从 start 开始打点计时，然后我们在第一个小红旗那里打了一个点，记录这段代码的耗时，然后又在第二个小红旗那里打了一个点，记录这中间代码的耗时。然后在结束的地方打一个点，然后把所有打点的结果展示出来。同时，我们为每段计时加上标注，用来区分这段时间是执行了什么操作花费的时间。这样一来，我们就能快速精准的知道究竟是谁拖慢了启动。

## 02.定位元凶

下面这张截图是贝聊老师端没有开始优化的耗时，因为涉及到公司具体的业务，所以我将部分信息加了遮挡。借助于我们的工具，我们可以定位任何一行代码的耗时。

我们看 `t2` 耗时那里，总共花费了 `6.361` 秒，这是从 `didFinishLaunchingWithOptions` 到第一个界面渲染出来花费的时间。从这个结果来看，我们的启动时间的优化已经到了刻不容缓的地步了。

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/122741.jpg)

再仔细分析一下上面的结果， `t2` 时间也分为了两个部分，`didFinishLaunchingWithOptions` 花了 `4.010`秒，第一个页面渲染耗时花了 `2.531` 秒。好，看样子大魔头住在 `didFinishLaunchingWithOptions` 这个方法里，另外，第一页面的渲染中也有不少问题。下面我们分别展开。

#### 02.1.`didFinishLaunchingWithOptions`

上面说到大魔头住在 `didFinishLaunchingWithOptions`，现在我们仔细看一下 `didFinishLaunchingWithOptions` 方法里的代码耗时，有两行代码的耗时居然为一秒以上，而且耗时最多的居然有 `1.620` 秒之多。

![](https://i.imgur.com/8L5KZpb.jpg)

其实 `didFinishLaunchingWithOptions` 方法里我们一般都有以下的逻辑：

> *   初始化第三方 SDK
> *   配置 APP 运行需要的环境
> *   自己的一些工具类的初始化
> *   ...

#### 02.2.第一个页面渲染

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/122815.jpg)

如果我们的 UI 架构是上面这样的话。然后我们在 AppDelegate 里写下这么一段代码：

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSLog(@"didFinishLaunchingWithOptions 开始执行");

    self.window = [[UIWindow alloc] initWithFrame:[UIScreen mainScreen].bounds];
    BLTabBarController *tabBarVc = [BLTabBarController new];
    self.window.rootViewController = tabBarVc;
    [self.window makeKeyAndVisible];

    NSLog(@"didFinishLaunchingWithOptions 跑完了");

    return YES;
}

```

然后我们来到 `BLTabBarController` 里的 `viewDidLoad` 方法里进行它的 `viewControllers` 的设置，然后再进入到每个 `viewController` 的 `viewDidLoad` 方法里进行更多的初始化操作。那么你觉得从 `didFinishLaunchingWithOptions` 到最后显示展示的 `viewController` 的 `viewDidLoad` 这些方法的执行顺序是怎么样的呢？

下面是我写的一个 demo，用来展示加载的顺序：

```
2017-08-15 10:46:57.860 Demo[1404:325698] didFinishLaunchingWithOptions 开始执行
2017-08-15 10:46:57.862 Demo[1404:325698] 开始加载 BLTabBarController 的 viewDidLoad
2017-08-15 10:46:57.874 Demo[1404:325698] didFinishLaunchingWithOptions 跑完了
2017-08-15 10:46:57.876 Demo[1404:325698] 开始加载 BLViewController 的 viewDidLoad, 然后执行一堆初始化的操作

```

上面的情况是能保证我们不在 `BLTabBarController` 中操作 `BLViewController` 的 `view`，如果我们在`BLTabBarController` 中操作了 `BLViewController` 的 `view` 的话，那么调用顺序将会是这样：

```
2017-08-15 11:09:03.661 Demo[1458:349413] didFinishLaunchingWithOptions 开始执行
2017-08-15 11:09:03.663 Demo[1458:349413] 开始加载 BLTabBarController 的 viewDidLoad
2017-08-15 11:09:03.664 Demo[1458:349413] 开始加载 BLViewController 的 viewDidLoad, 然后执行一堆初始化的操作
2017-08-15 11:09:03.676 Demo[1458:349413] didFinishLaunchingWithOptions 跑完了

```

这是很可怕的一件事情，为什么呢？因为一般我们都把界面的初始化、网络请求、数据解析、视图渲染等操作放在了 `viewDidLoad` 方法里，这样一来每次启动 APP 的时候，在用户看到第一个页面之前，我们要把这些事件全部都处理完，才会进入到视图渲染阶段。

## 03.解决策略

上面分析了拖慢 `t2` 的两个因素，它们是 `didFinishLaunchingWithOptions`里面的初始化以及第一个页面渲染耗时。对于这两个不同的方面，我们的优化思路也是不一样的。

#### 03.1.`didFinishLaunchingWithOptions`

对于 `didFinishLaunchingWithOptions`，这里面的初始化是必须执行的，但是我们可以适当的根据功能的不同对应的适当延迟启动的时机。对于我们项目，我将初始化分为三个类型：

> *   日志、统计等必须在 APP 一起动就最先配置的事件
> *   项目配置、环境配置、用户信息的初始化 、推送、IM等事件
> *   其他 SDK 和配置事件

对于第一类，由于这类事件的特殊性，所以必须第一时间启动，仍然把它留在 `didFinishLaunchingWithOptions` 里启动。第二类事件，这些功能在用户进入 APP 主体的之前是必须要加载完的，所以我们可以把它放在第二批，也就是用户已经看到广告页面，再进行广告倒计时的时候再启动。第三类事件，由于不是必须的，所以我们可以放在第一个界面渲染完成以后的 `viewDidAppear` 方法里，这里完全不会影响到启动时间。

就这样，进行过这一轮优化以后，我们的 `t2` 事件就从 `6 秒多` 降到 `2 秒多`。

#### 03.2.第一个页面渲染

我们的思路是这样的，用户点击 APP，我先尽快把广告页面加载出来。这样，用户就不会觉得启动慢了，同时我们可以在广告读秒的过程中进行第二批启动事件的加载，这个加载用户也感觉不到。但还没完，等会广告展示完，切到主 APP 的时候，如果一系列 `viewDidLoad` 里方法里有很多耗时的操作，那用户还是会感觉到卡顿。

所以对于第一个页面渲染的优化思路就是，先立马展示一个空壳的 UI 给用户，然后在 `viewDidAppear` 方法里进行数据加载解析渲染等一系列操作，这样一来，用户已经看到界面了，就不会觉得是启动慢，这个时候的等待就变成等待数据请求了，这样就把这部分时间转嫁出去了。

经过这两轮优化，我们的 `t2` 时间就从 `6 秒多` 变成了 `0.1 秒不到`，也即是总共砍掉了 `6 秒多` 的启动时间。

#### 03.3.总结

为此，我专门建了一个类来负责启动事件，为什么呢？如果不这么做，那么此次优化以后，以后再引入第三方的时候，别的同事可能很直觉的就把第三方的初始化放到了 `didFinishLaunchingWithOptions` 方法里，这样久而久之， `didFinishLaunchingWithOptions` 又变得不堪重负，到时候又要专门花时间来做重复的优化。

下面是这个类的头文件：

```
/**
 * 注意: 这个类负责所有的 didFinishLaunchingWithOptions 延迟事件的加载.
 * 以后引入第三方需要在 didFinishLaunchingWithOptions 里初始化或者我们自己的类需要在 didFinishLaunchingWithOptions 初始化的时候,
 * 要考虑尽量少的启动时间带来好的用户体验, 所以应该根据需要减少 didFinishLaunchingWithOptions 里耗时的操作.
 * 第一类: 比如日志 / 统计等需要第一时间启动的, 仍然放在 didFinishLaunchingWithOptions 中.
 * 第二类: 比如用户数据需要在广告显示完成以后使用, 所以需要伴随广告页启动, 只需要将启动代码放到 startupEventsOnADTimeWithAppDelegate 方法里.
 * 第三类: 比如直播和分享等业务, 肯定是用户能看到真正的主界面以后才需要启动, 所以推迟到主界面加载完成以后启动, 只需要将代码放到 startupEventsOnDidAppearAppContent 方法里.
 */

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface BLDelayStartupTool : NSObject

/**
 * 启动伴随 didFinishLaunchingWithOptions 启动的事件.
 * 启动类型为:日志 / 统计等需要第一时间启动的.
 */
+ (void)startupEventsOnAppDidFinishLaunchingWithOptions;

/**
 * 启动可以在展示广告的时候初始化的事件.
 * 启动类型为: 用户数据需要在广告显示完成以后使用, 所以需要伴随广告页启动.
 */
+ (void)startupEventsOnADTime;

/**
 * 启动在第一个界面显示完(用户已经进入主界面)以后可以加载的事件.
 * 启动类型为: 比如直播和分享等业务, 肯定是用户能看到真正的主界面以后才需要启动, 所以推迟到主界面加载完成以后启动.
 */
+ (void)startupEventsOnDidAppearAppContent;

@end

NS_ASSUME_NONNULL_END

```

下面是 `.m` 文件，这里做了一层自动校验，如果 `30 秒` 以后，这些启动项有没有被启动的，就会在 `DEBUG` 环境下弹出警告信息。同时也会将那些没有启动的启动项进行启动。

```
#import "BLDelayStartupTool.h"

static BOOL _isCalledStartupEventsOnAppDidFinishLaunchingWithOptions = NO;
static BOOL _isCalledStartupEventsOnADTimeWithAppDelegate = NO;
static BOOL _isCalledStartupEventsOnDidAppearAppContent = NO;
const NSTimeInterval kBLDelayStartupEventsToolCheckCallTimeInterval = 30;
@implementation BLDelayStartupTool

+ (void)load {
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(kBLDelayStartupEventsToolCheckCallTimeInterval * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
        [self checkStartupEventsDidLaunched];
    });
}

+ (void)checkStartupEventsDidLaunched {
    NSString *alertString = @"";
    if (!_isCalledStartupEventsOnAppDidFinishLaunchingWithOptions) {
        alertString = [alertString stringByAppendingString:@"AppDidFinishLaunching, "];
        [self startupEventsOnAppDidFinishLaunchingWithOptions];
    }
    if (!_isCalledStartupEventsOnADTimeWithAppDelegate) {
        alertString = [alertString stringByAppendingString:@"ADTime, "];
        [self startupEventsOnADTime];
    }
    if (!_isCalledStartupEventsOnDidAppearAppContent) {
        alertString = [alertString stringByAppendingString:@"DidAppearAppContent"];
        [self startupEventsOnDidAppearAppContent];
    }

    if (alertString.length > 0) {

#if DEBUG
        alertString = [alertString stringByAppendingString:@" 等延迟启动项没有启动, 这会造成应用奔溃"];
        UIAlertView *alertView = [[UIAlertView alloc] initWithTitle:@"注意" message:alertString delegate:nil cancelButtonTitle:@"好的" otherButtonTitles:nil];
        [alertView show];
#endif
    }
}

+ (void)startupEventsOnAppDidFinishLaunchingWithOptions {
    _isCalledStartupEventsOnAppDidFinishLaunchingWithOptions = YES;
}

+ (void)startupEventsOnADTime {
    _isCalledStartupEventsOnADTimeWithAppDelegate = YES;
}

+ (void)startupEventsOnDidAppearAppContent {
    _isCalledStartupEventsOnDidAppearAppContent = YES;
}

@end

```

## 04\. `pre-main` 时间

上面已经将 `t2` 时间处理好了，接下来看看 `pre-main`。

苹果为查看 `pre-main` 提供了支持，具体配置如下，配置的 key 为：`DYLD_PRINT_STATISTICS`。

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/122854.jpg)

还需要勾选下面这个选项：

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/122841.jpg)

然后再运行项目，`Xcode` 就会在控制台输出这部分 `pre-main` 的耗时：

```
Total pre-main time: 2.2 seconds (100.0%)
 dylib loading time: 1.0 seconds (45.2%)
rebase/binding time: 100.05 milliseconds (4.3%)
    ObjC setup time: 207.21 milliseconds (9.0%)
   initializer time: 946.39 milliseconds (41.3%)
slowest intializers :
           libSystem.B.dylib :   8.54 milliseconds (0.3%)
 libBacktraceRecording.dylib :  46.30 milliseconds (2.0%)
        libglInterpose.dylib : 187.42 milliseconds (8.1%)
                     beiliao : 896.56 milliseconds (39.1%)

```

但是这部分不是那么好处理，因为这部分主要是由以下几个方面影响的：

> *   用到的系统的动态库的数量，比如 `UIKit.framework` 等
> *   cocoapods 里引用的第三方框架数量
> *   项目中类的数量
> *   `load` 方法中执行的代码
> *   组件化
> *   swift 混编

其他还有，请大神补充。上面几点中，我们能做的也就是把所有类的 `load` 方法扫一遍，不要在这里面执行耗时的操作。其他的不是短时间能改变的。

如果你想在这些方面有所突破的话，请看下面参考文章。

> 参考文章：
> [App Startup Time: Past, Present, and Future](https://developer.apple.com/videos/play/wwdc2017/413/)
> [iOS App 启动性能优化](https://mp.weixin.qq.com/s?__biz=MzA3NTYzODYzMg==&mid=2653579242&idx=1&sn=8f2313711f96a62e7a80d63851653639&chksm=84b3b5edb3c43cfb08e30f2affb1895e8bac8c5c433a50e74e18cda794dcc5bd53287ba69025&mpshare=1&scene=1&srcid=081075Vt9sYPaGgAWwb7xd1x&key=4b95006583a3cb388791057645bf19a825b73affa9d3c1303dbc0040c75548ef548be21acce6a577731a08112119a29dfa75505399bba67497ad729187c6a98469674924c7b447788c7370f6c2003fb4&ascene=0&uin=NDA2NTgwNjc1&devicetype=iMac16%2C2+OSX+OSX+10.12.6+build(16G29)&version=12020110&nettype=WIFI&fontScale=100&pass_ticket=IDZVtt6EyfPD9ZLcACRVJZYH8WaaMPtT%2BF3nfv7yZUQBCMKM4H1rDCbevGd7bXoG)
> [WWDC 之优化 App 启动速度](https://juejin.im/entry/57c3d611a633bd005d7b3b62)
> [iOS Dynamic Framework 对App启动时间影响实测](https://www.jianshu.com/p/3263009e9228)
> [优化 App 的启动时间](http://yulingtianxia.com/blog/2016/10/30/Optimizing-App-Startup-Time/)

## 05.最后

打点计时器的 GitHub 地址在这里 [BLStopwatch](https://github.com/beiliao-mobile/BLStopwatch)。

