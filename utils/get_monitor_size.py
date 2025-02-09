from screeninfo import Monitor, get_monitors


class ScreenWidthHeight:
	monitor: Monitor = get_monitors()[0]
	height: int = monitor.height
	width: int = monitor.width
