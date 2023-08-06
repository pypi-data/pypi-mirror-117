# easysteam
Currently in development stages, this tool can get Steam marketplace games, software, soundtracks, etc. relatively quickly.


## Usage
Currently the tool only has two functions; Pull, Pull_All.

First create an instance of the class:
```
store = Market()
```

Then you either pull using the steam category link:
```
store.Pull('https://store.steampowered.com/genre/Free%20to%20Play/', 'NewReleasesRows')
```

Or using a name for the category:
```
store.Pull('Free to Play, 'NewReleasesRows')
```

The second input as you can see has 'NewReleasesRows' as the row input. You can set it to either ``NewReleasesRows`` or ``TopSellersRows`` to choose between:
- New and Trending (for the category)
- Top Selling (for the category)
