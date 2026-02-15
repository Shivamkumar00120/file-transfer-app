import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class MyApp(Gtk.Window):

    def __init__(self):
        super().__init__(title="File Transfer") 
        self.set_default_size(900, 550)
        self.set_border_width(10)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(main_box)

        
        top_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        btn_send = Gtk.Button(label="Send")
        btn_receive = Gtk.Button(label="Receive")

        btn_send.get_style_context().add_class("top-btn")
        btn_receive.get_style_context().add_class("top-btn")

        
        left_spacer = Gtk.Label()
        right_spacer = Gtk.Label()

        left_spacer.set_hexpand(True)
        right_spacer.set_hexpand(True)

        top_bar.pack_start(left_spacer, True, True, 0)
        top_bar.pack_start(btn_send, False, False, 0)
        top_bar.pack_start(btn_receive, False, False, 0)
        top_bar.pack_start(right_spacer, True, True, 0)

        main_box.pack_start(top_bar, False, False, 0)

        
        center = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)

        center.set_halign(Gtk.Align.CENTER)
        center.set_valign(Gtk.Align.CENTER)

        
        icon = Gtk.Image.new_from_icon_name(
            "go-down",
            Gtk.IconSize.DIALOG
        )

        
        title = Gtk.Label(label="Receive files")
        title.get_style_context().add_class("title")

        
        subtitle = Gtk.Label(
            label="Enter the transmit code from the sender"
        )
        subtitle.get_style_context().add_class("subtitle")

        
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Transmit Code")
        self.entry.set_width_chars(25)
        self.entry.get_style_context().add_class("entry")

        
        receive_btn = Gtk.Button(label="Receive File")
        receive_btn.get_style_context().add_class("main-btn")
        receive_btn.connect("clicked", self.on_receive)

        
        center.pack_start(icon, False, False, 0)
        center.pack_start(title, False, False, 0)
        center.pack_start(subtitle, False, False, 0)
        center.pack_start(self.entry, False, False, 0)
        center.pack_start(receive_btn, False, False, 0)

        main_box.pack_start(center, True, True, 0)

        
        self.load_css()

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    
    
    def load_css(self):

        css= b"""
        window {
        background-color: @window_bg_color;
        color: @window_fg_color;
    }

    .top-btn {
        background-color: @accent_bg_color;
        color: @accent_fg_color;
        padding: 6px 15px;
        border-radius: 8px;
        font-weight: bold;
    }

    .top-btn:hover {
        background-color: shade(@accent_bg_color, 0.9);
    }

    .title {
        font-size: 26px;
        font-weight: bold;
        color: @window_fg_color;
    }

    .subtitle {
        font-size: 14px;
        color: @window_fg_color;
    }

    .entry {
        background-color: @view_bg_color;
        color: @view_fg_color;
        border-radius: 8px;
        padding: 8px;
    }

    .main-btn {
        background-color: @accent_color;
        color: @accent_fg_color;
        padding: 10px 25px;
        border-radius: 20px;
        font-weight: bold;
    }

    .main-btn:hover {
        background-color: shade(@accent_color, 0.85);
    }
    """

        provider = Gtk.CssProvider()
        provider.load_from_data(css)

        Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    
    def on_receive(self, button):

        code = self.entry.get_text()

        if code == "":
            print("Enter code first!")
        else:
            print("Receiving file with code:", code)


app = MyApp()
Gtk.main()


