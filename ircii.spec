Summary:	Popular Unix Irc client
Name:		ircii
Version:	4.4J
Release:	1
Copyright:	BSD
Group:		Applications/Communications
Source:		ftp://ircii.warped.com/pub/ircII/%{name}-%{version}.tar.gz
Source1:	ircii.wmconfig
Patch:		ircii-config.patch
Obsoletes:	ircii-help
BuildRoot:	/tmp/%{name}-%{version}-root
Summary(de):	Beliebter Unix-IRC-Client
Summary(fr):	Client irc UNIX populaire.
Summary(tr):	Yaygýn Unix Irc istemcisi
Summary(pl):	Popularny Unixowy Klient Irc

%description
This is a popular Internet Relay Chat (IRC) client.  It
is a program used to connect to IRC servers around the
globe so that the user can ``chat'' with others.

%description -l pl
To jest popularny klient IRC (Internet Relay Chat). To jest
program u¿ywany do ³±czenia siê z serwerami IRC dooko³a
globu tak by u¿ytkownicy mogli ze sob± rozmawiaæ.

%description -l de
Dies ist ein beliebter IRC-Client (Internet Relay Chat). Sie können eine
Verbindung zu einem beliebigen IRC-Server aufbauen und mit
anderen Benutzern 'chatten'.

%description -l fr
Le très poulaire client Internet Relay Chat (IRC). C'est
un programme utilisé pour se connecter aux serveurs IRC à
travers le monde entier et ``bavarder'' avec les autres.

%description -l tr
Bu, yaygýn kullanýlan bir IRC (Internet Relay Chat) istemcisidir. Dünya
üzerinde herhangi bir IRC sunucusuna baðlantý saðlar; baðlantý saðlandýktan
sonra kullanýcý diðer insanlarla sohbet edebilir.

%prep
%setup -q
%patch -p1

%build
%configure \
    --with-cast \
    --with-default-server=warszawa.irc.pl:6667

cd include; make; cd ..
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make	prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT/usr \
	bindir=$RPM_BUILD_ROOT%{_bindir} mandir=$RPM_BUILD_ROOT%{_mandir}/man1 install
ln -sf	irc-%{version} $RPM_BUILD_ROOT%{_bindir}/irc
install	%SOURCE1 $RPM_BUILD_ROOT/etc/X11/wmconfig/ircii
strip	$RPM_BUILD_ROOT%{_bindir}/* || :
gzip	-9nf doc/* $RPM_BUILD_ROOT%{_mandir}/man1/*

%post
if [ ! -f /etc/irc/ircII.servers ]; then
if [ ! -d /etc/irc ]; then
install -d /etc/irc
fi
cat  << EOF > /etc/irc/ircII.servers
warszawa.irc.pl:6667
lublin.irc.pl:6667
krakow.irc.pl:6667
poznan.irc.pl:6667
hub.irc.pl:6667
EOF
chown root.root /etc/irc
chown root.root /etc/irc/ircII.servers
chmod 755 /etc/irc
chmod 644 /etc/irc/ircII.servers
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %dir %{_datadir}/irc
%attr(644,root,root) %{_datadir}/irc
%attr(644,root,root) /etc/X11/wmconfig/ircii
%{_mandir}/man1/*
