from huaweisms.api.common import (
    post_to_url,
    get_from_url,
)


def information(ctx):
    url = "{}/device/information".format(ctx.api_base_url)
    return get_from_url(url, ctx)


def basic_information(ctx):
    url = "{}/device/information".format(ctx.api_base_url)
    return get_from_url(url, ctx)


def reboot(ctx):
    """
    Reboots the modem.
    """

    url = '{}/device/control'.format(ctx.api_base_url)
    headers = {
        '__RequestVerificationToken': ctx.token,
    }

    payload = '<?xml version: "1.0" encoding="UTF-8"?><request><Control>1</Control></request>'
    return post_to_url(url, payload, ctx, additional_headers=headers)
