
sum.o:	file format mach-o arm64

Disassembly of section __TEXT,__text:

0000000000000000 <ltmp0>:
       0: d10083ff     	sub	sp, sp, #32
       4: f9000fe0     	str	x0, [sp, #24]
       8: b90017e1     	str	w1, [sp, #20]
       c: b90013ff     	str	wzr, [sp, #16]
      10: b9000fff     	str	wzr, [sp, #12]
      14: 14000001     	b	0x18 <ltmp0+0x18>
      18: b9400fe8     	ldr	w8, [sp, #12]
      1c: b94017e9     	ldr	w9, [sp, #20]
      20: 6b090108     	subs	w8, w8, w9
      24: 1a9fb7e8     	cset	w8, ge
      28: 370001a8     	tbnz	w8, #0, 0x5c <ltmp0+0x5c>
      2c: 14000001     	b	0x30 <ltmp0+0x30>
      30: f9400fe8     	ldr	x8, [sp, #24]
      34: b9800fe9     	ldrsw	x9, [sp, #12]
      38: b8697909     	ldr	w9, [x8, x9, lsl  #2]
      3c: b94013e8     	ldr	w8, [sp, #16]
      40: 0b090108     	add	w8, w8, w9
      44: b90013e8     	str	w8, [sp, #16]
      48: 14000001     	b	0x4c <ltmp0+0x4c>
      4c: b9400fe8     	ldr	w8, [sp, #12]
      50: 11000508     	add	w8, w8, #1
      54: b9000fe8     	str	w8, [sp, #12]
      58: 17fffff0     	b	0x18 <ltmp0+0x18>
      5c: b94013e0     	ldr	w0, [sp, #16]
      60: 910083ff     	add	sp, sp, #32
      64: d65f03c0     	ret

0000000000000068 <_newsum>:
      68: d100c3ff     	sub	sp, sp, #48
      6c: f90017e0     	str	x0, [sp, #40]
      70: b90027e1     	str	w1, [sp, #36]
      74: b90023ff     	str	wzr, [sp, #32]
      78: b9001fff     	str	wzr, [sp, #28]
      7c: b9001bff     	str	wzr, [sp, #24]
      80: b90017ff     	str	wzr, [sp, #20]
      84: b90013ff     	str	wzr, [sp, #16]
      88: 14000001     	b	0x8c <_newsum+0x24>
      8c: b94013e8     	ldr	w8, [sp, #16]
      90: b94027e9     	ldr	w9, [sp, #36]
      94: 5280008a     	mov	w10, #4
      98: 1aca0d29     	sdiv	w9, w9, w10
      9c: 6b090108     	subs	w8, w8, w9
      a0: 1a9fb7e8     	cset	w8, ge
      a4: 370001a8     	tbnz	w8, #0, 0xd8 <_newsum+0x70>
      a8: 14000001     	b	0xac <_newsum+0x44>
      ac: f94017e8     	ldr	x8, [sp, #40]
      b0: b98013e9     	ldrsw	x9, [sp, #16]
      b4: b8697909     	ldr	w9, [x8, x9, lsl  #2]
      b8: b94023e8     	ldr	w8, [sp, #32]
      bc: 0b090108     	add	w8, w8, w9
      c0: b90023e8     	str	w8, [sp, #32]
      c4: 14000001     	b	0xc8 <_newsum+0x60>
      c8: b94013e8     	ldr	w8, [sp, #16]
      cc: 11000508     	add	w8, w8, #1
      d0: b90013e8     	str	w8, [sp, #16]
      d4: 17ffffee     	b	0x8c <_newsum+0x24>
      d8: b94027e8     	ldr	w8, [sp, #36]
      dc: 52800089     	mov	w9, #4
      e0: 1ac90d08     	sdiv	w8, w8, w9
      e4: b9000fe8     	str	w8, [sp, #12]
      e8: 14000001     	b	0xec <_newsum+0x84>
      ec: b9400fe8     	ldr	w8, [sp, #12]
      f0: b94027e9     	ldr	w9, [sp, #36]
      f4: 5280004a     	mov	w10, #2
      f8: 1aca0d29     	sdiv	w9, w9, w10
      fc: 6b090108     	subs	w8, w8, w9
     100: 1a9fb7e8     	cset	w8, ge
     104: 370001a8     	tbnz	w8, #0, 0x138 <_newsum+0xd0>
     108: 14000001     	b	0x10c <_newsum+0xa4>
     10c: f94017e8     	ldr	x8, [sp, #40]
     110: b9800fe9     	ldrsw	x9, [sp, #12]
     114: b8697909     	ldr	w9, [x8, x9, lsl  #2]
     118: b9401fe8     	ldr	w8, [sp, #28]
     11c: 0b090108     	add	w8, w8, w9
     120: b9001fe8     	str	w8, [sp, #28]
     124: 14000001     	b	0x128 <_newsum+0xc0>
     128: b9400fe8     	ldr	w8, [sp, #12]
     12c: 11000508     	add	w8, w8, #1
     130: b9000fe8     	str	w8, [sp, #12]
     134: 17ffffee     	b	0xec <_newsum+0x84>
     138: b94027e8     	ldr	w8, [sp, #36]
     13c: 52800049     	mov	w9, #2
     140: 1ac90d08     	sdiv	w8, w8, w9
     144: b9000be8     	str	w8, [sp, #8]
     148: 14000001     	b	0x14c <_newsum+0xe4>
     14c: b9400be8     	ldr	w8, [sp, #8]
     150: b94027ea     	ldr	w10, [sp, #36]
     154: 52800069     	mov	w9, #3
     158: 1b0a7d29     	mul	w9, w9, w10
     15c: 5280008a     	mov	w10, #4
     160: 1aca0d29     	sdiv	w9, w9, w10
     164: 6b090108     	subs	w8, w8, w9
     168: 1a9fb7e8     	cset	w8, ge
     16c: 370001a8     	tbnz	w8, #0, 0x1a0 <_newsum+0x138>
     170: 14000001     	b	0x174 <_newsum+0x10c>
     174: f94017e8     	ldr	x8, [sp, #40]
     178: b9800be9     	ldrsw	x9, [sp, #8]
     17c: b8697909     	ldr	w9, [x8, x9, lsl  #2]
     180: b9401be8     	ldr	w8, [sp, #24]
     184: 0b090108     	add	w8, w8, w9
     188: b9001be8     	str	w8, [sp, #24]
     18c: 14000001     	b	0x190 <_newsum+0x128>
     190: b9400be8     	ldr	w8, [sp, #8]
     194: 11000508     	add	w8, w8, #1
     198: b9000be8     	str	w8, [sp, #8]
     19c: 17ffffec     	b	0x14c <_newsum+0xe4>
     1a0: b94027e9     	ldr	w9, [sp, #36]
     1a4: 52800068     	mov	w8, #3
     1a8: 1b097d08     	mul	w8, w8, w9
     1ac: 52800089     	mov	w9, #4
     1b0: 1ac90d08     	sdiv	w8, w8, w9
     1b4: b90007e8     	str	w8, [sp, #4]
     1b8: 14000001     	b	0x1bc <_newsum+0x154>
     1bc: b94007e8     	ldr	w8, [sp, #4]
     1c0: b94027e9     	ldr	w9, [sp, #36]
     1c4: 6b090108     	subs	w8, w8, w9
     1c8: 1a9fb7e8     	cset	w8, ge
     1cc: 370001a8     	tbnz	w8, #0, 0x200 <_newsum+0x198>
     1d0: 14000001     	b	0x1d4 <_newsum+0x16c>
     1d4: f94017e8     	ldr	x8, [sp, #40]
     1d8: b98007e9     	ldrsw	x9, [sp, #4]
     1dc: b8697909     	ldr	w9, [x8, x9, lsl  #2]
     1e0: b94017e8     	ldr	w8, [sp, #20]
     1e4: 0b090108     	add	w8, w8, w9
     1e8: b90017e8     	str	w8, [sp, #20]
     1ec: 14000001     	b	0x1f0 <_newsum+0x188>
     1f0: b94007e8     	ldr	w8, [sp, #4]
     1f4: 11000508     	add	w8, w8, #1
     1f8: b90007e8     	str	w8, [sp, #4]
     1fc: 17fffff0     	b	0x1bc <_newsum+0x154>
     200: b94023e8     	ldr	w8, [sp, #32]
     204: b9401fe9     	ldr	w9, [sp, #28]
     208: 0b090108     	add	w8, w8, w9
     20c: b9401be9     	ldr	w9, [sp, #24]
     210: 0b090108     	add	w8, w8, w9
     214: b94017e9     	ldr	w9, [sp, #20]
     218: 0b090100     	add	w0, w8, w9
     21c: 9100c3ff     	add	sp, sp, #48
     220: d65f03c0     	ret

0000000000000224 <_sum>:
     224: d10083ff     	sub	sp, sp, #32
     228: a9017bfd     	stp	x29, x30, [sp, #16]
     22c: 910043fd     	add	x29, sp, #16
     230: f90007e0     	str	x0, [sp, #8]
     234: b90007e1     	str	w1, [sp, #4]
     238: f94007e0     	ldr	x0, [sp, #8]
     23c: b94007e1     	ldr	w1, [sp, #4]
     240: 94000000     	bl	0x240 <_sum+0x1c>
		0000000000000240:  ARM64_RELOC_BRANCH26	_newsum
     244: a9417bfd     	ldp	x29, x30, [sp, #16]
     248: 910083ff     	add	sp, sp, #32
     24c: d65f03c0     	ret
