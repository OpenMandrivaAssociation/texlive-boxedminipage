Name:		texlive-boxedminipage
Version:	54827
Release:	2
Summary:	A package for producing framed minipages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/boxedminipage
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boxedminipage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boxedminipage.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX package which defines the boxedminipage environment --
like minipage, but with a frame around it.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/boxedminipage
%doc %{_texmfdistdir}/doc/latex/boxedminipage

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
