import flet as ft
import asyncio
from bleak import BleakScanner


def main(page: ft.Page):
    page.title = "Flet BLE Device Scanner"
    devices_list = ft.Column()

    async def test_devices():
        devices_list.controls.clear()
        devices = await BleakScanner.discover()
        for d in devices:
            devices_list.controls.append(
                ft.Text(f"Name: {d.name}, Address: {d.address}")
            )
        page.update()

    def start_scan(e):
        asyncio.run(test_devices())

    scan_button = ft.ElevatedButton("Scan Devices", on_click=start_scan)

    page.add(
        ft.Column(
            [
                ft.Text("Discovered BLE Devices:", weight="bold", size=20),
                scan_button,
                devices_list,
            ]
        )
    )


ft.app(target=main)
