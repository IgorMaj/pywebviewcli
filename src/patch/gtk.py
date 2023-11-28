# Patches webview inspector in such a way so that web inspector doesn't show on load (GTK Webkit)
# User can still open it from the context menu when they actually need it
def patch_gtk_inspector():
    try:
        from webview.platforms.gtk import webkit

        class MockedInspector:
            def show(self):
                pass

        webkit.WebView.get_inspector = lambda self: MockedInspector()
    except:
        pass
