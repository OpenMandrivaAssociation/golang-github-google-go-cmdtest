
# Run tests in check section
%bcond_without check

# https://github.com/google/go-cmdtest
%global goipath		github.com/google/go-cmdtest
%global forgeurl	https://github.com/google/go-cmdtest
Version:		0.4.0

%gometa

Summary:	Simplifies testing of command-line interfaces
Name:		golang-github-google-go-cmdtest

Release:	1
Source0:	https://github.com/google/go-cmdtest/archive/v%{version}/go-cmdtest-%{version}.tar.gz
URL:		https://github.com/google/go-cmdtest
License:	ASL 2.0
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildRequires:	golang(github.com/google/go-cmp/cmp)
BuildRequires:	golang(github.com/google/renameio)
BuildArch:	noarch

%description
The cmdtest package simplifies testing of command-line interfaces.
It provides a simple, cross-platform, shell-like language to express
command execution.  It can compare actual output with the expected
output, and can also update a file with new "golden" output that
is deemed correct.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTING.md README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n go-cmdtest-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

