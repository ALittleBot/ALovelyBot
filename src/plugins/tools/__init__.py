from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.adapters import Event
from nonebot.permission import SUPERUSER

__plugin_meta__ = PluginMetadata(
    name="工具插件",
    description="一些实用工具",
    usage="输入 /user_id 以查看用户id",
    type="application",
    supported_adapters={"~qq"}
)

user_id = on_command("user_id")
is_admin = on_command("is_admin", permission=SUPERUSER)


@user_id.handle()
async def _user_id(event: Event):
    await user_id.finish(event.get_user_id())


@is_admin.handle()
async def _is_admin():
    await user_id.finish("Admin Yes!!!")
