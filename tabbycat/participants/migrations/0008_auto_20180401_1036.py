# Generated by Django 2.0.3 on 2018-04-01 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0007_auto_20180318_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='emoji',
            field=models.CharField(blank=True, choices=[('☁️', '☁️'), ('❄️', '❄️'), ('♠️', '♠️'), ('♥️', '♥️'), ('♦️', '♦️'), ('♣️', '♣️'), ('✉️', '✉️'), ('✂️', '✂️'), ('☕', '☕'), ('⬛', '⬛'), ('⬜', '⬜'), ('⛑', '⛑'), ('⛰', '⛰'), ('⛪', '⛪'), ('⛺', '⛺'), ('⛵', '⛵'), ('⛔', '⛔'), ('⛅', '⛅'), ('⛈', '⛈'), ('⛱', '⛱'), ('⛄', '⛄'), ('⚽', '⚽'), ('⛸', '⛸'), ('⛏', '⛏'), ('😂', '😂'), ('😆', '😆'), ('😉', '😉'), ('😊', '😊'), ('😎', '😎'), ('😍', '😍'), ('😘', '😘'), ('😇', '😇'), ('😐', '😐'), ('😏', '😏'), ('😣', '😣'), ('😥', '😥'), ('😜', '😜'), ('😓', '😓'), ('😖', '😖'), ('😷', '😷'), ('😲', '😲'), ('😭', '😭'), ('😱', '😱'), ('😳', '😳'), ('😵', '😵'), ('😡', '😡'), ('👿', '👿'), ('👨', '👨'), ('👩', '👩'), ('👴', '👴'), ('👵', '👵'), ('👶', '👶'), ('👮', '👮'), ('👷', '👷'), ('👸', '👸'), ('💂', '💂'), ('🎅', '🎅'), ('👼', '👼'), ('👰', '👰'), ('🙅', '🙅'), ('🙆', '🙆'), ('💁', '💁'), ('🙋', '🙋'), ('🙇', '🙇'), ('🙌', '🙌'), ('🙏', '🙏'), ('💃', '💃'), ('👪', '👪'), ('👫', '👫'), ('👬', '👬'), ('👭', '👭'), ('💪', '💪'), ('👆', '👆'), ('✊', '✊'), ('✋', '✋'), ('👊', '👊'), ('👌', '👌'), ('👍', '👍'), ('👎', '👎'), ('👏', '👏'), ('💅', '💅'), ('👣', '👣'), ('👀', '👀'), ('👂', '👂'), ('👃', '👃'), ('👅', '👅'), ('👄', '👄'), ('💘', '💘'), ('💔', '💔'), ('💖', '💖'), ('💌', '💌'), ('💧', '💧'), ('💤', '💤'), ('💣', '💣'), ('💥', '💥'), ('💦', '💦'), ('💨', '💨'), ('💫', '💫'), ('👓', '👓'), ('👔', '👔'), ('👜', '👜'), ('👟', '👟'), ('👠', '👠'), ('👑', '👑'), ('👒', '👒'), ('🎩', '🎩'), ('💄', '💄'), ('💍', '💍'), ('💎', '💎'), ('👻', '👻'), ('💀', '💀'), ('👽', '👽'), ('👾', '👾'), ('💩', '💩'), ('🐵', '🐵'), ('🙈', '🙈'), ('🙉', '🙉'), ('🙊', '🙊'), ('🐶', '🐶'), ('🐺', '🐺'), ('🐯', '🐯'), ('🐴', '🐴'), ('🐮', '🐮'), ('🐑', '🐑'), ('🐭', '🐭'), ('🐹', '🐹'), ('🐰', '🐰'), ('🐻', '🐻'), ('🐨', '🐨'), ('🐼', '🐼'), ('🐔', '🐔'), ('🐣', '🐣'), ('🐤', '🐤'), ('🐦', '🐦'), ('🐧', '🐧'), ('🐸', '🐸'), ('🐢', '🐢'), ('🐍', '🐍'), ('🐲', '🐲'), ('🐳', '🐳'), ('🐬', '🐬'), ('🐠', '🐠'), ('🐙', '🐙'), ('🐚', '🐚'), ('🐌', '🐌'), ('🐛', '🐛'), ('🐝', '🐝'), ('💐', '💐'), ('🌸', '🌸'), ('🌹', '🌹'), ('🌻', '🌻'), ('🌷', '🌷'), ('🌱', '🌱'), ('🌴', '🌴'), ('🌵', '🌵'), ('🌿', '🌿'), ('🍀', '🍀'), ('🍁', '🍁'), ('🍇', '🍇'), ('🍉', '🍉'), ('🍋', '🍋'), ('🍌', '🍌'), ('🍍', '🍍'), ('🍎', '🍎'), ('🍑', '🍑'), ('🍒', '🍒'), ('🍓', '🍓'), ('🍆', '🍆'), ('🌽', '🌽'), ('🍄', '🍄'), ('🍞', '🍞'), ('🍔', '🍔'), ('🍟', '🍟'), ('🍕', '🍕'), ('🍙', '🍙'), ('🍩', '🍩'), ('🍪', '🍪'), ('🍰', '🍰'), ('🍭', '🍭'), ('🍼', '🍼'), ('🍷', '🍷'), ('🍹', '🍹'), ('🍺', '🍺'), ('🍴', '🍴'), ('🌋', '🌋'), ('🏠', '🏠'), ('🏢', '🏢'), ('🏥', '🏥'), ('🏰', '🏰'), ('🌊', '🌊'), ('🎡', '🎡'), ('🎢', '🎢'), ('🎪', '🎪'), ('🎨', '🎨'), ('🚃', '🚃'), ('🚄', '🚄'), ('🚝', '🚝'), ('🚍', '🚍'), ('🚔', '🚔'), ('🚘', '🚘'), ('🚲', '🚲'), ('🚨', '🚨'), ('🚣', '🚣'), ('🚁', '🚁'), ('🚀', '🚀'), ('🚦', '🚦'), ('🚧', '🚧'), ('🚫', '🚫'), ('🚷', '🚷'), ('🚻', '🚻'), ('🚽', '🚽'), ('🚿', '🚿'), ('🛀', '🛀'), ('⏳', '⏳'), ('⏰', '⏰'), ('🌑', '🌑'), ('🌕', '🌕'), ('🌗', '🌗'), ('🌞', '🌞'), ('🌈', '🌈'), ('🌟', '🌟'), ('🔥', '🔥'), ('🎃', '🎃'), ('🎄', '🎄'), ('🎈', '🎈'), ('🎉', '🎉'), ('🎓', '🎓'), ('🎯', '🎯'), ('🎀', '🎀'), ('🏀', '🏀'), ('🏈', '🏈'), ('🎾', '🎾'), ('🎱', '🎱'), ('🏊', '🏊'), ('🎮', '🎮'), ('🎲', '🎲'), ('📣', '📣'), ('📯', '📯'), ('🔔', '🔔'), ('🎶', '🎶'), ('🎤', '🎤'), ('🎹', '🎹'), ('🎺', '🎺'), ('🎻', '🎻'), ('📻', '📻'), ('📱', '📱'), ('📞', '📞'), ('🔋', '🔋'), ('🔌', '🔌'), ('💾', '💾'), ('💿', '💿'), ('🎬', '🎬'), ('📺', '📺'), ('📷', '📷'), ('🔍', '🔍'), ('🔭', '🔭'), ('💡', '💡'), ('📕', '📕'), ('📰', '📰'), ('💰', '💰'), ('💸', '💸'), ('📦', '📦'), ('📫', '📫'), ('💼', '💼'), ('📅', '📅'), ('📎', '📎'), ('📏', '📏'), ('📐', '📐'), ('🔒', '🔒'), ('🔑', '🔑'), ('🔧', '🔧'), ('🔩', '🔩'), ('💉', '💉'), ('💊', '💊'), ('🔪', '🔪'), ('🔫', '🔫'), ('🚬', '🚬'), ('🏁', '🏁'), ('🔮', '🔮'), ('❌', '❌'), ('❓', '❓'), ('🔞', '🔞'), ('🆒', '🆒'), ('🆗', '🆗'), ('🆘', '🆘'), ('😙', '😙'), ('😑', '😑'), ('😮', '😮'), ('😴', '😴'), ('😧', '😧'), ('😬', '😬'), ('🕵', '🕵'), ('🖕', '🖕'), ('🖖', '🖖'), ('👁', '👁'), ('🛍', '🛍'), ('🐿', '🐿'), ('🕊', '🕊'), ('🕷', '🕷'), ('🕸', '🕸'), ('🏵', '🏵'), ('🌶', '🌶'), ('🏕', '🏕'), ('🏛', '🏛'), ('🛢', '🛢'), ('🛥', '🛥'), ('🛩', '🛩'), ('🛎', '🛎'), ('🕰', '🕰'), ('🌡', '🌡'), ('🌩', '🌩'), ('🌪', '🌪'), ('🌬', '🌬'), ('🎖', '🎖'), ('🎗', '🎗'), ('🎞', '🎞'), ('🏷', '🏷'), ('🏋', '🏋'), ('🕹', '🕹'), ('🖥', '🖥'), ('🖨', '🖨'), ('🖲', '🖲'), ('📸', '📸'), ('🕯', '🕯'), ('🗞', '🗞'), ('🖋', '🖋'), ('🗑', '🗑'), ('🛠', '🛠'), ('🗡', '🗡'), ('🛡', '🛡'), ('🏳', '🏳'), ('🏴', '🏴'), ('🤗', '🤗'), ('🤔', '🤔'), ('🙄', '🙄'), ('🤐', '🤐'), ('🤓', '🤓'), ('🙃', '🙃'), ('🤒', '🤒'), ('🤕', '🤕'), ('🤑', '🤑'), ('🤘', '🤘'), ('📿', '📿'), ('🤖', '🤖'), ('🦁', '🦁'), ('🦄', '🦄'), ('🦀', '🦀'), ('🦂', '🦂'), ('🧀', '🧀'), ('🌭', '🌭'), ('🌮', '🌮'), ('🌯', '🌯'), ('🍿', '🍿'), ('🍾', '🍾'), ('🏏', '🏏'), ('🏐', '🏐'), ('🏓', '🏓'), ('🏹', '🏹'), ('🤣', '🤣'), ('🤤', '🤤'), ('🤢', '🤢'), ('🤧', '🤧'), ('🤠', '🤠'), ('🤡', '🤡'), ('🤥', '🤥'), ('🤴', '🤴'), ('🤵', '🤵'), ('🤰', '🤰'), ('🤶', '🤶'), ('🤦', '🤦'), ('🤷', '🤷'), ('🕺', '🕺'), ('🤺', '🤺'), ('🤸', '🤸'), ('🤼', '🤼'), ('🤹', '🤹'), ('🤳', '🤳'), ('🤞', '🤞'), ('🤙', '🤙'), ('🤝', '🤝'), ('🖤', '🖤'), ('🦊', '🦊'), ('🦇', '🦇'), ('🦅', '🦅'), ('🦆', '🦆'), ('🦉', '🦉'), ('🦎', '🦎'), ('🦈', '🦈'), ('🦐', '🦐'), ('🦑', '🦑'), ('🦋', '🦋'), ('🥝', '🥝'), ('🥑', '🥑'), ('🥔', '🥔'), ('🥕', '🥕'), ('🥒', '🥒'), ('🥜', '🥜'), ('🥐', '🥐'), ('🥖', '🥖'), ('🥞', '🥞'), ('🥚', '🥚'), ('🥗', '🥗'), ('🥛', '🥛'), ('🥃', '🥃'), ('🥄', '🥄'), ('🛶', '🛶'), ('🥊', '🥊'), ('🥋', '🥋'), ('🥅', '🥅'), ('🥁', '🥁'), ('🛒', '🛒')], default=None, max_length=2, null=True, verbose_name='emoji'),
        ),
    ]