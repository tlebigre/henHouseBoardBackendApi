@echo off-
cd %~dp0

if not exist generated mkdir generated
if not exist generated\__init__.py type nul > generated\__init__.py

python -m grpc_tools.protoc ^
    -I proto ^
    --python_out=generated ^
    --grpc_python_out=generated ^
    proto\board.proto

echo Proto files generated successfully.
pause