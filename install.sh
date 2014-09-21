#!/bin/bash
# App install batch
# Target
TDIR="/opt/mediDbase";
[[ "$PWD" == "$TDIR" ]] && {
		echo "You are in target, canceling";
		echo "Check location";
		exit 10;
	} || {
		[[ -d "$TDIR" ]] && {
			d=`mktemp -d`;
			echo "Saving dbases";
			mv "$TDIR/books" $d;
			mv "$TDIR/lists" $d;
			mv "$TDIR/dblst.csv" $d;

			rm -r "$TDIR";
			echo "Copying";
			cp -r "$PWD" "$TDIR";

			mv "$d/books" "$TDIR";
			mv "$d/lists" "$TDIR";
			mv "$d/dblst.csv" "$TDIR";

			rm -r $d;
		} || {
			echo "Copying";
			cp -r "$PWD" "$TDIR";
			rm -r "$TDIR/books/*.txt";
			rm "$TDIR/lists/*.txt";
			echo "" > "$TDIR/dblst.csv";
		}
	}

