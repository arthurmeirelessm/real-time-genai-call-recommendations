class AudioHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path

    async def handle_audio(self, websocket):
        with open(self.file_path, "wb") as audio_file:
            try:
                while True:
                    data = await websocket.receive_bytes()
                    self.save_audio_chunk(audio_file, data)
            except Exception as e:
                print(f"Erro ao receber áudio: {e}")

    def save_audio_chunk(self, audio_file, data: bytes):
        audio_file.write(data)
