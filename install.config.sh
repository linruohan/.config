git clone git@github.com:theniceboy/.config.git theniceboy.config
cd theniceboy.config && {
  patch < ./theniceboy.config.patch
  cp -arv `ls | grep -v *.patch` .
}

