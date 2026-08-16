from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = ""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("💻 Coding", callback_data="coding"),
            InlineKeyboardButton("📚 Notes", callback_data="notes"),
        ],
        [
            InlineKeyboardButton("🐍 Python", callback_data="python"),
            InlineKeyboardButton("🆘 Help", callback_data="help"),
        ],
    ]

    await update.message.reply_text(
        "👋 Hello Piyush!\n\n"
        "🤖 Welcome to Code With Danger Bot!\n"
        "🚀 Choose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "coding":
        keyboard = [
            [
                InlineKeyboardButton("🌐 HTML", callback_data="html"),
                InlineKeyboardButton("🎨 CSS", callback_data="css"),
            ],
            [
                InlineKeyboardButton("⚡ JavaScript", callback_data="javascript"),
                InlineKeyboardButton("🔵 C", callback_data="c"),
            ],
            [
                InlineKeyboardButton("🟣 C++", callback_data="cpp"),
            ],
            [
                InlineKeyboardButton("🔙 Back", callback_data="back"),
            ],
        ]

        await query.edit_message_text(
            "💻 Coding Menu\n\nChoose a language:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "dsa":
        await query.message.reply_video(
            video=open("hero.mp4", "rb"),
            caption="📊 DSA Video\n\n🎓 Data Structures & Algorithms"
        )

    elif query.data == "dbms":
        await query.edit_message_text(
            "🗄️ DBMS Notes\n\n"
            "• Keys\n"
            "• ER Model\n"
            "• SQL\n"
            "• Normalization\n"
            "• Transactions\n"
            "• Joins"
        )

    elif query.data == "os":
        await query.edit_message_text(
            "💻 Operating System Notes\n\n"
            "• Process\n"
            "• CPU Scheduling\n"
            "• Deadlock\n"
            "• Memory Management\n"
            "• Paging\n"
            "• Virtual Memory"
        )

    elif query.data == "cg":
        await query.edit_message_text(
            "🎨 Computer Graphics Notes\n\n"
            "• DDA Algorithm\n"
            "• Bresenham Algorithm\n"
            "• 2D Transformations\n"
            "• Clipping\n"
            "• Bezier Curve\n"
            "• B-Spline Curve"
        )

    elif query.data == "html":
        await query.edit_message_text(
            "🌐 HTML\n\n"
            "HTML is used to create the structure of a webpage.\n\n"
            "Example:\n"
            "<html>\n"
            "  <h1>Hello World</h1>\n"
            "</html>"
        )

    elif query.data == "css":
        await query.edit_message_text(
            "🎨 CSS\n\n"
            "CSS is used to style webpages.\n\n"
            "Example:\n"
            "body {\n"
            "  background: black;\n"
            "  color: white;\n"
            "}"
        )

    elif query.data == "javascript":
        await query.edit_message_text(
            "⚡ JavaScript\n\n"
            "JavaScript adds interaction to webpages.\n\n"
            "Example:\n"
            "alert('Hello World!');"
        )

    elif query.data == "c":
        await query.edit_message_text(
            "🔵 C Language\n\n"
            "Simple C program:\n\n"
            "#include <stdio.h>\n\n"
            "int main() {\n"
            "    printf(\"Hello World\");\n"
            "    return 0;\n"
            "}"
        )

    elif query.data == "cpp":
        await query.edit_message_text(
            "🟣 C++\n\n"
            "Simple C++ program:\n\n"
            "#include <iostream>\n"
            "using namespace std;\n\n"
            "int main() {\n"
            "    cout << \"Hello World\";\n"
            "    return 0;\n"
            "}"
        )
    elif query.data == "notes":
        keyboard = [
            [
                InlineKeyboardButton("📊 DSA", callback_data="dsa"),
                InlineKeyboardButton("🗄️ DBMS", callback_data="dbms"),
            ],
            [
                InlineKeyboardButton("💻 OS", callback_data="os"),
                InlineKeyboardButton("🎨 Computer Graphics", callback_data="cg"),
            ],
            [
                InlineKeyboardButton("🔙 Back", callback_data="back"),
            ],
        ]

        await query.edit_message_text(
            "📚 Notes Menu\n\nChoose a subject:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "python":
        await query.edit_message_text(
            "🐍 Python\n\n"
            "Python programs and projects coming soon! 🚀"
        )

    elif query.data == "help":
        await query.edit_message_text(
            "🆘 Help\n\n"
            "/start - Open main menu\n"
            "/help - Show help"
        )

    elif query.data == "back":
        keyboard = [
            [
                InlineKeyboardButton("💻 Coding", callback_data="coding"),
                InlineKeyboardButton("📚 Notes", callback_data="notes"),
            ],
            [
                InlineKeyboardButton("🐍 Python", callback_data="python"),
                InlineKeyboardButton("🆘 Help", callback_data="help"),
            ],
        ]

        await query.edit_message_text(
            "🏠 Main Menu",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()