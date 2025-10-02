# clangd test


```
clangd --check=src/spi.c
```

With result
```
#1  > clangd --check=src/spi.c
I[12:21:19.150] Homebrew clangd version 18.1.8
I[12:21:19.150] Features: mac+xpc
I[12:21:19.150] PID: 97111
I[12:21:19.150] Working directory: /Users/pandysong/temp/clangd_test
I[12:21:19.150] argv[0]: clangd
I[12:21:19.150] argv[1]: --check=src/spi.c
I[12:21:19.151] Entering check mode (no LSP server)
I[12:21:19.151] Testing on source file /Users/pandysong/temp/clangd_test/src/spi.c
I[12:21:19.151] Loading compilation database...
I[12:21:19.166] Failed to find compilation database for /Users/pandysong/temp/clangd_test/src/spi.c
I[12:21:19.166] Generic fallback command is: [/Users/pandysong/temp/clangd_test/src] /Library/Developer/CommandLineTools/usr/bin/clang -I${PROJECT_ROOT}/include/ -resource-dir=/opt/homebrew/Cellar/llvm@18/18.1.8/lib/clang/18 -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk -- /Users/pandysong/temp/clangd_test/src/spi.c
I[12:21:19.167] Parsing command...
I[12:21:19.167] internal (cc1) args are: -cc1 -triple arm64-apple-macosx14.4.0 -Wundef-prefix=TARGET_OS_ -Werror=undef-prefix -Wdeprecated-objc-isa-usage -Werror=deprecated-objc-isa-usage -fsyntax-only -disable-free -clear-ast-before-backend -disable-llvm-verifier -discard-value-names -main-file-name spi.c -mrelocation-model pic -pic-level 2 -mframe-pointer=non-leaf -ffp-contract=on -fno-rounding-math -funwind-tables=1 -target-sdk-version=14.4 -fcompatibility-qualified-id-block-type-checking -fvisibility-inlines-hidden-static-local-var -fbuiltin-headers-in-system-modules -fdefine-target-os-macros -target-cpu apple-m1 -target-feature +zcm -target-feature +zcz -target-feature +v8.5a -target-feature +aes -target-feature +crc -target-feature +dotprod -target-feature +complxnum -target-feature +fp-armv8 -target-feature +fullfp16 -target-feature +fp16fml -target-feature +jsconv -target-feature +lse -target-feature +pauth -target-feature +ras -target-feature +rcpc -target-feature +rdm -target-feature +sha2 -target-feature +sha3 -target-feature +neon -target-abi darwinpcs -debugger-tuning=lldb -fdebug-compilation-dir=/Users/pandysong/temp/clangd_test/src -target-linker-version 1115.7.3 -fcoverage-compilation-dir=/Users/pandysong/temp/clangd_test/src -resource-dir /opt/homebrew/Cellar/llvm@18/18.1.8/lib/clang/18 -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk -I ${PROJECT_ROOT}/include/ -internal-isystem /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/local/include -internal-isystem /opt/homebrew/Cellar/llvm@18/18.1.8/lib/clang/18/include -internal-externc-isystem /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include -ferror-limit 19 -stack-protector 1 -fblocks -fencode-extended-block-signature -fregister-global-dtors-with-atexit -fgnuc-version=4.2.1 -fskip-odr-check-in-gmf -fmax-type-align=16 -no-round-trip-args -D__GCC_HAVE_DWARF2_CFI_ASM=1 -x c /Users/pandysong/temp/clangd_test/src/spi.c
I[12:21:19.167] Building preamble...
I[12:21:19.173] Built preamble of size 637852 for file /Users/pandysong/temp/clangd_test/src/spi.c version null in 0.01 seconds
I[12:21:19.173] Indexing headers...
E[12:21:19.173] [pp_file_not_found] Line 1: 'spi.h' file not found
I[12:21:19.173] Building AST...
E[12:21:19.176] IncludeCleaner: Failed to get an entry for resolved path : No such file or directory
E[12:21:19.177] [undeclared_var_use] Line 6: use of undeclared identifier 'ABC'
I[12:21:19.177] Indexing AST...
I[12:21:19.177] Building inlay hints
I[12:21:19.177] Building semantic highlighting
I[12:21:19.177] Testing features at each token (may be slow in large files)
E[12:21:19.178] IncludeCleaner: Failed to get an entry for resolved path : No such file or directory
E[12:21:19.178] IncludeCleaner: Failed to get an entry for resolved path : No such file or directory
E[12:21:19.178] IncludeCleaner: Failed to get an entry for resolved path : No such file or directory
I[12:21:19.178] All checks completed, 2 errors
```

When you are using Coc.nvim, following error pop up:

[Errror](file_not_found.jpg)

# Problem

Although I have configure the .clangd file:

```
CompileFlags:
  Add:
    - -Iinclude/
```

However when src/spi.c is compiled, the working directly is switched to `src/`,
so `include/` is not valid anymore, instead you will need `../include/`.

as discussed in the following link:

```
https://github.com/clangd/clangd/issues/1827#issuecomment-3358914913
```

The problem might be resolved by introducing environment variables, which
however is not supported.

# workaround

The workaournd is to put your config in a file and then use a script to
convert to .clangd with absolute paths.
 
```
cat clangd | python3 clangd_convert.py > .clangd
```

Restart vim or :CocRestart to use the new .clangd file
