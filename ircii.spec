Name:		ircii
Version:	4.4J
Release:	1
Copyright:	BSD
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source:		ftp://ircii.warped.com/pub/ircII/%{name}-%{version}.tar.gz
Source1:	ircii.wmconfig
Patch0:		ircii-config.patch
Patch1:		ircii-nick.patch
Obsoletes:	ircii-help
BuildRequires:	ncompress
BuildRoot:	/tmp/%{name}-%{version}-root
Summary:        Popular Unix Irc client
Summary(de):	Beliebter Unix-IRC-Client
Summary(fr):	Client irc UNIX populaire.
Summary(tr):	Yayg�n Unix Irc istemcisi
Summary(pl):	Popularny Unixowy Klient Irc

%description
This is a popular Internet Relay Chat (IRC) client.  It
is a program used to connect to IRC servers around the
globe so that the user can ``chat'' with others.

%description -l pl
To jest popularny klient IRC (Internet Relay Chat). To jest
program u�ywany do ��czenia si� z serwerami IRC dooko�a
globu tak by u�ytkownicy mogli ze sob� rozmawia�.

%description -l de
Dies ist ein beliebter IRC-Client (Internet Relay Chat). Sie k�nnen eine
Verbindung zu einem beliebigen IRC-Server aufbauen und mit
anderen Benutzern 'chatten'.

%description -l fr
Le tr�s poulaire client Internet Relay Chat (IRC). C'est
un programme utilis� pour se connecter aux serveurs IRC �
travers le monde entier et ``bavarder'' avec les autres.

%description -l tr
Bu, yayg�n kullan�lan bir IRC (Internet Relay Chat) istemcisidir. D�nya
�zerinde herhangi bir IRC sunucusuna ba�lant� sa�lar; ba�lant� sa�land�ktan
sonra kullan�c� di�er insanlarla sohbet edebilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
    --with-cast \
    --with-default-server=warszawa.irc.pl:6667

make -C include
make

%install
rm -rf $RPM_BUILD_ROOT

install -d		$RPM_BUILD_ROOT/etc/{X11/wmconfig,irc}
make			DESTDIR=$RPM_BUILD_ROOT	install
ln -sf	irc-%{version}	$RPM_BUILD_ROOT%{_bindir}/irc
install	%{SOURCE1}	$RPM_BUILD_ROOT/etc/X11/wmconfig/ircii
chmod -R a=rX,u=rwX	$RPM_BUILD_ROOT%{_datadir}/ircii
strip			$RPM_BUILD_ROOT%{_bindir}/* || :
gzip			-9nf doc/* $RPM_BUILD_ROOT%{_mandir}/man1/* NEWS INSTALL ChangeLog
compress		$RPM_BUILD_ROOT%{_datadir}/ircii/{help/{*/*,*},script/*} || :

%post
if [ ! -f /etc/irc/ircII.servers ]; then
	if [ ! -d /etc/irc ]; then
		install -d /etc/irc
		chmod 755 /etc/irc
	fi
cat  << EOF > /etc/irc/ircII.servers
warszawa.irc.pl:6667
lublin.irc.pl:6667
krakow.irc.pl:6667
poznan.irc.pl:6667
hub.irc.pl:6667
EOF
	chown root.root /etc/irc/ircII.servers
	chmod 644 /etc/irc/ircII.servers
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,INSTALL,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %dir /etc/irc
%attr( - ,root,root) %{_datadir}/ircii
%attr(644,root,root) %{_mandir}/man1/*
%attr(644,root,root) /etc/X11/wmconfig/ircii
