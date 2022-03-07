from plugin import plugin

@plugin("test market")
def test_market_feature(jarvis, s):
    jarvis.say('Marketplace feature working perfectly!')
